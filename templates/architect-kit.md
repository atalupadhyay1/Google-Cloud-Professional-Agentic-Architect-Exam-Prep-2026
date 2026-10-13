# The Architect's Kit — All 8 Course Tools (Copy-Paste Templates)
*From the course outline: solution design canvas, model & prompt spec, integration security review, RAG & observability design, eval plan & metrics sheet, guardrail & compliance matrix, decision record & handoff pack, readiness scorecard.*

## 1. Solution Design Canvas (Module 1)
| Field | Your entry |
|---|---|
| Problem & user (volume) | |
| Value hypothesis + metric | |
| SLAs: quality / latency p95 / cost per task / safety | |
| Pattern (workflow / augmented / agent) + 3-sentence defence | |
| Flow: input → processing → output → feedback | |
| Data/retrieval need | |
| Tools & top risks | |
| Eval plan (link) | |

## 2. Model & Prompt Spec (Module 2)
`Task | Model tier + eval evidence | System prompt layers (role/rules/process/output contract/escalation) | Technique (zero/few-shot/CoT + why) | Context budget (tokens per section) | Cache design (stable prefix, expected hit %) | Prompt version + date`

## 3. Integration Security Review (Module 3)
| Tool | Agent | Type (R/W/irreversible) | Uses (evidence) | Keep/Remove/Gate | AuthZ & limits | Credential scope |
|---|---|---|---|---|---|---|

Protocol per integration: `System | MCP / API / CLI / A2A | Why | Trust/vetting | Version pinning`

## 4. RAG & Observability Design (Module 4)
`Doc shapes → parsing | Chunking strategy + size tested | Index fields (source, version, dates, ACL) | Retrieval (keyword/vector/hybrid + why) | Rerank + top-k | Citation & 'I don't know' policy | Refresh: versioned + atomic swap, stale eviction | Logs per request | Dashboards & alerts (owner, runbook link)`

## 5. Eval Plan & Metrics Sheet (Module 5)
| Metric | Grader | Threshold | Baseline | Subsets reported |
|---|---|---|---|---|
Test set: `golden __% | edge __% | regression __% | adversarial __% | total cases ___ | CI gate: ___ | Human calibration cadence: ___`

## 6. Guardrail & Compliance Matrix (Module 6)
| Risk | Layer (input/model/tool/output/human/detective) | Type (prevent/detect/correct) | Control | HITL point & SLA | Compliance (GDPR/HIPAA/FedRAMP) | Owner |
|---|---|---|---|---|---|---|

## 7. Decision Record (ADR) + Handoff Pack (Module 7)
**ADR:** `Title | Date | Status | Context | Options | Decision | Consequences (+/−) | Evidence links | Review trigger`
**Handoff:** ☐ diagram+ADRs ☐ prompt/model versions ☐ eval suite+how to run ☐ dashboards+runbooks ☐ tool inventory+credential rotation ☐ compliance matrix ☐ cost model ☐ limitations+roadmap ☐ on-call contacts

## 8. Readiness Scorecard (Module 8)
| Domain | Weight | Trainer % | Mock % | Weighted pts | Next action |
|---|---|---|---|---|---|
| D1 / D2 / D3 / D4 / D5 / D6 / D7 | 17/13/19/16/14/14/7 | | | | |

Timed attempts: `#1 date/score ___  #2 date/score ___ | Decision: book / study ___ more days | Verify official pass mark & policies before booking.`
