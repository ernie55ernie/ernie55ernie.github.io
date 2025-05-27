---
layout: post
title: "Expected Tosses Until Two Consecutive Heads"
date: 2025-05-27
category: quantitative interview
---

We want to compute the expected number of tosses required to get **two heads in a row** using:

- A **fair coin** (\\( P(H) = 0.5 \\))
- A **biased coin** (\\( P(H) = 0.25 \\))

---

### Setup: Markov States

We define three states:

- \\( S_0 \\): Start (no heads yet)
- \\( S_1 \\): Last toss was Head
- \\( S_2 \\): Two consecutive heads (target)

Let \\( E_0 \\), \\( E_1 \\), \\( E_2 = 0 \\) be the expected number of steps to reach \\( S_2 \\) from each state.

---

### Recurrence Relations

Let \\( p \\) be the probability of Heads.

Then:

- From \\( S_0 \\):  
  \\[
  E_0 = 1 + p E_1 + (1 - p) E_0
  \Rightarrow E_0 = \frac{1 + p E_1}{p}
  \\]

- From \\( S_1 \\):  
  \\[
  E_1 = 1 + p \cdot 0 + (1 - p) E_0
  = 1 + (1 - p) E_0
  \\]

---

### Part 1: Fair Coin (\\( p = 0.5 \\))

Plug in \\( p = 0.5 \\):

From \\( E_1 = 1 + 0.5 E_0 \\)

Substitute into \\( E_0 \\):

\\[
E_0 = \frac{1 + 0.5(1 + 0.5 E_0)}{0.5}
= \frac{1 + 0.5 + 0.25 E_0}{0.5}
= \frac{1.5 + 0.25 E_0}{0.5}
= 3 + 0.5 E_0
\\]

Solve:

\\[
E_0 - 0.5 E_0 = 3 \Rightarrow 0.5 E_0 = 3 \Rightarrow \boxed{E_0 = 6}
\\]

---

### Part 2: Biased Coin (\\( p = 0.25 \\))

Now \\( p = 0.25 \\). From:

\\[
E_1 = 1 + (1 - 0.25) E_0 = 1 + 0.75 E_0
\\]

\\[
E_0 = \frac{1 + 0.25 E_1}{0.25}
= \frac{1 + 0.25(1 + 0.75 E_0)}{0.25}
= \frac{1 + 0.25 + 0.1875 E_0}{0.25}
= \frac{1.25 + 0.1875 E_0}{0.25}
= 5 + 0.75 E_0
\\]

Solve:

\\[
E_0 - 0.75 E_0 = 5 \Rightarrow 0.25 E_0 = 5 \Rightarrow \boxed{E_0 = 20}
\\]

---

## Conclusion

- Fair coin (\\( p = 0.5 \\)): \\( \boxed{6} \\) tosses
- Biased coin (\\( p = 0.25 \\)): \\( \boxed{20} \\) tosses

# Reference

* [1] [Expected Number of coin flips for 2 consecutive heads for first time](https://math.stackexchange.com/questions/2845196/expected-number-of-coin-flips-for-2-consecutive-heads-for-first-time)