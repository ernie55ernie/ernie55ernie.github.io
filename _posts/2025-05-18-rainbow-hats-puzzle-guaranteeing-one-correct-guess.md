---
layout: post
title: "Rainbow Hats Puzzle: Guaranteeing One Correct Guess"
date: 2025-05-18
category: quantitative interview
---

This colorful twist on a logic puzzle goes as follows:

> **Seven prisoners**, each wearing a **rainbow-colored hat** (chosen from **7 possible colors**) stand in a line or act simultaneously.  
> Each sees the other six hats, but not their own.  
> Without communication after the hats are placed, each prisoner must **guess the color of their own hat**.
>
> If **at least one guess is correct**, all go free.  
> If **no one guesses correctly**, they are executed.

**Can the prisoners devise a strategy that guarantees survival?**

---

## Step 1: Key Observations

- There are **7 possible hat colors** (think: Red, Orange, Yellow, Green, Blue, Indigo, Violet).
- Hats may **repeat**.
- The challenge is to ensure **at least one prisoner guesses correctly**—every time.

---

## Step 2: Use Modulo Arithmetic (Z₇)

Label the hat colors with numbers:

\[
\text{Red} = 0,\quad \text{Orange} = 1,\quad \ldots,\quad \text{Violet} = 6
\]

Now think of the color assignments as values in **mod 7 arithmetic**.

Let the prisoners be numbered \(P_0, P_1, \ldots, P_6\).

Each prisoner can see the hat colors of everyone else, so they know the values \(c_0, \ldots, c_6\) except for their own.

---

## Step 3: Strategy

The prisoners agree on the following rule:

Each prisoner \(P_i\) assumes that the **sum of all hat colors modulo 7 is congruent to \(i\)**.  
Then prisoner \(P_i\) guesses their own hat color as:

\[
g_i = (i - \sum_{j \ne i} c_j) \mod 7
\]

So each prisoner **computes** what their own hat color **must be** to make the total modulo 7 sum equal to their index.

---

## Step 4: Why It Works

Let’s suppose the actual hat colors are \(c_0, c_1, \ldots, c_6\).

Then the true total sum is:

\[
T = \sum_{i=0}^{6} c_i \mod 7
\]

Now, **only the prisoner \(P_T\)** will have guessed their own hat color correctly:

- \(P_T\) assumes the total should be \(T\), and since the real total is \(T\), their calculated guess is correct.

All other prisoners will be wrong—but **one will always be right**.

---

## Final Answer

> Yes, the prisoners can guarantee freedom by using a **mod 7 parity strategy**.  
> Each assumes the total color sum mod 7 equals their index, and deduces their own color accordingly.  
> Exactly **one** prisoner is guaranteed to guess correctly—ensuring they all survive.

# Reference

* [1] [Rainbow Hats Puzzle](https://math.stackexchange.com/questions/149915/rainbow-hats-puzzle)
