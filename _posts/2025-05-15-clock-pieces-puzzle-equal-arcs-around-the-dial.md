---
layout: post
title: "Clock Pieces Puzzle: Equal Arcs Around the Dial"
date: 2025-05-15
category: quantitative interview
---

A classic clock puzzle presents a tidy little number theory challenge:

> By drawing **two straight lines** across a circular clock face, divide the numbers into **three pieces** such that the **sum of the numbers on each piece is equal**.

<iframe src="{{ site.baseurl }}/assets/clock_pieces_interactive.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

---

## Step 1: Total Sum of the Clock

The numbers on the clock are:

\\[
1 + 2 + \cdots + 12 = \frac{12 \times 13}{2} = 78
\\]

So, if the clock breaks into **three pieces** with equal sums, each piece must sum to:

\\[
\frac{78}{3} = 26
\\]

---

## Step 2: Slice the Clock

We need to slice the clock so the numbers in each region sum to 26. Let's look for contiguous sequences around the edge that naturally add up to 26:

- **Top sequence**: 11 + 12 + 1 + 2 = **26**
- **Bottom sequence**: 5 + 6 + 7 + 8 = **26**

If we draw **two parallel straight lines** across the clock face to slice off these two sequences, we create three distinct pieces:

- **Piece 1 (Top)**: A line drawn between 10 & 11 and 2 & 3. Contains `[11, 12, 1, 2]`.
- **Piece 2 (Bottom)**: A line drawn between 8 & 9 and 4 & 5. Contains `[5, 6, 7, 8]`.
- **Piece 3 (Middle)**: The remaining numbers wedged between the two lines. Contains `[9, 10]` on the left and `[3, 4]` on the right. 

Let's verify the middle piece: `9 + 10 + 3 + 4 = 26`. It works perfectly!

---

## Final Answer

**Draw two parallel lines across the clock to form these three pieces:**

- **Top Piece**: `[11, 12, 1, 2]`
- **Middle Piece**: `[9, 10]` and `[3, 4]`
- **Bottom Piece**: `[5, 6, 7, 8]`

Each region neatly sums to **26**.

# Reference

* [1] [Brain Teaser 20: Clock Pieces](https://medium.com/@shelvia1039/brain-teaser-20-clock-pieces-60ac58e047d3)
