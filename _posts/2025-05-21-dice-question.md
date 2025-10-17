---
layout: post
title: "Dice Duel: Rolling a 12 Before Two Sevens in a Row"
date: 2025-05-21
category: quantitative interview
---

### The Setup

Two players engage in a dice game:

- **Player A** wins if a roll of **12** appears **before** Player B achieves **two consecutive** rolls summing to **7**.
- **Player B** wins if at any point there are **two consecutive** rolls each summing to **7**, occurring before the first 12.

The game continues with repeated rolls of two fair six-sided dice until one of these conditions is met.

---

## Modeling the Game

To analyze this game, we model it as a Markov chain with the following states:

- **State S₀**: No 7 was rolled on the previous turn (initial state).
- **State S₁**: A 7 was rolled on the previous turn.
- **State A**: Player A wins (a 12 is rolled).
- **State B**: Player B wins (two consecutive 7s are rolled).

### Transition Probabilities

The probabilities of rolling certain sums with two dice are:

- **P(12)**: Only one combination (6+6) yields 12, so \\( \frac{1}{36} \\).
- **P(7)**: Six combinations yield 7, so \\( \frac{6}{36} = \frac{1}{6} \\).
- **P(other)**: The remaining 29 combinations, so \\( \frac{29}{36} \\).

Based on these, the transitions are:

- From **S₀**:
  - To **A**: \\( \frac{1}{36} \\)
  - To **S₁**: \\( \frac{6}{36} = \frac{1}{6} \\)
  - Stay in **S₀**: \\( \frac{29}{36} \\)

- From **S₁**:
  - To **B**: \\( \frac{6}{36} = \frac{1}{6} \\)
  - To **A**: \\( \frac{1}{36} \\)
  - To **S₀**: \\( \frac{29}{36} \\)

---

## Solving the System

Let:

- \\( p_0 \\): Probability that Player A wins starting from **S₀**.
- \\( p_1 \\): Probability that Player A wins starting from **S₁**.

We can set up the following equations:

1. \\( p_0 = \frac{1}{36} + \frac{6}{36} p_1 + \frac{29}{36} p_0 \\)
2. \\( p_1 = \frac{1}{36} + \frac{29}{36} p_0 \\)

Solving Equation 1:

\\[
p_0 - \frac{29}{36} p_0 = \frac{1}{36} + \frac{6}{36} p_1
\\]
\\[
\Rightarrow \frac{7}{36} p_0 = \frac{1}{36} + \frac{6}{36} p_1
\\]
\\[
\Rightarrow 7 p_0 = 1 + 6 p_1 \quad \text{(Equation 3)}
\\]

Substitute Equation 2 into Equation 3:

\\[
7 p_0 = 1 + 6 \left( \frac{1}{36} + \frac{29}{36} p_0 \right )
\\]
\\[
\Rightarrow 7 p_0 = 1 + \frac{6}{36} + \frac{174}{36} p_0
\\]
\\[
\Rightarrow 7 p_0 = \frac{42}{36} + \frac{174}{36} p_0
\\]
\\[
\Rightarrow 7 p_0 - \frac{174}{36} p_0 = \frac{42}{36}
\\]
\\[
\Rightarrow \left(7 - \frac{174}{36}\right) p_0 = \frac{42}{36}
\\]
\\[
\Rightarrow \left(\frac{252 - 174}{36}\right) p_0 = \frac{42}{36}
\\]
\\[
\Rightarrow \frac{78}{36} p_0 = \frac{42}{36}
\\]
\\[
\Rightarrow p_0 = \frac{42}{78} = \frac{7}{13}
\\]

---

## Final Answer

\\[
\boxed{\frac{7}{13}}
\\]

Therefore, the probability that **Player A** wins (i.e., a 12 is rolled before two consecutive 7s) is **7/13**.

---

## Reference

* [1] [Probability you get 12 before two consecutive 7s](https://math.stackexchange.com/questions/4494380/probability-you-get-12-before-two-consecutive-7s)
