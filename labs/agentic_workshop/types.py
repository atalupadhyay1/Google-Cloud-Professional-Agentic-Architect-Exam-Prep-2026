"""Shared, intentionally small data types used by the local lab harness."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Caller:
    """Authenticated caller context supplied by the application, not user text."""

    user_id: str
    tenant: str
    groups: frozenset[str] = frozenset()
    scopes: frozenset[str] = frozenset()
    authenticated: bool = True


@dataclass(frozen=True)
class SearchHit:
    document_id: str
    title: str
    excerpt: str
    version: str
    score: float


@dataclass
class WorkflowResult:
    status: str
    answer: str
    state_trace: list[str] = field(default_factory=list)
    source_ids: list[str] = field(default_factory=list)
    handoff_to: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "answer": self.answer,
            "state_trace": list(self.state_trace),
            "source_ids": list(self.source_ids),
            "handoff_to": self.handoff_to,
        }


@dataclass(frozen=True)
class ToolResult:
    ok: bool
    data: dict[str, Any] = field(default_factory=dict)
    error: str | None = None
    elapsed_ms: int = 0


@dataclass(frozen=True)
class EvalFinding:
    case_id: str
    passed: bool
    expected_status: str
    actual_status: str
    expected_source: str | None
    actual_sources: tuple[str, ...]
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class EvaluationSummary:
    findings: tuple[EvalFinding, ...]

    @property
    def total(self) -> int:
        return len(self.findings)

    @property
    def passed(self) -> int:
        return sum(finding.passed for finding in self.findings)

    @property
    def pass_rate(self) -> float:
        return self.passed / self.total if self.total else 0.0

    @property
    def all_passed(self) -> bool:
        return self.total > 0 and self.passed == self.total
