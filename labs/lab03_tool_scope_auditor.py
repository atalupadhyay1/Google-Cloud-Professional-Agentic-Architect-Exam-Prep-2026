#!/usr/bin/env python3
"""Lab 3: Least-privilege tool-scope auditor. Run: python3 labs/lab03_tool_scope_auditor.py"""
TOOLS = [
    # name, type(read/write/irreversible), uses_last_90d, role_needs
    ("get_order", "read", 5200, True), ("search_kb", "read", 8100, True), ("draft_reply", "write", 6000, True),
    ("issue_refund", "write", 310, True), ("refund_any_amount", "write", 2, False), ("delete_account", "irreversible", 1, False),
    ("export_all_customers", "read", 0, False), ("send_email_anyone", "write", 3, False), ("reset_password", "write", 45, False),
    ("update_address", "write", 900, True), ("view_admin_billing", "read", 0, False), ("run_sql_anywhere", "irreversible", 0, False),
]
if __name__ == "__main__":
    print(f"{'TOOL':22} {'TYPE':13} {'USES':>5}  RECOMMENDATION")
    for name, typ, uses, needs in TOOLS:
        if not needs and typ == "irreversible": rec = "REMOVE (or separate privileged agent + pre-approval)"
        elif not needs and uses < 50: rec = "REMOVE — no evidenced role need (capability bloat)"
        elif typ == "irreversible": rec = "GATE — human pre-approval + limits + audit"
        elif typ == "write": rec = "KEEP SCOPED — server-side AuthZ, per-user scope, caps"
        else: rec = "KEEP — read-only, log access"
        print(f"{name:22} {typ:13} {uses:5}  {rec}")
    print("\nRule: prompts guide, permissions enforce. Justify-or-remove every tool. See docs/03.")
