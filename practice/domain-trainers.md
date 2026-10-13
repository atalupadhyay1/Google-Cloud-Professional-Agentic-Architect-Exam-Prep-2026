# Domain Trainers — 84 Original Practice Questions (7 trainers × 12)
*Original questions written for this guide — not real exam items. Method: answer first, then read why each wrong option fails (Module 0, §6). Tag every miss by domain and redo only missed domains after 48h.*

## D1 Solution Design (Trainer 1)

**Q1.** Support steps are always verify→policy→draft, but team built a free-looping agent with rising cost. Best change?
- A. Longer prompt
- B. Routed workflow with fixed steps
- C. Free agent with more tools
- D. Bigger model
<details><summary>Answer</summary>

**B. Routed workflow with fixed steps** — Fixed known steps = workflow: predictable cost/latency/audit. Agent/tools/model don't fix pattern mismatch. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q2.** Law-firm contract Q&A needs cited single answers.
- A. Augmented LLM + RAG with citations and low-confidence handoff
- B. Multi-agent research swarm
- C. Agent that browses until confident
- D. Workflow with no retrieval
<details><summary>Answer</summary>

**A. Augmented LLM + RAG with citations and low-confidence handoff** — One grounded answer suffices; swarm adds cost/error, browsing lacks grounding control, no retrieval = hallucination risk. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q3.** A task's path truly depends on findings mid-investigation.
- A. Unbounded agent
- B. Fixed 3-step chain
- C. Single zero-shot call
- D. Agent with budgets, max iterations, tool allow-list and escalation
<details><summary>Answer</summary>

**D. Agent with budgets, max iterations, tool allow-list and escalation** — Open-ended path justifies agent only with controls; unbounded is unsafe, fixed/single cannot adapt. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q4.** Sponsor asks for 'an agent for HR'. Architect's first move?
- A. List 20 tools
- B. Write system prompt
- C. Quantify outcome, volume, failure cost and SLAs
- D. Pick largest model
<details><summary>Answer</summary>

**C. Quantify outcome, volume, failure cost and SLAs** — Value/SLA first drives every later choice; tech-first is the classic trap. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q5.** Three independent document sections must be summarised fast.
- A. Skip merge validation
- B. Parallelise sub-tasks then merge with defined merge rules
- C. Sequential agent loop
- D. One mega-prompt for all
<details><summary>Answer</summary>

**B. Parallelise sub-tasks then merge with defined merge rules** — Independent work parallelises; sequential wastes latency, mega-prompt risks truncation, merge needs rules. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q6.** Generator keeps revising forever.
- A. Evaluator-optimiser with threshold and max iterations
- B. Remove evaluator
- C. More revision loops
- D. Bigger context
<details><summary>Answer</summary>

**A. Evaluator-optimiser with threshold and max iterations** — Bounded improvement loop; removing evaluator loses quality gate, unbounded loops burn cost. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q7.** Mixed intents handled by one mega-prompt with errors.
- A. Add 20 examples
- B. Raise temperature
- C. Multi-agent for every intent
- D. Router classifying intent to specialised flows
<details><summary>Answer</summary>

**D. Router classifying intent to specialised flows** — Routing narrows task per flow, cheaper/more accurate; examples/model tweaks don't fix conflation. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q8.** Multi-agent proposed to fix vague single prompt.
- A. Add critic agent
- B. Split by persona
- C. Clarify/decompose and test single design first; multi-agent only for independently testable sub-tasks
- D. Add supervisor agent
<details><summary>Answer</summary>

**C. Clarify/decompose and test single design first; multi-agent only for independently testable sub-tasks** — Multi-agent compensates poorly for vagueness and multiplies cost/debug surface. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q9.** High failure-cost irreversible action in flow.
- A. Agent self-approval
- B. Keep pattern but place pre-action human approval
- C. Full autonomy to cut latency
- D. Remove logging
<details><summary>Answer</summary>

**B. Keep pattern but place pre-action human approval** — Failure cost sets autonomy; self-approval is no control. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q10.** No one knows if shipped system still helps users.
- A. Add feedback loop: logging, sampled eval, correction intake
- B. Larger model
- C. More tools
- D. New UI
<details><summary>Answer</summary>

**A. Add feedback loop: logging, sampled eval, correction intake** — Missing measurement is the gap; tech swaps are unprovable without it. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q11.** Volume ×20, predictable quality required.
- A. Free agents per request
- B. Capable model everywhere
- C. No budgets
- D. Simplest reliable pattern, load/cost model per task
<details><summary>Answer</summary>

**D. Simplest reliable pattern, load/cost model per task** — Scale punishes variable loops and top-tier-everything. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q12.** Complex research: search, source-critique, synthesis need different tools.
- A. Workflow with no critique
- B. Single call
- C. Multi-agent or orchestrated workers with per-agent scope, budgets and whole-system eval
- D. One agent with all tools
<details><summary>Answer</summary>

**C. Multi-agent or orchestrated workers with per-agent scope, budgets and whole-system eval** — Different tool scopes + independent critique legitimately justify decomposition — with controls. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

## D2 Models, Prompting & Context (Trainer 2)

**Q1.** Largest model used to classify billing vs support; cost SLA breached, accuracy already 99% on eval.
- A. Longer CoT
- B. Fast tier for classification, escalate only uncertain cases
- C. Capable model + caching only
- D. More few-shots
<details><summary>Answer</summary>

**B. Fast tier for classification, escalate only uncertain cases** — Narrow task passes on fast tier; others keep the expensive default. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q2.** Repeated 4k-token handbook resent every request.
- A. Stable prefix first, variable content last, enable prompt caching and measure hit rate
- B. Randomise prefix per user
- C. Paste docs after user msg
- D. Bigger window
<details><summary>Answer</summary>

**A. Stable prefix first, variable content last, enable prompt caching and measure hit rate** — Cache reuse needs identical stable prefix; randomising/placing after variable kills hits. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q3.** Output must feed billing system.
- A. Free-text with 'please format nicely'
- B. Few-shot only
- C. CoT
- D. Structured output contract (JSON schema) + validation
<details><summary>Answer</summary>

**D. Structured output contract (JSON schema) + validation** — Downstream automation needs enforceable schema. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q4.** Tone/format inconsistent despite clear task.
- A. Switch model blindly
- B. Zero-shot forever
- C. Add 2-5 representative few-shot examples and eval
- D. Add 30 random examples
<details><summary>Answer</summary>

**C. Add 2-5 representative few-shot examples and eval** — Show, don't only tell — few representative examples; random bulk adds cost/noise. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q5.** Multi-step diagnosis errors.
- A. Fastest tier
- B. Add step-by-step reasoning, verify gain on eval
- C. Remove process steps
- D. Shorten prompt randomly
<details><summary>Answer</summary>

**B. Add step-by-step reasoning, verify gain on eval** — Reasoning scaffolding can help complex tasks if measured. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q6.** Per-user ID injected into cached prefix; hit rate ~0.
- A. Move variable user data after cached prefix
- B. Disable caching
- C. Cache per user anyway
- D. Enlarge window
<details><summary>Answer</summary>

**A. Move variable user data after cached prefix** — One early variable token invalidates reuse. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q7.** Five agents copy-paste same instruction blob, drifting apart.
- A. Email the prompt around
- B. Each team forks it
- C. Hardcode in code comments
- D. Modular prompt / reusable Skill, versioned and eval'd centrally
<details><summary>Answer</summary>

**D. Modular prompt / reusable Skill, versioned and eval'd centrally** — Single governed module stops drift. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q8.** Team wants model upgrade 'for quality' with no data.
- A. Stay forever
- B. Ask users vibes
- C. Eval cheapest plausible tier vs candidate on golden set, decide on delta
- D. Upgrade all traffic
<details><summary>Answer</summary>

**C. Eval cheapest plausible tier vs candidate on golden set, decide on delta** — Model choice needs evidence. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q9.** Answers truncated.
- A. Longer history
- B. Reserve output budget and trim low-value context
- C. Add more retrieved chunks
- D. More examples
<details><summary>Answer</summary>

**B. Reserve output budget and trim low-value context** — Truncation = budget problem; more input worsens it. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q10.** Prompt edited Friday, quality fell Monday, no record.
- A. Version prompts and gate changes on eval suite
- B. Revert by memory
- C. Bigger model Monday
- D. Blame users
<details><summary>Answer</summary>

**A. Version prompts and gate changes on eval suite** — Prompt=code: version + test. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q11.** Easy 80% / hard 20% workload on capable tier.
- A. Capable everywhere
- B. Fast everywhere regardless
- C. Random routing
- D. Cascade: fast tier first, capable on low confidence/hard
<details><summary>Answer</summary>

**D. Cascade: fast tier first, capable on low confidence/hard** — Pay for capability where evidence needs it. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q12.** Huge history stuffed into every call; answers worsen.
- A. More history
- B. No system prompt
- C. Summarise/curate context; keep only task-relevant history
- D. Max window always
<details><summary>Answer</summary>

**C. Summarise/curate context; keep only task-relevant history** — Irrelevant context dilutes attention and adds cost. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

## D3 Integration, MCP & Least Privilege (Trainer 3)

**Q1.** Support agent refunded via injected email instruction; it has refund tool 'just in case'.
- A. Bigger model
- B. Hide tool name
- C. Remove/narrow refund capability; server-side AuthZ + approval for legitimate path
- D. Prompt: 'never be injected'
<details><summary>Answer</summary>

**C. Remove/narrow refund capability; server-side AuthZ + approval for legitimate path** — Permissions enforce; prompt pleading doesn't. Capability wasn't needed un-gated. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q2.** Agent holds 22 tools, picks wrong ones, slow.
- A. Capable model
- B. Remove unused tools + progressive discovery for the rest
- C. Add tool descriptions x3 length
- D. Add 10 more tools
<details><summary>Answer</summary>

**B. Remove unused tools + progressive discovery for the rest** — Bloat hurts accuracy/latency/security simultaneously. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q3.** Shared super-user API key across agents.
- A. Per-agent scoped short-lived identities, rotation, audit
- B. Longer key
- C. Prompt confidentiality
- D. Shared key in vault only
<details><summary>Answer</summary>

**A. Per-agent scoped short-lived identities, rotation, audit** — Blast radius and attribution need per-agent identity; vault storage alone doesn't scope. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q4.** Reusable integrations needed across 3 apps.
- A. Copy API code 3×
- B. One agent calls another for everything
- C. CLI scraping
- D. MCP servers (vetted, pinned, scoped) exposing tools/resources
<details><summary>Answer</summary>

**D. MCP servers (vetted, pinned, scoped) exposing tools/resources** — MCP is the standard reuse layer — with governance. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q5.** Model supplies refund amount; system executes it.
- A. Prompt 'calculate carefully'
- B. CoT for maths
- C. Server re-derives amount from order system and enforces caps
- D. Trust model arithmetic
<details><summary>Answer</summary>

**C. Server re-derives amount from order system and enforces caps** — Money must be verified server-side. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q6.** Existing internal CLI is the sanctioned ops interface.
- A. MCP without vetting
- B. CLI integration sandboxed with least-privilege and command allow-list
- C. Raw shell access
- D. API rewrite immediately
<details><summary>Answer</summary>

**B. CLI integration sandboxed with least-privilege and command allow-list** — Use sanctioned interface but constrain execution. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q7.** Specialist team owns a capability with its own tools/eval.
- A. Delegate via agent-to-agent with contract, budget and tracing
- B. Give parent all specialist tools
- C. Shared prompt
- D. No logging
<details><summary>Answer</summary>

**A. Delegate via agent-to-agent with contract, budget and tracing** — Independent ownership/testability justifies A2A; absorbing tools recreates bloat. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q8.** New MCP server from internet requested in prod.
- A. Install same day
- B. Give it prod keys to test
- C. Prompt it to behave
- D. Vet code/permissions, pin version, scope, monitor before prod
<details><summary>Answer</summary>

**D. Vet code/permissions, pin version, scope, monitor before prod** — An MCP server is code with access — supply-chain review applies. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q9.** Read-only KB tool needs broad access; refund tool same agent.
- A. Prompt separation
- B. Weekly review only
- C. Split scopes (separate agents/identities) by risk
- D. One identity for convenience
<details><summary>Answer</summary>

**C. Split scopes (separate agents/identities) by risk** — Risk-differing scopes shouldn't share a blast radius. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q10.** Latency up after adding 80 tool schemas to prompt.
- A. Cache user message
- B. Progressive discovery: index first, load tool detail on demand
- C. Smaller font in prompt
- D. Capable model
<details><summary>Answer</summary>

**B. Progressive discovery: index first, load tool detail on demand** — Monolithic tool context is the cost/confusion source. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q11.** Audit asks who approved a deletion the agent performed.
- A. Propagate user identity + approval record in audit log per tool call
- B. Model's chat transcript
- C. Shared log file
- D. Prompt version
<details><summary>Answer</summary>

**A. Propagate user identity + approval record in audit log per tool call** — Accountability needs actor/on-behalf-of at action layer. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q12.** Accuracy-vs-latency config dispute in review.
- A. Seniority decides
- B. Pick fastest
- C. Pick most accurate
- D. Present A/B eval: accuracy delta vs p95 latency vs SLA
<details><summary>Answer</summary>

**D. Present A/B eval: accuracy delta vs p95 latency vs SLA** — Configuration is defended with measured trade-off. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

## D3-RAG Retrieval & Observability (Trainer 4)

**Q1.** RAG answers degraded right after document refresh.
- A. Rewrite prompt
- B. Capable model
- C. Increase top-k to 50
- D. Check stale chunks: index versioning, eviction, atomic swap
<details><summary>Answer</summary>

**D. Check stale chunks: index versioning, eviction, atomic swap** — After-refresh timing points at retrieval freshness first. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q2.** Questions cite exact error codes; semantic search misses them.
- A. Prompt quoting
- B. Larger chunks
- C. Hybrid keyword+vector retrieval
- D. Vector only w/ more chunks
<details><summary>Answer</summary>

**C. Hybrid keyword+vector retrieval** — Exact tokens need keyword matching. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q3.** Right chunks exist but never retrieved.
- A. More few-shots
- B. Inspect chunking/query/index; test chunk sizes and retrieval on eval questions
- C. Blame model
- D. Add guardrail paragraph
<details><summary>Answer</summary>

**B. Inspect chunking/query/index; test chunk sizes and retrieval on eval questions** — Retrieval-miss branch of fault tree. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q4.** Right chunks in context, answer still invents.
- A. Grounding prompt + citation enforcement + possibly model tier
- B. Re-index everything
- C. Delete index
- D. Top-k=100
<details><summary>Answer</summary>

**A. Grounding prompt + citation enforcement + possibly model tier** — Generation branch: chunks were present. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q5.** Chunk starts mid-sentence of a policy rule.
- A. Random splits
- B. One chunk per library
- C. OCR again blindly
- D. Structure-aware chunking on headings with heading metadata
<details><summary>Answer</summary>

**D. Structure-aware chunking on headings with heading metadata** — Chunk boundaries must respect document structure. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q6.** Users see other departments' documents in answers.
- A. Post-filter answer text
- B. Hide citations
- C. ACL metadata filtering at retrieval by user permissions
- D. Prompt 'don't share'
<details><summary>Answer</summary>

**C. ACL metadata filtering at retrieval by user permissions** — Access control belongs in retrieval, not cosmetics. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q7.** Two policy versions both retrieved, conflicting.
- A. More context
- B. Version/freshness filter + dedupe, latest effective doc wins
- C. Let model choose
- D. Average answers
<details><summary>Answer</summary>

**B. Version/freshness filter + dedupe, latest effective doc wins** — Conflict is a data-governance-at-retrieval problem. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q8.** No way to debug a wrong answer from last week.
- A. Log query, chunk IDs+scores, doc versions, prompt/model version per request
- B. Log final answer only
- C. Ask user to reproduce
- D. Full PII logging
<details><summary>Answer</summary>

**A. Log query, chunk IDs+scores, doc versions, prompt/model version per request** — Chunk-level traceability makes RAG debuggable. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q9.** Top-k raised 5→30; accuracy fell, cost rose.
- A. Top-k=100
- B. Remove reranker
- C. Smaller model
- D. Rerank candidates and keep top few relevant
<details><summary>Answer</summary>

**D. Rerank candidates and keep top few relevant** — More noise dilutes; reranking restores precision. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q10.** Index half-updated during business hours; mixed old/new answers.
- A. Manual chunk deletes
- B. Cache answers
- C. Build new index offline, validate, atomic swap
- D. Update in place nightly
<details><summary>Answer</summary>

**C. Build new index offline, validate, atomic swap** — Atomic versioned refresh prevents mixed state. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q11.** Retrieval returns nothing for vague questions often.
- A. Longer prompt
- B. Query rewriting/expansion, tested on eval, plus 'I don't know' path
- C. Force an answer
- D. Capable model
<details><summary>Answer</summary>

**B. Query rewriting/expansion, tested on eval, plus 'I don't know' path** — Vague-query handling + honest no-answer beats invention. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q12.** Alerting needed in production RAG.
- A. Alert on no-result/low-score rate, stale-index age, citation rate, sampled accuracy
- B. Alert on every error
- C. CPU only
- D. Monthly manual check
<details><summary>Answer</summary>

**A. Alert on no-result/low-score rate, stale-index age, citation rate, sampled accuracy** — Alert on user-harm proxies with runbooks. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

## D4 Evaluation & Optimisation (Trainer 5)

**Q1.** New prompt 'feels better', tickets quietly rise.
- A. Ship on vibes
- B. Poll team
- C. Bigger model
- D. Run fixed eval vs baseline with thresholds before/after ship
<details><summary>Answer</summary>

**D. Run fixed eval vs baseline with thresholds before/after ship** — Feelings aren't measurement; regression needs a gate. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q2.** Average accuracy +3pts, non-English subset collapses.
- A. Remove subset
- B. Re-weight average
- C. Block ship: subset regression despite average gain
- D. Ship, average wins
<details><summary>Answer</summary>

**C. Block ship: subset regression despite average gain** — Averages hide harm; report subsets. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q3.** Only grader is an LLM judge scoring 95/100.
- A. No graders
- B. Calibrate judge vs human labels; add code/human graders (mixed methods)
- C. Trust judge
- D. Judge with bigger model
<details><summary>Answer</summary>

**B. Calibrate judge vs human labels; add code/human graders (mixed methods)** — Uncalibrated judge is a trap. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q4.** Past outage bug keeps reappearing after fixes.
- A. Add it as permanent regression case before fixing
- B. Fix and forget
- C. Note in chat
- D. Manual check quarterly
<details><summary>Answer</summary>

**A. Add it as permanent regression case before fixing** — Every failure becomes a test. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q5.** Extraction format must be exact.
- A. Human reads all
- B. LLM judge
- C.  vibes rubric
- D. Deterministic code/rule grader
<details><summary>Answer</summary>

**D. Deterministic code/rule grader** — Exact tasks allow cheap exact grading. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q6.** Change prompt+model+retrieval together; results improve, why unknown.
- A. Change more
- B. Ask model why
- C. Re-run changing one variable (or designed experiment) with pre-set metrics
- D. Ship and celebrate
<details><summary>Answer</summary>

**C. Re-run changing one variable (or designed experiment) with pre-set metrics** — Attribution needs isolation. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q7.** A/B test: cost -30%, safety violations double.
- A. Hide metric
- B. Don't ship: guardrail metric breached despite primary win
- C. Ship on cost
- D. Extend test until safety looks ok
<details><summary>Answer</summary>

**B. Don't ship: guardrail metric breached despite primary win** — Guardrails veto primary-metric wins. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q8.** Fluent answers cite nothing and invent policy.
- A. Grounding/hallucination diagnosis: check retrieval+citation eval
- B. Model mismatch always
- C. Tone problem
- D. Latency tuning
<details><summary>Answer</summary>

**A. Grounding/hallucination diagnosis: check retrieval+citation eval** — Unsupported fluency = grounding failure class. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q9.** Easy cases fail rarely, hard reasoning cases fail often on fast tier.
- A. Fast tier + more prompts
- B. Capable for everything forever
- C. Ignore hard cases
- D. Model mismatch by difficulty: route hard cases up a tier
<details><summary>Answer</summary>

**D. Model mismatch by difficulty: route hard cases up a tier** — Difficulty-sliced eval reveals routing fix. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q10.** Cost per call down, cost per solved task up (retries).
- A. More retries
- B. Cheaper model again
- C. Optimise cost per successful task
- D. Celebrate per-call
<details><summary>Answer</summary>

**C. Optimise cost per successful task** — Unit economics = successful outcome. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q11.** Eval set = 10 happy-path demos.
- A. Only golden
- B. Add edge, regression, adversarial slices from real failures/tickets
- C. Add 10 more demos
- D. Only adversarial
<details><summary>Answer</summary>

**B. Add edge, regression, adversarial slices from real failures/tickets** — Representative + hostile coverage. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q12.** Threshold discussion: 'monitor quality'.
- A. Numeric metric+threshold+baseline+owner (e.g., citation correctness ≥95%)
- B. Dashboard with no threshold
- C. Weekly feelings review
- D. Alert on everything
<details><summary>Answer</summary>

**A. Numeric metric+threshold+baseline+owner (e.g., citation correctness ≥95%)** — Monitor without threshold never fires a decision. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

## D5 Governance, Safety & Compliance (Trainer 6)

**Q1.** Webpage text instructs agent to email customer list; agent can.
- A. Hide webpage
- B. Treat retrieved content as untrusted data; tool AuthZ + remove email-anyone capability
- C. Stronger 'don't' prompt
- D. Capable model
<details><summary>Answer</summary>

**B. Treat retrieved content as untrusted data; tool AuthZ + remove email-anyone capability** — Indirect injection is stopped at capability/permission layer. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q2.** Agent can delete accounts autonomously.
- A. Pre-action human approval + caps + audit (irreversible/high impact)
- B. Post-hoc monthly review
- C. Prompt caution
- D. Faster approval by agent
<details><summary>Answer</summary>

**A. Pre-action human approval + caps + audit (irreversible/high impact)** — Reversibility × impact sets HITL placement. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q3.** EU candidate data sent wholesale to model; logs keep it forever.
- A. Prompt confidentiality
- B. Encrypt laptop
- C. Anonymise after logging
- D. Minimise fields, retention/deletion incl. index, access control, DPIA mindset (GDPR)
<details><summary>Answer</summary>

**D. Minimise fields, retention/deletion incl. index, access control, DPIA mindset (GDPR)** — GDPR is architectural: minimisation + lifecycle. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q4.** Clinic wants PHI in a tool with no BAA.
- A. Pilot with real PHI carefully
- B. Sign later
- C. Stop: no PHI flow until BAA + HIPAA safeguards (access, encryption, audit, minimum-necessary)
- D. De-identify by prompt
<details><summary>Answer</summary>

**C. Stop: no PHI flow until BAA + HIPAA safeguards (access, encryption, audit, minimum-necessary)** — BAA/safeguards precede data flow — hard gate. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q5.** Federal workload on non-authorised services.
- A. Document risk acceptance alone
- B. Choose FedRAMP-authorised services at required level; inherit controls, continuous monitoring
- C. Self-attest security
- D. VPN suffices
<details><summary>Answer</summary>

**B. Choose FedRAMP-authorised services at required level; inherit controls, continuous monitoring** — Authorised platform choices carry the compliance boundary. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q6.** Reviewers approve every AI draft in ~2s.
- A. Fix rubber-stamping: show uncertainty/sources, active confirmation, track agreement rates
- B. More reviewers
- C. Faster UI
- D. Remove review
<details><summary>Answer</summary>

**A. Fix rubber-stamping: show uncertainty/sources, active confirmation, track agreement rates** — 100% instant approval = broken HITL. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q7.** Hiring tool quality differs by demographic group.
- A. Prompt 'be fair'
- B. Remove group data and ignore outcomes
- C. Average metric
- D. Subgroup eval subsets, investigate data/prompt/model causes, document mitigation
<details><summary>Answer</summary>

**D. Subgroup eval subsets, investigate data/prompt/model causes, document mitigation** — Fairness is measured by outcomes per group. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q8.** Harmful output reached users; only input filter exists.
- A. Apology template
- B. Block all users
- C. Add output classifiers + escalation + sampled human audit
- D. Longer input filter
<details><summary>Answer</summary>

**C. Add output classifiers + escalation + sampled human audit** — Controls at the layer of the risk — output risk needs output controls. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q9.** Users don't know they're talking to AI or how to contest.
- A. Agent explains itself
- B. Disclose AI involvement; provide correction/appeal path
- C. Hide AI for UX
- D. FAQ page only
<details><summary>Answer</summary>

**B. Disclose AI involvement; provide correction/appeal path** — Transparency + redress are governance basics. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q10.** Runaway agent loop billed heavily overnight.
- A. Budgets, max iterations, timeout, kill switch, cost alerts
- B. Prompt 'be efficient'
- C. Weekly bill check
- D. Capable model
<details><summary>Answer</summary>

**A. Budgets, max iterations, timeout, kill switch, cost alerts** — Denial-of-wallet needs hard limits. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q11.** Safety plan = one system-prompt paragraph for a payments agent.
- A. Longer paragraph
- B. Legal disclaimer footer
- C. User warning
- D. Layered guardrails: input, grounding, tool AuthZ/limits, output checks, HITL, monitoring
<details><summary>Answer</summary>

**D. Layered guardrails: input, grounding, tool AuthZ/limits, output checks, HITL, monitoring** — High risk demands defence in depth. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q12.** Model confidently advises beyond its data freshness.
- A. Disclaimer only
- B. Bigger context
- C. Ground in retrieval, state limits/cutoff, escalate high-stakes
- D. Promise up-to-date
<details><summary>Answer</summary>

**C. Ground in retrieval, state limits/cutoff, escalate high-stakes** — Design around known limitations. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

## D6+D7 Delivery, Stakeholders & Claude Code (Trainer 7)

**Q1.** Sponsor expected autonomy; team built supervised assistant; launch friction.
- A. Demo only successes
- B. Early expectation alignment with options/trade-offs recorded in ADR
- C. Add autonomy at launch
- D. Blame sponsor
<details><summary>Answer</summary>

**B. Early expectation alignment with options/trade-offs recorded in ADR** — Alignment before build prevents launch surprise. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q2.** New lead asks why refunds use a workflow, not agent.
- A. Point to ADR with context, options, evidence, review trigger
- B. Rebuild as agent
- C. Architect's preference
- D. Chat history
<details><summary>Answer</summary>

**A. Point to ADR with context, options, evidence, review trigger** — Decisions live in records, not memories. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q3.** Legal hears about data flows at go-live.
- A.  brief legal faster
- B. Remove data flows
- C. Launch quietly
- D. Include risk owners (Legal/Security/Compliance) in discovery stakeholder map
<details><summary>Answer</summary>

**D. Include risk owners (Legal/Security/Compliance) in discovery stakeholder map** — Missing stakeholder = predictable launch-day surprise. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q4.** SLA promised: 'fast and accurate', unmeasured.
- A. Industry standard claim
- B. Best effort wording
- C. Define SLO metrics/measurement first, then promise SLA
- D. Promise, measure later
<details><summary>Answer</summary>

**C. Define SLO metrics/measurement first, then promise SLA** — Unmeasured promises are unmanageable. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q5.** Handoff = repo link; on-call can't handle 3 a.m. accuracy dip.
- A. Slack channel
- B. Handoff pack: runbook, dashboards, eval suite, ADRs, contacts + game-day
- C. More code comments
- D.  architect on call forever
<details><summary>Answer</summary>

**B. Handoff pack: runbook, dashboards, eval suite, ADRs, contacts + game-day** — Handoff passes the 3 a.m. test or it isn't handoff. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q6.** Accuracy dips after index deploy at 2 a.m.; first triage step?
- A. Check recent changes + stage observability (retrieval vs generation), replay eval, rollback if needed
- B. Rewrite prompt
- C. Upgrade model
- D. Wait for users
<details><summary>Answer</summary>

**A. Check recent changes + stage observability (retrieval vs generation), replay eval, rollback if needed** — Operational debugging starts with change + stage data. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q7.** Coding agent given prod repo + secrets, merges unreviewed.
- A. Faster merging
- B. Prompt 'be careful'
- C. More agents
- D. Least-privilege access, no secrets in context, PR review + test gates
<details><summary>Answer</summary>

**D. Least-privilege access, no secrets in context, PR review + test gates** — Dev agents obey the same least-privilege rules. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q8.** Team measures AI coding productivity by lines generated.
- A. Tokens generated
- B. Commits count
- C. Measure cycle time + defect/review outcomes
- D. Lines is fine
<details><summary>Answer</summary>

**C. Measure cycle time + defect/review outcomes** — Output volume ≠ productivity. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q9.** Claude Code workflow for a migration.
- A. Skip tests (AI wrote it)
- B. Context → plan → review plan → small steps → tests → human diff review
- C. One-shot full rewrite
- D. Auto-merge
<details><summary>Answer</summary>

**B. Context → plan → review plan → small steps → tests → human diff review** — Accountable human-in-the-loop engineering. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q10.** Requirements: 'make support better with AI'.
- A. Structured discovery: current process, volumes, pain/failure cost, testable requirements
- B. Start prototyping agent
- C. Pick model
- D. Survey tools
<details><summary>Answer</summary>

**A. Structured discovery: current process, volumes, pain/failure cost, testable requirements** — Testable requirements precede build. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q11.** Executives vs engineers need the design defended.
- A. Same slide dump both
- B. Tech-only defence
- C. Vision-only defence
- D. Tailor: execs value/cost/risk/SLA; engineers architecture/evals — same evidence
<details><summary>Answer</summary>

**D. Tailor: execs value/cost/risk/SLA; engineers architecture/evals — same evidence** — Stakeholder communication translates, doesn't dilute. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

**Q12.** Decision made 8 months ago may be stale after new model launch.
- A. Revisit on argument
- B. Auto-upgrade
- C. ADR review trigger fires: re-eval options with current evidence
- D. Never revisit
<details><summary>Answer</summary>

**C. ADR review trigger fires: re-eval options with current evidence** — Recorded triggers keep decisions alive. Wrong options fail because they either fix a different problem, act at the wrong layer, or violate the stated constraint.
</details>

---
Total trainer questions: 84. Next: timed mock in `mock-exam-63.md`.
