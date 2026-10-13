#!/usr/bin/env python3
"""Lab 2: Model-tier + prompt-caching simulator. Illustrative prices ONLY — replace with current official pricing.
Run: python3 labs/lab02_prompt_caching_cost.py"""
def monthly(requests, prefix_tok, var_tok, out_tok, in_price, out_price, cached_price=None, hit=0.0):
    cached_tok = prefix_tok * hit
    fresh = prefix_tok - cached_tok + var_tok
    cost = requests * (fresh/1_000_000*in_price + cached_tok/1_000_000*(cached_price if cached_price is not None else in_price) + out_tok/1_000_000*out_price)  # prices are $ per million tokens
    return cost

if __name__ == "__main__":
    R, PRE, VAR, OUT = 1_000_000, 4000, 600, 300
    tiers = {"fast": (0.30, 1.50), "balanced": (1.00, 5.00), "capable": (5.00, 25.00)}  # $/MTok illustrative
    for name,(i,o) in tiers.items():
        print(f"{name:9} no-cache ${monthly(R,PRE,VAR,OUT,i,o):>10,.0f}/mo | cached(90% hit, cached=10% price) ${monthly(R,PRE,VAR,OUT,i,o,i*0.1,0.9):>10,.0f}/mo")
    print("\nRouted workload (80% fast / 20% capable, cached): ",
          f"${0.8*monthly(R,PRE,VAR,OUT,*tiers['fast'],cached_price=tiers['fast'][0]*0.1,hit=0.9)+0.2*monthly(R,PRE,VAR,OUT,*tiers['capable'],cached_price=tiers['capable'][0]*0.1,hit=0.9):,.0f}/mo")
    print("Try: hit=0.7 vs 1.0; add 10 few-shot examples (+1500 prefix tokens) with/without caching. See docs/02.")
