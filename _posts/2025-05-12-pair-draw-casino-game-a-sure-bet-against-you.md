---
layout: post
title: "Pair-Draw Casino Game: A Sure Bet Against You"
date: 2025-05-12
category: quantitative interview
---

You’re in a casino offered a curious card game involving a standard 52-card deck. The rules seem simple—and tempting:

### Game Mechanics

1. A full 52-card deck is well shuffled.
2. Cards are turned over **two at a time** until the deck is exhausted.
3. For each pair:
   - If **both are red**, they go into **your pile**.
   - If **both are black**, they go into the **dealer’s pile**.
   - If one red and one black, **both are discarded**.
4. At the end:
   - If **your pile has more cards**, you **win \$100**.
   - If not (tie or dealer has more), you **win nothing**.
5. You get to choose the **entry fee** before playing.

### What Should You Pay?

Let’s analyze the symmetry and probability:

- The deck has **26 red** and **26 black** cards.
- Pairs are drawn randomly.
- Every red card that goes to you is matched by a black card that can go to the dealer.
- Whenever two red cards go to you, a black-black pair is equally likely.

### Key Insight

Over many games, you’ll find that the number of **red-red pairs (your gain)** and **black-black pairs (dealer’s gain)** will be **exactly equal in expectation**. In fact, the red and black pairs are symmetric due to identical counts and uniform shuffling.

### Mathematical Outcome

The **expected number of red pairs** equals the **expected number of black pairs**. So, the **expected win** is $0.

Moreover, the **dealer wins ties**, so your chances of actually **winning \$100** are **less than 50%**.

Hence, the **expected value of the game is negative**.

## Final Answer

**The maximum fee you should pay is \$0.**

Playing this game has negative expected value—it’s a cleverly disguised losing proposition.

# Reference

* [1] [Card game - Insidious casino](https://puzzling.stackexchange.com/questions/54812/card-game-insidious-casino)
