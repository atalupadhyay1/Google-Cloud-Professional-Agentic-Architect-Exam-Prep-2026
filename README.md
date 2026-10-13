# Claude Certified Architect – Professional (CCAR-P)
## Extensive Study Material, Detailed Concepts & Complete Hands-On Labs
### Beginner → Advanced | Step-by-Step | Humanised, Practical, Exam-Focused

> **Independent study material.** This repository is **not affiliated with, sponsored by, or endorsed by Anthropic or Udemy**. It is an original study guide created from the *publicly listed course/exam outline* for: **“Claude Certification CCAR-P: Exam Trainers + Mock Exam”** (PapaHR / Mike Pritula, Udemy).  
> No real exam questions, dumps, or copyrighted course content are reproduced. All explanations, labs, templates, and practice questions here are original.
>
> **Source outline referenced:** https://www.udemy.com/course/claude-certification-ccar-p-exam-trainers-mock-exam/  
> Always confirm current exam details on Anthropic's official Partner Academy / exam guide pages — models, pricing, limits, and protocols change.

---

## Who this is for (in plain human language)

Imagine you can already *use* Claude. You can write a prompt, call the API, maybe you even shipped a chatbot.

This guide is for the next step: **thinking like an architect.**

An architect doesn't just ask *"Can Claude do this?"*  
An architect asks:

- *Should* this be a simple workflow, an augmented LLM, or a full agent — and what will each choice cost in money, latency, and risk?
- Which model, which prompt structure, and what do we cache?
- Which tools does this system *actually* need — and which ones are a security incident waiting to happen?
- When the RAG system starts answering confidently-and-wrongly, where do I look *first*?
- How do I *prove* a change made things better (not just feel it)?
- Where must a human stay in the loop, and what do GDPR / HIPAA / FedRAMP demand from my design?
- How do I explain and defend all of this to stakeholders, then hand it over so a team can run it without me?

If those questions feel familiar — or intimidating — you're in the right place. We start at beginner level and build, step by step, to professional architect judgment.

---

## How this repository is organised (course structure preserved)

The original course has **8 sections / 8 lectures / ~6h 06m**, built around the **7 CCAR-P exam domains**. This guide preserves that exact structure and expands every lecture into: concepts + worked examples + hands-on lab + exam trainer + templates + checklist.

| # | Course Section (preserved) | Exam Domain & Weight* | Your Study Guide | Hands-On Lab |
|---|---|---|---|---|
| 1 | Claude Solution Architecture: Design Patterns and Multi-Agent Systems (46 min) | Domain 1 — Solution Design & Architecture Patterns **(17%)** | [`docs/01-solution-architecture.md`](docs/01-solution-architecture.md) | Lab 1 |
| 2 | Claude Models and Prompt Engineering: System Prompts, Prompt Caching (47 min) | Domain 2 — Models, Prompting & Context Engineering **(13%)** | [`docs/02-models-prompt-context-engineering.md`](docs/02-models-prompt-context-engineering.md) | Lab 2 |
| 3 | Claude Integration: MCP, API, Agent-to-Agent and Least Privilege (45 min) | Domain 3 — Integration **(19%, part 1)** | [`docs/03-integration-mcp-security.md`](docs/03-integration-mcp-security.md) | Lab 3 |
| 4 | RAG Pipeline Design for Claude: Chunking, Retrieval and Observability (46 min) | Domain 3 — Integration **(19%, part 2)** | [`docs/04-rag-pipelines-observability.md`](docs/04-rag-pipelines-observability.md) | Lab 4 |
| 5 | LLM Evaluation for Claude: Evals, A/B Testing, Cost and Latency (46 min) | Domain 4 — Evaluation, Testing & Optimisation **(16%)** | [`docs/05-evaluation-testing-optimisation.md`](docs/05-evaluation-testing-optimisation.md) | Lab 5 |
| 6 | AI Governance and Safety: Guardrails, Human in the Loop, GDPR, HIPAA (46 min) | Domain 5 — Governance, Safety & Risk **(14%)** | [`docs/06-governance-safety-compliance.md`](docs/06-governance-safety-compliance.md) | Lab 6 |
| 7 | AI Solution Delivery: Discovery, Decision Records, SLAs, Claude Code (44 min) | Domain 6 — Stakeholder Communication **(14%)** + Domain 7 — Developer Productivity & Claude Code **(7%)** | [`docs/07-delivery-stakeholders-claude-code.md`](docs/07-delivery-stakeholders-claude-code.md) | Lab 7 |
| 8 | CCAR-P Mock Exam: 63 Practice Questions, Timer and Readiness Score (46 min) | All 7 domains | [`docs/08-exam-strategy-and-mock-exam.md`](docs/08-exam-strategy-and-mock-exam.md) | Lab 8 (timed mock) |

\* Weights as listed on the public course page. **Verify against the current official exam guide** — treat any third-party weight as a study-planning aid, not a contract.

**Start here first:** [`docs/00-start-here-blueprint-and-study-plans.md`](docs/00-start-here-blueprint-and-study-plans.md)

---

## Complete map of this repo

```
.
├── README.md                                   ← you are here
├── docs/
│   ├── 00-start-here-blueprint-and-study-plans.md   Blueprint, personas, 14-day / 6-week / 12-week plans
│   ├── 01-solution-architecture.md
│   ├── 02-models-prompt-context-engineering.md
│   ├── 03-integration-mcp-security.md
│   ├── 04-rag-pipelines-observability.md
│   ├── 05-evaluation-testing-optimisation.md
│   ├── 06-governance-safety-compliance.md
│   ├── 07-delivery-stakeholders-claude-code.md
│   └── 08-exam-strategy-and-mock-exam.md
├── labs/
│   ├── README.md                               Lab setup (runs WITHOUT an API key in mock mode)
│   ├── lab01_pattern_selector.py               Workflow vs augmented LLM vs agent — cost/latency simulator
│   ├── lab02_prompt_caching_cost.py            Token & prompt-caching cost simulator
│   ├── lab03_tool_scope_auditor.py             Least-privilege / capability-bloat auditor
│   ├── lab04_rag_pipeline.py                   Mini RAG: chunk → embed (hashing) → retrieve → rerank → cite
│   ├── lab05_eval_harness.py                   Eval harness: graders, thresholds, regression detection
│   ├── lab06_guardrail_matrix.py               Risk → guardrail → human-review mapper
│   ├── lab07_adr_and_sla.py                    Architecture Decision Record + SLA/SLO generator
│   └── lab08_readiness_score.py                Readiness score vs scaled pass mark (720-style)
├── templates/
│   └── architect-kit.md                        All 8 course tools in one copy-paste kit
├── practice/
│   ├── domain-trainers.md                      84-style trainer: 12 original Qs per domain area (with “why wrong options fail”)
│   └── mock-exam-63.md                         Full 63-question original mock (answer key + domain tagging at end)
└── cheatsheets/
    └── exam-day-cheatsheet.md                  One-page traps, decision tables, mnemonics
```

---

## How to study (the method that actually works)

**For every module, in this order — don't skip steps:**

1. **Read the “human story” opener.** It tells you *why this matters* before any jargon.
2. **Learn the concepts** with the diagrams (Mermaid) and decision tables.
3. **Do the worked example** on paper. Say your reasoning out loud, like you're defending it to a client.
4. **Run the hands-on lab.** Break it on purpose. Change one variable. Predict, then observe.
5. **Use the template** to produce a real artefact (canvas, spec, matrix, ADR…).
6. **Sit the domain trainer** in [`practice/domain-trainers.md`](practice/domain-trainers.md). For every wrong option, you must be able to say *why it fails* — that's the Professional-level skill.
7. **Tick the checklist** at the end of the module. If you can't tick it honestly, loop back — that's not failure, that's the process.

> 💡 **Beginner note:** If terms like *MCP, RAG, evals, chunking* are new, start with `docs/00` (it has a full glossary in plain English), then go in order 1→8. Nothing here assumes you already ship Claude in production — we build that intuition with labs that run **without any API key**.

> 🎯 **Experienced note:** If you already ship Claude systems, skim the beginner boxes, but *do not skip the decision tables, anti-patterns, and “exam traps”* — the exam tests judgment between four plausible answers, not recall.

---

## Quick facts (from the public course page — verify officially)

| Item | Detail |
|---|---|
| Exam | Claude Certified Architect – Professional (CCAR-P) |
| Format | 63 questions, 120 minutes, multiple-choice + multiple-response (“choose two”) |
| Scaled pass mark | 720 (as referenced in the course) — confirm current value officially |
| Retake (as referenced in course) | Failed attempt cost ~$175 and ≥14 days wait were cited on the course page — **verify current pricing/policy officially** |
| Recommended background (exam guide, via course page) | 3+ years systems architecture, 6+ months production work with Claude or similar LLMs |
| Course includes | 7 interactive exam trainers (84 Qs), study games (flashcards/memory/match), 63-Q mock, architect's kit of 8 tools |
| Prerequisites (course) | Hands-on Claude API / tools / MCP / Claude Code / production prompts; Foundations mechanics are not repeated there — **this guide does cover the foundations you need, in plain language** |

---

## Run the labs in 2 minutes

```bash
git clone <this-repo> && cd Google-Cloud-Professional-Agentic-Architect-Exam-Prep-2026
python3 labs/lab01_pattern_selector.py     # no API key, no pip install needed (stdlib only)
python3 labs/lab04_rag_pipeline.py
python3 labs/lab08_readiness_score.py
```

See [`labs/README.md`](labs/README.md) for all labs, expected outputs, and “break-it” exercises. Optional: if you have an Anthropic API key, each lab doc shows how to swap the mock model call for a real one — **never commit API keys**.

---

## A note on honesty & currency

Claude models, pricing, context limits, MCP specs, and compliance guidance change every few months. This guide teaches **durable architect judgment** (patterns, trade-offs, failure diagnosis) and clearly marks volatile facts with “⚠️ verify”. Where a number is used in a lab, it is an *illustrative teaching number*, not a price quote.

**Good luck. Study like an architect: decide, measure, defend, hand over.** 🚀
