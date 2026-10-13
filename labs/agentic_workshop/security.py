"""Local authorization, content-check, approval, and audit exercises.

This module models policy ideas only. It is not Agent Identity, Agent Gateway,
Model Armor, IAM, OAuth, or a substitute for their current product controls.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from typing import Any

from .types import Caller


@dataclass(frozen=True)
class AgentIdentity:
    agent_id: str
    tenant: str
    permissions: frozenset[str]
    allowed_tools: frozenset[str]
    resource_prefixes: tuple[str, ...]


@dataclass(frozen=True)
class SecurityDecision:
    allowed: bool
    reason: str


class SecurityPolicy:
    """Require caller, agent, tool, scope, tenant, and resource checks to agree."""

    @staticmethod
    def _resource_in_boundary(resource: str, prefixes: tuple[str, ...]) -> bool:
        normalized = resource.strip("/")
        for prefix in prefixes:
            allowed = prefix.strip("/")
            if normalized == allowed or normalized.startswith(allowed + "/"):
                return True
        return False

    def authorize(
        self,
        caller: Caller,
        agent: AgentIdentity,
        *,
        tool_name: str,
        required_scope: str,
        resource: str,
    ) -> SecurityDecision:
        if not caller.authenticated:
            return SecurityDecision(False, "caller_not_authenticated")
        if caller.tenant != agent.tenant:
            return SecurityDecision(False, "tenant_mismatch")
        if tool_name not in agent.allowed_tools:
            return SecurityDecision(False, "tool_not_allowlisted")
        if required_scope not in agent.permissions:
            return SecurityDecision(False, "agent_scope_missing")
        if required_scope not in caller.scopes:
            return SecurityDecision(False, "caller_delegation_missing")
        if not self._resource_in_boundary(resource, agent.resource_prefixes):
            return SecurityDecision(False, "resource_outside_boundary")
        return SecurityDecision(True, "allowed")


@dataclass(frozen=True)
class ContentDecision:
    action: str
    reason: str


class LocalModelArmorExample:
    """A deliberately basic pattern check, not a production content filter."""

    _INJECTION = re.compile(
        r"\b(ignore|disregard|bypass)\b.{0,60}\b(instructions|rules|policy|system)\b"
        r"|\b(reveal|print|exfiltrate)\b.{0,40}\b(secret|credential|token)\b",
        re.IGNORECASE,
    )
    _SECRET_OUTPUT = re.compile(
        r"(?i)\b(password|token|api[_ -]?key|recovery code)\b\s*[:=]\s*\S+"
    )

    def inspect_prompt(self, text: str) -> ContentDecision:
        if self._INJECTION.search(text):
            return ContentDecision("block_or_review", "untrusted instruction pattern")
        return ContentDecision("allow_to_next_control", "no local pattern matched")

    def inspect_output(self, text: str) -> ContentDecision:
        if self._SECRET_OUTPUT.search(text):
            return ContentDecision("block", "possible credential in output")
        return ContentDecision("allow_to_next_control", "no local pattern matched")


_SECRET_PATTERNS = (
    (re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/-]+=*"), "Bearer [REDACTED]"),
    (
        re.compile(r"(?i)\b(password|token|api[_ -]?key|recovery code)\s*[:=]\s*[^\s,;]+"),
        lambda match: f"{match.group(1)}=[REDACTED]",
    ),
    (re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE), "[EMAIL REDACTED]"),
)


def redact_text(text: str) -> str:
    redacted = text
    for pattern, replacement in _SECRET_PATTERNS:
        redacted = pattern.sub(replacement, redacted)
    return redacted


@dataclass
class AuditLog:
    """Metadata-only audit log: deliberately never accepts a prompt field."""

    events: list[dict[str, Any]] = field(default_factory=list)

    def record(
        self,
        *,
        request_id: str,
        caller: Caller,
        agent: AgentIdentity,
        tool_name: str,
        resource: str,
        decision: SecurityDecision,
        approval_id: str | None = None,
    ) -> dict[str, Any]:
        principal_digest = hashlib.sha256(
            f"{caller.tenant}:{caller.user_id}".encode("utf-8")
        ).hexdigest()[:16]
        event = {
            "request_id": redact_text(request_id),
            "principal_ref": principal_digest,
            "agent_id": agent.agent_id,
            "tool": tool_name,
            "resource": redact_text(resource),
            "allowed": decision.allowed,
            "reason": decision.reason,
            "approval_id": redact_text(approval_id) if approval_id else None,
            # Intentionally no prompt, tool arguments, or token value is recorded.
        }
        self.events.append(event)
        return event


class ApprovalGate:
    HIGH_IMPACT_TOOLS = frozenset(
        {"access.grant", "data.delete", "payment.issue", "account.disable"}
    )

    def check(
        self,
        *,
        tool_name: str,
        resource: str,
        approved: bool = False,
        approver: str | None = None,
        approval_action: str | None = None,
    ) -> SecurityDecision:
        if tool_name not in self.HIGH_IMPACT_TOOLS:
            return SecurityDecision(True, "low_impact_path_no_approval_required")
        expected_action = f"{tool_name}:{resource}"
        if not approved or not approver or approval_action != expected_action:
            return SecurityDecision(False, "specific_human_approval_required")
        return SecurityDecision(True, "specific_human_approval_verified")
