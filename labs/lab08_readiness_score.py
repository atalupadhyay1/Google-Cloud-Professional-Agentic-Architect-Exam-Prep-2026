#!/usr/bin/env python3
"""Lab 8: Readiness estimate by domain weight. Illustrative planning tool — NOT a real exam score prediction.
Run: python3 labs/lab08_readiness_score.py  (edit SCORES with your trainer/mock % per domain)"""
SCORES = {"D1 Solution Design (17%)": 75, "D2 Models/Prompt (13%)": 70, "D3 Integration+RAG (19%)": 62,
          "D4 Evaluation (16%)": 68, "D5 Governance (14%)": 80, "D6 Stakeholders (14%)": 72, "D7 Dev Productivity (7%)": 65}
WEIGHTS = {"D1 Solution Design (17%)": .17, "D2 Models/Prompt (13%)": .13, "D3 Integration+RAG (19%)": .19,
           "D4 Evaluation (16%)": .16, "D5 Governance (14%)": .14, "D6 Stakeholders (14%)": .14, "D7 Dev Productivity (7%)": .07}
w = sum(SCORES[k]*WEIGHTS[k] for k in SCORES)
scaled = round(200 + w/100*600)  # illustrative mapping onto a 200-800-style scale; verify official scale/pass mark
zone = "READY (guide)" if w>=75 and min(SCORES.values())>=60 else "BORDERLINE" if w>=65 else "NOT YET"
print(f"Weighted practice score: {w:.1f}%  | Illustrative scaled estimate: ~{scaled} (course references pass 720 — verify officially) | Zone: {zone}")
for k,v in sorted(SCORES.items(), key=lambda x: x[1]*WEIGHTS[x[0]]): print(f"  {k:28} {v}%  (weighted points {v*WEIGHTS[k]:.1f})")
print("\nWeakest weighted domain first — that's your next study session. No domain below 60% before booking.")
