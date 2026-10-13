# Hands-On Labs — Complete Guide
*Beginner-friendly. Every lab runs with Python standard library only — no API key, no pip install.*

```bash
python3 --version   # 3.10+
python3 labs/lab01_pattern_selector.py
python3 labs/lab02_prompt_caching_cost.py   # after fix: costs are realistic $/month at 1M requests
python3 labs/lab03_tool_scope_auditor.py
python3 labs/lab04_rag_pipeline.py
python3 labs/lab05_eval_harness.py
python3 labs/lab06_guardrail_matrix.py
python3 labs/lab07_adr_and_sla.py
python3 labs/lab08_readiness_score.py
```

| Lab | Module | What you'll learn by doing | Break-it exercise |
|---|---|---|---|
| 01 Pattern Selector | 01 | Agent loops breach latency SLAs; workflow cost is predictable | Set loop max high — watch worst case; add budget/stop |
| 02 Caching & Tiers | 02 | Stable prefix + cached pricing + routing 80/20 easy/hard | Add 10 few-shots uncached — quantify, then fix |
| 03 Tool Auditor | 03 | Justify-or-remove; irreversible ≠ “used once so keep” | Defend gating `delete_account` |
| 04 Mini RAG | 04 | **Stale-chunk failure after refresh**, fixed by version filter/atomic swap | Mix v1+v2 with no filter — reproduce the exam scenario |
| 05 Eval Harness | 05 | Averages hide subset regressions (edge/adversarial) | Add your own production failure as a regression case |
| 06 Guardrail Matrix | 06 | Control at the right layer, with an owner | Remove HITL for irreversible action — who notices? |
| 07 ADR + SLA | 07 | Decision record with review trigger; measured SLOs | Delete review trigger — when does decision expire? |
| 08 Readiness | 08 | Weighted domain score → next study target | Edit `SCORES` with your real trainer results |

**Optional real-API extension (never commit keys):** `export ANTHROPIC_API_KEY=...` then replace the mock/extractive generation step in Lab 4 with an Anthropic Messages API call, keeping retrieval/citation logging identical. Verify current SDK/model names in official docs.

**Lab report template (use for every lab):** `Hypothesis → Change (one variable) → Result (numbers/screenshot of output) → Decision → Regression case added?`
