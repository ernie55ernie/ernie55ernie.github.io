---
layout: post
title: "12-Ball Balance Puzzle: Solving in Three Weighings"
date: 2025-05-12
category: quantitative interview
---

This classic logic challenge asks: Can you identify a single defective ball—either heavier or lighter—from a set of 12, using only **three weighings** on a balance scale?

The answer is **yes**, but it requires a precise and clever weighing strategy.

### Puzzle Summary

- You have **12 balls**, visually identical.
- One is **defective**: **heavier or lighter**, unknown which.
- You have **three weighings** on a **balance scale** (which shows heavier side or balance).
- Your goal: Identify the **odd ball** and whether it is **heavier or lighter**.

## High-Level Strategy

Each weighing on a balance scale gives **3 outcomes**: left heavier, right heavier, or balanced.  
With 3 weighings, you have at most \\( 3^3 = 27 \\) unique outcome sequences.

There are 12 possible balls × 2 defect types (heavier/lighter) = **24 possibilities** to distinguish.

So 27 > 24 — enough outcomes to identify the culprit in 3 weighings.

<iframe src="{{ site.baseurl }}/assets/12_ball_balance_puzzle.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

## Step-by-Step Solution

### First Weighing:
Weigh balls **1, 2, 3, 4** vs. **5, 6, 7, 8**

**Three outcomes:**

#### 1. If balanced:
The defective ball is among **9, 10, 11, 12**, and balls 1–8 are known to be normal.

**Second Weighing:** Weigh **9, 10, 11** vs. **1, 2, 3** (known normal).
- **If balanced:** Ball 12 is the odd one. 
  - **Third Weighing:** Weigh **12** vs. **1**. If 12 goes down, it's heavy; if it goes up, it's light.
- **If left is heavy:** The odd ball is 9, 10, or 11, and it is heavy. 
  - **Third Weighing:** Weigh **9** vs. **10**. If 9 goes down, 9 is heavy. If 10 goes down, 10 is heavy. If balanced, 11 is heavy.
- **If left is light:** The odd ball is 9, 10, or 11, and it is light. 
  - **Third Weighing:** Weigh **9** vs. **10**. If 9 goes up, 9 is light. If 10 goes up, 10 is light. If balanced, 11 is light.

#### 2. If unbalanced (e.g., left is heavier):
Assume left (1, 2, 3, 4) is heavier than right (5, 6, 7, 8). This means either one of {1, 2, 3, 4} is heavy, or one of {5, 6, 7, 8} is light. Balls 9–12 are known normal.

**Second Weighing:** Weigh **1, 2, 3, 5** vs. **4, 9, 10, 11**.
*(We kept 1, 2, 3 on the left, moved 4 to the right, moved 5 to the left, and filled the rest with normal balls).*

- **If left is heavy again:** The odd ball must be one that stayed on the same side and was suspected heavy. So it's **1, 2, or 3** (all heavy candidates).
  - **Third Weighing:** Weigh **1** vs. **2**. If 1 is heavy, it goes down. If 2 is heavy, it goes down. If balanced, 3 is heavy.
- **If right is heavy:** The imbalance flipped. The odd ball must be one that switched sides. So it's either **4** (switched to right, making it heavy) or **5** (switched to left, making it light).
  - **Third Weighing:** Weigh **4** vs. **9** (normal). If 4 goes down, 4 is heavy. If balanced, 5 is light.
- **If balanced:** The odd ball must be one of the unweighed balls from the suspected light group: **6, 7, or 8** (all light candidates).
  - **Third Weighing:** Weigh **6** vs. **7**. If 6 goes up, 6 is light. If 7 goes up, 7 is light. If balanced, 8 is light.

*(If the first weighing resulted in the left being lighter, you apply the exact same logic but mirror the heavy/light expectations).*

## Final Answer

**Yes**, you can always identify the defective ball and its nature (heavier/lighter) in exactly **3 weighings**. 

This puzzle illustrates **information theory** and the power of base-3 logic: each weighing gives 3 possible outcomes. Three weighings give \\( 3^3 = 27 \\) possible outcomes, which is just enough to distinguish the 24 possible states (12 balls × 2 states).

# Reference

* [1] [12 Ball Problem (Wikipedia)](https://en.wikipedia.org/wiki/Balance_puzzle#12-ball_problem)