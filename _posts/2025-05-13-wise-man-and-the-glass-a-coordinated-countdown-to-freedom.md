---
layout: post
title: "Wise Men and the Glass: A Coordinated Countdown to Freedom"
date: 2025-05-13
category: quantitative interview
---

This puzzle is a variant of the famous "prisoners and the light bulb" problem, where 50 wise men are tested not by riddles, but by **coordination under uncertainty**.

### The Setup

- **50 wise men** are imprisoned separately.
- Outside their cells is a **glass**, initially **upside-down**.
- Each minute, the sultan **randomly selects one** man to visit the glass.
- That man may **flip the glass** (or not), based solely on his memory.
- Once separated, the men have **no communication**, and the only observable shared object is the glass.

At any point, one man may **declare** that everyone has been called.  
If correct: **all are freed**.  
If wrong: **they all die**.

They get **one chance** before being separated to agree on a strategy.

---

## Goal

Design a **guaranteed strategy** to eventually make the correct declaration—regardless of the randomness in the sultan’s choices.

---

## Key Idea: Designate a Counter

The strategy uses **one designated counter**, say **Wise Man #1**, and the other 49 act as **signalers**.

### Pre-agreed roles:

- **One counter** (Wise Man #1)
- **49 signalers** (all others)

### The Protocol

- The counter is responsible for **counting unique signalers**.
- The glass has two states: **up** and **down**.
- All signalers **know** the initial state is **down**.

#### Rules for signalers (non-counters):

- **Exactly once**, when a signaler sees the glass **down**, they **flip it up**—this is their signal.
- After doing so once, they **never flip the glass again**.

#### Rules for the counter:

- When the counter sees the glass **up**, he:
  - Flips it back **down**.
  - Increments his internal count by **1**.
- When the glass is down, he does **nothing**.

Eventually, once the counter has seen **49 flips up**, he knows all 49 signalers have been summoned **at least once**.

At that point, he **declares** that all 50 have been called (including himself, since he's being called now).

---

## Why It Works

- Each signaler flips the glass **once**, the first time they’re called and it’s down.
- Only the **counter** resets the glass to down and increments the tally.
- This guarantees a one-to-one correspondence between signaler appearances and the counter's count.
- No false positives occur, because no one flips the glass more than once.

Eventually, the counter will tally **49** ups, proving all others have appeared.

---

## Final Answer

> **Designate one man as counter**.  
> All others flip the glass **from down to up only once**, the first time they’re called and the glass is down.  
> The counter flips it **down to up**, and increments a count.  
> When he reaches **49**, he declares that all have been summoned.

# Reference

* [1] [100 Prisoners and a Light Bulb Riddle & Solution](https://medium.com/i-math/100-prisoners-and-a-light-bulb-573426272f4c)
