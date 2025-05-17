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

## Step-by-Step Solution

### First Weighing:
Weigh balls **1, 2, 3, 4** vs. **5, 6, 7, 8**

**Three outcomes:**

#### 1. If balanced:
Then the defective ball is among **9, 10, 11, 12**.

### Second Weighing (Case: Balanced First Weighing):
Weigh **1, 2, 9** vs. **3, 4, 10**

- If **balanced**, the odd ball is **11 or 12**
- Weigh **11 vs. 1** (known normal)
  - If equal → ball 12 is odd
  - If 11 heavier/lighter → 11 is odd and its type is known

- If **unbalanced**, you compare positions of 9 or 10 to deduce which is odd and whether it's heavy or light

#### 2. If **left heavier** in the first weighing:
The defective ball is in **1–8**, and you know the odd ball caused an imbalance.

Track the combinations of outcomes across weighings to eliminate possibilities. The logic tree splits depending on which balls are on which sides in each weighing.

You continue with carefully selected weighings:

### Second Weighing (Case: Left Heavy First):
Weigh **1, 5, 9** vs. **2, 6, 10**

Again, interpret outcomes:

- Balanced → Odd ball in {3, 4, 7, 8}
- Left heavy → Infer about 1/5 vs 2/6
- Right heavy → Same logic

### Third Weighing:
Use the information narrowed down from the first two steps to make a final weighing that distinguishes between the last 3 suspects.

## Final Answer

**Yes**, you can identify the defective ball and its nature (heavier/lighter) in **3 weighings** using a decision tree based on outcomes of each weighing.

This puzzle illustrates **information theory** and the power of base-3 logic.

# Reference

* [1] [12 Ball Problem (Wikipedia)](https://en.wikipedia.org/wiki/Balance_puzzle#12-ball_problem)