---
layout: post
title: "Probability of Strictly Increasing Dice Rolls"
date: 2025-05-19
category: quantitative interview
---

### The Puzzle

You roll **three fair six-sided dice** in sequence.

**Question:** What is the probability that the three outcomes come up in **strictly increasing order** (i.e. first < second < third)?

---

## Total Outcomes

Each die has 6 sides, and they are rolled independently. So the total number of possible outcomes is:

\\[
6 \times 6 \times 6 = 216
\\]

---

## Favorable Outcomes

We count the number of **strictly increasing** sequences. Since all dice must show **distinct values** in **increasing order**, we:

1. Choose 3 **distinct** numbers from \\( \{1, 2, 3, 4, 5, 6\} \\). There are:

\\[
\binom{6}{3} = 20
\\]

2. Each such triple has exactly **one** increasing arrangement (e.g. 2, 4, 6).

So, there are 20 favorable outcomes.

---

## Final Probability

\\[
P(\text{strictly increasing}) = \frac{20}{216} = \frac{5}{54}
\\]

---

## Answer

\\[
\boxed{\frac{5}{54}}
\\]

## Reference

* [1] [Increasing Dice Order I - Quant Interview Question](https://www.youtube.com/watch?v=UcZbX1xdmLg)
