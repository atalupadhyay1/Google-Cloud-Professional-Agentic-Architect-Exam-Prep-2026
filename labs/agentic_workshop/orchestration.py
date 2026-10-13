"""Typed handoffs and deterministic orchestration patterns for Lab 5."""

from __future__ import annotations

import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from typing import Any, Callable, Mapping

_SECRET_MARKER = re.compile(
    r"(?i)(password|token|api[_ -]?key|recovery code)\s*[:=]"
)


class HandoffValidationError(ValueError):
    pass


@dataclass(frozen=True)
class HandoffEnvelope:
    schema_version: str
    task_id: str
    context_id: str
    sender: str
    recipient: str
    objective: str
    evidence_ids: tuple[str, ...] = ()
    constraints: tuple[str, ...] = ()

    def validate(self) -> None:
        required = {
            "schema_version": self.schema_version,
            "task_id": self.task_id,
            "context_id": self.context_id,
            "sender": self.sender,
            "recipient": self.recipient,
            "objective": self.objective,
        }
        missing = [key for key, value in required.items() if not value.strip()]
        if missing:
            raise HandoffValidationError(f"missing required field(s): {', '.join(missing)}")
        if self.schema_version != "1":
            raise HandoffValidationError("unsupported handoff schema version")
        payload = " ".join((self.objective, *self.evidence_ids, *self.constraints))
        if _SECRET_MARKER.search(payload):
            raise HandoffValidationError("handoff appears to contain a credential")
        if len(payload) > 4000:
            raise HandoffValidationError("handoff exceeds the local size limit")


@dataclass(frozen=True)
class AgentCard:
    agent_id: str
    skills: frozenset[str]
    version: str
    owner: str


class AgentDirectory:
    """Toy capability directory; discovery is not authorization."""

    def __init__(self) -> None:
        self._cards: dict[str, AgentCard] = {}

    def register(self, card: AgentCard) -> None:
        if not card.agent_id.strip() or not card.owner.strip() or not card.skills:
            raise ValueError("agent id, owner, and at least one skill are required")
        self._cards[card.agent_id] = card

    def discover(self, skill: str) -> tuple[AgentCard, ...]:
        return tuple(
            sorted(
                (card for card in self._cards.values() if skill in card.skills),
                key=lambda card: card.agent_id,
            )
        )


@dataclass(frozen=True)
class ExecutionResult:
    status: str
    state: dict[str, Any]
    trace: tuple[str, ...]
    errors: tuple[str, ...] = ()


def run_sequential(
    nodes: list[tuple[str, Callable[[dict[str, Any]], Mapping[str, Any]]]],
    initial_state: Mapping[str, Any],
    *,
    fail_node: str | None = None,
) -> ExecutionResult:
    """Run dependent steps; each producer may add new keys, not overwrite state."""
    state = dict(initial_state)
    trace: list[str] = []
    for name, node in nodes:
        trace.append(name)
        try:
            if name == fail_node:
                raise TimeoutError("simulated node timeout")
            output = node(dict(state))
            if not isinstance(output, Mapping):
                raise TypeError("node output must be a mapping")
            collisions = set(output).intersection(state)
            if collisions:
                raise ValueError(f"node attempted to overwrite state keys: {sorted(collisions)}")
            state.update(output)
        except Exception as exc:  # lab harness records failure rather than hiding it
            return ExecutionResult(
                status="failed",
                state=state,
                trace=tuple(trace),
                errors=(f"{name}: {type(exc).__name__}: {exc}",),
            )
    return ExecutionResult(status="complete", state=state, trace=tuple(trace))


def run_parallel(
    branches: Mapping[str, Callable[[dict[str, Any]], Mapping[str, Any]]],
    initial_state: Mapping[str, Any],
    *,
    fail_branches: frozenset[str] = frozenset(),
    require_all: bool = True,
) -> ExecutionResult:
    """Run independent branches and apply a strict, collision-aware merge."""
    if not branches:
        return ExecutionResult("failed", dict(initial_state), (), ("no branches configured",))
    state = dict(initial_state)
    outputs: dict[str, Mapping[str, Any]] = {}
    errors: list[str] = []
    with ThreadPoolExecutor(max_workers=len(branches)) as executor:
        futures = {}
        for name, branch in branches.items():
            def invoke(fn: Callable[[dict[str, Any]], Mapping[str, Any]] = branch, branch_name: str = name):
                if branch_name in fail_branches:
                    raise TimeoutError("simulated branch timeout")
                return fn(dict(initial_state))
            futures[executor.submit(invoke)] = name
        for future in as_completed(futures):
            name = futures[future]
            try:
                result = future.result()
                if not isinstance(result, Mapping):
                    raise TypeError("branch output must be a mapping")
                outputs[name] = result
            except Exception as exc:
                errors.append(f"{name}: {type(exc).__name__}: {exc}")

    # Preserve declared order for deterministic evidence and collision handling.
    ordered_names = [name for name in branches if name in outputs]
    merged_keys: set[str] = set()
    for name in ordered_names:
        output = outputs[name]
        collisions = merged_keys.intersection(output)
        collisions.update(set(output).intersection(state))
        if collisions:
            errors.append(f"{name}: conflicting output key(s): {sorted(collisions)}")
            continue
        state.update(output)
        merged_keys.update(output)

    if errors and require_all:
        return ExecutionResult(
            status="failed",
            state=dict(initial_state),
            trace=tuple(branches.keys()),
            errors=tuple(errors),
        )
    if errors:
        return ExecutionResult(
            status="partial",
            state=state,
            trace=tuple(branches.keys()),
            errors=tuple(errors),
        )
    return ExecutionResult(status="complete", state=state, trace=tuple(branches.keys()))


def run_graph(
    start: str,
    nodes: Mapping[str, Callable[[dict[str, Any]], Mapping[str, Any]]],
    route: Callable[[str, Mapping[str, Any]], str | None],
    initial_state: Mapping[str, Any],
    *,
    max_steps: int = 8,
) -> ExecutionResult:
    """Run a state graph with explicit routing and a hard step budget."""
    if start not in nodes:
        return ExecutionResult("failed", dict(initial_state), (), ("unknown start node",))
    if max_steps < 1:
        return ExecutionResult("failed", dict(initial_state), (), ("max_steps must be positive",))
    state = dict(initial_state)
    trace: list[str] = []
    current: str | None = start
    for _ in range(max_steps):
        if current is None:
            return ExecutionResult("complete", state, tuple(trace))
        if current not in nodes:
            return ExecutionResult("failed", state, tuple(trace), (f"unknown route: {current}",))
        trace.append(current)
        try:
            output = nodes[current](dict(state))
            if not isinstance(output, Mapping):
                raise TypeError("node output must be a mapping")
            collisions = set(output).intersection(state)
            if collisions:
                raise ValueError(f"node attempted to overwrite state keys: {sorted(collisions)}")
            state.update(output)
            current = route(trace[-1], output)
            if current is None:
                return ExecutionResult("complete", state, tuple(trace))
        except Exception as exc:
            return ExecutionResult(
                "failed", state, tuple(trace), (f"{trace[-1]}: {type(exc).__name__}: {exc}",)
            )
    return ExecutionResult("failed", state, tuple(trace), ("step_limit_exceeded",))
