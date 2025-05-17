---
layout: post
title: "Clock Pieces Puzzle: Equal Arcs Around the Dial"
date: 2025-05-15
category: quantitative interview
---

A seemingly broken clock presents a tidy little number theory challenge:

> A circular clock face (with numbers **1 through 12** in the usual order) breaks into **three contiguous arcs**—each with one or more adjacent numbers.  
> You find that the **sum of the numbers on each piece is equal**.

---

## Step 1: Total Sum of the Clock

The numbers on the clock are:

\\[
1 + 2 + \cdots + 12 = \frac{12 × 13}{2} = 78
\\]

So, if the clock breaks into **three pieces** with equal sums, each piece must sum to:

\\[
\frac{78}{3} = 26
\\]

---

## Step 2: Try Contiguous Groups Summing to 26

We’re looking for **three contiguous arcs** (sequential numbers on the clock) that each sum to 26. Since the clock is circular, we can start anywhere.

After trial and logic, one solution is:

- **Piece 1**: 12 + 1 + 2 + 11 = **26**
- **Piece 2**: 3 + 10 + 4 + 9 = **26**
- **Piece 3**: 5 + 8 + 6 + 7 = **26**

All are contiguous when placed around the clock face:

- **Arc 1**: 12 → 1 → 2 → 11  
- **Arc 2**: 3 → 10 → 4 → 9  
- **Arc 3**: 5 → 8 → 6 → 7

Each segment adds up to 26 and wraps around the circle neatly.

---

## Final Answer

**The three clock face pieces are:**

- **[12, 1, 2, 11]**
- **[3, 10, 4, 9]**
- **[5, 8, 6, 7]**

Each arc is contiguous and sums to **26**.

# Reference

* [1] [Brain Teaser 20: Clock Pieces](https://medium.com/@shelvia1039/brain-teaser-20-clock-pieces-60ac58e047d3)
