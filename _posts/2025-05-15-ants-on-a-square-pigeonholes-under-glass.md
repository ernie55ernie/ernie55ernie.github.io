---
layout: post
title: "Ants on a Square: Pigeonholes Under Glass"
date: 2025-05-15
category: quantitative interview
---

You're given a deceptively simple geometry-meets-pigeonhole puzzle:

> **There are 51 ants** scattered anywhere on a **unit square**.  
> You’re given a **glass disk of radius \\( \frac{1}{7} \\)**.  
> **Prove**: No matter how the ants are placed, you can always position the glass to cover **at least 3 ants**.

---

## Step 1: Divide and Conquer

The key is to break the unit square into manageable **smaller regions**.

Divide the square into a **5×5 grid** of equal squares:

- Each small square has side length \\( \frac{1}{5} = 0.2 \\)
- There are **25 sub-squares** total.

This spatial partition gives us the perfect framework to apply the **pigeonhole principle**.

---

## Step 2: Apply the Pigeonhole Principle

We have **51 ants** placed anywhere in the square.

With only **25 sub-squares**, some squares must contain **multiple ants**.

In fact:

- If each of the 25 squares held at most 2 ants, that would total only \\( 25 × 2 = 50 \\) ants.
- But we have **51 ants** → at least one square must contain **3 or more ants**.

So, **at least one** of the 25 sub-squares contains **at least 3 ants**.

---

## Step 3: Fit the Glass

Now we must show that a circle of radius \\( \frac{1}{7} \\) is large enough to cover any three ants within such a small square.

### Key Fact:

- The **diagonal** of each small square is:
  \\[
  \sqrt{(0.2)^2 + (0.2)^2} = \sqrt{0.08} ≈ 0.2828
  \\]

So, the **maximum distance** between any two ants inside the same small square is less than 0.283.

A circle of radius \\( \frac{1}{7} ≈ 0.143 \\) has a **diameter of \\( \frac{2}{7} ≈ 0.2857 \\)**.

Thus, a circle of diameter 2/7 can **cover the entire sub-square**.

So: **any three ants** within that square can all fit under the glass.

---

## Final Answer

> Divide the square into 25 equal parts.  
> By the pigeonhole principle, one part must contain **at least 3 ants**.  
> That part fits inside a circle of radius \\( \frac{1}{7} \\), so the glass can cover them.

# Reference

* [1] [Pigeonhole principle in geometric task](https://math.stackexchange.com/questions/2198633/pigeonhole-principle-in-geometric-task)
