---
layout: post
title: "Chess Tournament Puzzle: When Do the Top Two Meet?"
date: 2025-05-18
category: quantitative interview
---

## Chess Tournament Puzzle: When Do the Top Two Meet?

A knockout tournament poses a surprising question about randomness and ranking:

> There are \\(2^n\\) players labeled \\(1, 2, \ldots, 2^n\\), ordered by **strictly decreasing skill**.  
> The best player is **#1**, second-best is **#2**, etc.  
> The tournament is **single elimination**, and pairings are **random in each round**.  
> **Better player always wins**.
>
> **Question:** What is the probability that **players 1 and 2** will meet **only in the final**, not in any earlier round?

---

## Step 1: Understand the Structure

- The tournament has \\(n\\) rounds (since \\(2^n\\) players are halved each time).
- Player 1 **never loses**.
- Player 2 loses **only** to Player 1.
- To meet in the **final**, they must be in **opposite halves** of the bracket throughout.

Each round’s pairings are randomized, so it’s not a fixed bracket.

---

## Step 2: Key Insight

Think recursively: as long as players 1 and 2 avoid each other in every round until the final, they survive.

So the question becomes:

> What’s the chance that 1 and 2 **don’t get paired together** in any round **before** the final?

---

## Step 3: Derive the Formula

The total number of distinct matchups in a \\(2^n\\) tournament tree is:

\\[
2^n - 1
\\]

Why? Because each match eliminates one player, and there are \\(2^n - 1\\) eliminations total.

Now consider: out of all these matches, in **exactly one** of them will players 1 and 2 meet—assuming they both survive to that point.

If they meet **in the final**, that match must be the **last one** (the \\(2^n - 1\\)-th match).

So: The number of total match trees where 1 and 2 meet **only in the final** is:

\\[
\text{Favorable cases} = 2^{n-1}
\\]

(Why? Because in a random binary tree with \\(2^n\\) leaves, the number of ways to position two specific players in **opposite halves** is \\(2^{n-1}\\)).

Hence:

\\[
P(\text{1 vs 2 only in final}) = \frac{2^{n - 1}}{2^n - 1}
\\]

---

## Final Answer

> The probability that players 1 and 2 meet **only in the final** is:
>
> \\[
> \boxed{\frac{2^{n - 1}}{2^n - 1}}
> \\]

# Reference

* [1] [Cannot Make Sense of Chess Tournament Solution](https://math.stackexchange.com/questions/3492258/cannot-make-sense-of-chess-tournament-solution)