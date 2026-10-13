#!/usr/bin/env python3
"""Lab 7: ADR + SLA draft generator (interactive-lite, defaults provided). Run: python3 labs/lab07_adr_and_sla.py"""
import datetime
title="ADR-001: Routed workflow instead of autonomous agent for refunds"
print(f"# {title}\nDate: {datetime.date.today()} | Status: Accepted\n")
print("Context: Refund errors are costly/irreversible; steps (verify order->policy->draft->approve) are known and stable.")
print("Options: A) Autonomous agent with refund tool  B) Routed workflow + human approval above EUR 50  C) Manual only")
print("Decision: B. Consequences: +auditability, +predictable cost/latency, -less autonomy (accepted by sponsor).")
print("Evidence: Eval plan docs/05; pilot thresholds: citation accuracy>=95%, p95<4s. Review trigger: volume>5k/mo or new model tier.\n")
print("## SLA/SLO draft\n| Metric | SLO (internal) | SLA (promised) | Measured via |\n|---|---|---|---|")
for m in ["Accuracy (sampled eval) >=92% | >=90% | Weekly sampled grading","Latency p95 <=4s | <=5s | Stage latency dashboard","Cost/successful task <=0.08u | budget alert +20% | Token/cost logs"]:
    print(f"| {m} |")
print("\nNow rewrite this for YOUR Lab-1 scenario and file it with the handoff pack (docs/07).")
