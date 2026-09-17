---
layout: post
title: "First-Ace Puzzle: Expected Stopping Time in a Deck"
date: 2025-05-20
category: quantitative interview
---

### The Setup

You have a **standard 52-card deck** with 4 aces. You shuffle the deck thoroughly and then **turn over cards one at a time**, stopping when you reveal the **first ace**.

### Question:

What is the **expected number of cards** you will turn over to see that first ace?

---

## Key Insight

The 4 aces are **randomly distributed** among the 52 positions in the deck. We're interested in the **expected position of the first ace**.

---

## Linearity of Expectation

Let \\( A_1, A_2, A_3, A_4 \\) be the positions of the 4 aces in the shuffled deck.

The expected position of the **first ace** is the **minimum** of these 4 random variables.

For \\( n \\) cards and \\( k \\) randomly placed distinguished items, the expected position of the **first** distinguished item is:

\\[
E[\text{min}] = \frac{n + 1}{k + 1}
\\]

For our case:

\\[
n = 52,\quad k = 4
\Rightarrow E[\text{first ace}] = \frac{52 + 1}{4 + 1} = \boxed{\frac{53}{5} = 10.6}
\\]

---

## Final Answer

\\[
\boxed{10.6}
\\]

So, on average, you will turn over **10.6 cards** before encountering the first ace.

---

## Reference

* [1] [Expected number of cards you should turn before finding an ace](https://math.stackexchange.com/questions/1138853/expected-number-of-cards-you-should-turn-before-finding-an-ace)