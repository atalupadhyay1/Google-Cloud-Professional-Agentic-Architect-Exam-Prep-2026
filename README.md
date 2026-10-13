# Google Cloud Professional Agentic Architect — 2026 Study Guide

A course-aligned, original companion workbook for the [**Google Cloud Professional Agentic Architect Exam Prep 2026** Udemy course](https://www.udemy.com/course/google-cloud-professional-agentic-architect-exam-prep-2026/). It keeps the course's four-section, eight-lesson order and adds beginner-to-advanced explanations, seven runnable local lab drills, review questions, and a practical study plan.

> **Scope and exam note (checked 13 October 2026):** Google describes this as a hybrid certification: a proctored multiple-choice component and a separate hands-on lab component. The beta window (8–30 September 2026) has closed; Google’s published FAQ says the generally available version will use a two-hour multiple-choice session and that candidates who pass then complete separate labs. Dates, exam details, service names, and product behavior can change. Check the [official exam guide](https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf), [certification FAQ](https://support.google.com/cloud-certification/answer/18080541?hl=en), and [Google Skills learning path](https://www.skills.google/paths/4525) before booking.
>
> This is independent study material, not a Google publication, not affiliated with or endorsed by Google, and not a reproduction of the Udemy lessons. The local labs are educational simulations—not Google’s assessed certification labs. They make no cloud calls, use no credentials, and incur no cloud charges.

## Start here

1. Read [`docs/study-guide.md`](docs/study-guide.md) in course order. Each lesson follows **what → why → how → trade-offs → exam lens**.
2. Open [`docs/lab-workbook.md`](docs/lab-workbook.md) and work through the seven lab drills. Each one names the evidence to save and a failure case to test.
3. Run the local reference implementation and its tests:

   ```bash
   python --version                 # Python 3.10+
   python -m labs.agentic_workshop.demo
   python -m unittest discover -s labs/tests -v
   ```

4. Complete the final capstone, then use Lesson 8’s readiness worksheet. Track question performance and independent lab execution as **separate** signals.

No third-party Python packages are required. No Google Cloud project is required. Optional cloud adaptation notes are clearly marked; only try those with an authorized sandbox, least-privilege access, budget alerts, and a cleanup plan.

## Preserved course structure

| Course section | Lesson | Study guide | Hands-on drill |
|---|---|---|---|
| Google Cloud Low-Code Agents and Coding Agent Lab Drills | Build Low-Code Agents | Lesson 1 | Lab 1 — bounded support workflow |
|  | Use Coding Agents Safely | Lesson 2 | Lab 2 — sandboxed code-change review |
| Custom Agents, Memory and Enterprise Knowledge Integration | Build Custom Agents and Memory | Lesson 3 | Lab 3 — custom agent and isolated memory |
|  | Connect Enterprise Knowledge and Tools | Lesson 4 | Lab 4 — grounded retrieval and scoped tools |
| Multiagent Orchestration, Agent Evaluation and Deployment | Orchestrate Multiagent Workflows | Lesson 5 | Lab 5 — typed handoffs and failure-aware orchestration |
|  | Evaluate and Operate Agentic Workflows | Lesson 6 | Lab 6 — golden set, release gate, and runtime choice |
| Agent Security, Governance and Full Mock Exam Preparation | Secure and Govern Agentic Workflows | Lesson 7 | Lab 7 — identity, policy, redaction, and approval |
|  | Exam Strategy, Mock Exam and Labs | Lesson 8 | Capstone — run, inspect, and plan your next study cycle |

## What is included

- [`docs/study-guide.md`](docs/study-guide.md) — concepts, architecture patterns, step-by-step design methods, trade-offs, mistakes to avoid, knowledge checks, glossary, and official references.
- [`docs/lab-workbook.md`](docs/lab-workbook.md) — seven beginner-to-advanced drills with objectives, setup, actions, expected observations, failure-path tests, evidence records, cleanup, and optional Google Cloud mapping.
- [`docs/scenario-practice.md`](docs/scenario-practice.md) — 20 original scenario questions with answer reasoning mapped across all five domains (not official exam items).
- [`labs/agentic_workshop/`](labs/agentic_workshop/) — deterministic, standard-library-only reference exercises, plus sample data.
- [`labs/tests/`](labs/tests/) — executable checks for grounding, tenant isolation, authorization, handoffs, evaluation, and safety behavior.

## Suggested pace

- **Week 1:** Lessons 1–2 and Labs 1–2; practice workflow boundaries and safe coding-agent use.
- **Week 2:** Lessons 3–4 and Labs 3–4; build a custom-agent mental model and trace an answer back to authorized evidence.
- **Week 3:** Lessons 5–6 and Labs 5–6; design handoffs, test failure behavior, and make an evidence-based release decision.
- **Week 4:** Lesson 7 and Lab 7; run the capstone and do a timed practice attempt using the current official timing.

Adjust the plan to your own baseline. The exam-domain percentages are useful for allocating revision time, not a guarantee of the number of questions on a particular form.

## Landing page preview

A responsive, dependency-free course landing page is available at the repository root (`index.html`, `styles.css`, and `script.js`). Preview it locally with:

```bash
python -m http.server 8000 --bind 0.0.0.0
```

Then open `http://localhost:8000`. The page includes the course roadmap, practice overview, an interactive local workflow scenario, and FAQs. It links to the public Udemy course and official Google Cloud exam references; the workflow demo itself sends no data anywhere.
