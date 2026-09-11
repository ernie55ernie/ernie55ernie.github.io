---
layout: post
title: "Chess Tournament Puzzle: When Do the Top Two Meet?"
date: 2025-05-18
category: quantitative interview
---

A knockout tournament poses a surprising question about randomness and ranking:

> There are \\(2^n\\) players labeled \\(1, 2, \ldots, 2^n\\), ordered by **strictly decreasing skill**.  
> The best player is **#1**, second-best is **#2**, etc.  
> The tournament is **single elimination**, and the initial bracket is **randomly seeded**.  
> **Better player always wins**.
>
> **Question:** What is the probability that **players 1 and 2** will meet **only in the final**, not in any earlier round?

---

## Step 1: Understand the Structure

- The tournament has \\(n\\) rounds.
- Player 1 **never loses**, meaning they will always make it to the final.
- Player 2 loses **only** to Player 1.
- If they meet *before* the final, Player 2 gets eliminated early.
- To meet in the **final**, they must be placed in **opposite halves** of the initial bracket.

---

## Step 2: Use Symmetry for Bracket Placement

Instead of simulating matches round by round, let's look at the initial random assignment of players to the \\(2^n\\) bracket spots.

Place **Player 1** in any spot on the bracket. 

There are now:
\\[
2^n - 1 \text{ remaining spots}
\\]
for **Player 2** to be placed into.

---

## Step 3: Calculate Favorable Spots

To avoid meeting Player 1 before the final, Player 2 must be placed in the **opposite half** of the bracket.

How many spots are in the opposite half? Exactly half of the total initial spots:
\\[
\text{Opposite half spots} = \frac{2^n}{2} = 2^{n-1}
\\]

Since Player 2 is equally likely to be placed in any of the remaining \\(2^n - 1\\) spots, the probability they land in one of the \\(2^{n-1}\\) safe spots is simply the ratio of favorable spots to total remaining spots.

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