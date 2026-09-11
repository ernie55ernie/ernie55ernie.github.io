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

<iframe src="{{ site.baseurl }}/assets/two_gamblers_unequal_numbers_of_coins.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

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

## Step 4: The Symmetry Argument

Consider the first \\(n\\) coins flipped by both A and B. Let \\(H_A(n)\\) be A's heads in these first \\(n\\) flips, and \\(H_B\\) be B's heads. There are three mutually exclusive scenarios:

1. **\\(H_A(n) > H_B\\):** A already has strictly more heads. A has won, regardless of what happens on the extra \\((n+1)\\)-th flip.
2. **\\(H_A(n) < H_B\\):** A has fewer heads. Even if A flips a head on the extra flip, A can at best tie. A has lost.
3. **\\(H_A(n) = H_B\\):** They are tied. A's extra flip now acts as the tiebreaker!

Because A and B flip the exact same number of coins in this first phase, scenarios 1 and 2 are **perfectly symmetric**. This means \\(P(H_A(n) > H_B) = P(H_A(n) < H_B)\\).

Let \\(p_{tie}\\) be the probability they tie. Then the probability A wins outright in the first phase is exactly half of the non-tie probability: \\(\frac{1 - p_{tie}}{2}\\).

If they tie, A wins if their final extra coin lands heads (which happens half the time): \\(\frac{p_{tie}}{2}\\).

Adding A's winning probabilities together yields the exact answer:
\\[
P(\text{A wins}) = \frac{1 - p_{tie}}{2} + \frac{p_{tie}}{2} = \frac{1}{2} - \frac{p_{tie}}{2} + \frac{p_{tie}}{2} = \frac{1}{2}
\\]

---

## Final Answer

> The probability that Gambler A ends up with **strictly more heads** than Gambler B is:
>
> \\[
> \boxed{\frac{1}{2}}
> \\]

# Reference

* [1] [The Asymmetric Coin Toss Problem](https://medium.com/@rishidarkdevil/an-asymmetric-coin-toss-problem-fc3835631af8)
