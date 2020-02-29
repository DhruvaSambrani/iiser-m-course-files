---
title: NFA
date: February 12, 2020
author: Dhruva Sambrani
---

## Formal Defn of an NFA

M = ( Q, Σ, δ, q<sub>0</sub>, F )

δ : Q × (Σ ∪ {ϵ}) → 𝒫(Q)

An NFA N accepts a string s = w<sub>1</sub>w<sub>2</sub>w<sub>3</sub>...w<sub>n</sub> iff
∃ a sequence of r<sub>0</sub>r<sub>1</sub>...r<sub>n</sub> ∈ Q such that
r<sub>n</sub> ∈ F and
r<sub>i+1</sub> ∈ δ(r<sub>i</sub>, w<sub>i</sub>)

## Equivalence of NFA and DFA

**Theorem:**
L is regular iff it can be recognized by an NFA.

**Proof:**

If L is recognisable by a NFA (let) N = (Q, Σ, δ, q<sub>0</sub>, F)

Consider the DFA,  D = (Q', Σ, δ', q<sub>0</sub>', F') where  -

- Q' = 𝒫(Q)
- δ' : Q' → Q' and
  - δ'(A, c) → ⋃ E(δ(a,c)), where
    - a∈A
    - E(A) = the set of states connected to some q∈A by ϵ. Trivially, some qs map to themselves via a ϵ.
- q<sub>0</sub>' = E(q<sub>0</sub>)
- F' = {A'∈Q' | A∩F ≠ ∅}

If S is accepted by N iff ∃ r<sub>0</sub>...r<sub>n</sub> ∈ Q r<sub>0</sub>=q<sub>0</sub> and r<sub>i+1</sub> ∈ δ(r<sub>i</sub>, w<sub>i</sub>)

⟹ r<sub>i+1</sub> ∈ R<sub>i</sub> = E(δ(r<sub>i</sub>, w<sub>i</sub>)) and r<sub>n</sub> ∈ R<sub>n</sub> ∈ F.
