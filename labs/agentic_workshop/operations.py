"""Runtime decision and privacy-conscious operational evidence examples."""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from typing import Iterable


@dataclass(frozen=True)
class RuntimeRequirements:
    managed_agent_lifecycle_fit: bool = False
    request_driven_http: bool = True
    needs_kubernetes_control: bool = False
    team_can_operate_kubernetes: bool = False


@dataclass(frozen=True)
class RuntimeChoice:
    name: str
    rationale: str
    caveat: str


def choose_runtime(requirements: RuntimeRequirements) -> RuntimeChoice:
    """A teaching decision aid, not a service feature/availability guarantee."""
    if requirements.needs_kubernetes_control:
        if not requirements.team_can_operate_kubernetes:
            return RuntimeChoice(
                "revisit-requirements",
                "The workload asks for Kubernetes-level control, but the team cannot currently operate it safely.",
                "Reduce the control requirement or establish an operations owner before choosing GKE.",
            )
        return RuntimeChoice(
            "GKE",
            "The stated workload requires Kubernetes-level control and the team has an operations owner.",
            "Validate cluster design, reliability, security, regional availability, and total operating cost.",
        )
    if requirements.managed_agent_lifecycle_fit:
        return RuntimeChoice(
            "Agent Runtime",
            "A managed agent lifecycle appears to fit the workload requirements.",
            "Confirm current feature support, region, limits, integrations, and pricing before selection.",
        )
    if requirements.request_driven_http:
        return RuntimeChoice(
            "Cloud Run",
            "A request-driven containerized service appears to fit without requiring cluster control.",
            "Validate startup, concurrency, request deadlines, state externalization, and cost behavior.",
        )
    return RuntimeChoice(
        "revisit-requirements",
        "The requirements do not identify a suitable managed-agent or request-driven runtime path.",
        "Clarify workload lifecycle and operational constraints before selecting infrastructure.",
    )


@dataclass(frozen=True)
class TraceRecord:
    request_id: str
    agent_version: str
    outcome: str
    duration_ms: int
    tool_names: tuple[str, ...] = ()
    error_kind: str | None = None
    source_ids: tuple[str, ...] = ()
    # No prompt, raw tool arguments, token, or raw document text is stored here.


@dataclass(frozen=True)
class TraceSummary:
    requests: int
    failures: int
    error_rate: float
    p95_duration_ms: int
    tool_calls: int


def summarize_traces(records: Iterable[TraceRecord]) -> TraceSummary:
    items = tuple(records)
    if not items:
        return TraceSummary(0, 0, 0.0, 0, 0)
    ordered_durations = sorted(max(0, item.duration_ms) for item in items)
    p95_index = max(0, ceil(0.95 * len(ordered_durations)) - 1)
    operational_error_outcomes = {"error", "timeout", "failed", "system_error"}
    failures = sum(
        item.outcome.lower() in operational_error_outcomes or item.error_kind is not None
        for item in items
    )
    calls = sum(len(item.tool_names) for item in items)
    return TraceSummary(
        requests=len(items),
        failures=failures,
        error_rate=failures / len(items),
        p95_duration_ms=ordered_durations[p95_index],
        tool_calls=calls,
    )


@dataclass(frozen=True)
class ReleaseDecision:
    approved: bool
    reasons: tuple[str, ...]


def release_gate(
    *,
    evaluation_pass_rate: float,
    security_cases_pass: bool,
    denied_path_tested: bool,
    canary_error_rate: float,
    rollback_defined: bool,
    max_canary_error_rate: float = 0.02,
) -> ReleaseDecision:
    reasons: list[str] = []
    if evaluation_pass_rate < 1.0:
        reasons.append("golden-set gate is not fully green")
    if not security_cases_pass:
        reasons.append("security evaluation failed")
    if not denied_path_tested:
        reasons.append("denied path has not been verified")
    if canary_error_rate > max_canary_error_rate:
        reasons.append("canary error rate exceeds the configured threshold")
    if not rollback_defined:
        reasons.append("rollback owner or procedure is missing")
    return ReleaseDecision(approved=not reasons, reasons=tuple(reasons))
