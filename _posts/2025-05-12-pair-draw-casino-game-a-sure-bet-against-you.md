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

You don't even need to rely on probability or expected values! Let’s look at the deterministic math of every single deck:

- Every mixed pair (discarded) consumes exactly **1 red card** and **1 black card**.
- The remaining cards form the mono-color pairs (your pile and the dealer’s pile).

### Mathematical Outcome

Let \\( M \\) be the number of mixed pairs. These \\( M \\) pairs consume exactly \\( M \\) red cards and \\( M \\) black cards from the deck. 

This leaves exactly \\( 26 - M \\) red cards for your pile, and \\( 26 - M \\) black cards for the dealer’s pile. 

Because your pile and the dealer's pile will **always** have the exact same number of cards, the game **always ends in a tie**, regardless of how the deck is shuffled.

Since the rules state you only win if you have *more* cards, your chances of winning are exactly **0%**.

## Final Answer

**The maximum fee you should pay is \$0.**

Playing this game has zero expected value—it’s a cleverly disguised losing proposition.

# Reference

* [1] [Card game - Insidious casino](https://puzzling.stackexchange.com/questions/54812/card-game-insidious-casino)
