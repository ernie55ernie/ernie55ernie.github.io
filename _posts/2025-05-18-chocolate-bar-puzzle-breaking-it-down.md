---
layout: post
title: "Chocolate Bar Puzzle: Breaking It Down"
date: 2025-05-18
category: quantitative interview
---

You’re handed a sweet but tricky problem:

> A chocolate bar is made of **6 rows** and **8 columns** of small \\(1 \times 1\\) squares — that’s **48 total pieces**.  
> You want to split it into all individual squares.
>
> Each break splits **one piece** (which may be a rectangle) into **two smaller rectangles** along grid lines.
>
> **Question:** How many total breaks are required?

---

## Step 1: Understand the Process

Each break increases the number of pieces by **1**.

- Start: 1 large bar
- End: 48 individual pieces

So, every time you break one piece into two, the total number of pieces increases by 1.

---

## Step 2: Apply the Principle

To go from **1 piece → 48 pieces**, you need:

\\[
48 - 1 = 47 \text{ breaks}
\\]

This logic is **independent** of how you make the breaks—whether you go row by row, column by column, or randomly.

Each break contributes **exactly one new piece**.

---

## Final Answer

> **47 breaks** are always required to split a chocolate bar into 48 individual squares—no matter the strategy.

# Reference

* [1] [Brain Teaser 33: Chocolate Bar](https://medium.com/@shelvia1039/brain-teaser-32-chocolate-bar-79853194b0e4)