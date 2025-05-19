---
layout: post
title: "Alternating Coin Toss Game: Who Wins on HT?"
date: 2025-05-19
category: quantitative interview
---

### The Game

- Two players, **A** and **B**, take turns flipping a **fair coin**.
- Player **A** flips first, then **B**, and so on.
- The game ends as soon as the pattern **HT** (a Head immediately followed by a Tail) appears.
- The player who flipped the **Tail** in the **HT** wins.

---

## Question

What is the probability that **Player A** wins the game?

---

## Strategy and State Analysis

Let’s define some game states:

- **Start (S)**: No flips yet.
- **H_A**: Last flip was **H** by Player A.
- **H_B**: Last flip was **H** by Player B.
- **A_Wins**, **B_Wins**: terminal winning states.

### From the start:

- A flips:
  - H with probability \\( \frac{1}{2} \\) → state **H_A**
  - T with probability \\( \frac{1}{2} \\) → back to **S** (no pattern HT)

### From **H_A**:

- B flips:
  - T → **B wins** (completes HT)
  - H → state **H_B**

### From **H_B**:

- A flips:
  - T → **A wins** (completes HT)
  - H → back to **H_A**

---

## Recursive Probabilities

Let:

- \\( P_A \\): probability that A wins starting from the initial state

Using the recursive transitions, we derive:

\\[
P_A = \frac{1}{2}P_{H_A} + \frac{1}{2}P_A
\\]

Solve for \\( P_{H_A} \\) via:

\\[
P_{H_A} = \frac{1}{2} \cdot 0 + \frac{1}{2} \cdot P_{H_B} = \frac{1}{2} P_{H_B}
\\]

\\[
P_{H_B} = \frac{1}{2} \cdot 1 + \frac{1}{2} \cdot P_{H_A}
\\]

Substitute backwards and solve the system to get:

\\[
P_A = \frac{4}{9}
\\]

---

## Final Answer

The probability that **Player A** wins is:

\\[
\boxed{\frac{4}{9}}
\\]

## Reference

* [1] [First to the sequence HT between two players](https://math.stackexchange.com/questions/1455393/first-to-the-sequence-ht-between-two-players)
