---
layout: post
title: "Gambler’s Ruin: Reaching the Goal Before Going Broke"
date: 2025-05-19
category: quantitative interview
---

### The Puzzle

A gambler starts with \\( i \\) dollars. Each time he plays:

- He **wins \$1** with probability \\( p \\)
- He **loses \$1** with probability \\( q = 1 - p \\)

He continues playing until:

- He reaches **\\( N \\)** dollars (goal), or
- He reaches **0** dollars (ruin)

### Question:

What is the probability that he **reaches \\( N \\)** before going broke?

---

## Solution

Let \\( P_i \\) be the probability that the gambler reaches \\( N \\) starting from \\( i \\).

---

### Case 1: \\( p = q = \frac{1}{2} \\) (Fair Game)

This is the symmetric case. Then:

\\[
P_i = \frac{i}{N}
\\]

So the probability of success is simply proportional to how far along he is toward \\( N \\).

---

### Case 2: \\( p \ne \frac{1}{2} \\) (Biased Game)

The general formula is:

\\[
P_i = \frac{1 - \left( \frac{q}{p} \right)^i}{1 - \left( \frac{q}{p} \right)^N} \quad \text{for } p \ne q
\\]

This is derived using recurrence relations and boundary conditions \\( P_0 = 0 \\), \\( P_N = 1 \\).

---

## Summary

| Case                     | Probability of reaching \\( N \\) |
|--------------------------|-------------------------------|
| Fair game (\\( p = \frac{1}{2} \\))  | \\( \frac{i}{N} \\) |
| Biased game (\\( p \ne \frac{1}{2} \\)) | \\( \frac{1 - (q/p)^i}{1 - (q/p)^N} \\) |

---

## Reference

* [1] [Wikipedia: Gambler's ruin](https://en.wikipedia.org/wiki/Gambler%27s_ruin)