---
layout: post
title: "Coin Piles Puzzle: Equal Heads Without Seeing"
date: 2025-05-13
category: quantitative interview
---

You're blindfolded, faced with a deceptively simple task:

> You have **1,000 coins** scattered on the floor.  
> Exactly **20** are heads-up, the rest are tails.  
> You **can’t see** or distinguish the coins by touch.  
> You may divide them into **two piles**, and **flip any subset** of coins.  
> Your goal: Create **two piles with the same number of heads**.

Sounds impossible without sight? It’s not—just clever.

---

## The Key Trick: Use Randomness Against Itself

You can **force symmetry** using a neat, invariant-based move.

### Step-by-Step Solution

1. **Randomly select any 20 coins** from the 1,000 coins. (You know there are 20 heads total, but not where they are.)

2. **Place those 20 coins into a separate pile (Pile A).**  
   The remaining 980 coins go into **Pile B**.

3. **Flip every coin in Pile A.**

Done!

---

## Why It Works

Let’s say in the 20 coins you picked for Pile A, **\( h \)** were originally heads-up.  
Then there are \( 20 - h \) tails in Pile A.

That means in Pile B (the remaining 980 coins), there must be **\( 20 - h \)** heads—because there are 20 total heads.

When you flip the **\( h \)** heads and **\( 20 - h \)** tails in Pile A, it becomes:

- \( h \) → tails  
- \( 20 - h \) → heads

So now Pile A has exactly **\( 20 - h \)** heads.  
Pile B already had \( 20 - h \) heads.

### Result: Both piles now contain **the same number of heads**.

---

## Final Answer

**Pick any 20 coins to make one pile. Flip all of them.**  
> Now both piles have an **equal number of heads**.

# Reference

* [1] [Can You Solve Apple's Split The Coins Riddle?](https://www.youtube.com/watch?v=WsjQXUXUmSc)
