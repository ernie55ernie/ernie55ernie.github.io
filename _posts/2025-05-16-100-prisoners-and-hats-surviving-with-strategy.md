---
layout: post
title: "100 Prisoners and Hats: Surviving with Strategy"
date: 2025-05-16
category: quantitative interview
---

This iconic logic puzzle blends information theory and group strategy:

> **100 prisoners**, each randomly assigned a **red or blue hat**, must guess their own hat color **without seeing it**.
>
> - Each can see **all other hats**, but not their own.
> - They are called up one at a time **in random order**.
> - Each must say **“red” or “blue”**.
> - If correct → **survive**. If wrong → **executed immediately**.
> - All **hear prior guesses** and outcomes.
>
> They may agree on a **strategy beforehand**, but **no communication afterward**.

---

## Objective

> What is the best strategy, and **how many prisoners can be guaranteed to survive**?

<iframe src="{{ site.baseurl }}/assets/100_prisoners_hat_parity.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

---

## Step 1: Key Insight — Use Parity Encoding

Let’s assign binary values:

- **Red = 1**, **Blue = 0**

The group decides to use the **parity (XOR sum)** of all 100 hat colors as a **shared secret**.

---

## Step 2: The Strategy

The **first prisoner** to speak acts as the informant and is the only one who may **not survive**.

They compute the **parity of all 99 visible hats**. Instead of trying to guess their own hat, they use their turn to communicate this parity to the group:

- They announce a hat color such that the **assumed total parity of all 100 hats** (their guess + the 99 they see) is **even (0)**.

This means:
- If the 99 hats have an odd parity (1), they guess "Red" (1) so the total is even.
- If the 99 hats have an even parity (0), they guess "Blue" (0).
- This prisoner has a **50% chance** of survival, since their true hat color is independent of the other 99.

---

## Step 3: Everyone Else

Each subsequent prisoner now knows the exact parity of the 99 hats (excluding the first speaker). 

To figure out their own hat, they simply:
- Look at the other 98 hats (or determine the true colors of previously called prisoners based on their guesses and outcomes).
- Compare the parity of those 98 hats to the total parity announced by the first speaker.
- **Reconstruct their own hat color exactly** to make up the difference!

They are thus guaranteed to guess correctly.

---

## Step 4: Outcome

- **1 prisoner** (the first) has a 50/50 chance.
- **99 prisoners** are **guaranteed to survive**.

This is the **best possible outcome** under the rules.

---

## Final Answer

> Using a parity-based strategy, the group can **guarantee 99 survivors**, with **only the first guess** left to chance.

# Reference

* [1] [100 Prisoners Hat Puzzle (Information Theory)](https://en.wikipedia.org/wiki/Hat_puzzle#100_prisoners)
