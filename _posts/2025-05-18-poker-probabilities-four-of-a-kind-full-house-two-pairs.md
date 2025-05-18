---
layout: post
title: "Poker Probabilities: Four-of-a-Kind, Full House, Two Pairs"
date: 2025-05-18
category: quantitative interview
---

In 5-card poker, the odds of specific hands reveal the beautiful combinatorics of a 52-card deck.

> **Problem:**  
> What is the probability of being dealt each of the following 5-card hands?
>
> 1. **Four-of-a-kind**  
> 2. **Full house**  
> 3. **Two pairs**

---

## Total Possible Hands

There are:

\\[
\binom{52}{5} = 2,\!598,\!960 \text{ possible 5-card hands}
\\]

We'll calculate the number of favorable hands for each case and divide by this total.

---

## 1. Four-of-a-Kind

- Choose the **rank** for the four-of-a-kind: \\(13\\) choices
- Choose **4 suits** for that rank: exactly 1 way
- Choose the **fifth card**: any of the remaining \\(52 - 4 = 48\\) cards (but **not** the same rank)

\\[
\text{Favorable hands} = 13 \times 48 = 624
\\]
\\[
\text{Probability} = \frac{624}{2,\!598,\!960} \approx \boxed{0.000240}
\\]

---

## 2. Full House

- Choose the **rank** for the three-of-a-kind: \\(13\\) choices
- Choose **3 suits** from 4: \\(\binom{4}{3} = 4\\)
- Choose a **different rank** for the pair: \\(12\\) choices
- Choose **2 suits** from 4: \\(\binom{4}{2} = 6\\)

\\[
\text{Favorable hands} = 13 \times 4 \times 12 \times 6 = 3,\!744
\\]
\\[
\text{Probability} = \frac{3,\!744}{2,\!598,\!960} \approx \boxed{0.001440}
\\]

---

## 3. Two Pairs

- Choose 2 distinct **ranks** for the pairs: \\(\binom{13}{2} = 78\\)
- Choose 2 suits for each pair: \\(\binom{4}{2} \times \binom{4}{2} = 6 \times 6\\)
- Choose a **third rank** (not used above) for the kicker: \\(13 - 2 = 11\\)
- Choose any 1 suit for that card: 4

\\[
\text{Favorable hands} = 78 \times 6 \times 6 \times 11 \times 4 = 123,\!552
\\]
\\[
\text{Probability} = \frac{123,\!552}{2,\!598,\!960} \approx \boxed{0.047539}
\\]

---

## Final Answers

| Hand            | Count     | Probability      |
|-----------------|-----------|------------------|
| Four-of-a-kind  | 624       | 0.000240         |
| Full House      | 3,744     | 0.001440         |
| Two Pairs       | 123,552   | 0.047539         |

# Reference

* [1] [Poker Hand Combinatorics](https://en.wikipedia.org/wiki/Poker_probability)
