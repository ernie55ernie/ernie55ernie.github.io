---
layout: post
title: "Aces in a Bridge Deal: Equal Distribution"
date: 2025-05-19
category: quantitative interview
---

### The Puzzle

You deal a **standard 52-card deck** evenly to **four players** (13 cards each).

**Question:** What is the probability that **each player gets exactly one Ace**?

---

## Total Number of Deals

The total number of ways to deal the entire deck to 4 players with 13 cards each is:

\\[
\binom{52}{13,13,13,13} = \frac{52!}{(13!)^4}
\\]

This is the size of the sample space.

---

## Favorable Outcomes

We want each player to get exactly **one Ace**.

### Step 1: Distribute the 4 Aces

There are:

\\[
4! = 24
\\]

ways to assign one Ace to each of the 4 players.

### Step 2: Distribute the Remaining 48 Cards

We now deal the remaining 48 cards such that each player receives 12 more cards (to make 13 total). The number of such distributions is:

\\[
\binom{48}{12,12,12,12} = \frac{48!}{(12!)^4}
\\]

---

## Final Probability

Combining both steps, the probability is:

\\[
\frac{4! \cdot \frac{48!}{(12!)^4}}{\frac{52!}{(13!)^4}} = \frac{24 \cdot 48! \cdot (13!)^4}{52! \cdot (12!)^4}
\\]

This simplifies numerically to:

\\[
\boxed{\frac{778169210}{12493275315}} \approx \boxed{0.0626}
\\]

So, there's about a **6.26%** chance that each player in a Bridge deal ends up with exactly one Ace.

---

## Reference

* [1] [Probability of deck of cards such that each person receives one ace](https://math.stackexchange.com/questions/2521017/probability-of-deck-of-cards-such-that-each-person-receives-one-ace)