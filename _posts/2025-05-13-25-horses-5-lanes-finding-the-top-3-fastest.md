---
layout: post
title: "25 Horses, 5 Lanes: Finding the Top 3 Fastest"
date: 2025-05-13
category: quantitative interview
---

This classic logic puzzle asks:

> With **25 horses** and a track that can race at most **5 at a time**, what is the **minimum number of races** required to identify the **top 3 fastest horses**, knowing only the **rank order** of each race?

### Constraints

- No stopwatch; only relative order matters.
- Each horse has a distinct but fixed speed.
- Goal: Identify **exactly** the top 3 fastest horses.
- Races are limited to **5 horses at a time**.

## Step-by-Step Strategy

### Step 1: Group and Race
Divide the 25 horses into **5 groups of 5**.  
Race each group once → **5 races**

Label horses by group and placement. Suppose the groups and results are:

- **Race A**: A1, A2, A3, A4, A5 (A1 fastest)
- **Race B**: B1, B2, B3, B4, B5
- **Race C**: C1, C2, C3, C4, C5
- **Race D**: D1, D2, D3, D4, D5
- **Race E**: E1, E2, E3, E4, E5

### Step 2: Race Winners
Now race the **winners** of each group: A1, B1, C1, D1, E1 → **1 race**

Let’s assume result is:
**Race F**: A1 > B1 > C1 > D1 > E1

This tells us:  
- **A1 is the fastest horse overall**
- **B1 and C1 are possible candidates for 2nd and 3rd**

So far: **6 races**

### Step 3: Eliminate Horses

From the race results, we can now eliminate many horses:

- Any horse from groups D and E is out (since D1 is at best 4th).
- From group C, **C1** can be at best 3rd (behind A1 and B1). Therefore, C2, C3, C4, and C5 are at best 4th and are eliminated.
- From group B, **B1** can be at best 2nd. **B2** can be at best 3rd. B3, B4, and B5 are eliminated.
- From group A, A1 is guaranteed 1st overall. **A2** can be at best 2nd, and **A3** can be at best 3rd. A4 and A5 are eliminated.

This leaves exactly **5 horses** competing for the 2nd and 3rd place spots:  
**A2, A3, B1, B2, C1**

Race these 5 horses → **7th race**

### Step 4: Final Determination

Take the **top 2 finishers** from this 7th race—those are the **2nd and 3rd fastest horses overall**, joining A1 on the podium.

## Final Answer

**Minimum number of races: 7**

- 5 initial group races
- 1 race of the group winners
- 1 final race among the refined candidates

# Reference

* [1] [Puzzle 9 \| (Find the fastest 3 horses)](https://www.geeksforgeeks.org/puzzle-9-find-the-fastest-3-horses/)
