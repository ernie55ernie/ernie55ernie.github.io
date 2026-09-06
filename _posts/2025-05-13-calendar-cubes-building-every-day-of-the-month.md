---
layout: post
title: "Calendar Cubes: Building Every Day of the Month"
date: 2025-05-13
category: quantitative interview
---

You're given a delightful constraint puzzle:

> You have two six-sided cubes. You can assign **one digit per face**, using digits 0–9.  
> Your task is to arrange digits on the cubes such that **every day of the month** from **01 to 31** can be displayed.  
> Importantly, for dates 01–09, a **leading zero is required**.

Digits can appear on both cubes, and the two cubes are placed **side by side** (in either order) to form each two-digit number.

<iframe src="{{ site.baseurl }}/assets/two_cubes_calendar_puzzle.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

## Step 1: What Digits Are Needed?

We need to display every number from **01 to 31**. So, we need to form:

- 01 to 09 (leading zero)
- 10 to 31

The digits required across all combinations:  
**0, 1, 2, 3, 4, 5, 6, 7, 8, 9**

So, both cubes must between them represent **all 10 digits**, possibly duplicating some.

## Step 2: Logical Deduction

Let's figure out what must go on the cubes by pure deduction:

1. **The Double Digits:** To display **11** and **22**, the digits **1** and **2** must be present on **both cubes**. (We don't need 33 for a month calendar).
2. **The Zero:** To display dates **01 through 09**, a **0** must be paired with all 9 digits (1-9). Since a single cube only has 6 faces, it cannot hold all 9 digits to pair with a single 0. Therefore, the digit **0 must also be on both cubes** to split the load.

At this point, we've used 3 faces on both cubes:
- **Cube 1:** 0, 1, 2, _, _, _
- **Cube 2:** 0, 1, 2, _, _, _

## Step 3: The Missing Digits and The Trick

We have exactly **6 empty faces** left across both cubes. 
The digits we still need to place are: **3, 4, 5, 6, 7, 8, 9** (7 digits).

This looks impossible since we need 7 digits but only have 6 faces! 

This is where the classic puzzle trick comes in: **allow the digit 6 to double as 9** by turning the cube upside down.

This reduces the remaining required digits to exactly 6: **3, 4, 5, 6, 7, 8**.

We can distribute these 6 digits evenly across the 6 remaining empty faces. For example:
- Place 3, 4, 5 on Cube 1
- Place 6, 7, 8 on Cube 2

## Final Answer

**Cube 1**: 0, 1, 2, 3, 4, 5  
**Cube 2**: 0, 1, 2, 6, 7, 8  
(*Treat 6 as 9 when needed*)

# Reference

* [1] [Facebook Interview Puzzle \|\| Two Cubes Calendar \|\| Logic Questions Asked At Facebook Interviews](https://www.youtube.com/watch?v=NoLAPLIiNIU)
