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

Let’s define the game states based on whose turn it is and the previous flip:

- **S_A**: It is A's turn, and there is no previous H (e.g., start of game, or after a T).
- **S_B**: It is B's turn, and there is no previous H.
- **H_A**: Last flip was **H** by Player A (it is B's turn).
- **H_B**: Last flip was **H** by Player B (it is A's turn).

### From **S_A**:

- A flips:
  - H with probability \\( \frac{1}{2} \\) → state **H_A**
  - T with probability \\( \frac{1}{2} \\) → state **S_B** (it is now B's turn)

### From **S_B**:

- B flips:
  - H with probability \\( \frac{1}{2} \\) → state **H_B**
  - T with probability \\( \frac{1}{2} \\) → state **S_A** (it is now A's turn)

### From **H_A**:

- B flips:
  - T → **B wins** (completes HT, A wins with prob 0)
  - H → state **H_B**

### From **H_B**:

- A flips:
  - T → **A wins** (completes HT, A wins with prob 1)
  - H → state **H_A**

---

## Recursive Probabilities

Let \\( P(\text{State}) \\) be the probability that **Player A** wins starting from that state. We want to find \\( P_{S_A} \\).

First, solve the subsystem for the states where an **H** was just flipped:

\\[
P_{H_A} = \frac{1}{2} \cdot 0 + \frac{1}{2} \cdot P_{H_B} = \frac{1}{2} P_{H_B}
\\]

\\[
P_{H_B} = \frac{1}{2} \cdot 1 + \frac{1}{2} \cdot P_{H_A} = \frac{1}{2} + \frac{1}{2} \left( \frac{1}{2} P_{H_B} \right) = \frac{1}{2} + \frac{1}{4} P_{H_B}
\\]

Solving gives \\( P_{H_B} = \frac{2}{3} \\) and therefore \\( P_{H_A} = \frac{1}{3} \\).

Next, use the initial states to find \\( P_{S_A} \\):

\\[
P_{S_B} = \frac{1}{2} P_{H_B} + \frac{1}{2} P_{S_A} = \frac{1}{3} + \frac{1}{2} P_{S_A}
\\]

\\[
P_{S_A} = \frac{1}{2} P_{H_A} + \frac{1}{2} P_{S_B} = \frac{1}{6} + \frac{1}{2} P_{S_B}
\\]

Substitute \\( P_{S_B} \\) into \\( P_{S_A} \\):

\\[
P_{S_A} = \frac{1}{6} + \frac{1}{2} \left( \frac{1}{3} + \frac{1}{2} P_{S_A} \right) = \frac{1}{3} + \frac{1}{4} P_{S_A}
\\]

\\[
\frac{3}{4} P_{S_A} = \frac{1}{3} \implies P_{S_A} = \frac{4}{9}
\\]

---

## Final Answer

The probability that **Player A** wins is:

\\[
\boxed{\frac{4}{9}}
\\]

## Reference

* [1] [First to the sequence HT between two players](https://math.stackexchange.com/questions/1455393/first-to-the-sequence-ht-between-two-players)
