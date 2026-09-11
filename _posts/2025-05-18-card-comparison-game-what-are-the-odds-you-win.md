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
\\[
P(\text{your card rank} > \text{dealer's card rank})
\\]

---

## Step 2: Use Symmetry

Instead of brute-force counting every card combination, let’s use a key insight: **Symmetry**.

There are only three possible outcomes: you win, you lose, or you tie.
Because you and the dealer are drawing from the same deck, the game is perfectly symmetric. Therefore, your probability of winning is exactly equal to the dealer's probability of winning (which is your probability of losing):

\\[
P(\text{Win}) = P(\text{Lose})
\\]

---

## Step 3: Calculate the Tie Probability

It is much easier to calculate the probability of a **tie**.

1. You draw your card (it doesn't matter what rank it is).
2. There are **51 cards left** in the deck.
3. For the dealer to tie you, they must draw one of the remaining **3 cards** that share the exact same rank as your card.

So, the probability of a tie is trivially:
\\[
P(\text{Tie}) = \frac{3}{51} = \frac{1}{17}
\\]

Since all probabilities must sum to 1:
\\[
P(\text{Win}) + P(\text{Lose}) + P(\text{Tie}) = 1
\\]

Substitute our known values and solve:
\\[
2 \times P(\text{Win}) + \frac{1}{17} = 1
\\]
\\[
2 \times P(\text{Win}) = \frac{16}{17}
\\]
\\[
P(\text{Win}) = \frac{8}{17}
\\]

---

## Final Answer

> The probability that your card beats the dealer’s in this single-draw game is:
>
> \\[
> \boxed{\frac{8}{17}}
> \\]

# Reference

* [1] [Probability Theory in Quantitative Finance Interviews: Part 2](https://medium.com/@yinningzengsteven/probability-theory-in-quantitative-finance-interviews-part-2-ce0b38fb622f)