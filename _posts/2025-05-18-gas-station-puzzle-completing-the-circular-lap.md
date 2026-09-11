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

<iframe src="{{ site.baseurl }}/assets/gas_station_circle_visualization.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

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

## Step 2: The Cumulative Deficit Insight

Imagine starting at Station 1 and driving the full lap, **allowing your fuel tank to drop below zero**. 
Compute the running cumulative fuel balance (the sum of \\(\Delta_i\\)) as you arrive at each station.

- Because the total gas equals the total cost, your balance at the very end of the lap will be exactly **0**.
- During the lap, your balance will fluctuate. There must be at least **one place** where this running balance hits its **absolute lowest point** (the maximum deficit).

If you shift your starting point to be **immediately after** that lowest point, you effectively "reset" the lowest point to 0. Since no other point was lower, your running balance will **never drop below zero** for the rest of the lap!

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
