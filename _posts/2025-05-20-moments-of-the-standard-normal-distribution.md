---
layout: post
title: "Moments of the Standard Normal Distribution"
date: 2025-05-20
category: quantitative interview
---

Let \\( X \sim N(0,1) \\) be a **standard normal** random variable. We are asked to compute the **raw moments**:

\\[
E[X^n] \quad \text{for } n = 1, 2, 3, 4
\]

---

## Moment Definitions

For a random variable \\( X \\), the \\( n \\)-th **raw moment** is:

\\[
\mu_n' = E[X^n]
\]

For the standard normal, the moments can be derived either by integrating against the density or using known properties of the distribution.

---

## Computations

### 1. First Moment

\\[
E[X] = 0
\]

(because the normal is symmetric about zero)

---

### 2. Second Moment (Variance)

\\[
E[X^2] = \text{Var}(X) + (E[X])^2 = 1 + 0 = 1
\]

---

### 3. Third Moment

\\[
E[X^3] = 0
\]

(odd moment of a symmetric distribution around 0)

---

### 4. Fourth Moment

The fourth moment of a standard normal is:

\\[
E[X^4] = 3
\]

This comes from the identity for the fourth moment of a normal variable:

\\[
E[X^4] = 3\sigma^4 \quad \text{when } X \sim N(0, \sigma^2)
\]

---

## Final Results

\\[
\boxed{
E[X] = 0,\quad
E[X^2] = 1,\quad
E[X^3] = 0,\quad
E[X^4] = 3
}
\]

---

## Reference

* [1] [Wikipedia: Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution#Moments)