#!/usr/bin/env python3
"""Lab 6: Guardrail & compliance matrix scaffold. Run: python3 labs/lab06_guardrail_matrix.py"""
ROWS=[
 ("Prompt injection via retrieved docs","TOOL layer","Preventive","Treat retrieved content as untrusted data; server-side AuthZ on every tool call","Security"),
 ("Irreversible refund/deletion","HUMAN layer","Preventive","Pre-action human approval with summary+citations; amount caps","Ops lead"),
 ("PII in prompts/logs (GDPR)","INPUT+DETECTIVE","Preventive+Detective","Minimise/redact fields; log IDs not raw PII; retention+deletion incl. index","DPO/Privacy"),
 ("PHI without safeguards (HIPAA)","ALL layers","Preventive","No PHI flow until BAA, access control, encryption, audit logs in place","Compliance"),
 ("Harmful/biased output","OUTPUT layer","Detective","Output classifier + subgroup eval subsets + appeal/correction path","Product"),
 ("Runaway agent cost","MODEL/TOOL","Corrective","Max iterations, token budget, timeout, kill switch, cost alerts","Platform"),
]
if __name__=="__main__":
    print(f"{'RISK':38} {'LAYER':13} {'TYPE':22} CONTROL / OWNER")
    for r,l,t,c,o in ROWS: print(f"{r:38} {l:13} {t:22} {c}  [Owner: {o}]")
    print("\nComplete the full matrix in templates/architect-kit.md for YOUR use case. Prompts guide — controls enforce.")
