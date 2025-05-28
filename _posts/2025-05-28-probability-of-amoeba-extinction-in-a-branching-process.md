---
layout: post
title: "Probability of Amoeba Extinction in a Branching Process"
date: 2025-05-28
category: quantitative interview
---

## Problem Setup

You start with **1 amoeba**. Each minute, an amoeba independently:

- Dies with probability \\( \frac{1}{4} \\)
- Does nothing (\\( \to \\) 1 amoeba) with probability \\( \frac{1}{4} \\)
- Splits into 2 amoebas with probability \\( \frac{1}{4} \\)
- Splits into 3 amoebas with probability \\( \frac{1}{4} \\)

Each new amoeba behaves identically and independently.

What is the probability that **the entire population eventually dies out**?

---

## Step 1: Model as a Galton–Watson Process

Let \\( X \\) be the number of children an amoeba produces (including 0 if it dies). The **offspring distribution** is:

\\[
P(X = 0) = \frac{1}{4},\quad
P(X = 1) = \frac{1}{4},\quad
P(X = 2) = \frac{1}{4},\quad
P(X = 3) = \frac{1}{4}
\\]

---

### Step 2: Compute the Expected Number of Offspring

\\[
\mathbb{E}[X] = 0 \cdot \frac{1}{4} + 1 \cdot \frac{1}{4} + 2 \cdot \frac{1}{4} + 3 \cdot \frac{1}{4}
= \frac{0 + 1 + 2 + 3}{4} = \frac{6}{4} = \boxed{1.5}
\\]

Since the expected number of offspring is **greater than 1**, **extinction is not guaranteed**, but **it is possible**.

---

### Step 3: Use the Extinction Probability Equation

Let \\( q \\) be the probability of eventual extinction. For Galton–Watson processes, \\( q \\) is the **smallest fixed point** in \\( [0,1] \\) of the generating function:

\\[
f(s) = \mathbb{E}[s^X] = \frac{1}{4}(s^0 + s^1 + s^2 + s^3) = \frac{1}{4}(1 + s + s^2 + s^3)
\\]

We solve:

\\[
q = f(q) = \frac{1 + q + q^2 + q^3}{4}
\\]

Multiply both sides:

\\[
4q = 1 + q + q^2 + q^3 \Rightarrow q^3 + q^2 - 3q + 1 = 0
\\]

---

### Step 4: Solve the Cubic Equation

\\[
q^3 + q^2 - 3q + 1 = 0
\\]

Check rational roots (Rational Root Theorem): try \\( q = 1 \\):

\\[
1 + 1 - 3 + 1 = 0 \Rightarrow \boxed{q = 1} \text{ is a root.}
\\]

Factor:

\\[
(q - 1)(q^2 + 2q - 1) = 0
\\]

Solve the quadratic:

\\[
q = \frac{-2 \pm \sqrt{4 + 4}}{2} = \frac{-2 \pm \sqrt{8}}{2} = \frac{-2 \pm 2\sqrt{2}}{2} = -1 \pm \sqrt{2}
\\]

Only root in \\( [0,1] \\) besides 1 is:

\\[
q = -1 + \sqrt{2} \approx 0.4142
\\]

---

## Final Answer

\\[
\boxed{
\text{The probability that the amoebas eventually die out is } \boxed{-1 + \sqrt{2}} \approx \boxed{0.4142}
}
\\]

# Reference

* [1] [ML Interview Q Series: Amoeba Extinction Probability: A Branching Process Fixed-Point Solution](https://www.rohan-paul.com/p/ml-interview-q-series-amoeba-extinction)