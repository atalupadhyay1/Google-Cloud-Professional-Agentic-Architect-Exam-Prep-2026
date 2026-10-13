# Local workshop harness

This folder contains small, deterministic Python examples supporting the seven drills in [`../docs/lab-workbook.md`](../docs/lab-workbook.md).

## Run

From the repository root:

```bash
python --version
python -m labs.agentic_workshop.demo
python -m unittest discover -s labs/tests -v
```

Python 3.10+ is recommended. The workshop uses only the Python standard library; there is no requirements installation step. Use `python3` instead of `python` if that is how Python is installed on your machine.

## Modules

| Module | Lab | Demonstrates |
|---|---:|---|
| `agentic_workshop/workflow.py` | 1 | Explicit states, evidence-backed answers, clarify/escalate/deny paths |
| `agentic_workshop/coding_agent.py` | 2 | Named mock tools, default-deny sandbox policy, before/after SQL patch check |
| `agentic_workshop/custom_agent.py` | 3 | Composite session keys and allowlisted, deletable profile memory |
| `agentic_workshop/knowledge.py`, `integrations.py` | 4 | Tenant/group/freshness filtering and read-only mock tool outcomes |
| `agentic_workshop/orchestration.py` | 5 | Handoff validation, sequential/parallel/graph workflows, failure rules |
| `agentic_workshop/evaluation.py`, `operations.py` | 6 | Synthetic evalset, trace summaries, runtime discussion aid, release gate |
| `agentic_workshop/security.py` | 7 | Mock identity/scope/boundary checks, redaction, content check, approval gate |
| `agentic_workshop/data/knowledge.json` | 1, 4 | Synthetic and permission-labelled source records |
| `tests/` | all | Regression and failure-path assertions |

## Important limits

- These are **teaching simulations**. They are not ADK code, Agent Identity, PAB, Agent Gateway, Agent Registry, Model Armor, a real MCP/A2A implementation, a real database/SaaS connector, or a production security sandbox.
- No model is called and no external connection is made. The lexical search is not vector retrieval. The policy regex is not a security filter. The release thresholds are examples, not production SLAs.
- Do not copy the local authorization code into production and assume the boundary is enforced. Use current Google Cloud product documentation and independently enforced identity, network, workload, and data controls.
- The fixtures contain no real secrets or customer records. Keep it that way.
