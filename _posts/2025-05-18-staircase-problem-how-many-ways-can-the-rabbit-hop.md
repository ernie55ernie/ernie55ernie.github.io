---
layout: post
title: "Staircase Problem: How Many Ways Can the Rabbit Hop?"
date: 2025-05-18
category: quantitative interview
---

## Staircase Problem: How Many Ways Can the Rabbit Hop?

This classic combinatorics puzzle is also known as the "hopping rabbit" problem:

> A rabbit is at the bottom of a staircase with \\(n\\) steps.  
> Each move, it can hop up **either 1 or 2 steps**.  
> **How many distinct ways** can the rabbit reach the top?

---

## Step 1: Build a Recurrence

Let \\(F(n)\\) be the number of ways to reach the top of an \\(n\\)-step staircase.

To reach step \\(n\\), the rabbit must have come from:
- Step \\(n - 1\\) via a **1-step hop**, or
- Step \\(n - 2\\) via a **2-step hop**

So:

\\[
F(n) = F(n-1) + F(n-2)
\\]

This is the famous **Fibonacci recurrence**.

---

## Step 2: Base Cases

We need starting values:

- \\(F(0) = 1\\) (one way to be at the bottom with no moves)
- \\(F(1) = 1\\) (one 1-step move)

Then:

- \\(F(2) = F(1) + F(0) = 1 + 1 = 2\\)
- \\(F(3) = F(2) + F(1) = 2 + 1 = 3\\)
- \\(F(4) = F(3) + F(2) = 3 + 2 = 5\\)
- and so on…

---

## Step 3: Final Formula

The number of ways to climb an \\(n\\)-step staircase using 1- or 2-step hops is:

\\[
F(n) = \text{the }(n+1)\text{-th Fibonacci number}
\\]

(Counting starts from \\(F(0) = 1\\), \\(F(1) = 1\\))

---

## Final Answer

> The number of ways to hop up an \\(n\\)-step staircase (1 or 2 steps at a time) is:
>
> \\[
> \boxed{F(n) = F(n-1) + F(n-2)} \quad \text{with } F(0) = 1,\ F(1) = 1
> \\]

# Reference

* [1] [Fibonacci and Staircase Problem](https://en.wikipedia.org/wiki/Fibonacci_number#Applications)
