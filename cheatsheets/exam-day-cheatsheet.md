# Exam-Day Cheatsheet (one page — read the morning of)

**The loop:** Value → Pattern → Economics → Trust → Proof → Delivery. *Name the broken step first.*

| Symptom in stem | First suspect / best fix |
|---|---|
| Fixed steps built as free agent; cost/latency breach | Replace with routed workflow; cap/remove autonomy |
| Wrong answer after document refresh | **Stale chunks / index versioning & atomic swap** (before prompt/model!) |
| Agent misused a dangerous tool | Remove/narrow capability + server-side AuthZ (not prompt pleading) |
| 60+ tools, wrong-tool picks, slow | Trim tools + progressive discovery |
| Bill explodes, repeated long instructions | Stable prefix first + prompt caching; route easy→fast tier |
| “New prompt feels better” | Fixed eval set, baseline vs candidate, thresholds, subsets |
| Average up, one user group down | Subset regression — block ship |
| Injection hidden in a document/email | Retrieved content = untrusted data; tool-layer AuthZ; output checks |
| Irreversible + high impact | Pre-action human approval with summary + citations |
| PHI / EU personal data | Minimise, BAA/safeguards, retention+deletion (incl. index), access control |
| “Why did you choose X?” (auditor/new lead) | ADR with evidence + review trigger |
| Unmeasured SLA promise | Define SLO, measure (observability), then promise |

**Decision shortcuts:** Simplest pattern that works • Cheapest tier that passes eval • Fewest tools that do the job • Control at the layer of the risk • Measure, don't vibe.

**Pacing:** 63 Q / 120 min ≈ 1m54s each → target 90s, flag hard ones, final 10 min review. Never blank (verify no-negative-marking policy).

**“Choose two” = pair that completes the control** (prevent+detect, remove+gate, baseline+threshold).

⚠️ Verify on official pages before exam day: domain weights, pass mark (course cites 720), price/retake, model/protocol facts.
