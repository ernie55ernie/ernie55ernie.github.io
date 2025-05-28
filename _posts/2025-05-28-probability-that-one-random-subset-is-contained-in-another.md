---
layout: post
title: "Probability that One Random Subset is Contained in Another"
date: 2025-05-28
category: quantitative interview
---

## Problem

Let \\( X \\) be a finite set with \\( n \\) elements. Choose two subsets \\( A \\) and \\( B \\) of \\( X \\) **uniformly at random and independently**.

What is the probability that:

\\[
A \subseteq B \ ?
\\]

---

## Step-by-Step Solution

### 1. Total Number of Pairs

Each of the \\( 2^n \\) subsets is equally likely, so the total number of pairs \\( (A, B) \\) is:

\\[
2^n \times 2^n = 4^n
\\]

---

### 2. When Is \\( A \subseteq B \\)?

For each element \\( x \in X \\), there are 3 possible outcomes for \\( (x \in A, x \in B) \\):

- Case 1: \\( x \notin A, x \notin B \\)
- Case 2: \\( x \notin A, x \in B \\)
- Case 3: \\( x \in A, x \in B \\)

But the case \\( x \in A, x \notin B \\) **violates** \\( A \subseteq B \\). So among the 4 possible combinations of inclusion for \\( x \\), **only 3 are allowed**.

---

### 3. Per-Element Probability

For each element, the total number of valid combinations satisfying \\( A \subseteq B \\) is **3** out of 4. Since elements are independent:

\\[
P(A \subseteq B) = \left( \frac{3}{4} \right)^n
\\]

---

## Final Answer

\\[
\boxed{P(A \subseteq B) = \left( \frac{3}{4} \right)^n}
\\]

This decreases exponentially as \\( n \\) increases.

# Reference

* [1] [Probability that one randomly chosen subset of a finite set is a subset of another](https://math.stackexchange.com/questions/509147/probability-that-one-randomly-chosen-subset-of-a-finite-set-is-a-subset-of-anoth)