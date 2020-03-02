---
title: Context-free Grammars and Regular Languages
date: March 02, 2020
author: Dhruva Sambrani
---

## Write a context free grammar for every rular language.

Every state is nothing but a rule.
If δ(a,q<sub>i</sub>) = q<sub>j</sub>

then R<sub>i</sub> → aR<sub>j</sub>

R<sub>j</sub> → ϵ if q<sub>j</sub> ∈ F

And the Context free grammar is
- V = \{R<sub>j</sub>\}
- Σ = Σ
- R given as above
- S is R<sub>0</sub>

## Contd.

## Parse to check if Expr.

1. Initialise a Stack with $
1. Push S to a Stack
1. Branch and make stacks every possible rule
1. If left most element


## Push Down automaton
**Defn:** It is a Tuple
P = (Q, Σ, Γ, δ, q<sub>0</sub>, F)
- Q is a finite set of "states"
- Σ is a finite set called the alphabet
- Γ is a finite set called the stack alphabet
- q<sub>0</sub> ∈ Q is start state
- F⊆Q
- δ: Q × (Σ∪\{ϵ\}) × (Γ∪\{ϵ\}) → 𝒫(Q × (Γ ∪ \{ϵ\})

### Example
0<sup>N</sup>1<sup>N</sup>

**Informal-**
1. If read a zero, push to stack
2. If read a one, pop from stack
3. Accept if stack is empty

**Formal**

Build P = (Q, Σ, Γ, q<sub>0</sub>, F, δ)
