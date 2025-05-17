---
layout: post
title: "Card Comparison Game: What Are the Odds You Win?"
date: 2025-05-18
category: quantitative interview
---

You play a simple game against the house:

> - From a **standard 52-card deck**, you draw one card.  
> - Then the **dealer** draws one card **without replacement**.  
> - If your card’s **rank** is **strictly higher**, you **win \$1**.  
> - If it’s **equal or lower**, you **lose**.

**Question:** What’s the probability that your card beats the dealer’s?

---

## Step 1: Understand the Deck and the Rules

- Each **rank** (2 through Ace) appears **4 times**.
- Only the **rank** matters—not suit.
- You and the dealer each get **one card**, no replacement.

You want:
\[
P(\text{your card rank} > \text{dealer's card rank})
\]

---

## Step 2: Use Symmetry

Instead of brute-force enumeration, let’s use a key insight:

- The game is symmetric—each pair of distinct ranks occurs equally often.
- For example, there are:
  - 4 × 4 = 16 ways for you to draw a 7 and dealer a 5.
  - Also 16 ways to draw a 5 and 7 in the opposite order.

---

## Step 3: Count Winning Pairs

There are a total of:
\[
52 × 51 = 2652 \text{ possible (ordered) card pairs}
\]

Let’s compute how many of these result in **your rank > dealer’s rank**.

There are 13 ranks, and for every pair of distinct ranks \( (r_i, r_j) \), there are:

- 4 × 4 = 16 ways to draw one card of each rank.

Among the \(\binom{13}{2} = 78\) unordered rank pairs, **half** of the 16 × 78 = 1248 ordered pairs favor you (i.e., you have the higher rank), the other half favor the dealer.

So:
- Total wins: **1248**
- Total losses or ties: **2652 - 1248 = 1404**

Hence, the probability of winning is:

\[
\frac{1248}{2652} = \frac{8}{17}
\]

---

## Final Answer

> The probability that your card beats the dealer’s in this single-draw game is:
>
> \[
> \boxed{\frac{8}{17}}
> \]

# Reference

* [1] [Probability Theory in Quantitative Finance Interviews: Part 2](https://medium.com/@yinningzengsteven/probability-theory-in-quantitative-finance-interviews-part-2-ce0b38fb622f)