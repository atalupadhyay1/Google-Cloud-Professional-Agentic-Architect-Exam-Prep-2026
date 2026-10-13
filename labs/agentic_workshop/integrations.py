"""Mock read-only database and SaaS adapters for Lab 4.

These adapters are local fixtures. They deliberately expose named operations,
not arbitrary SQL or a real OAuth client.
"""

from __future__ import annotations

from time import monotonic

from .types import Caller, ToolResult


class MockReadOnlyDatabase:
    _ASSETS = {
        "asset-42": {"asset_id": "asset-42", "status": "assigned", "owner_group": "IT"},
        "asset-73": {"asset_id": "asset-73", "status": "available", "owner_group": "IT"},
    }

    def get_asset_status(self, asset_id: str) -> dict[str, str] | None:
        # A production adapter would use a parameterized query or a narrow view.
        return self._ASSETS.get(asset_id)


class MockSaaSClient:
    _TICKETS = {
        "ticket-900": {"ticket_id": "ticket-900", "status": "in_progress", "assigned_group": "Identity Support"},
        "ticket-901": {"ticket_id": "ticket-901", "status": "waiting_for_user", "assigned_group": "IT Helpdesk"},
    }

    def get_ticket_status(self, ticket_id: str, *, simulate: str = "ok") -> dict[str, str] | None:
        if simulate == "timeout":
            raise TimeoutError("mock SaaS request timed out")
        if simulate != "ok":
            raise ValueError("simulate must be 'ok' or 'timeout'")
        return self._TICKETS.get(ticket_id)


class IntegrationBroker:
    """Application-side scope checks around two read-only mock capabilities."""

    def __init__(
        self,
        database: MockReadOnlyDatabase | None = None,
        saas: MockSaaSClient | None = None,
    ) -> None:
        self.database = database or MockReadOnlyDatabase()
        self.saas = saas or MockSaaSClient()

    def invoke(self, tool_name: str, caller: Caller, **arguments: str) -> ToolResult:
        started = monotonic()
        if not caller.authenticated:
            return ToolResult(ok=False, error="unauthenticated", elapsed_ms=0)
        if tool_name == "asset.status.read":
            required_scope = "asset.read"
        elif tool_name == "ticket.status.read":
            required_scope = "ticket.read"
        else:
            return ToolResult(ok=False, error="unknown_tool", elapsed_ms=0)
        if required_scope not in caller.scopes:
            return ToolResult(ok=False, error="permission_denied", elapsed_ms=0)
        try:
            if tool_name == "asset.status.read":
                asset_id = arguments.get("asset_id", "")
                if not asset_id or len(asset_id) > 40:
                    return ToolResult(ok=False, error="invalid_argument", elapsed_ms=0)
                data = self.database.get_asset_status(asset_id)
            else:
                ticket_id = arguments.get("ticket_id", "")
                if not ticket_id or len(ticket_id) > 40:
                    return ToolResult(ok=False, error="invalid_argument", elapsed_ms=0)
                data = self.saas.get_ticket_status(
                    ticket_id,
                    simulate=arguments.get("simulate", "ok"),
                )
        except TimeoutError:
            elapsed = int((monotonic() - started) * 1000)
            return ToolResult(ok=False, error="timeout", elapsed_ms=max(elapsed, 1))
        except ValueError:
            return ToolResult(ok=False, error="invalid_argument", elapsed_ms=0)
        elapsed = int((monotonic() - started) * 1000)
        if data is None:
            return ToolResult(ok=False, error="not_found", elapsed_ms=elapsed)
        return ToolResult(ok=True, data=dict(data), elapsed_ms=elapsed)
