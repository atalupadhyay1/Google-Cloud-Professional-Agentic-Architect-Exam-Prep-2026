# Original Scenario Practice — 20 Questions

These are original learning questions written for this repository, mapped to the published Professional Agentic Architect exam guide. They are **not** official Google questions, exam dumps, or a prediction of a passing score. Try the questions before opening the answer key. For each one, name the constraint that decides the answer and explain why the tempting option is unsafe or unnecessarily complex.

---

## Questions

### Domain 1 — Building agents using low-code tools

**1. A support agent answers routine VPN questions from an internal search source. Some users belong to a contractor group that cannot read the employee-only VPN runbook. The low-code workflow currently sends the top search result to the model and tells it not to reveal contractor-only information. What is the most important design change?**

A. Increase the model’s reasoning budget so it can identify restricted documents.<br>
B. Apply caller/tenant authorization during retrieval so unauthorized content never enters the model context.<br>
C. Remove all source citations from the final answer.<br>
D. Add a few-shot example where the model refuses a contractor.

**2. A field-support agent answers questions about a safety procedure recorded in a video. A transcript is ingested, but users need the agent to identify the step and where it occurs. Which design best supports a reviewable answer?**

A. Store only the generated summary and ask the model to infer the time of the step.<br>
B. Preserve the video’s approved access metadata and source version, and return a grounded answer with a transcript segment or timestamp when supported.<br>
C. Give the agent permission to search every video in the company drive.<br>
D. Use a larger model; multimodal source provenance is unnecessary if the answer sounds right.

**3. A workflow answers a question that is not covered by any approved source. The product owner asks that the agent “always give something useful.” What is the safest useful behavior?**

A. Generate a likely answer from the model’s general knowledge and label it internal guidance.<br>
B. Retry retrieval indefinitely until a result appears.<br>
C. Say that approved evidence was not found, ask a focused clarification or route to the named support queue.<br>
D. Return the highest-scoring result even if its source is stale.

**4. A low-code flow uses a prompt template that asks the model to reveal its complete private reasoning to make answers auditable. What is a better audit design?**

A. Keep the full private reasoning in every response and log it permanently.<br>
B. Ask for a concise user-facing explanation with approved citations, and record a privacy-safe trace of states, evidence IDs, tool outcomes, and policy decisions.<br>
C. Remove all explanations and all logs.<br>
D. Allow the model to choose which governance logs to retain.

### Domain 2 — Using coding agents for application development

**5. A coding agent must refactor a service and run unit tests. It asks for an engineer’s broad personal cloud credentials and unrestricted network access. What should the team do?**

A. Provide the credentials temporarily; remove them after the agent completes.<br>
B. Use a disposable, isolated workspace, synthetic fixtures, scoped repository/tool access, and a test runner; deny broad network and secrets unless a separately approved task requires them.<br>
C. Put the credentials in the system prompt so they are not checked into source code.<br>
D. Disable code review because the agent can run tests.

**6. A coding agent proposes changing a database lookup from string concatenation to a parameterized query. Which evidence is strongest before review?**

A. The agent explains that its patch is secure.<br>
B. A screenshot of the final code editor.<br>
C. A known baseline, a minimal diff, regression tests for valid input, an injection-oriented test showing input remains data, and a human review of the diff.<br>
D. A clean build only.

**7. A newly discovered MCP server exposes `read_file`, `run_tests`, `shell`, and `upload_directory`. The requested task is a local unit-test run. What is the safest next step?**

A. Trust the server because MCP provides a standard protocol.<br>
B. Enable all tools and rely on the coding agent’s system instructions.<br>
C. Verify the server and tool behavior, then allow only the needed scoped test capability; keep arbitrary shell and upload denied.<br>
D. Let a subagent decide which tools are safe.

**8. An organization wants subagents for code review, test generation, and dependency analysis. Which control is most important when splitting work?**

A. Send each subagent the entire repository history, all secrets, and the user’s full conversation.<br>
B. Give each subagent a defined role, minimal context and tools, scoped identity, explicit handoff schema, and a reviewable result.<br>
C. Allow subagents to approve and merge one another’s changes.<br>
D. Reuse one global identity so that the traces are shorter.

### Domain 3 — Developing custom agents

**9. A support workflow handles short FAQ lookups. It has a strict data boundary, moderate quality needs, and a low latency budget. How should the team choose a model?**

A. Select the largest available model; it will satisfy every requirement.<br>
B. Compare appropriate model/hosting candidates against a representative evaluation set for quality, latency, cost, privacy, and availability; use deterministic code for parts that do not need a model.<br>
C. Choose an open-source model solely because it is open source.<br>
D. Choose a SaaS model solely because it needs less infrastructure.

**10. A managed session store keys conversation state only by a caller-supplied `session_id`. Two tenants can accidentally submit the same value. What is the best fix?**

A. Make session IDs longer but continue trusting them as identity.<br>
B. Derive the access key from authenticated tenant, user, and session context; keep long-term memory separate and explicitly scoped.<br>
C. Put all sessions in a shared namespace to simplify retrieval.<br>
D. Disable authentication for read-only conversations.

**11. A vector search returns a highly similar confidential HR document for a user outside the HR group. What should the RAG pipeline do?**

A. Give it to the model but remove the citation from the final answer.<br>
B. Use a higher similarity threshold.<br>
C. Filter candidates by the authenticated caller’s authorization before their content reaches the model; then rank only permitted sources.<br>
D. Let the model decide whether the user seems trustworthy.

**12. A travel-planning agent needs a calendar tool and must delegate a flight-research task to a separate approved agent. Which protocol distinction is most accurate?**

A. MCP is generally used to expose tools/context; A2A is designed for task-oriented communication between agents. Either still requires identity and authorization checks.<br>
B. MCP and A2A are interchangeable labels for vector search.<br>
C. A2A authorizes an agent to call every discovered tool.<br>
D. MCP proves that a tool server is safe.

**13. A custom agent uses a read-only database capability and a simulated SaaS status tool. The SaaS call times out. What is the best behavior?**

A. Retry forever to avoid disappointing the user.<br>
B. Switch to a broader service identity and repeat the call.<br>
C. Return a truthful timeout/unknown status, apply only bounded safe retry policy, and hand off if necessary; do not claim success.<br>
D. Ask the model to invent the likely ticket status.

### Domain 4 — Evaluating and deploying agentic workflows

**14. A new agent version gives more fluent answers but sometimes cites a stale source and calls the wrong tool. What should the release evaluation add?**

A. Exact-match comparison of final text only.<br>
B. A reviewed golden set checking response, source freshness/citation, tool selection and arguments, trajectory, edge cases, and safety behavior.<br>
C. A single live demo with the product owner.<br>
D. A larger model as the only release control.

**15. Which dataset best supports continuous agent evaluation?**

A. Only the requests where the current agent already succeeds.<br>
B. A reviewed set of synthetic or approved cases with expected outcomes, sources/tool behavior, ordinary cases, and edge cases such as no evidence, denial, timeout, and prompt injection.<br>
C. An unlabelled dump of every production conversation, including secrets.<br>
D. A set of questions that all expect the same “answered” status.

**16. A containerized, request-driven API needs managed deployment and does not need Kubernetes-level control. The team wants to minimize infrastructure operations. Which runtime is the best initial candidate among Agent Runtime, Cloud Run, and GKE?**

A. GKE by default, regardless of control needs.<br>
B. Cloud Run as a candidate for the request-driven container, after validating startup, deadlines, state, scaling, and cost requirements.<br>
C. Agent Runtime because every agent must run there.<br>
D. A self-managed VM because managed services cannot be secured.

**17. A multiagent workflow sometimes repeats the same tool call and its tail latency is growing. What is the most useful first operational response?**

A. Increase retries and hide the trace from users.<br>
B. Inspect correlated, privacy-safe traces for loop count, tool latency, errors, and workflow state; set step/time limits and verify a rollback threshold.<br>
C. Log all prompts, access tokens, and retrieved documents permanently.<br>
D. Disable evaluation after a release to reduce cost.

### Domain 5 — Securing and governing agentic workflows

**18. An agent calls a SaaS API on a user’s behalf. Which authorization pattern is safest?**

A. Put a long-lived bearer token in the prompt so the model can decide how to use it.<br>
B. Use an approved delegated identity flow with the narrowest required scope, validate audience/expiry, protect short-lived credentials, and enforce the resource/action policy in the application and tool.<br>
C. Use a project-owner credential to prevent permission errors.<br>
D. Treat successful authentication as proof that every action is authorized.

**19. A principal has a permission to read a resource but a Principal Access Boundary excludes that resource. How should an architect reason about the boundary?**

A. A PAB grants any access required for the task.<br>
B. A PAB constrains the resource set; it is not itself a permission grant. Effective access still depends on applicable permissions and policy.<br>
C. The agent can ignore the boundary if Agent Registry lists its capability.<br>
D. The model can override the boundary by asking for human approval.

**20. A Model Armor check detects suspicious text, but the workflow also has a tool capable of deleting customer records. What is the best layered design?**

A. Rely on the content filter as the only control for deletion.<br>
B. Remove the tool’s authorization checks because Model Armor blocks unsafe prompts.<br>
C. Keep least-privilege identity and tool authorization, validate the exact target/action, use policy/content checks, require action-specific human approval for high-impact deletion, and audit safely.<br>
D. Let the agent register the deletion tool itself.

---

## Answer key and reasoning

### Domain 1

**1. B.** Retrieval relevance and authorization are separate. Filter by authenticated tenant/group policy before content enters the model. Prompt examples (D) may help behavior but cannot enforce access; model capacity (A) does not solve authorization; removing citations (C) hides evidence without stopping a leak.

**2. B.** A reviewable multimodal answer needs approved access metadata and provenance such as source/version and a grounded segment or timestamp when available. A summary alone (A) can lose location and uncertainty; broad access (C) is overprivileged; model size (D) cannot create missing provenance.

**3. C.** Correct abstention, focused clarification, or a named human route is useful and safe. A likely answer (A) is ungrounded; indefinite retries (B) can create cost/latency loops; stale evidence (D) is not an answer merely because it ranks first.

**4. B.** Give users concise evidence-backed explanations and keep privacy-safe operational traces. Private reasoning is not a required audit artifact. Permanent reasoning logs (A) create privacy and security risk; no logs (C) harms operations; letting the model choose retention (D) bypasses governance.

### Domain 2

**5. B.** Use an isolated, disposable environment, synthetic data, scoped tools, and deny-by-default network/secret access. Temporary broad credentials (A) remain exposed during the task; prompts are not secret stores (C); tests do not replace code review (D).

**6. C.** Strong evidence combines baseline, minimal diff, behavior regression, security-specific checks, and human review. An agent assertion (A), screenshot (B), or build-only result (D) does not establish the security property.

**7. C.** MCP standardizes interaction; it does not establish server trust or capability safety. Vet the server and expose only the required capability. Options A, B, and D outsource authorization to protocol, prompt, or another agent instead of enforcing it.

**8. B.** Delegation creates data, identity, and tool boundaries. Minimize context and authority, make the handoff typed, and review outputs. Full history/secrets (A), autonomous merging (C), and shared global identity (D) increase blast radius and weaken attribution.

### Domain 3

**9. B.** Model choice is a measured trade-off across quality, latency, cost, data boundary, availability, and hosting. The largest model (A) can be slower and more expensive; open source (C) and SaaS (D) are deployment choices, not universal answers.

**10. B.** Bind state to authenticated tenant, user, and session. A longer caller-chosen string (A) is still not identity; shared namespaces (C) leak data; disabling authentication (D) is not acceptable.

**11. C.** Apply authorization before content reaches the model. A threshold (B) is not an ACL; hiding the citation (A) does not undo context exposure; model judgement (D) is not authorization.

**12. A.** MCP is the tool/context connection; A2A supports agent-to-agent task interaction. Neither protocol grants access or establishes trust. Options B–D confuse protocol roles with retrieval, authorization, or security attestation.

**13. C.** Distinguish timeout from success; retry only within a safe, bounded policy and hand off when appropriate. Infinite retries (A) waste resources; switching identity (B) is escalation; guessing (D) fabricates state.

### Domain 4

**14. B.** Evaluate the full system path: response, source freshness, tool, trajectory, and safety. Final text only (A) misses operational and security behavior; a demo (C) is too small; a larger model (D) does not fix the release process.

**15. B.** A reviewed representative set needs expected outcomes and failure/edge cases, handled with appropriate data controls. Success-only data (A) hides risks; raw production dumps (C) can expose sensitive data and lack labels; same-status cases (D) fail to test abstention and handoff.

**16. B.** Cloud Run is a plausible first candidate for a request-driven container without Kubernetes control, subject to runtime-specific validation. GKE (A) adds unnecessary ops; Agent Runtime (C) is not mandatory for every agent; managed services can be securely configured (D).

**17. B.** Correlated traces reveal repeated steps and latency bottlenecks; limits and rollback protect users. More retries (A) amplify loops; indiscriminate logging (C) creates risk; disabling evaluation (D) removes an important release signal.

### Domain 5

**18. B.** Use a scoped, approved delegation model and validate identity/token properties plus application/resource policy. Prompts (A) are not secret stores; broad credentials (C) violate least privilege; authentication (D) is not authorization.

**19. B.** A boundary limits resource reach; it does not grant the permissions needed to act. Registry metadata (C) and a human approval (D) do not make a denied resource accessible. Follow current Google Cloud policy semantics for implementation.

**20. C.** Safety controls are layered: identity, narrow tools, target validation, policy/content review, specific human approval, and auditable outcomes. Model Armor is not a substitute for authorization. Options A/B over-trust a content filter; D lets the agent grant itself capability.

## Review your result

Do not turn 20 questions into a pass/fail prediction. For every missed or uncertain question, note:

- the primary domain and concept;
- the constraint you missed;
- why each distractor is unsafe or mismatched;
- a lab or documentation page that would close the gap;
- whether you can demonstrate the same principle in a failure-path test.

For current exam timing and eligibility, use Google’s [official certification FAQ](https://support.google.com/cloud-certification/answer/18080541?hl=en). The practice questions are original study aids, not official test items.
