---
layout: post
title: "Simplex Volume: Probability the Sum of Uniforms is ≤ 1"
date: 2025-05-20
category: quantitative interview
---

### The Problem

Let \\( X_1, \dots, X_n \\) be independent and identically distributed random variables from the **Uniform(0,1)** distribution.

We want to compute:

\\[
\Pr\left(X_1 + X_2 + \cdots + X_n \le 1\right)
\\]

---

## Geometric Interpretation

This is equivalent to asking for the **volume** of the region:

\\[
\left\{ (x_1, \dots, x_n) \in [0,1]^n : x_1 + x_2 + \cdots + x_n \le 1 \right\}
\\]

This region is the **standard n-dimensional simplex** within the unit cube.

---

## Known Result

The volume of this simplex is:

\\[
\boxed{\frac{1}{n!}}
\\]

This result can be derived via iterated integrals or combinatorics, and is a classical formula in probability and geometry.

---

## Final Answer

\\[
\boxed{\frac{1}{n!}}
\\]

This is both the probability that the sum of \\( n \\) independent Uniform(0,1) variables is at most 1, and the volume of the corresponding simplex.

---

## Reference

* [1] [Simplex volume and Uniform sums](https://en.wikipedia.org/wiki/Simplex#Volume)