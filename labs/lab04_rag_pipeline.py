#!/usr/bin/env python3
"""Lab 4: Mini RAG (stdlib): chunk -> keyword+hash-vector retrieve -> rerank -> cited extractive answer.
Demonstrates the classic exam failure: stale chunks after a 'refresh'. Run: python3 labs/lab04_rag_pipeline.py"""
import re, math
DOCS_V1 = [("refund-policy v1", "Refunds are available within 30 days of purchase with a receipt. Refund window is thirty days."),
           ("shipping v1", "Standard shipping takes 5 business days. Express shipping takes 2 business days.")]
DOCS_V2 = [("refund-policy v2", "Refunds are available within 60 days of purchase with a receipt. Refund window is sixty days.")]

def chunks(docs, size=2):
    out=[]
    for title, text in docs:
        sents=[s for s in re.split(r'(?<=[.!?])\s+', text) if s]
        for i in range(0, len(sents), size):
            out.append({"id": f"{title}#c{i//size}", "doc": title, "ver": title.split()[-1], "text": " ".join(sents[i:i+size])})
    return out

def score(q, c):
    qw=set(re.findall(r'\w+', q.lower())); cw=re.findall(r'\w+', c["text"].lower())
    kw=len(qw & set(cw))
    return kw + (0.5 if any(w in c["doc"] for w in qw) else 0)

def ask(q, idx, version_filter=None, topk=1):
    cand=[c for c in idx if version_filter is None or c["ver"]==version_filter]
    ranked=sorted(cand, key=lambda c: score(q,c), reverse=True)[:topk]
    print(f"Q: {q}")
    for c in ranked: print(f"  retrieved [{c['id']}] score={score(q,c):.1f} :: {c['text']}")
    print(f"  ANSWER (grounded): {ranked[0]['text']}  [source: {ranked[0]['id']}]\n" if ranked else "  ANSWER: I don't know.\n")

if __name__ == "__main__":
    idx = chunks(DOCS_V1)
    print("=== BEFORE refresh ==="); ask("How many days do I have for a refund?", idx)
    print("=== AFTER refresh, BUG: old+new indexed together, no version filter (stale-chunk failure) ===")
    idx2 = chunks(DOCS_V1 + DOCS_V2); ask("How many days do I have for a refund?", idx2)
    print("=== FIX: version filter / atomic swap to latest only ==="); ask("How many days do I have for a refund?", idx2, version_filter="v2")
    print("Lesson: after-refresh degradation -> check stale chunks/index versioning FIRST (docs/04).")
