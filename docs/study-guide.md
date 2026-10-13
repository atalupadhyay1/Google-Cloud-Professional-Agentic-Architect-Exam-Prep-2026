# Complete Study Guide: Google Cloud Professional Agentic Architect

**Edition:** course-aligned companion, checked 13 October 2026.<br>
**Audience:** a curious beginner who can read simple Python, through a practicing architect preparing to defend production decisions.<br>
**Purpose:** understand the *why* behind agentic architectures, practise the *how*, and learn to explain decisions from evidence rather than product-name memorization.

> This guide follows the [Udemy course’s](https://www.udemy.com/course/google-cloud-professional-agentic-architect-exam-prep-2026/) original four sections and eight lecture titles in order. It is original explanatory material, not a transcript or replacement for the course, current Google Cloud documentation, the official exam guide, or Google’s assessed labs. Product capabilities and names can change quickly; check the official links in [References](#references-and-change-control).

## How to use this guide

For every lesson, do these five things:

1. **Read the scenario first.** Say what the user needs, what the system is allowed to do, and what could go wrong.
2. **Learn the mental model.** Understand the components and the boundaries between them before learning a product label.
3. **Draw the path.** Show the user, agent, model, data, tools, identity, and human decision points. Mark trust boundaries.
4. **Run the matching lab.** The drills in [`lab-workbook.md`](lab-workbook.md) use a small local simulation so you can practise safely without a cloud account.
5. **Explain the trade-off aloud.** A good architecture answer says why it satisfies the stated constraints, what it deliberately does not do, and how failure is detected.

A “correct” agent is not one that sounds confident. It is one that returns a useful answer or action, stays within authority, exposes enough evidence to review, and fails safely when it lacks evidence or permission.

## Exam map and study weighting

The current official exam guide groups objectives into five sections. The approximate weights are useful when scheduling revision; they are not a promise about the number of questions in a particular exam form.

| Official domain | Approx. weight | Course lessons |
|---|---:|---|
| 1. Building agents using low-code tools | 13% | Lesson 1 |
| 2. Using coding agents for application development | 17% | Lesson 2 |
| 3. Developing custom agents | 33% | Lessons 3, 4, and 5 |
| 4. Evaluating and deploying agentic workflows | 22% | Lesson 6 |
| 5. Securing and governing agentic workflows | 15% | Lesson 7 |

Lesson 8 connects the five domains and prepares you to review the multiple-choice and practical portions separately. The official guide’s in-scope list includes ADK, agent evaluation, Agent Gateway, Agent Identity, Agent Registry, Agent Retrieval and Vector Search, Agent Runtime, Agent Search, A2A, MCP, Agents CLI, Antigravity, OAuth 2.0, BigQuery, Cloud Run, Cloud SQL, Cloud Storage, Firestore, Gemini Enterprise and Gemini models, Cloud Logging/Trace, GKE, Memorystore for Redis, Model Armor, Model Garden, RAG Engine, Sensitive Data Protection, and Skill Registry. Knowing why a component belongs in a design is more valuable than memorizing a list.

---

# Section 1 — Google Cloud Low-Code Agents and Coding Agent Lab Drills

## Lesson 1 — Build Low-Code Agents

### The scenario

A new employee, Maya, messages an internal support agent: “I’m starting my first shift and I can’t get my MFA device working. Can you help?” Maya deserves a kind, direct answer. She does **not** need to paste a password or one-time code into a chat, and the agent must not invent a reset procedure or grant itself account-administration privileges.

### What is a low-code agent?

A low-code agent is a configured workflow assembled mostly through a visual or declarative interface rather than a wholly custom program. It can still use models, enterprise search, tools, conditions, and human handoffs. “Low-code” describes how the workflow is built; it does **not** mean that the system is automatically safe, simple, or deterministic.

A useful mental model separates four jobs:

1. **Conversation policy** — what the agent may say, ask, and do.
2. **Workflow state** — where the interaction is and what event moves it forward.
3. **Knowledge and tools** — which approved information or actions it may use.
4. **Safety and operations** — how access, errors, review, and measurement work.

If these jobs are mixed into one long prompt, it becomes difficult to test the result. A workflow graph makes the control path inspectable.

### Why use states and transitions?

A **state** is a named point in the interaction, such as `collect_request`, `verify_scope`, `retrieve_evidence`, `answer`, or `handoff`. A **transition** is an explicit rule from one state to another. An **event handler** responds to a defined event—such as missing information, a tool timeout, a safety signal, or a user cancellation.

Think of the workflow as a train route. The model may help interpret what the passenger means, but the route decides which stations are reachable. A missing station should not be replaced with a confident guess.

Example support flow:

```text
START → understand request → check safety / authorization
                                 ├─ sensitive or privileged action → HUMAN HANDOFF
                                 ├─ missing details → ASK ONE CLARIFYING QUESTION
                                 └─ safe question → search approved sources
                                                        ├─ evidence found → answer with source
                                                        ├─ source unavailable → explain limitation / hand off
                                                        └─ search failed → retry within limit, then safe fallback
```

For Gemini Enterprise Agent Designer or CX Agent Studio, the screen names and configuration mechanics may differ by product release. The architecture questions remain the same: which states exist, which transitions are permitted, what data enters each state, what tool identity is used, and what happens on timeout or ambiguity?

### System instructions: a boundary, not an authorization system

Good instructions describe the agent’s role, permitted sources, response style, uncertainty behavior, and escalation boundary. Keep them specific and testable. For example:

> You are Northstar’s internal IT support assistant. Answer account-help questions only from approved support articles returned by the knowledge tool. Give a short, empathetic explanation and identify the article used. Never request or repeat passwords, one-time codes, recovery codes, or access tokens. Do not change account permissions. If the approved source does not answer the question, say what is missing and route the user to the support team.

This is useful behavioral guidance, but a prompt is not a security boundary. Enforce access in identity, tool permissions, data filtering, and workflow conditions too. A model can misunderstand or be manipulated; authorization must still deny an unapproved action.

Few-shot examples can clarify format and edge cases. Select them to represent ordinary, ambiguous, denied, and failure situations—not only ideal requests. Treat examples as data: do not put credentials or confidential customer records into a prompt template.

The exam guide mentions prompt techniques such as chain-of-thought as examples. For a production user interface, prefer a concise answer with cited evidence and an auditable decision summary rather than asking an agent to disclose private internal reasoning. The answer should be reviewable without exposing hidden reasoning traces.

### Connecting enterprise sources and multimodal content

An enterprise source is not “safe” merely because it is inside the organization. Before connecting it, answer:

- Who owns the source, and who may access it?
- Are permissions preserved during ingestion and at query time?
- What does “fresh” mean, and how are updates or deletions propagated?
- Which content is structured, unstructured, or multimodal?
- What is the expected source citation or provenance in the answer?

For image, audio, and video inputs, also consider transcription or extraction errors, timestamps, speaker attribution, sensitive content, file-size limits, and whether the source actually supports the answer. A transcript is an interpretation of the media, not the media itself. For a high-impact claim, retain a pointer to the original object and a location such as a page, frame, timestamp, or segment where available.

### Step-by-step design method

1. Write the user task in one sentence and list what is explicitly out of scope.
2. List the workflow states; keep each state responsible for one decision.
3. Draw every success, clarification, denied, timeout, no-evidence, cancellation, and human-review route.
4. Define inputs and outputs for each tool; use typed, minimal fields rather than an unrestricted “do anything” tool.
5. Attach sources to the answer path; filter by caller authorization before exposing retrieved content.
6. Write bounded instructions for tone and behavior; never rely on instructions as the sole access control.
7. Test representative examples plus adversarial and failure examples. Record actual transitions and outputs.
8. Review the workflow with a human owner. Confirm who handles each escalation and how quickly.

### Common mistakes

- One “agent” node has every tool and can decide its own access.
- Every failure route loops indefinitely or silently returns a plausible answer.
- A workflow answers from a search snippet without checking source version or access.
- The agent asks for a password or one-time code because it is trying to be helpful.
- A successful demo is treated as evidence that the workflow is reliable.

### Exam lens

When a prompt asks for a low-code workflow, look for **explicit states and routes**, **approved data access**, **bounded behavior**, and **testable fallback paths**. Choose a simple path for routine requests and an explicit human route for privileged or unsupported work. A choice that only improves conversational polish does not solve a missing authorization or missing-evidence problem.

**Quick check:** A low-code agent finds a relevant answer in a source the current employee is not authorized to read. Should it paraphrase the result because the search found it? **No.** Permission filtering must prevent that result from becoming answer evidence; retrieval relevance is not authorization.

**Lab:** [Lab 1 — Bounded support workflow](lab-workbook.md#lab-1--build-a-bounded-low-code-support-workflow).

---

## Lesson 2 — Use Coding Agents Safely

### What is a coding agent?

A coding agent is an AI-assisted development system that can inspect a repository, propose edits, run tools, and iterate. It may connect to an editor, a command line, a repository, documentation, or an MCP server. The capability to act is the important security change: a suggestion-only assistant has a different risk profile from an agent that can write files, execute commands, and reach external services.

### Why tool boundaries matter

Model Context Protocol (MCP) provides a structured way for an application or agent to discover and use tools, resources, or prompts exposed by an MCP server. MCP is a **tool/context connection protocol**; it does not make an exposed tool trustworthy and does not itself grant appropriate business authorization. A dangerous tool remains dangerous when it has a neat schema.

Before enabling a tool, ask:

- What exact operation does it perform?
- Which identity does it use?
- What arguments and outputs can it see?
- Can it read, write, execute, or reach the network?
- Can access be constrained to one repository, folder, resource, or operation?
- How is the call logged and revoked?

Use the narrowest tool set that can finish the task. For example, a refactor agent may need repository read access, a patch-writing tool limited to a working tree, and a test runner. It does not need production credentials, unrestricted shell access, or unrestricted internet access.

### Sandboxing as layers

A sandbox is not a single checkbox. Use multiple independent layers:

1. **Identity:** a dedicated, short-lived identity; no developer’s broad personal credentials.
2. **Filesystem:** a disposable checkout or workspace, limited write paths, no mounted secret files.
3. **Process:** allowlisted commands, resource limits, no privileged container or host socket.
4. **Network:** deny by default; allow only specific destinations if the task needs them.
5. **Repository:** branch protection and review; do not let an agent merge its own change.
6. **Data:** synthetic or redacted fixtures; no production exports unless approved and necessary.
7. **Human review:** inspect the diff, test results, and permission changes before merge or deployment.

Cloud Workstations, GKE, and Antigravity are examples named in the exam guide. Select the environment based on isolation, development workflow, access controls, operational skill, and cost—not because a product name appears in an answer option.

### Rules, skills, hooks, extensions, and subagents

Exact labels vary by coding-agent product, but the ideas are distinct:

- **Rules/instructions:** persistent guardrails or repository conventions. They guide behavior; external policy still enforces access.
- **Skills:** reusable task procedures, templates, or domain knowledge that the agent can invoke.
- **Hooks/extensions/plugins:** code or integration points triggered by lifecycle events or added to the agent environment. Treat them as executable code and review their permissions.
- **Subagents:** delegated work units with separate roles or context. Delegation can reduce cognitive load but creates a new identity, data-sharing, and handoff boundary.
- **MCP servers:** externalized tool/resource capabilities. Inventory, vet, scope, version, and monitor them.
- **Agents CLI:** a command-line lifecycle surface for building, managing, or operating agents. Follow the current product documentation for exact commands; do not infer a command from a similarly named product.

### Safe patch lifecycle

1. **Baseline:** check out a known revision and run the current tests.
2. **Task boundary:** write the intended change, allowed files, forbidden actions, and acceptance criteria.
3. **Minimal access:** grant the agent only the tools and paths needed; use a disposable sandbox.
4. **Plan:** ask for a short change plan before edits. Reject unrelated scope.
5. **Patch:** review the diff continuously; do not accept broad hidden changes.
6. **Validation:** run regression, security, dependency, and static checks. Compare behavior before and after.
7. **Review:** a human inspects the code, tool trace, tests, and any new permissions.
8. **Merge and cleanup:** use the normal reviewed process; revoke temporary credentials and remove the sandbox.

A “green test” is not enough if tests do not cover the security requirement. For example, a query-injection fix should preserve expected benign behavior and prove that user input remains a parameter rather than executable SQL syntax.

### Exam lens

Look for answers that use **scoped tool access**, **sandbox isolation**, **least privilege**, and **before/after evidence**. Reject options that hand a coding agent long-lived credentials, unbounded shell/network access, or self-approval authority. The right level of isolation depends on the blast radius: a documentation-only change may need fewer controls than a production code change, but still deserves a reviewable diff.

**Quick check:** A coding agent needs to run unit tests but asks for a production service-account key so it can “verify the fix.” What is the safer response? **Do not mount the key.** Run the tests using synthetic fixtures in the isolated workspace. If production validation is necessary, use an approved, separately controlled deployment path with least privilege and a human reviewer.

**Lab:** [Lab 2 — Sandboxed code-change review](lab-workbook.md#lab-2--use-a-coding-agent-safely).

---

# Section 2 — Custom Agents, Memory and Enterprise Knowledge Integration

## Lesson 3 — Build Custom Agents and Memory

### What makes an agent custom?

A custom agent is an application in which the developer explicitly defines a model, instructions, tools, state, memory, control flow, and integration behavior. The “agent” is not just the language model. It is the complete system around the model—including the software that authorizes tool calls and decides whether to continue, stop, clarify, or hand off.

A common loop is:

```text
receive request → build authorized context → model proposes a response or tool call
       → validate the proposed call → execute only if authorized → inspect result
       → continue within a bounded step/time budget → answer, clarify, or hand off
```

The model proposes. The application validates. Identity and policy decide. The tool executes. Observability records a privacy-safe trace.

### Choosing a model is a constraint problem

Do not begin with “Which model is smartest?” Start with the task and constraints:

| Decision factor | Questions to ask |
|---|---|
| Quality | Does the task require broad reasoning, code, multimodal understanding, or a narrow classification? What test set measures the needed quality? |
| Latency | What end-to-end deadline includes retrieval, tools, retries, and human review? |
| Cost | What are request volume, context size, tool cost, caching potential, and cost of a wrong action? |
| Data and privacy | What data leaves the chosen boundary? Are retention, residency, and access controls acceptable? |
| Hosting | Is a managed SaaS model suitable, or are self-hosting/network/control constraints decisive? |
| Reliability | Is the model/version available in the required region and does a fallback preserve safety? |
| Architecture | Can the task be handled by a smaller model or deterministic code? Does the design need multimodal input or structured output? |

LLM versus SLM, SaaS versus self-hosted, and open-source versus proprietary are not quality rankings. Each is a trade-off. Use a small/cheap model for a narrow low-risk step only after measuring it; route sensitive or uncertain cases to a stronger model, deterministic code, or a person where appropriate. Never let a fallback model silently acquire broader permissions.

### ADK concepts without memorizing syntax

The Agent Development Kit (ADK) is an open-source framework named in the exam guide. Learn the architecture concepts before memorizing a particular release’s Python API:

- **Agent:** role, instruction, model, and behavior.
- **Tool:** typed capability the agent can request. A tool is application code with an authorization boundary—not a prompt trick.
- **Runner/orchestrator:** executes turns and tool cycles under limits.
- **Session:** conversation state for a particular interaction context.
- **Memory:** selected information retained beyond the immediate session, with deliberate scope and lifecycle.
- **Evaluation:** repeatable datasets and checks around responses, retrieval, tools, and trajectories.

The local workshop uses a small deterministic agent-like harness. It teaches boundaries and test design; it is **not** ADK code and does not pretend to call Google Cloud.

### Session is not memory

A **session** is the working context of one interaction: messages, intermediate state, and tool results. A **profile or long-term memory** is a selected fact retained for future interactions. A **knowledge base** is organizational content to retrieve. A **cache** is an optimization. These objects have different authorization and retention rules; do not treat them as one “memory” bucket.

A safe scope key usually includes at least tenant, user, and session identifier. A session ID by itself is not proof of identity. On every request, derive the user and tenant from authenticated context, not from a value the caller can change at will.

Memory needs a policy:

- What exact facts may be remembered, and why?
- Is the fact user-provided, derived, sensitive, or uncertain?
- Did the user consent where required?
- Who can read it? Can one tenant or person see another’s information?
- How does the user inspect, correct, export, and delete it?
- Does a model call or log duplicate it elsewhere?

Prefer allowlisted preferences (for example, a requested answer style) over unrestricted conversation summaries. Avoid remembering credentials, payment details, health data, or unnecessary identifiers. A long-term memory store should have access controls, retention, and deletion behavior just like any other database.

### Build sequence

1. Write one narrow task and one measurable “done” condition.
2. Pick a model using quality, latency, privacy, hosting, cost, and failure requirements.
3. Define a small input/output schema and an agent with a bounded role.
4. Add one read-only tool first. Validate its arguments and result in ordinary code.
5. Add session state using an authenticated, composite scope key.
6. Add long-term memory only if the use case needs it; make the allowed fields and lifecycle explicit.
7. Put a maximum on tool calls, retries, tokens, and wall-clock time.
8. Test two users, two sessions, missing data, tool failure, and a request outside scope.
9. Keep the first implementation observable and easy to replace; expand capabilities only after evidence.

### Common mistakes

- Treating previous chat turns as trusted instructions.
- Reusing a session identifier across users or tenants.
- Saving the whole transcript when one preference would suffice.
- Giving the agent a writable tool before proving a read-only design.
- Choosing a model based on a benchmark unrelated to the actual task.
- Assuming an ADK helper or managed memory feature eliminates application authorization.

### Exam lens

A strong custom-agent design selects the model against stated constraints, separates short-lived session state from approved long-term memory, keeps users isolated, and exposes only required tools. If an answer says “use the most capable model” without addressing privacy, latency, or cost, it has not completed the architecture decision.

**Quick check:** A user’s session contains an access token. Should the application write a summary of the full session to long-term memory for convenience? **No.** Exclude the credential, minimize memory, and review logs, model context, and any retention stores for the same exposure.

**Lab:** [Lab 3 — Custom agent and isolated memory](lab-workbook.md#lab-3--build-a-custom-agent-and-isolate-memory).

---

## Lesson 4 — Connect Enterprise Knowledge and Tools

### RAG: from source to supported answer

Retrieval-augmented generation (RAG) retrieves relevant source material and supplies it as context for a model to produce a grounded answer. RAG can improve freshness and traceability, but it does not guarantee truth. It can retrieve stale, irrelevant, malicious, or unauthorized content; the model can still misread it.

A production-minded pipeline is:

1. **Approve sources:** identify owners, classifications, access policy, and retention.
2. **Ingest:** read source content and metadata; handle deletes and changes.
3. **Normalize:** extract text or structure; preserve identifiers, permissions, versions, and source locations.
4. **Chunk:** split for useful retrieval while preserving enough context. Avoid cutting a rule from its exception or a table from its labels.
5. **Embed/index:** create searchable representations. Store metadata needed for filtering and provenance.
6. **Authorize:** filter candidates by tenant and caller access before content can reach the model. Do not rely on hiding a citation after retrieval.
7. **Retrieve:** use lexical, vector, or hybrid search appropriate to the query.
8. **Rerank:** reorder candidates using a stronger relevance signal; reranking does not grant access.
9. **Generate:** instruct the model to answer only from supplied evidence, identify uncertainty, and abstain when evidence is insufficient.
10. **Verify:** check citations, source version, answer coverage, and policy before delivery.
11. **Observe and refresh:** measure retrieval quality, stale content, failed ingestion, and deletion propagation.

**Embeddings** map content into vectors so semantically similar items can be found even when wording differs. **Similarity scoring** ranks candidate vectors; it is not a proof of truth. **Reranking** reorders a smaller candidate set with more context. **Hybrid retrieval** combines lexical and semantic signals. **Agent Retrieval, Vector Search, Agent Search, and RAG Engine** are examples named in the official guide; select a service only after verifying current capabilities, region, data boundaries, and product documentation.

### Retrieval controls that prevent plausible leaks

Apply access checks at the point where documents are indexed and/or retrieved according to the service’s model. Preserve source ACLs; use the caller’s authenticated identity or an approved delegated model; constrain tenant and group. Test a negative case deliberately. A hidden result should not be inserted into a prompt “just in case.”

Use metadata such as `source_id`, `version`, `effective_date`, `tenant`, `allowed_groups`, and a content location. Let downstream answers expose an approved source reference, not raw internal metadata that the user should not see.

Prompt injection can live inside a retrieved document. Treat retrieved text as **untrusted data**, not instructions. Mark source boundaries, prevent document text from changing tools or system policy, and test a source that says “ignore previous rules.” Model Armor and other safety controls can help inspect content; they do not replace ACL checks, tool policy, or human judgment.

### Tool integrations: schema, identity, and failure

A tool should be a narrow API with a contract:

- Name, purpose, and owner.
- Typed input with validation and size limits.
- Typed output with only necessary fields.
- Required identity/scope and resource boundary.
- Read/write classification and side effects.
- Deadline, retry behavior, idempotency key, and rate limit.
- Error classes, audit fields, and sensitive-data handling.

For a read-only database path, expose a parameterized operation or constrained view—not arbitrary model-generated SQL with a privileged database identity. For SaaS, use a dedicated OAuth client or other approved identity, request only required scopes, store credentials in a managed secret facility rather than prompts, and handle token expiration, revocation, and audience correctly. OAuth 2.0 is a protocol family; the exact grant and delegation pattern depend on the application and identity provider.

**Agent Identity** concerns the agent’s identity and authorized access. **Agent Registry** helps describe or manage agent/capability metadata. **MCP servers** expose tool/context capabilities. These solve related but different problems: discovery answers “what exists?”; identity/policy answers “who may use it?”; the tool implementation answers “what happens?” Registration in a directory is not authorization.

### Tool failure behavior

- **Denied:** tell the agent the operation is not authorized; do not retry with a more privileged identity.
- **Not found:** return a clear absence; do not invent a record.
- **Timeout:** apply a small, bounded retry only when safe; otherwise show a noncommittal status and hand off.
- **Rate-limited:** back off according to policy; avoid retry storms.
- **Partial response:** mark which fields are missing; do not present a partial result as complete.
- **Duplicate submission:** use an idempotency key and check the existing outcome before repeating a side effect.

### Exam lens

Follow the entire evidence chain: **approved source → permission-aware retrieval → relevance → grounded generation → citation/verification**. For tools, seek the narrowest API, read-only where possible, with a scoped identity and explicit timeout/denial paths. A vector database solves similarity retrieval; it does not solve identity, source quality, or authorization by itself.

**Quick check:** Search returns a high-similarity HR document for a contractor who is not in the HR group. What is the right design? **Filter by authorization before the text is supplied to the model.** Similarity is not a permission check; test that the document never enters the contractor’s model context or answer.

**Lab:** [Lab 4 — Grounded retrieval and scoped tools](lab-workbook.md#lab-4--connect-enterprise-knowledge-and-scoped-tools).

---

# Section 3 — Multiagent Orchestration, Agent Evaluation and Deployment

## Lesson 5 — Orchestrate Multiagent Workflows

### Why use more than one agent?

A multiagent design can divide a complex task into smaller roles—such as triage, research, and response review. It can also add latency, cost, more failure points, duplicated context, and a larger security surface. Use multiple agents only when the decomposition improves quality, maintainability, isolation, or scale enough to justify the coordination overhead. A deterministic function may be a better “agent” for a fixed transformation.

### MCP versus A2A

A reliable exam distinction:

- **MCP** connects an AI application/agent to tools, resources, and other contextual capabilities exposed by servers.
- **Agent2Agent (A2A)** supports communication and task handoff between distinct agents, including discovery/capability descriptions and task-oriented interaction.

They are not interchangeable. An agent may use MCP to call a database tool and use A2A to delegate a research task to another agent. In either case, validate the endpoint, identity, capability, authorization, payload, and result. A protocol gives structure to interaction; it does not mean every remote agent is trusted.

### Choose an orchestration pattern

| Pattern | Use it when | Main design obligations |
|---|---|---|
| Sequential | Later work depends on earlier output, e.g., classify → retrieve → draft | Define a typed handoff schema; validate producer output before the next step; bound retries. |
| Parallel | Independent branches can run at once, e.g., policy check + knowledge lookup | Set a deadline; define merge rules, conflict resolution, and partial-failure behavior. |
| Graph/state machine | Routes depend on results, policy, or events, including loops | Declare allowed edges, termination, retry budget, state owner, and a safe exit for every route. |

Do not send the entire conversation to every worker by default. Pass the minimum context needed, with a schema and source references. Make handoffs explainable: a task ID, context ID, sender, recipient, objective, constraints, evidence IDs, schema version, deadline, and authorization context. Avoid placing secrets in a handoff.

### State keys and handoff contracts

Treat workflow state as an API. Define keys such as `request`, `classification`, `evidence_refs`, `draft`, `policy_result`, and `final_status`. Say which node owns each key and which node may read or write it. Validate expected types. Reject unknown or conflicting fields rather than quietly overwriting them.

A handoff contract should answer:

- What does the next agent need to do?
- What is the source and freshness of each supplied fact?
- Which identity and permissions apply?
- What may the receiver return?
- What happens if the receiver is unavailable, returns malformed output, or asks for a broader scope?

### Retries, loops, and partial failure

Retries can duplicate actions. Use them for transient failures only; enforce an attempt and time budget. Make write tools idempotent. Record a stable operation key. Detect repeated states or reasoning loops and stop. When one parallel branch fails, decide in advance whether the task can continue safely with the remaining branch, must be marked partial, or must go to a human. Never quietly omit a failed safety or authorization branch.

### Registry and runtime

A registry can help discover approved agent identities, versions, and capabilities. It is not a substitute for checking that the discovered destination is authorized for this task. Agent Runtime and agent policies may support managed lifecycle and execution; verify current product behavior and the actual authentication model before deployment. Do not trust a registry entry just because its name matches a familiar agent.

### Exam lens

First identify the dependency structure. Use sequential flow for dependencies, parallel flow for independent work, and a graph when conditional routing matters. Then ask for explicit state schemas, controlled handoffs, retry limits, merge policy, identity propagation, and failure handling. If an answer says “parallelize everything,” it likely ignores dependencies and consistency.

**Quick check:** Two independent agents return a policy finding and a relevant article; the policy agent times out. Is it safe to merge the article into a final answer? **Only if the workflow’s pre-defined policy says that this particular task can proceed without the policy check.** Otherwise mark the result incomplete and escalate; never treat a failed safety branch as an approval.

**Lab:** [Lab 5 — Typed handoffs and failure-aware orchestration](lab-workbook.md#lab-5--orchestrate-with-typed-handoffs-and-bounded-failure).

---

## Lesson 6 — Evaluate and Operate Agentic Workflows

### Why evaluation must test the whole trajectory

A fluent final sentence can hide a bad search, an unauthorized tool call, a repeated loop, or an unsafe action. Evaluate the **system path**, not only the final text.

A reviewed **golden dataset** contains representative requests, expected outcomes, source expectations, tool expectations, and edge cases. Include ordinary, ambiguous, no-answer, stale-source, access-denied, timeout, prompt-injection, and high-impact-action cases. Each case should have an owner and a reason for inclusion. Treat user data as governed data; use synthetic or approved de-identified cases when possible.

Evaluation layers:

1. **Task outcome:** did the system answer, clarify, deny, or hand off as expected?
2. **Response quality:** is it correct, complete enough, clear, and appropriately calibrated?
3. **Grounding:** are claims supported by authorized, current evidence? Are citations correct?
4. **Tool behavior:** were the right tools called with valid arguments and permission? Were side effects expected?
5. **Trajectory:** did the steps respect the workflow? Were there loops, redundant calls, or skipped checks?
6. **Safety:** did it reveal secrets, follow untrusted instructions, or take an unapproved action?
7. **Operations:** were latency, errors, cost, and resource use within objectives?

ADK evaluation tooling, evalsets, an Agent Platform GenAI evaluation service, and custom autoraters are examples in the official guide. Use deterministic checks where possible (schema, source presence, allowed tool calls) and human review where judgment is needed. An automated judge is another model with failure modes; validate it against human labels and monitor disagreement.

### Metrics and interpretation

Useful measures include task success, grounded-answer rate, correct abstention, authorized-tool-call rate, invalid-argument rate, unsafe-action rate, retrieval recall/precision on labeled cases, p50/p95 latency, timeout rate, and cost per successful task. Define numerator and denominator. Segment by task, model version, source collection, tenant, and release; aggregate scores can hide a bad subgroup.

No one metric proves that an agent is safe. For example, a high answer rate can reward hallucination if abstention is counted as failure. Measure **correct abstention** and **evidence quality** alongside helpfulness. Keep a baseline and compare versions on the same dataset before and after a change.

### Development-to-production evaluation loop

1. Curate and review the eval set; protect its data.
2. Run deterministic unit/contract checks on tools and policies.
3. Run model/system evaluation on representative and adversarial cases.
4. Inspect failures by trace: prompt/context, retrieved evidence, decision, tool call, result, final response—redacted appropriately.
5. Fix the root cause (source, policy, prompt, model, tool, or orchestration), not just the failing example.
6. Re-run the entire suite, including regressions.
7. Canary a limited release, compare agreed metrics, and pause/rollback when thresholds fail.
8. Continue monitoring production drift and refresh the dataset when real failure modes change.

### Runtime choice: managed runtime, Cloud Run, or GKE

Do not choose by habit. Compare operational ownership, control, integration needs, scaling pattern, observability, latency, cost, and compliance.

- **Agent Runtime** (the official guide notes the former AgentEngine name) is a candidate when its managed agent lifecycle and supported integrations fit. Verify regional availability, session/memory behavior, runtime limits, pricing, and deployment model in current docs.
- **Cloud Run** is a candidate for a containerized HTTP service where managed deployment and request-driven scaling fit. Consider startup time, concurrency, request deadlines, state externalization, and container constraints.
- **GKE** is a candidate when the workload needs Kubernetes-level control, specialized networking, sidecars, complex multi-service patterns, or cluster-level operations the team can responsibly manage. That flexibility carries more operational work.

A managed service does not absolve the team from access control, evaluation, incident response, and cost ownership. A self-managed environment is not automatically more secure.

### Observability and incident response

Use correlation IDs across user request, orchestration, retrieval, tool call, and model response. Capture latency, outcome, version, retry count, and approved source/tool identifiers. Do not indiscriminately log prompts, raw documents, tokens, or personal data. Redact or omit sensitive content and restrict log access. Logs and traces are themselves data stores.

For an incident, preserve the trace needed to diagnose, stop or disable the unsafe path, revoke credentials if exposed, identify affected tenants, notify the right owners, and re-run tests before restoring traffic. Define rollback criteria before release. Keep a safe fallback—often clarification or human handoff—rather than returning to an older but insecure configuration.

### Exam lens

Look for **a reviewed evalset plus continuous evaluation**, **tool and trajectory checks**, **a runtime matched to constraints**, and **observable, reversible releases**. Be suspicious of an answer that evaluates only BLEU/exact-match text, or that declares success from one demo.

**Quick check:** Your new model produces more helpful answers but doubles tool calls and occasionally times out. Is a higher response-quality score enough to ship? **No.** Reassess task success, authorization, latency, reliability, cost, and safety against explicit release thresholds; investigate the trajectory and canary before rollout.

**Lab:** [Lab 6 — Golden set, release gate, and runtime choice](lab-workbook.md#lab-6--evaluate-and-operate-a-release).

---

# Section 4 — Agent Security, Governance and Full Mock Exam Preparation

## Lesson 7 — Secure and Govern Agentic Workflows

### A simple security model

For every action, identify the **human caller**, **agent identity**, **tool/service identity**, **resource**, **policy decision**, and **audit record**. These may be different principals. The model is not an identity provider, and text in a prompt is not proof that someone is authorized.

A practical access decision is the intersection of independent controls:

```text
request is allowed only when
  caller is authenticated and may request the task
  AND agent identity may use this tool
  AND delegated scope is valid for this resource/action
  AND resource boundary permits the target
  AND service/tool policy permits the operation
  AND any required human approval is current
```

Any denial should stop the action. Avoid “fallback” identities with broader access.

### Authentication, OAuth 2.0, and delegated authorization

Authentication answers “who is this principal?” Authorization answers “what may this principal do to which resource?” OAuth 2.0 is commonly used to obtain scoped access to APIs. Design for the correct actor and audience; use short-lived, narrowly scoped credentials; validate issuer, audience, expiry, and scopes; protect refresh tokens; and support revocation. Do not place bearer tokens in prompts, source code, logs, screenshots, or handoff payloads.

Delegation deserves care. The user may authorize an agent to act within a specific task, but that does not mean the agent inherits every permission the user has. Define which identity is used for each tool, which scope is delegated, what consent/approval is required, and how the action is attributed. The agent should not silently switch to its own broader service identity when user authorization is missing.

### Principal Access Boundaries and least privilege

A Principal Access Boundary (PAB) is a boundary that limits the resources a principal can access; it should not be confused with a grant of permission. A useful mental model is: permissions say what actions may be performed, while a boundary constrains the maximum resource set. The effective access still depends on the applicable IAM and service policies. Verify the current Google Cloud semantics and policy evaluation rules before implementation.

Use a dedicated identity for each agent or capability where practical. Grant only the resource and operation required. Start read-only. Separate development, test, and production identities. Review access periodically and remove stale grants.

### Agent Gateway, Registry, and Model Armor

- **Agent Gateway** is an in-scope governance/traffic-control concept in the exam guide. Think of it as a place to route, observe, and enforce policy around agent interactions. Confirm the exact current capabilities and integration path in product documentation.
- **Agent Registry** helps manage discoverability and capability metadata. Registration does not prove trust or confer permissions; verify identity, version, owner, destination, and policy before use.
- **Model Armor** is an in-scope content-safety control. It can help inspect inputs/outputs for threats such as prompt injection or unsafe content. It is a defense layer—not an authorization engine, not a guarantee of correctness, and not a replacement for secure tool design.

Use layered controls: input validation, source trust labels, least-privilege tools, policy enforcement, output checks, human review, and privacy-safe audit. Each layer has a distinct purpose.

### Human-in-the-loop (HITL)

Route a task to a human when the impact or uncertainty is too high for an autonomous action. Examples include granting privileged access, deleting data, committing funds, changing legal/medical decisions, or taking an irreversible action. A good approval screen presents the intended action, exact target, source/evidence, side effects, and an expiration time. Record who approved what and when. An approval should not be a vague “yes” that can be replayed for a different action.

Use risk-based autonomy:

- **Low risk, reversible, well-tested:** automate within a narrow policy.
- **Moderate impact:** ask for explicit confirmation or limit the action.
- **High impact, irreversible, or ambiguous:** stop and require an authorized human.

Human review is not a magic safety net. A reviewer needs enough context and authority, a manageable queue, and the ability to reject. Monitor overrides and approval quality.

### Audit and privacy

Audit what is needed to explain and investigate: stable request ID, agent/version, authenticated principal reference, tool name, resource, policy outcome, approval reference, timestamp, and error category. Do not store full prompts or tokens by default. Use redaction, retention limits, access controls, and an incident procedure. A log that contains the secret is itself a security incident.

### Threats to rehearse

- Prompt injection in user input or retrieved documents.
- Cross-tenant or cross-user session/memory leakage.
- Over-privileged OAuth scopes or an agent identity with broad resource access.
- Tool description confusion or malicious MCP/A2A endpoint.
- Duplicate side effects from retries.
- Stale or poisoned knowledge sources.
- Sensitive output or verbose logs.
- Unreviewed agent changes or registry entries.
- A “human approval” step that can be bypassed or replayed.

### Exam lens

Prefer a layered design: authenticate the caller, use a dedicated agent identity, grant scoped access, enforce resource boundaries, route/monitor through approved controls, inspect content, and require human approval for high-impact actions. A content filter cannot repair an overbroad service account. A registry cannot make an unknown endpoint safe. A permission boundary does not grant the permissions it limits.

**Quick check:** A tool call is blocked because the agent identity cannot access a resource. Can the workflow retry using a broad project-owner credential? **No.** Fix the intended least-privilege policy or hand off. A broader credential turns a clear denial into an uncontrolled privilege escalation.

**Lab:** [Lab 7 — Identity, policy, redaction, and approval](lab-workbook.md#lab-7--secure-and-govern-the-workflow).

---

## Lesson 8 — Exam Strategy, Mock Exam and Labs

### Know the certification shape; check the current page

As checked on 13 October 2026, Google’s official FAQ describes the beta as a three-hour multiple-choice component followed by separate hands-on labs for candidates who pass; the beta exam window ended on 30 September 2026. The FAQ describes the generally available version as following the standard two-hour professional exam format, with a separate lab component. The course offers an 80-question practice mock, including a beta-style 180-minute mode and a 120-minute practice mode. **The course’s practice length is not an official claim about the exact GA question count.** Confirm current structure, eligibility, results timing, and lab availability on the official certification page before scheduling.

This is a new certification and the product surface is evolving. If a question uses a newer name, identify the architecture role and then verify the latest official wording. Do not overfit to an old “Vertex AI AgentEngine” label when the current guide says Agent Runtime, for example.

### A repeatable scenario-question method

For each scenario:

1. **Read the last sentence first** to identify what the question asks: choose a runtime, secure a tool, improve retrieval, handle a timeout, and so on.
2. **Extract constraints:** user identity, sensitivity, latency, scale, budget, operational skill, region, and whether the action is read or write.
3. **Name the failure being prevented:** leakage, hallucination, unauthorized write, stale answer, latency, cost, or operational burden.
4. **Map the task to a domain and pattern:** RAG, MCP, A2A, sessions, evaluation, deployment, identity, governance, etc.
5. **Eliminate unsafe or irrelevant options:** broad credentials, unbounded retries, unrestricted tools, hidden ACLs, no evidence, or unnecessary complexity.
6. **Pick the smallest design that meets every stated requirement.**
7. **Check the residual risk:** what happens when evidence is missing, a tool is denied, or a service times out?

Do not choose an option only because it contains the most product names. The best answer often combines a simple workflow with a specific control and an observable failure route.

### Timed mock routine

- Use the current official duration as the timing reference; take course mock modes as practice simulations only.
- For a first pass, answer clear questions and flag uncertain ones rather than spending too long on one item.
- On review, state the requirement in your own words and explain why each distractor fails.
- Classify every miss as a concept gap, product-name confusion, overlooked constraint, security blind spot, or time-management issue.
- Revisit missed objectives after a break. Retaking the same questions immediately can measure memory rather than understanding.
- Keep the mock score separate from lab evidence. Knowing the right command or architecture answer is not the same as independently producing and verifying the result.

For additional original scenario practice with distractor analysis, use the [20-question practice set](scenario-practice.md). It is a study aid, not an official question bank or passing-score predictor.

### Build a study plan from evidence

Use two independent readiness axes:

| Axis | Evidence to record | What it tells you |
|---|---|---|
| Scenario knowledge | Domain-level questions attempted, correct/incorrect, confidence, explanation quality | Which concepts and trade-offs need revision |
| Practical execution | Lab task completed without solution, expected result observed, failure path verified, cleanup evidence | Whether you can carry the architecture through an implementation-like task |

A practical score is not an official Google passing score, and neither is a course mock percentage. Use them as diagnostics. Give additional time to the largest combination of **domain weight × personal gap × practical importance**, while maintaining a baseline review of the other domains.

### Four-week plan

**Week 1 — Foundations and safe workflow design**
- Lesson 1 and Lab 1; write a state diagram and test unsupported/no-evidence requests.
- Lesson 2 and Lab 2; review sandbox policy and patch evidence.
- End-of-week: explain why a prompt is not an authorization boundary.

**Week 2 — Agents, memory, knowledge**
- Lesson 3 and Lab 3; test session separation with two users and two sessions.
- Lesson 4 and Lab 4; explain how access filtering, retrieval, reranking, evidence, and tool scopes fit together.
- End-of-week: trace an answer from caller to source and back.

**Week 3 — Orchestration and operations**
- Lesson 5 and Lab 5; test partial failure and loop limits.
- Lesson 6 and Lab 6; build a small golden set, calculate results, and defend a runtime choice.
- End-of-week: write a release/rollback checklist.

**Week 4 — Security and exam readiness**
- Lesson 7 and Lab 7; prove allowed and denied cases, inspect redacted audit events, and test approval gating.
- Run all tests and complete the capstone in the lab workbook.
- Take one timed mock. Review by objective and book a second attempt only when review—not recollection—shows readiness.

For a shorter schedule, preserve the order but do not skip hands-on practice. For a longer schedule, add new edge cases to the golden set and repeat the labs from a clean checkout.

### Readiness worksheet

Rate each item 0–2: **0 = cannot yet explain/do**, **1 = can explain with notes or need help**, **2 = can explain and demonstrate independently**. This is a personal diagnostic, not a certification score.

- I can draw a low-code workflow with explicit no-evidence, denied, timeout, and human paths.
- I can set up a coding-agent task with scoped tools, sandbox boundaries, and reviewable tests.
- I can explain model trade-offs and distinguish a session from long-term memory.
- I can trace an authorized RAG answer through source, ACL, retrieval, reranking, and citation.
- I can distinguish MCP tool integration from A2A agent handoff.
- I can describe sequential, parallel, and graph workflows, including merge and retry rules.
- I can design an evaluation set that checks answer, retrieval, tool, trajectory, and safety behavior.
- I can defend Agent Runtime vs Cloud Run vs GKE using workload constraints.
- I can explain caller, agent, and tool identity; least privilege; OAuth scopes; and resource boundaries.
- I can say when Model Armor helps, what it cannot guarantee, and when human approval is needed.
- I can execute the local labs, inspect failure cases, and clean up without copying a solution blindly.

Plan the next study block around the lowest items. If knowledge scores are high but practical execution is low, spend time building and observing. If labs pass but explanations are weak, practise architecture trade-offs and scenario reasoning.

### Final exam-day checklist

- Verify the current official exam format, ID, system/test-center requirements, allowed materials, and time.
- Sleep, eat, and have a strategy for flagged questions.
- Read constraints before selecting services.
- Do not confuse a plausible answer with a supported answer.
- For the practical component, read the task and acceptance criteria fully; inspect environment, permissions, and starter state before changing anything; test expected and failure paths; record evidence; clean up.
- If blocked, capture the exact error and identify whether the issue is authentication, authorization, configuration, dependency, or application logic. Avoid random broad permission grants.
- Remember that certification requires completing every official component listed by Google. Course labs are preparation only.

---

# Appendix A — One-page architecture checklist

Before approving an agentic workflow, ask:

1. **Purpose:** What task is in scope, and what is explicitly out of scope?
2. **Autonomy:** Which actions can run automatically; which require confirmation or a human?
3. **Identity:** Who is the caller, which identity does each tool use, and how is delegation bounded?
4. **Data:** Which sources are approved, permission-filtered, fresh, and traceable?
5. **Tools:** Are schemas narrow, read/write effects clear, scopes minimal, and timeouts bounded?
6. **Orchestration:** Are state and handoff schemas explicit? Can retries duplicate actions? Can every route terminate?
7. **Quality:** Does the evalset contain ordinary, edge, adversarial, denied, timeout, and no-answer cases?
8. **Operations:** What will be monitored? What is the release gate, rollback threshold, and owner?
9. **Privacy:** What enters prompts, memory, traces, and logs? What is retained, redacted, or deleted?
10. **Human process:** Can a person review the action, reject it, and understand the evidence?

# Appendix B — Compact glossary

| Term | Plain-language meaning |
|---|---|
| Agent | Software using a model and tools to pursue a task within application-defined boundaries. |
| Agent identity | The principal representing the agent when it accesses resources or calls tools. |
| Agent Registry | A catalog/control-plane concept for agent and capability metadata; it is not itself authorization. |
| Agent Runtime | A managed runtime name used in the official guide (formerly AgentEngine); verify current service behavior. |
| Agent Gateway | An in-scope traffic, monitoring, or policy control concept; verify current product scope. |
| A2A | Agent2Agent protocol for discovery and task-oriented agent communication. |
| ADK | Agent Development Kit, an open-source framework for building agents. |
| Embedding | A vector representation used to compare semantic similarity. |
| Evalset / golden dataset | A reviewed collection of input cases, expectations, and edge cases used for repeatable evaluation. |
| HITL | Human-in-the-loop review or approval before/after a risk-sensitive decision. |
| MCP | Model Context Protocol for connecting an AI application/agent to tools and context provided by servers. |
| Model Armor | A content-safety control named in the exam guide; not a substitute for authorization or safe tools. |
| PAB | Principal Access Boundary, a resource boundary limiting what a principal can access; not a permission grant. |
| RAG | Retrieval-augmented generation: retrieve source material and use it as context for a generated response. |
| Reranking | Reordering retrieved candidates using a more detailed relevance estimate. |
| Session | Short-lived interaction state scoped to a user/tenant/context. |
| Tool | A typed capability, usually backed by application code or a service, that can read or change something. |
| Trajectory | The sequence of reasoning/control decisions, retrievals, and tool calls leading to an outcome. |

# References and change control

Use these primary sources for current facts and product details:

- [Professional Agentic Architect certification exam guide (Google Cloud PDF)](https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf) — current exam objectives and approximate domain weights.
- [Professional Agentic Architect certification FAQs (Google Cloud support)](https://support.google.com/cloud-certification/answer/18080541?hl=en) — exam components, beta/GA structure, eligibility, and lab timing.
- [Google Skills Professional Agentic Architect learning path](https://www.skills.google/paths/4525) — official preparation learning path.
- [Agent Development Kit documentation](https://google.github.io/adk-docs/) — framework concepts and current implementation details.
- [Model Context Protocol documentation](https://modelcontextprotocol.io/introduction) — MCP concepts and protocol details.
- [A2A protocol documentation](https://a2a-protocol.org/latest/) — Agent2Agent concepts and current protocol details.
- [Google Cloud documentation](https://cloud.google.com/docs) — authoritative service docs; search the exact current product name before implementing.

**Change-control habit:** record the date checked, current exam-guide revision, service/product names, region and API version used in your own notes. Re-check these sources before you spend money, grant access, or book an exam.
