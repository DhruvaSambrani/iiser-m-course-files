---
title: Non-deterministic Finite State Automaton

date: February 10, 2020

author: Dhruva Sambrani
---

## Problem of Language Unions
Given two regular languages, L and L' are regular, then L ∪ L' is also regular.

M = (Q, Σ, δ, q<sub>0</sub>, F)

M' = (Q', Σ, δ', q<sub>0</sub>', F')

### Make a DFA M'' which accepts L1 ∪ L2.

- Q'' = Q × Q'
- q<sub>0</sub>'' = q<sub>0</sub> × q<sub>0</sub>'
- δ'' ((q<sub>i</sub>, q<sub>j</sub>'), a) -> (δ(q<sub>i</sub>, a), δ(q<sub>j</sub>', a))
- F'' = \{F×Q' ∪ Q×F'\}

#### Proof that this works -
let s = w<sub>1</sub>w<sub>2</sub>w<sub>3</sub>...w<sub>n</sub> which is accepted.

Then ∃ r<sub>0</sub>'', r<sub>1</sub>'', ... r<sub>n</sub>'' st r<sub>n</sub>'' ∈ F''
and δ(r<sub>i</sub>'', w<sub>i</sub>'') = r<sub>i+1</sub>

But by definition, r<sub>n</sub>'' is (r<sub>j</sub>, r<sub>k</sub>') where either r<sub>j</sub> accepts s or r<sub>k</sub>' accepts s.

## Non-Deterministic Finite State Automaton
Instead of moving to one state only, it goes to a _set_ of states.

N = (Q, Σ, δ, q<sub>0</sub>, F)

δ: (Q × (Σ, ϵ)) -> ⋃ Q<sup>i</sup> where i ∈ 𝐍
