# Module 7 — AI Solution Delivery: Discovery, Decision Records, SLAs & Claude Code
**Course Section 7 (44 min) • Domain 6: Stakeholder Communication (14%) + Domain 7: Developer Productivity & Claude Code (7%)**  
*Tools from the course: Decision Record & Handoff Pack • Exam Trainers D6 + D7 • Study games*

---

## 1. The human story

The technically best system in this guide can still fail in the most human way: the sponsor expected a fully autonomous agent, the team built a supervised assistant, Legal hears about the data flows at launch, and six months later nobody on the support team knows what to do when accuracy dips. **Delivery is an architecture property.** Discovery, recorded decisions, agreed service levels, documentation, and a runbook are what let a system survive contact with an organisation — and survive *you* going on holiday.

### Learning objectives
1. Run structured discovery & requirement gathering.
2. Write Architecture Decision Records (ADRs) and align expectations early.
3. Agree SLAs/SLOs and manage the lifecycle: discovery → handoff → monitoring → iteration.
4. Enable teams with Claude Code & AI-assisted developer workflows, safely; debug operations.

---

## 2. Structured discovery (step-by-step)

**Step 1 — Stakeholder map:** Sponsor (funds, decides), users (live with it), operators (run it), risk owners (Legal/Security/Compliance), data owners. Missing one = a launch-day surprise.
**Step 2 — Problem before solution:** Current process, volumes, pain cost, failure cost, “what happens today when this goes wrong?” (Revisit Module 1's value method.)
**Step 3 — Requirements in testable language:**
- *Functional:* “Draft replies citing policy” → testable via eval.
- *Non-functional:* latency/cost/quality/safety SLAs, data residency, retention, languages, accessibility.
- *Constraints:* budget, timeline, systems of record, prohibited data/actions.
**Step 4 — Surface the hard trade-offs early** with options + numbers (pattern/model choices from Modules 1–2): “Autonomous = faster, needs these guardrails + reviewers; Supervised = slower, safer.” Let stakeholders *choose with eyes open* — then record it (ADR).
**Step 5 — Define success + stop/adjust criteria** before building: eval thresholds (Module 5), pilot scope, rollout gates.
**Step 6 — Expectation alignment ritual:** demo limitations honestly (show a failure case!), agree what the system will *never* do, name the human owner on call.

> Communication craft the exam rewards: translate tech into **value, cost, risk, and SLA** language for each audience. Engineers get architecture; executives get trade-offs and numbers; users get what changes in their day + how to appeal/correct the AI.

## 3. Architecture Decision Records (ADRs)

One page per significant decision. **Template (in architect-kit):**
`Title | Date | Status | Context (forces, constraints) | Options considered | Decision | Consequences (+ and −) | Evidence (eval/pilot links) | Review trigger`

Example ADR titles from this course: “ADR-003: Routed workflow instead of autonomous agent for refunds”, “ADR-007: Hybrid retrieval + reranker for policy RAG”, “ADR-011: Fast-tier router with capable-tier escalation”.

**Why ADRs win exam marks:** stems asking “team disagrees / new lead questions a choice / auditor asks why” → answer is *consult/update the decision record with evidence*, not “rebuild it” or “the architect decided”. Review triggers matter: “revisit when volume > X or new model tier launches.”

## 4. SLAs, lifecycle & handoff

| Lifecycle stage | Key artefacts | Exit criteria (examples) |
|---|---|---|
| Discovery | Stakeholder map, value hypothesis, constraints | Sponsor signs problem + success metric |
| Design | Canvas, model/prompt spec, security review, RAG design, compliance matrix | ADRs for major choices; eval plan exists |
| Build/Pilot | Working system on limited scope, eval suite | Thresholds met on pilot cohort |
| Launch | SLA/SLO agreement, runbook, training | Gradual rollout + monitoring dashboards live |
| Operate | Incident playbook, cost/quality reviews | On-call owner named; review cadence set |
| Iterate/Handoff | Handoff pack (below), regression suite | Receiving team runs a game-day without you |

**SLA vs SLO (plain):** SLO = internal target you engineer to (p95 latency, accuracy proxy). SLA = external promise with consequences. Agree: metrics, measurement method, review cadence, what happens on breach. Never promise an SLA you don't measure (Module 4/5 observability is the measurement).

**Handoff pack checklist:** architecture diagram + ADRs • prompt/model specs with versions • eval suite + how to run it • dashboards + alert→runbook links • tool inventory + credential rotation guide • compliance matrix + data flows • cost model + budgets • known limitations + roadmap • contacts/escalation.

**Operational debugging (triage order):** recent change? (prompt/model/index deploy) → observability: which stage degraded (retrieval vs generation vs tools) → eval replay on failing cases → rollback or fix → add regression case. Sound familiar? It's Modules 4+5 under pressure.

## 5. Claude Code & developer productivity (Domain 7)

Claude Code is Anthropic's agentic coding assistant (terminal/IDE workflows: explore codebase, plan, edit, run tests, review). ⚠️ *Verify current features/commands officially — tooling evolves monthly.*

**Architect-level principles (the examinable part):**
- **Workflow:** give context (relevant files/constraints) → ask for a plan → review the plan → implement in small steps → run tests/evals → human reviews the diff. The human remains the accountable engineer.
- **Guardrails for coding agents:** least-privilege repo/tool access (Module 3 applies to dev agents too!), no secrets in context, protected branches + PR review, test gates, sandbox for generated commands, audit trail of changes.
- **Team enablement:** shared project instructions/conventions for the assistant, reusable prompts/skills for recurring tasks (test generation, migration, docs), measured outcomes (cycle time, defect rate — not “lines generated”).
- **Anti-patterns:** unreviewed bulk merges, pasting production data/secrets into sessions, measuring productivity by output volume, skipping tests “because AI wrote it”.

## 6. Hands-On Lab 7 — ADR + SLA Generator & Handoff Drill
**Run:** `python3 labs/lab07_adr_and_sla.py` — answer its prompts for your Lab-1 scenario; it emits a draft ADR + SLA table.
1. Swap roles: hand your pack to a peer (or future-you in 7 days). Can they answer: *why this pattern? what breaks first? what do I do at 3 a.m.?*
2. **Break-it:** Delete the “review trigger” from your ADR. When would the decision silently expire? Add one back.
**Deliverable:** Decision Record + Handoff Pack (templates).

## 7. Exam traps & flashcards
**Traps:** ① Building before discovery/constraints ② Decisions in chat threads, unrecorded ③ Promising unmeasured SLAs ④ Handoff = code dump without runbook/evals ⑤ Coding agent with broad access + no review gate.
**Flashcards:** “Why did we choose X?” → *ADR with evidence + review trigger* • Launch readiness → *measured SLOs, runbook, named owner* • AI-written code ships when → *tests + human PR review pass*.
**Trainer:** Domains 6+7 Qs. **Checklist:** ☐ Stakeholders incl. risk owners mapped ☐ Top decisions have ADRs ☐ SLAs are measured ☐ Handoff pack passes the “3 a.m.” test.
**Next →** [`08-exam-strategy-and-mock-exam.md`](08-exam-strategy-and-mock-exam.md)
