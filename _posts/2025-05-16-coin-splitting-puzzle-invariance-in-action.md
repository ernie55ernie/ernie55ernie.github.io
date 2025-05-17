---
layout: post
title: "Coin-Splitting Puzzle: Invariance in Action"
date: 2025-05-16
category: quantitative interview
---

You begin with a single pile of **1,000 identical coins**. You repeatedly do the following:

1. **Split** any pile of size \\(n\\) into two parts of size \\(x\\) and \\(n - x\\),
2. Add the product \\(x(n - x)\\) to a **running total**,
3. Repeat until all piles are of size **1**.

> **Question:** What is the final total, and why is it **always the same**, no matter how you split?

---

## Step 1: Understand the Process

Every time you split a pile of size \\(n\\) into two parts \\(x\\) and \\(n - x\\):

- You generate a new term: \\(x(n - x)\\)
- Eventually, you end with **1,000 piles of 1 coin each**

So you make **999 splits** total to go from 1 pile → 1,000 piles.

---

## Step 2: Look for an Invariant

Let’s define a total function over all current piles:

\\[
F = \sum_{i=1}^k n_i^2
\\]
where \\(n_i\\) is the size of each pile and \\(k\\) is the number of piles.

Observe what happens in one split:

- You replace a pile of size \\(n\\) with two piles \\(x\\) and \\(n - x\\)
- The total \\(F\\) changes from:
  \\[
  n^2 \to x^2 + (n - x)^2 = n^2 - 2x(n - x)
  \\]

So each split **reduces \\(F\\)** by exactly:
\\[
\Delta F = -2x(n - x)
\\]

Hence, the term \\(x(n - x)\\) added to the running total corresponds to a **drop of \\( \Delta F = -2x(n - x) \\)**.

So if \\(T\\) is the running total sum of all \\(x(n - x)\\), then:

\\[
F_{\text{initial}} - F_{\text{final}} = 2T
\\]

---

## Step 3: Apply the Invariant

- Start with one pile of size 1,000 → \\(F_{\text{initial}} = 1000^2 = 1,000,000\\)
- End with 1,000 piles of 1 → \\(F_{\text{final}} = 1,000 \times 1^2 = 1,000\\)

Thus:

\\[
1,000,000 - 1,000 = 2T \Rightarrow T = \frac{999,000}{2} = 499,500
\\]

---

## Final Answer

> The final total is always **499,500**.  
> It is **invariant** under the splitting choices because the decrease in the sum of squares \\(F\\) is always **twice** the accumulated total.

# Reference

* [1] [Brain Teaser 32: Coin Split](https://medium.com/intuition/brain-teaser-32-coin-split-problem-3cca42e59b15)
