---
layout: post
title: "Galton–Watson Branching Process: Will the Amoebas Die Out?"
date: 2025-05-19
category: quantitative interview
---

This classic problem in probability theory explores extinction in a **branching process**.

---

### The Setup

You begin with **one amoeba**. At each time step, **each amoeba** independently produces offspring based on the following rules:

- 25% chance to **die** (0 offspring)
- 25% chance to produce **1 offspring**
- 25% chance to produce **2 offspring**
- 25% chance to produce **3 offspring**

All offspring behave identically in subsequent steps.

### Question:

**What is the probability that the population eventually goes extinct?**

---

## Step 1: Expected Offspring

Let \\( X \\) be the number of offspring from a single amoeba. Then:

\\[
\mathbb{E}[X] = \frac{1}{4}(0 + 1 + 2 + 3) = \frac{6}{4} = 1.5
\\]

Since the expected number of offspring is **greater than 1**, there’s a **positive probability of survival**.

---

## Step 2: Finding Extinction Probability

Let \\( q \\) be the extinction probability. For a Galton–Watson process, \\( q \\) satisfies the fixed-point equation:

\\[
q = f(q)
\\]

where \\( f(s) \\) is the generating function of the offspring distribution:

\\[
f(s) = \frac{1}{4}(s^0 + s^1 + s^2 + s^3) = \frac{1}{4}(1 + s + s^2 + s^3)
\\]

So we solve:

\\[
q = \frac{1}{4}(1 + q + q^2 + q^3)
\\]

Multiply both sides by 4:

\\[
4q = 1 + q + q^2 + q^3
\\]

Rearranged:

\\[
q^3 + q^2 - 3q + 1 = 0
\\]

We find the **smallest root in [0,1]**, which gives the extinction probability.

This cubic factors as:

\\[
(q - 1)(q^2 + 2q - 1) = 0
\\]

Solving \\( q^2 + 2q - 1 = 0 \\):

\\[
q = -1 \pm \sqrt{2}
\\]

Only the solution \\( q = \sqrt{2} - 1 \approx 0.4142 \\) lies in \\([0,1]\\).

---

## Final Answer

The probability that the amoeba population eventually **dies out** is:

\\[
\boxed{\sqrt{2} - 1}
\\]

## Reference

* [1] [Galton–Watson process](https://en.wikipedia.org/wiki/Galton%E2%80%93Watson_process)
