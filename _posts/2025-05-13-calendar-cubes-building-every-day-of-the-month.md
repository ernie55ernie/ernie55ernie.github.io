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

## Step 1: What Digits Are Needed?

We need to display every number from **01 to 31**. So, we need to form:

- 01 to 09 (leading zero)
- 10 to 31

The digits required across all combinations:  
**0, 1, 2, 3, 4, 5, 6, 7, 8, 9**

So, both cubes must between them represent **all 10 digits**, possibly duplicating some.

## Step 2: Important Observations

- To display **01–09**, cube one must show **0**, and cube two the digits **1 through 9**.
- To display **11, 22**, etc., some digits must be present on **both cubes**.
- Crucially, to display **6 and 9**, we can take advantage of a standard puzzle trick:  
  **Allow the digit 6 to double as 9**, by turning the cube upside down (or vice versa).

## Step 3: Minimum Digits, Maximum Coverage

We want to distribute the digits among the cubes such that all combinations for 01–31 are possible. Here's a **known valid solution**:

- **Cube 1**: 0, 1, 2, 3, 4, 5  
- **Cube 2**: 0, 1, 2, 6, 7, 8  
  (Using **6 as 9** when needed)

### Why This Works

- 0 is present on both (needed for 01–09).
- Cube 1 has digits up to 5; Cube 2 includes 6, 7, 8.
- To form 09 → 0 (cube 1) + 6 (cube 2, interpreted as 9)
- For 29 → 2 (cube 1) + 6 (cube 2 as 9)
- For 19 → 1 + 6 (as 9)
- All necessary combinations are covered.

## Final Answer

**Cube 1**: 0, 1, 2, 3, 4, 5  
**Cube 2**: 0, 1, 2, 6, 7, 8  
(*Treat 6 as 9 when needed*)

# Reference

* [1] [Facebook Interview Puzzle || Two Cubes Calendar || Logic Questions Asked At Facebook Interviews](https://www.youtube.com/watch?v=NoLAPLIiNIU)
