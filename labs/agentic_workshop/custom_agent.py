"""Local custom-agent, session, and allowlisted-memory exercise."""

from __future__ import annotations

import re
from dataclasses import dataclass

from .types import Caller, WorkflowResult
from .workflow import SupportWorkflow

_SENSITIVE_VALUE = re.compile(
    r"(?i)(password|token|api[_ -]?key|recovery code|one[- ]time code|\b\d{6}\b)"
)


@dataclass(frozen=True)
class Turn:
    role: str
    text: str


class SessionStore:
    """In-memory session store keyed by tenant, user, and session identifier."""

    def __init__(self) -> None:
        self._sessions: dict[tuple[str, str, str], list[Turn]] = {}

    @staticmethod
    def _key(caller: Caller, session_id: str) -> tuple[str, str, str]:
        if not caller.authenticated:
            raise PermissionError("authenticated caller context is required")
        if not session_id.strip():
            raise ValueError("session_id must not be empty")
        return (caller.tenant, caller.user_id, session_id)

    def append(self, caller: Caller, session_id: str, role: str, text: str) -> None:
        if role not in {"user", "assistant", "tool"}:
            raise ValueError("role must be user, assistant, or tool")
        key = self._key(caller, session_id)
        self._sessions.setdefault(key, []).append(Turn(role=role, text=text))

    def history(self, caller: Caller, session_id: str) -> tuple[Turn, ...]:
        key = self._key(caller, session_id)
        return tuple(self._sessions.get(key, ()))

    def clear(self, caller: Caller, session_id: str) -> None:
        self._sessions.pop(self._key(caller, session_id), None)


class MemoryBank:
    """Tiny allowlist memory: only non-sensitive response preferences are kept."""

    ALLOWED_KEYS = frozenset({"preferred_language", "response_style"})

    def __init__(self) -> None:
        self._profiles: dict[tuple[str, str], dict[str, str]] = {}

    def remember(self, caller: Caller, key: str, value: str) -> bool:
        if not caller.authenticated or key not in self.ALLOWED_KEYS:
            return False
        normalized = value.strip()
        if not normalized or len(normalized) > 80 or _SENSITIVE_VALUE.search(normalized):
            return False
        profile_key = (caller.tenant, caller.user_id)
        self._profiles.setdefault(profile_key, {})[key] = normalized
        return True

    def profile(self, caller: Caller) -> dict[str, str]:
        if not caller.authenticated:
            raise PermissionError("authenticated caller context is required")
        return dict(self._profiles.get((caller.tenant, caller.user_id), {}))

    def forget(self, caller: Caller, key: str | None = None) -> None:
        if not caller.authenticated:
            raise PermissionError("authenticated caller context is required")
        profile_key = (caller.tenant, caller.user_id)
        if key is None:
            self._profiles.pop(profile_key, None)
        else:
            self._profiles.get(profile_key, {}).pop(key, None)


class CustomSupportAgent:
    """A small orchestration shell around a bounded deterministic workflow."""

    def __init__(
        self,
        workflow: SupportWorkflow | None = None,
        sessions: SessionStore | None = None,
        memory: MemoryBank | None = None,
    ) -> None:
        self.workflow = workflow or SupportWorkflow()
        self.sessions = sessions or SessionStore()
        self.memory = memory or MemoryBank()

    def respond(self, question: str, caller: Caller, session_id: str) -> WorkflowResult:
        # The session key is derived from authenticated context, not from question text.
        self.sessions.append(caller, session_id, "user", question)
        result = self.workflow.run(question, caller)
        self.sessions.append(caller, session_id, "assistant", result.answer)
        return result
