---
layout: post
title: "Two Missing Numbers: Finding What’s Gone"
date: 2025-05-15
category: quantitative interview
---

You’re given a list of **98 distinct integers**, all from the set \\(\{1, 2, 3, \ldots, 100\}\\).  
Exactly **two numbers are missing**.

> **Task:** Devise a **fast, reliable** method to identify the missing numbers.

---

## Step 1: Use Sum and Sum of Squares

Let the missing numbers be \\(x\\) and \\(y\\).  
Then we know:

- The sum of numbers from 1 to 100 is:
  \\[
  S = \frac{100 × 101}{2} = 5050
  \\]
- The sum of squares from 1 to 100 is:
  \\[
  Q = \frac{100 × 101 × 201}{6} = 338350
  \\]

Let:

- \\(S'\\) = sum of the 98 given numbers
- \\(Q'\\) = sum of the squares of the 98 given numbers

Then:
- \\(x + y = S - S'\\)
- \\(x^2 + y^2 = Q - Q'\\)

---

## Step 2: Solve the System

We now know:
- \\(x + y = a\\)
- \\(x^2 + y^2 = b\\)

Use identity:

\\[
(x + y)^2 = x^2 + y^2 + 2xy \Rightarrow
\\]
\\[
a^2 = b + 2xy \Rightarrow xy = \frac{a^2 - b}{2}
\\]

Now we know \\(x + y = a\\), \\(xy = c\\) — the standard symmetric sum/product of roots.

We can solve:

\\[
t^2 - at + c = 0
\\]

This quadratic gives the **two missing numbers**.

---

## Final Answer

> Let \\(a = 5050 - \text{sum of given 98 numbers}\\)  
> Let \\(b = 338350 - \text{sum of their squares}\\)  
> Then:  
> \\[
> xy = \frac{a^2 - b}{2}
> \\]  
> Solve \\(t^2 - at + xy = 0\\) to find the missing numbers \\(x\\) and \\(y\\)

# Reference

* [1] [Brain Teaser 21: Missing Integers](https://medium.com/@shelvia1039/brain-teaser-21-missing-integers-b11374b0bf14)
