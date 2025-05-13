---
layout: post
title: "The Last Ball Puzzle: An Invariant Insight"
date: 2025-05-13
category: quantitative interview
---

You're given a bag of balls:

- **20 blue**, **14 red**

You perform the following steps repeatedly:

1. Draw two balls at random.
2. If they are **the same color**, discard both and **add a blue** ball.
3. If they are **different colors**, discard both and **add a red** ball.

Repeat until **only one ball remains**.

> **Question:** What will be the color of the final ball?

---

## Key Idea: Look for an Invariant

An **invariant** is a quantity that doesn't change, no matter how the system evolves.

Let's analyze:

- Every step **removes two balls** and **adds one**, reducing total count by 1.
- So, after 33 steps (since 34 balls), only **1 ball remains**.

But what's consistent through each operation?

### Consider Red Ball Parity

Let’s track the **parity (even or odd)** of the number of **red balls**:

- Start: **14 red balls** → **even**

Now consider the operations:

- **Two reds → add blue** → red count decreases by 2 → parity **unchanged**
- **Two blues → add blue** → red count unchanged → parity **unchanged**
- **One red + one blue → add red** → red count decreases by 1 and increases by 1 → net 0 → parity **unchanged**

**In all cases, the parity of the number of red balls remains the same!**

This is the invariant.

### What Does It Mean?

If you start with an **even number** of red balls, you'll always have an even number.

Eventually, only **one ball remains**—so that ball must also respect the invariant.

- If only **one red** remains, that's **odd** → contradiction!
- So the last ball **cannot be red** if you started with **even red count**

#### Thus:

- **Start with 14 red (even)** → Final ball is **blue**
- **Start with 13 red (odd)** → Final ball is **red**

## Final Answers

- **20 blue, 14 red** → Final ball is **blue**
- **20 blue, 13 red** → Final ball is **red**

# Reference

* [1] [Algorithmic Puzzles - X-Files](https://doc.lagout.org/science/0_Computer%20Science/2_Algorithms/Algorithmic%20Puzzles%20%5BLevitin%20%26%20Levitin%202011-10-14%5D.pdf)
