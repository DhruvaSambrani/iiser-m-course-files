---
title: Generalized FSA, Context Free Grammar
date: February 24, 2020
author: Dhruva Sambrani
---

## cont.

Let's black box a set of states to a single path.

Define the complexity of the FSA as the # of states. If we keep reducing the states, we'll eventually get to the simplest form.

Only one start state and only one accept state.
This can always be done.
If multiple starts, just put another state and take epsilons to the starts.
Similarly from the finals to a single Final state.

Lets attempt to make it simpler (as defined above).

**Defn:** A genralised path b/w states is one that accepts a Regex instead of just a character.

Hence we are building a "Generalised" FSA, where δ is not over Σ, but rather over 𝒫(Σ).
We also define a ∅ path(empty connection), which takes from q1 to q2 when it reads nothing.

Suppose ![fig 2402.1](2402.1.jpg)

Then, to remove R<sub>k</sub>, change the path from q<sub>i</sub> to q<sub>j</sub> via R<sub>ij</sub> ∪ R<sub>i</sub> ∘ R<sub>k</sub><sup>*</sup>∘R<sub>j</sub>

Now suppose R<sub>i</sub> was ∅, then R'<sub>ij</sub> will also be ∅, so its a nice theoretic help.

Hence we can keep repeating to finally get a single regex.

---

## Context Free Grammars

## Consider the grammer of Arithmetic over +,-,*,/

Every expression can be broken into smaller expressions.
The shortest expressions are those which are numbers.

Hence

E → E+E \| E-E \| E*E \| E/E \| (E) \| N

where,

N → 0 \| 1 \| ... \| 9 \| 0N \| 1N \| ... \| 9N

Hence checking if a string is E is basically a recursion to check if every part can be reduced to an expression.

(5+7) * 8

1. E → E * N
2. E → (E) * N
3. E → (N + N) * N

### 0<sup>N</sup>1<sup>N</sup>
E → 01 \| 0E1

### Defn

We can now define a context free gramm
