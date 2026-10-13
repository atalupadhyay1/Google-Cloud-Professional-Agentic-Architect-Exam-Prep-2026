"""Coding-agent safety and patch-validation patterns for Lab 2.

The MCP server and sandbox below are local teaching fakes. They do not provide
process, filesystem, network, or credential isolation; a real sandbox needs OS
or cloud enforcement in addition to application policy.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Callable


class PolicyDenied(PermissionError):
    pass


@dataclass(frozen=True)
class SandboxPolicy:
    allowed_tools: frozenset[str] = frozenset(
        {"read_scoped_file", "run_unit_tests", "propose_patch"}
    )
    allowed_roots: tuple[str, ...] = ("src", "tests")
    network_enabled: bool = False
    secrets_mounted: bool = False

    def authorize(
        self,
        tool_name: str,
        *,
        path: str | None = None,
        network: bool = False,
        needs_secret: bool = False,
    ) -> None:
        if tool_name not in self.allowed_tools:
            raise PolicyDenied(f"tool is not allowlisted: {tool_name}")
        if network and not self.network_enabled:
            raise PolicyDenied("network access is disabled in this sandbox")
        if needs_secret and not self.secrets_mounted:
            raise PolicyDenied("secrets are not mounted in this sandbox")
        if path is not None:
            candidate = PurePosixPath(path)
            if candidate.is_absolute() or ".." in candidate.parts:
                raise PolicyDenied("path must be relative and may not traverse directories")
            if not candidate.parts or candidate.parts[0] not in self.allowed_roots:
                raise PolicyDenied("path is outside the allowed repository roots")


class MockMCPToolServer:
    """A tiny in-process illustration of named, scoped tool exposure."""

    def __init__(self, policy: SandboxPolicy | None = None) -> None:
        self.policy = policy or SandboxPolicy()
        self._tools: dict[str, Callable[..., dict[str, str]]] = {
            "read_scoped_file": self._read_file_metadata,
            "run_unit_tests": self._run_tests,
            "propose_patch": self._propose_patch,
        }

    @staticmethod
    def _read_file_metadata(path: str) -> dict[str, str]:
        return {"result": "read request accepted for review", "path": path}

    @staticmethod
    def _run_tests(test_suite: str = "default") -> dict[str, str]:
        return {"result": "simulated tests passed", "test_suite": test_suite}

    @staticmethod
    def _propose_patch(path: str, summary: str) -> dict[str, str]:
        return {"result": "patch proposal recorded; human review required", "path": path, "summary": summary}

    def call(self, tool_name: str, **arguments: str) -> dict[str, str]:
        tool = self._tools.get(tool_name)
        if tool is None:
            raise PolicyDenied(f"unknown tool: {tool_name}")
        target_path = arguments.get("path")
        self.policy.authorize(tool_name, path=target_path)
        return tool(**arguments)


def unsafe_build_user_query(username: str) -> str:
    """Intentionally vulnerable fixture; do not use this construction in apps."""
    return f"SELECT user_id, display_name FROM users WHERE display_name = '{username}'"


def safe_build_user_query(username: str) -> tuple[str, tuple[str, ...]]:
    """Return SQL and parameters separately, as a parameterized query should."""
    return (
        "SELECT user_id, display_name FROM users WHERE display_name = ?",
        (username,),
    )


def inspect_query_builder(builder: Callable[..., object]) -> dict[str, bool]:
    """Check benign behavior and that an injection string remains a parameter."""
    benign = "Maya"
    attack = "x' OR 1=1 --"
    benign_result = builder(benign)
    attack_result = builder(attack)

    if isinstance(benign_result, tuple) and isinstance(attack_result, tuple):
        benign_sql, benign_params = benign_result
        attack_sql, attack_params = attack_result
        benign_preserved = "?" in benign_sql and benign_params == (benign,)
        injection_is_data = (
            "?" in attack_sql
            and attack_params == (attack,)
            and attack not in attack_sql
            and "OR 1=1" not in attack_sql
        )
    elif isinstance(benign_result, str) and isinstance(attack_result, str):
        benign_preserved = benign in benign_result
        injection_is_data = attack not in attack_result and "OR 1=1" not in attack_result
    else:
        benign_preserved = False
        injection_is_data = False

    return {
        "benign_input_preserved": benign_preserved,
        "injection_remains_data": injection_is_data,
        "passed": benign_preserved and injection_is_data,
    }


def patch_comparison() -> dict[str, dict[str, bool]]:
    """Produce before/after evidence for the vulnerable and fixed examples."""
    return {
        "before": inspect_query_builder(unsafe_build_user_query),
        "after": inspect_query_builder(safe_build_user_query),
    }
