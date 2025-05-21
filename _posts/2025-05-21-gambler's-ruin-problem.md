---
layout: post
title: "Biased Gambler’s Ruin: Unequal Initial Fortunes"
date: 2025-05-21
category: quantitative interview
---

### The Setup

Two players, **M** and **N**, play a series of games:

- M starts with \\( \$1 \\)
- N starts with \\( \$2 \\)
- Total capital is \\( \$3 \\)

At each step:

- M **wins \$1** with probability \\( p = \frac{2}{3} \\)
- M **loses \$1** with probability \\( q = \frac{1}{3} \\)

The game continues until one player is ruined.

### Question:

What is the probability that **M** wins (i.e., reaches \\( \$3 \\)) before being ruined?

---

## The Gambler’s Ruin Formula

Let \\( P(i) \\) be the probability that M wins, starting with \\( i \\) dollars out of \\( N = 3 \\).

For a biased game \\( (p \ne q) \\), the probability of reaching \\( N \\) before 0 is:

\\[
P(i) = \frac{1 - (q/p)^i}{1 - (q/p)^N}
\\]

Given:

- \\( i = 1 \\)
- \\( N = 3 \\)
- \\( p = \frac{2}{3} \\), \\( q = \frac{1}{3} \\)
- \\( q/p = \frac{1/3}{2/3} = \frac{1}{2} \\)

### Plug In:

\\[
P(1) = \frac{1 - (1/2)^1}{1 - (1/2)^3} = \frac{1 - 1/2}{1 - 1/8} = \frac{1/2}{7/8} = \boxed{\frac{4}{7}}
\\]

---

## Final Answer

\\[
\boxed{\frac{4}{7}}
\\]

So, the probability that **M** wins the game is **4/7**.

---

## Reference

* [1] [Gambler's Ruin – Biased Walks](https://en.wikipedia.org/wiki/Gambler%27s_ruin)
