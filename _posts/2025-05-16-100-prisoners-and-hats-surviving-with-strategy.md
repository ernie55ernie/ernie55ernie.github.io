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

---

## Step 1: Key Insight — Use Parity Encoding

Let’s assign binary values:

- **Red = 1**, **Blue = 0**

The group decides to use the **parity (XOR sum)** of all 100 hat colors as a **shared secret**.

---

## Step 2: The Strategy

The **first prisoner** to speak is the only one who may **not survive**.

They compute the **parity of all 99 visible hats** and use that to infer their own:

- They announce a hat color such that the **total parity of all 100 hats** is **even (or pre-agreed value)**.

This means:

- If the total parity is 0 (even), then the first prisoner says the color that **completes the parity to even**.
- This prisoner has a **50% chance** of survival.

---

## Step 3: Everyone Else

Each subsequent prisoner:

- **Heard all previous guesses**.
- **Knows the parity of everyone else's hats**.
- **Knows the overall parity from the first speaker**.
- **Can reconstruct their own hat color exactly** using prior information.

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
