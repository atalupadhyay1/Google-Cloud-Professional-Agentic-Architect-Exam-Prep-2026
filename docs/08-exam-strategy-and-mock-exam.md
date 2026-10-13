# Module 8 — Exam Strategy & Mock Exam: Readiness Score & 63-Question Test
**Course Section 8 (46 min) • All 7 domains**  
*Tools from the course: Readiness Scorecard • 63-Question Mock Exam (120-minute timer)*

---

## 1. The human story

It's the week before the exam. One candidate re-reads everything, panicking equally about all seven domains. Another looks at her trainer scores *by domain weight*, sees Integration and Evaluation are costing her the most points, spends three days there, retakes a timed mock, and walks in calm. Same knowledge, different strategy. **This module is the second candidate's playbook.**

### Learning objectives
1. Use domain weights + trainer scores to target study where points actually are.
2. Read Professional items the way they're written (one defensible change for a failing system).
3. Calculate a readiness score against the scaled pass mark (720, as referenced in the course — verify officially).
4. Execute a 120-minute exam plan: pacing, flagging, review.

---

## 2. How a Professional item is built (read like the examiner)

Anatomy: **Context** (system + business constraint) → **Failure/constraint pressure** (cost breach, stale answers, misused tool, unproven change…) → **Four plausible fixes**. The correct one: fixes *that* failure, respects *that* constraint, at the *right layer*, with *evidence*.

**The 4-question elimination drill (use on every item, ~30 seconds):**
1. Which architect loop step is broken? (Module 0: Value / Pattern / Economics / Trust / Proof / Delivery)
2. Which options fix a *different* problem? ✂️ eliminate.
3. Which options fix it but violate the stated constraint (SLA/cost/risk) or sit at the wrong layer (prompt vs permission)? ✂️ eliminate.
4. Between survivors: which is *simplest, most enforceable, most measurable*? That's your answer.

**“Choose two” items:** Look for a *pair* that completes a control: preventive + detective, remove capability + add approval, measure baseline + set threshold. Two half-fixes from the same layer rarely pair correctly.

## 3. Readiness score — method

After each trainer/mock, compute per domain: `correct ÷ attempted`, then weight it (D1 17%, D2 13%, D3 19%, D4 16%, D5 14%, D6 14%, D7 7% — verify current weights). **Run:** `python3 labs/lab08_readiness_score.py` and enter your domain scores; it estimates a scaled-style score and zone:

| Zone (guide, not a guarantee) | Meaning | Action |
|---|---|---|
| 🔴 Not yet (< ~65% weighted) | Gaps in heavy domains | Return to modules for your two weakest *weighted* domains; trainers again |
| 🟡 Borderline (~65–75%) | A bad day could fail you | One more timed mock after targeted review; focus on trap patterns |
| 🟢 Ready (> ~75% with no domain < 60%) | Balanced readiness | Book it. Light review + cheatsheet only |

> ⚠️ Any scaled-score estimate from practice is an *approximation for study decisions*, never a promise about the real exam. The honest signal is: **no weak heavy domain + two timed mocks passed.**

## 4. The 120-minute exam plan

- **Pacing math:** 63 questions / 120 min ≈ 1 min 54 s each. Budget ~90 seconds; bank time on recall items for heavy scenarios.
- **Two passes:** Pass 1 — answer what you're confident in, *flag* the rest (don't bleed 5 minutes on one item). Pass 2 — flagged items with fresh eyes + elimination drill.
- **Final 10 minutes:** Review screen (like the course mock): check flagged, “choose two” completeness, accidental misclicks. Changing answers: only with a concrete reason (“I misread ‘after refresh’”), not anxiety.
- **Guessing:** Never leave blanks if there's no negative marking (verify current policy); an eliminated-down-to-two guess is a coin you should flip.
- **Logistics:** Book only via official Anthropic Partner Academy pages; check ID, retake (course referenced ~$175 / ≥14 days — verify current), and accommodations policies officially, early.

## 5. Hands-On Lab 8 — The Full Mock (this is the workout)

1. Set a **real 120-minute timer**. Phone away. Open [`practice/mock-exam-63.md`](../practice/mock-exam-63.md) — *questions only section first* (answer key is separated at the end; no peeking).
2. Flag uncertain items on paper as you go (mimics the exam review screen).
3. Score by domain, run Lab 8 readiness calculator, write your **top-3 fixes list** (one per weak domain: module to revisit + trainer set to redo).
4. Wait ≥48h, review misses with the module docs open, then re-sit *only* the missed domains' trainers in [`practice/domain-trainers.md`](../practice/domain-trainers.md).
5. Repeat with a fresh timed run before booking. **Deliverable:** Readiness Scorecard (template) with two timed attempts recorded.

## 6. Final-week plan & exam-day checklist

**Final week:** Mon–Tue weakest domain labs • Wed timed mock #2 • Thu miss review only • Fri cheatsheet + templates skim • Weekend: rest, logistics, early night. *No new topics in the last 48h.*
**Exam day:** ID ready • Arrive/log in early • Water, break policy checked • First question ritual: breathe, name the broken loop-step, eliminate.

## 7. After the exam (pass or not — act like an architect)
- **Passed:** Keep the architect's kit alive on a real system; schedule model/eval reviews; mentor someone (teaching is the best retention).
- **Not yet:** Your score report by domain *is* your study plan. Wait the required retake period (verify), fix the two heaviest weak domains with labs (not just reading), re-mock, return. A failed attempt is data, not a verdict.

**Cheatsheet →** [`../cheatsheets/exam-day-cheatsheet.md`](../cheatsheets/exam-day-cheatsheet.md) • **All templates →** [`../templates/architect-kit.md`](../templates/architect-kit.md)

*You've built the judgment. Trust the loop: name the failure, fix that layer, prove it with evidence. Good luck — go earn it.* 🎓
