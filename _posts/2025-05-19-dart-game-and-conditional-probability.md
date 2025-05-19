---
layout: post
title: "Dart Game and Conditional Probability"
date: 2025-05-19
category: quantitative interview
---

Jason plays a game involving darts thrown at a board, all aimed at the center. Here’s the puzzle setup:

---

### The Problem

- Jason throws **two darts**. 
- The **second** dart lands **farther** from the center than the **first**.
- Now, Jason throws a **third** dart.

**Question:** What is the probability that the **third dart** lands **farther** from the center than the **first**?

All throws are **independent and identically distributed** around the center.

---

## Reasoning

Let the distances from the center be:

- \\( X_1 \\): distance of the **first** dart
- \\( X_2 \\): distance of the **second** dart
- \\( X_3 \\): distance of the **third** dart

We are told that:

\\[
X_2 > X_1
\\]

We are asked to compute:

\\[
P(X_3 > X_1 \mid X_2 > X_1)
\\]

---

### Key Insight

The distances \\( X_1, X_2, X_3 \\) are **i.i.d. continuous random variables**, so no two distances are exactly equal.

We condition on the event \\( X_2 > X_1 \\) and ask for the probability that \\( X_3 > X_1 \\).

Symmetry implies that all 6 permutations of the values \\( X_1, X_2, X_3 \\) are equally likely.

Given \\( X_2 > X_1 \\), we are equally likely to be in any of the 3 permutations of \\( X_1, X_2, X_3 \\) that satisfy \\( X_2 > X_1 \\). In two of these three, \\( X_3 > X_1 \\).

---

## Conclusion

Thus, the probability that the **third** dart is **farther** than the **first**, given that the **second** dart was farther than the first, is:

\\[
\boxed{\frac{2}{3}}
\\]

## Reference

* [1] [Dart Throw Probability](https://math.stackexchange.com/questions/1523507/dart-throw-probability)