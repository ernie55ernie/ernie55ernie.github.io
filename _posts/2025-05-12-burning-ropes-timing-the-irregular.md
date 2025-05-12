---
layout: post
title: "Burning Ropes: Timing the Irregular"
date: 2025-05-12
category: quantitative interview
---

## Burning Ropes: Timing the Irregular

This classic logic puzzle challenges you to measure **exactly 45 minutes** using just:

- **2 ropes**, each taking exactly **1 hour** to burn end-to-end,
- A **lighter**, and
- The knowledge that the ropes burn **non-linearly** (i.e., not at a consistent rate).

### Constraints

- You **cannot** fold or cut the ropes.
- You **cannot** assume uniform burning.
- But you **can** light either or both ends of either rope at any time.

## The Strategy

Here’s the clever trick: leverage the **doubling of burn rate** when lighting both ends.

### Step-by-Step Solution

1. **Light Rope A at both ends** and **Rope B at one end** **simultaneously**.

   - Rope A will burn twice as fast and take exactly **30 minutes** to be consumed.

2. **As soon as Rope A finishes burning (after 30 minutes)**, immediately **light the other end of Rope B**.

   - At this point, Rope B has burned for 30 minutes from one end, so **half remains**—but again, due to irregular burn rate, we don't know where the flame is.
   - Lighting the other end now causes it to burn from **both ends**, which doubles the burn rate of the remaining segment.

3. The remaining rope will now take **15 minutes** to finish burning.

   - 30 minutes + 15 minutes = **45 minutes** in total.

## Why It Works

Even though the burn rate is inconsistent, **lighting both ends guarantees a known time**: the rope burns completely in half the original time regardless of rate variability. That’s the core trick.

## Final Answer

**Light Rope A at both ends and Rope B at one end. When Rope A finishes (30 min), light the other end of Rope B. When Rope B finishes, 45 minutes have passed.**

# Reference

* [1] [Burning Rope Puzzle](https://en.wikipedia.org/wiki/Rope-burning_puzzle)
