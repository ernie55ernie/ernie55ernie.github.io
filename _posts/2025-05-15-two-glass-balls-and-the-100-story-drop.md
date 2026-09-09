---
layout: post
title: "Two Glass Balls and the 100-Story Drop"
date: 2025-05-15
category: quantitative interview
---

You're given a famous optimization challenge:

> A 100-story building, and **two identical glass balls**.  
> There exists a **threshold floor \\(X\\)** such that:
> - Balls **won’t break** if dropped from below \\(X\\),
> - Balls **will break** if dropped from \\(X\\) or higher.
>
> Your goal: Find **\\(X\\)** using the **fewest drops** possible in the **worst case**.

<iframe src="{{ site.baseurl }}/assets/two_glass_balls_100_floors.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

---

## Constraints

- You get **two balls**.
- If a ball breaks, it's **gone**.
- You want to **minimize the maximum number of drops** needed to determine \\(X\\).

---

## Naive Strategies

### Linear Search:
Drop the first ball starting from floor 1, 2, 3, ..., until it breaks.
- Worst case: 100 drops (if \\(X = 100\\))

### Binary Search:
Drop from floor 50, then 25/75, etc.
- Problem: If the **first ball breaks**, you have only one left—so you can’t binary search anymore.
- Binary search assumes **multiple balls**, not just two.

---

## Optimal Strategy: Minimize Worst Case

The idea is to **balance risk** between balls:

> Drop the first ball at **increasing floors**, with the step size between drops reducing by 1 each time.

### Why?

You want the sum of drops to cover all 100 floors:
\\[
n + (n-1) + (n-2) + \cdots + 1 = \frac{n(n+1)}{2} \geq 100
\\]

Solving:
\\[
\frac{n(n+1)}{2} \geq 100 \Rightarrow n = 14
\\]

### Step-by-Step Plan

1. Drop first ball from floor **14**  
2. If it doesn’t break, go to floor **27** (14 + 13)  
3. Then **39** (14 + 13 + 12), and so on…

Sequence of drops:  
14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99, 100...

Each step reduces the interval by 1, so in **worst-case**, you’ll need **14 drops max**.

### What If First Ball Breaks?

Suppose it breaks at floor 60 (after 5 drops).

Since it survived floor 50, you now know \\(X\\) is between **51 and 60**.

Use the **second ball** to test linearly from 51, 52, ..., up to 59 → max 9 additional drops. *(If it survives 59, you automatically know \\(X = 60\\) without needing to drop again).*

Total: 5 + 9 = 14

---

## Final Answer

> **Minimum number of drops needed in the worst case is 14**  
> Drop first ball at floors: 14, 27, 39, ..., decreasing the step size by 1 each time.  
> When it breaks, use second ball to search linearly below.

# Reference

* [1] [Egg Dropping Puzzle \| DP-11](https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/)
