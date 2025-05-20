---
layout: post
title: "Coupon Collector Problem: Full Collection and Expected Diversity"
date: 2025-05-20
category: quantitative interview
---

This classic problem models situations where you're collecting items (like cereal box prizes or trading cards) drawn randomly with replacement.

---

## The Setup

- There are \\( N \\) **distinct** coupon types.
- Each box (draw) gives one coupon, chosen **uniformly at random** among the \\( N \\) types.

---

### Part A: Expected Number of Draws to Collect All \\( N \\) Coupons

Let \\( T \\) be the number of draws needed to collect **all \\( N \\)** coupon types.

**Key Idea**: The process of collecting all coupons proceeds in **phases**:

- First new coupon: expected 1 draw
- Second new coupon: expected \\( \frac{N}{N-1} \\) draws
- ...
- Final coupon: expected \\( \frac{N}{1} = N \\) draws

So the total expected number is:

\\[
\mathbb{E}[T] = N \cdot \left( \frac{1}{1} + \frac{1}{2} + \cdots + \frac{1}{N} \right) = N \cdot H_N
\\]

where \\( H_N \\) is the \\( N \\)-th **harmonic number**.

**Approximation**: \\( H_N \approx \ln N + \gamma \\), where \\( \gamma \approx 0.5772 \\) is Euler–Mascheroni constant.

---

### Part B: Expected Number of Distinct Coupons After \\( n \\) Boxes

Let \\( D_n \\) be the number of **distinct** coupons observed after \\( n \\) draws.

For each coupon type \\( i \\), the probability it's **not seen** in \\( n \\) trials is \\( \left(1 - \frac{1}{N} \right)^n \\). So the probability it's **seen** is:

\\[
1 - \left(1 - \frac{1}{N} \right)^n
\\]

By linearity of expectation:

\\[
\mathbb{E}[D_n] = N \cdot \left(1 - \left(1 - \frac{1}{N} \right)^n\right)
\\]

---

## Final Answers

- **Part A**: Expected number of draws to collect all \\( N \\) coupons is:

  \\[
  \boxed{N \cdot H_N = N \left( \frac{1}{1} + \frac{1}{2} + \cdots + \frac{1}{N} \right)}
  \\]

- **Part B**: Expected number of distinct coupons seen after \\( n \\) draws is:

  \\[
  \boxed{N \cdot \left(1 - \left(1 - \frac{1}{N} \right)^n \right)}
  \\]

---

## Reference

* [1] [Wikipedia: Coupon collector's problem](https://en.wikipedia.org/wiki/Coupon_collector%27s_problem)
