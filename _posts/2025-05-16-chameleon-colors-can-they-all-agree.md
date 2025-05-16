---
layout: post
title: "Chameleon Colors: Can They All Agree?"
date: 2025-05-16
category: quantitative interview
---

You're told of a curious island:

> There are:
> - **13 red chameleons**
> - **15 green chameleons**
> - **17 blue chameleons**
>
> Rule: When **two chameleons of different colors meet**, they **both change** to the **third color**.

**Question:** Is it possible—through repeated pairwise meetings—for **all chameleons to eventually become the same color**?

---

## Step 1: Model the Rule

When two chameleons of **different colors** meet:

- **(Red, Green)** → both become **Blue**
- **(Green, Blue)** → both become **Red**
- **(Blue, Red)** → both become **Green**

Each meeting **reduces** two chameleons of different colors and **adds two of the third**.

So the **total number of chameleons remains constant**: 13 + 15 + 17 = 45.

---

## Step 2: Look for an Invariant

We look for a quantity that doesn’t change—an **invariant**.

Let \( (R, G, B) \) denote the number of red, green, and blue chameleons.

Key idea: Examine **differences mod 3**

Let’s track:

- \( G - R \mod 3 \)
- \( B - G \mod 3 \)

Let’s calculate the initial state:

- \( G - R = 15 - 13 = 2 \mod 3 \)
- \( B - G = 17 - 15 = 2 \mod 3 \)

Let’s try some examples of a color change:

### Suppose Red and Green meet → both become Blue:

- R ↓ by 1
- G ↓ by 1
- B ↑ by 2

So:
- \( G - R \) is unchanged (both ↓1 → difference unchanged)
- \( B - G \) increases by 3 → same mod 3

So both differences **mod 3 remain constant**.

---

## Step 3: Use the Invariant

Currently:

- \( G - R \equiv 2 \mod 3 \)
- \( B - G \equiv 2 \mod 3 \)

If all chameleons were to become the same color (say all red), then:

- G = 0, B = 0, R = 45 → \( G - R = -45 \equiv 0 \mod 3 \), contradiction.

In fact, for **any** same-color state:

- The differences G−R and B−G would be zero → \( \equiv 0 \mod 3 \)

But our current values are \( \equiv 2 \mod 3 \), and they **never change**.

---

## Final Answer

> **No**, it’s **not possible** for all chameleons to become the same color.  
> The values \( G - R \mod 3 \) and \( B - G \mod 3 \) are **invariant**, and they **don’t equal 0** initially—so total unification is impossible.

# Reference

* [1] [Chameleons Riddle](https://math.stackexchange.com/questions/145725/chameleons-riddle)
