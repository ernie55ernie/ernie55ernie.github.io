---
layout: post
title: "Correlation and Joint Probability Bounds: At Least One Default"
date: 2025-05-20
category: quantitative interview
---

You are given:

\\[
P(A \text{ defaults}) = 0.50, \quad P(B \text{ defaults}) = 0.30
\\]

Let’s denote:

- \\( 1_A \\): Indicator for A defaulting
- \\( 1_B \\): Indicator for B defaulting

---

## Part 1: Bounds on \\( P(A \cup B) \\)

By the inclusion-exclusion principle:

\\[
P(A \cup B) = P(A) + P(B) - P(A \cap B)
\\]

Since \\( P(A) = 0.5 \\) and \\( P(B) = 0.3 \\), we have:

\\[
P(A \cup B) = 0.5 + 0.3 - P(A \cap B)
\\]

To bound this, we need bounds on \\( P(A \cap B) \\).

- **Minimum** of \\( P(A \cap B) \\): \\( \max(0, P(A) + P(B) - 1) = \max(0, 0.5 + 0.3 - 1) = \boxed{0.0} \\)
- **Maximum** of \\( P(A \cap B) \\): \\( \min(P(A), P(B)) = \boxed{0.3} \\)

### Therefore:

- **Max \\( P(A \cup B) \\)** = \\( 0.5 + 0.3 - 0 = \boxed{0.8} \\)
- **Min \\( P(A \cup B) \\)** = \\( 0.5 + 0.3 - 0.3 = \boxed{0.5} \\)

---

## Part 2: Bounds on Correlation \\( \mathrm{Corr}(1_A, 1_B) \\)

We compute the correlation of the binary indicators:

\\[
\mathrm{Corr}(1_A, 1_B) = \frac{\mathrm{Cov}(1_A, 1_B)}{\sqrt{\mathrm{Var}(1_A) \cdot \mathrm{Var}(1_B)}}
\\]

- \\( \mathrm{Cov}(1_A, 1_B) = P(A \cap B) - P(A)P(B) \\)
- \\( \mathrm{Var}(1_A) = 0.5(1 - 0.5) = 0.25 \\)
- \\( \mathrm{Var}(1_B) = 0.3(1 - 0.3) = 0.21 \\)

\\[
\mathrm{Corr}(1_A, 1_B) = \frac{P(A \cap B) - 0.15}{\sqrt{0.25 \cdot 0.21}} = \frac{P(A \cap B) - 0.15}{\sqrt{0.0525}}
\\]

- Max \\( P(A \cap B) = 0.3 \\): Correlation = \\( \frac{0.3 - 0.15}{\sqrt{0.0525}} \approx \boxed{0.6547} \\)
- Min \\( P(A \cap B) = 0.0 \\): Correlation = \\( \frac{0 - 0.15}{\sqrt{0.0525}} \approx \boxed{-0.6547} \\)

---

## Final Answers

### (1) Bounds on \\( P(A \cup B) \\):

\\[
\boxed{0.5 \le P(A \cup B) \le 0.8}
\\]

### (2) Corresponding bounds on \\( \mathrm{Corr}(1_A, 1_B) \\):

\\[
\boxed{-0.6547 \le \mathrm{Corr}(1_A, 1_B) \le 0.6547}
\\]

---

## Reference

* [1] [Fréchet inequalities and correlation bounds](https://en.wikipedia.org/wiki/Fr%C3%A9chet_inequalities)
