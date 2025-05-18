---
layout: post
title: "Gas Station Puzzle: Completing the Circular Lap"
date: 2025-05-18
category: quantitative interview
---

You’re given a deceptively simple setup:

> A **circular one-way track** with **N gas cans** placed along it.  
> - Each can provides a certain amount of gas.
> - The **total fuel** in all the cans is **exactly enough** for one full lap.
> - Your car starts with an **empty tank**.
>
> **Question:** Can you always find a starting point so you can complete the lap without running out of gas?  
> And if so, **how** can you find it?

---

## Step 1: Reframe as a Difference Array

As you drive from point to point:

- You **gain** fuel from each can
- You **spend** fuel to drive between cans

Let’s define:

- \\(g_i\\): amount of gas at station \\(i\\)
- \\(c_i\\): cost to drive from \\(i\\) to \\(i+1\\)
- Total gas: \\(G = \sum g_i = \sum c_i = C\\)

Let:
\\[
\Delta_i = g_i - c_i
\\]
You want to find an index \\(s\\) where starting the trip at \\(s\\) ensures your **running fuel balance** never dips below zero.

---

## Step 2: Cumulative Deficit Insight

Compute cumulative sum of \\(\Delta_i\\) as you go:

- If total sum \\(\sum \Delta_i = 0\\), then at least **one place** must be the **lowest point** in the cumulative sum curve.
- Starting **just after** that lowest point ensures that all cumulative fuel balances from that point onward stay **non-negative**.

This ensures you **never run out of fuel**—you always get the gas you need just in time.

---

## Step 3: Finding the Start

To find the index:

1. Track cumulative fuel balance as you simulate the loop.
2. Mark the position **where this balance is lowest**.
3. Start at the next position—this guarantees you’ll finish the loop.

This process takes **linear time \\(O(N)\\)**.

---

## Final Answer

> **Yes**, there is always a starting point where you can complete the lap without running out of gas.  
> **Start immediately after** the point where your cumulative fuel balance is **lowest**.

# Reference

* [1] [Brain Teaser 34: Race Track)](https://medium.com/@shelvia1039/brain-teaser-34-race-track-049fa28fbac4)
