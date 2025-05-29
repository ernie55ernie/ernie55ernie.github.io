---
layout: post
title: "Optimal Betting Strategy for the World Series Using Dynamic Programming"
date: 2025-05-29
category: quantitative interview
---

### Problem Overview

The New York Yankees and the San Francisco Giants are playing in a best-of-seven World Series. You want to bet \$100 on the Yankees winning the series, but you are only allowed to place bets on individual games, each at even odds. The question is: **how much should you bet on the first game?**

To solve this, we utilize **dynamic programming** and model the game state using matrices to determine the optimal amount to bet at each stage of the series.

### State Representation

We define a matrix \\( P \\) that holds the **net payoff** in each state \\( (i, j) \\), where:

- \\( i \\): number of games won by the Yankees,
- \\( j \\): number of games lost by the Yankees,
- \\( 0 \leq i, j \leq 4 \\).

Boundary conditions are set as follows:

- \\( P(4, j) = 100 \\) for \\( 0 \leq j \leq 3 \\),
- \\( P(i, 4) = -100 \\) for \\( 0 \leq i \leq 3 \\),
- \\( P(4,4) \\) is not used as it is not a reachable state in a best-of-seven format.

We also define a matrix \\( B \\) that contains the **bet sizes** for each intermediate state. It satisfies:

\\[
P(i+1, j) = P(i, j) + B(i, j) \quad \text{(3.205)}
\\]
\\[
P(i, j+1) = P(i, j) - B(i, j) \quad \text{(3.206)}
\\]

Adding and subtracting these gives us:

\\[
P(i, j) = \frac{1}{2}(P(i+1, j) + P(i, j+1)) \quad \text{(3.207)}
\\]
\\[
B(i, j) = \frac{1}{2}(P(i+1, j) - P(i, j+1)) \quad \text{(3.208)}
\\]

These recursive equations allow us to compute \\( P \\) and \\( B \\) by working backward from the terminal states.

### Matrices

The computed matrices are:

\\[
P = 
\begin{pmatrix}
0 & -31.25 & -62.5 & -87.5 & -100 \\
31.25 & 0 & -37.5 & -75 & -100 \\
62.5 & 37.5 & 0 & -50 & -100 \\
87.5 & 75 & 50 & 0 & -100 \\
100 & 100 & 100 & 100 & 0
\end{pmatrix}
\\]

\\[
B = 
\begin{pmatrix}
31.25 & 31.25 & 25 & 12.5 \\
31.25 & 37.5 & 37.5 & 25 \\
25 & 37.5 & 50 & 50 \\
12.5 & 25 & 50 & 100
\end{pmatrix}
\\]

### First Game Betting Strategy

We start at state \\( (0, 0) \\) since no games have been played. From matrix \\( B \\), we find:

\\[
B(1,1) = 31.25
\\]

This means **we should bet \$31.25 on the Yankees in the first game**.

The strategy is robust: regardless of the outcome of individual games, the betting adjustments according to matrix \\( B \\) ensure that we end up with exactly \$100 if the Yankees win the series.

### Conclusion

Using dynamic programming, we calculate the optimal strategy for betting on a best-of-seven series. The key takeaway is that **we should bet \$31.25 on the first game**, and adjust subsequent bets according to matrix \\( B \\) to maintain an optimal expected outcome.

# Reference

* [1] [Solving the World Series problem by replication](https://math.stackexchange.com/questions/4449163/solving-the-world-series-problem-by-replication)