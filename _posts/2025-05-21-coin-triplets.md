---
layout: post
title: "Penney’s Game: Waiting Times, Sequence Races, and Optimal Strategies"
date: 2025-05-21
category: quantitative interview
---

### Part A: Expected Number of Tosses

We analyze the expected number of coin tosses required to first observe specific sequences when flipping a fair coin repeatedly.

#### 1. Expected Tosses Until HHH

Let \( E_n \) denote the expected number of tosses to achieve \( n \) consecutive heads. The recurrence relation is:

\[
E_n = 2E_{n-1} + 2 \quad \text{with} \quad E_1 = 2
\]

Solving this recurrence yields:

\[
E_n = 2^{n+1} - 2
\]

Therefore, for \( n = 3 \):

\[
E_3 = 2^{4} - 2 = 16 - 2 = 14
\]

So, the expected number of tosses to get HHH is **14**.

#### 2. Expected Tosses Until THH

This case requires a more detailed analysis, often involving Markov chains or state diagrams. The expected number of tosses to first see the sequence THH is known to be **8**.

---

### Part B: Probability HHH Appears Before THH

We consider the probability that the sequence HHH occurs before THH in repeated fair coin tosses.

This scenario is a classic example of Penney's game, which exhibits non-transitive properties. The probability that HHH appears before THH is known to be **1/8**.

---

### Part C: Strategic Penney’s Game

In Penney's game:

- **Player 1** selects a sequence of three coin toss outcomes (e.g., HHH).
- **Player 2**, knowing Player 1's choice, selects a different sequence.
- A fair coin is tossed repeatedly until one of the chosen sequences appears as a consecutive subsequence; the corresponding player wins.

#### Optimal Strategy

The game is non-transitive, meaning that for any sequence chosen by Player 1, there exists a sequence that Player 2 can choose to have a higher probability of winning.

A general strategy for Player 2 is:

- Take the last two elements of Player 1's sequence.
- Prefix them with the opposite of Player 1's second element.

For example, if Player 1 chooses HHH:

- Player 1's sequence: H H H
- Player 2's optimal response: T H H

This strategy ensures that Player 2 has a higher probability of winning.

#### Should You Go First or Second?

Given the strategic advantage, it's better to go **second** in Penney's game. The second player can always choose a sequence that has a higher probability of appearing first, regardless of the first player's choice.

#### Winning Probability for Second Player

The winning probability for the second player depends on the sequences chosen. For instance:

- If Player 1 chooses HHH and Player 2 responds with THH, Player 2's winning probability is **7/8**.

This demonstrates the significant advantage the second player holds when employing the optimal strategy.

---

## Reference

* [1] [Penney's Game – Wikipedia](https://en.wikipedia.org/wiki/Penney%27s_game)
* [2] [Expected Number of Trials to get N Consecutive Heads – GeeksforGeeks](https://www.geeksforgeeks.org/expected-number-of-trials-to-get-n-consecutive-heads/)
* [3] [Penney's Game Odds From No-Arbitrage – arXiv](https://arxiv.org/abs/1904.09888)
