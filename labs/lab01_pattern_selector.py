#!/usr/bin/env python3
"""Lab 1: Workflow vs Augmented LLM vs Agent — cost/latency simulator (stdlib only, illustrative numbers).
Run: python3 labs/lab01_pattern_selector.py"""
import random, statistics
random.seed(42)
# Illustrative teaching numbers ONLY (not real pricing): cost per 1k tokens, latency per call (sec)
TIERS = {"fast": (0.001, 0.4), "balanced": (0.004, 0.9), "capable": (0.015, 1.8)}

def simulate(name, calls_fn, n=2000, in_tok=1200, out_tok=300, tier="balanced"):
    price, lat = TIERS[tier]
    costs, lats = [], []
    for _ in range(n):
        c = calls_fn()
        costs.append(c * (in_tok + out_tok) / 1000 * price * 1000)  # cents-ish illustrative units
        lats.append(c * lat * random.uniform(0.8, 1.25))
    p95 = sorted(lats)[int(0.95 * n)]
    print(f"{name:28} calls~{calls_fn()} avg_cost={statistics.mean(costs):7.2f}u  p50_lat={statistics.median(lats):4.2f}s  p95_lat={p95:4.2f}s  SLA(5s)={'OK' if p95<=5 else 'BREACH'}")

if __name__ == "__main__":
    print("Same task, three patterns (illustrative numbers — plug in current official pricing for real decisions):\n")
    simulate("Workflow (3 fixed calls)", lambda: 3)
    simulate("Augmented LLM (1 call+RAG)", lambda: 1)
    simulate("Agent (loop 3-9 calls)", lambda: random.randint(3, 9))
    simulate("Agent capped (loop 3-5)", lambda: random.randint(3, 5))
    print("\nReflect: 1) When does agent p95 breach 5s? 2) Which cost is most predictable at 10x volume? 3) What budget/stop rule did capping add?")
