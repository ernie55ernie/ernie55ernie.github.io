---
layout: post
title: "Coin Toss Game: Who Wins with One Extra Flip?"
date: 2025-05-18
category: quantitative interview
---

This puzzle is a classic twist on probability:

> Two gamblers, A and B, flip coins:
> - Gambler **A** flips **\\(n+1\\)** fair coins.
> - Gambler **B** flips **\\(n\\)** fair coins.
>
> What is the probability that **A ends up with strictly more heads than B**?

---

## Step 1: Understand the Setup

Let \\( H_A \\) and \\( H_B \\) be the number of heads obtained by A and B, respectively.

We're interested in computing:

\\[
P(H_A > H_B)
\\]

Given that all coin flips are independent and fair (i.e., probability of heads = 0.5), we want to find this probability exactly.

---

## Step 2: Symmetry Insight

Let’s define a fair framework.

Think of B flipping all their coins first. Then A flips their **\\(n\\)** coins **plus one extra**.

There is a deep symmetry hidden in this setup.

---

## Step 3: Core Result

A beautiful and perhaps surprising fact:

> The probability that **A gets strictly more heads than B** is **exactly 0.5**.

This is true **for all values of \\(n\\)**.

---

## Step 4: Intuitive Explanation

Here’s one way to see why:

- Let’s fix the outcomes of B’s \\(n\\) flips.
- A's first \\(n\\) flips can match that exactly—and the **extra coin** then acts as a tiebreaker.

When A and B tie on the first \\(n\\) flips:
- A wins **half the time** (when the extra coin is heads).
- So overall, A has **exactly a 50% chance** of ending up with more heads.

This matches formal derivations using summations and generating functions as well.

---

## Final Answer

> The probability that Gambler A ends up with **strictly more heads** than Gambler B is:
>
> \\[
> \boxed{\frac{1}{2}}
> \\]

# Reference

* [1] [The Asymmetric Coin Toss Problem](https://medium.com/@rishidarkdevil/an-asymmetric-coin-toss-problem-fc3835631af8)
