---
layout: post
title: "Alice vs. Bob: Coin Toss Game and the Ballot Problem"
date: 2025-05-27
category: quantitative interview
---

**Scenario**:

- Alice tosses \\( n + 1 \\) **fair coins**.
- Bob tosses \\( n \\) **fair coins**.
- What is the probability that **Alice gets strictly more heads** than Bob?

---

### Reformulation and Intuition

Let:
- \\( A \sim \text{Bin}(n+1, \frac{1}{2}) \\): number of heads Alice gets
- \\( B \sim \text{Bin}(n, \frac{1}{2}) \\): number of heads Bob gets

We want:

\\[
P(A > B)
\\]

Rather than summing over binomial probabilities directly, this problem is closely related to a classic result in combinatorics: the **Ballot Problem**.

---

### Ballot Problem Analogy

In the Ballot Problem:

> If candidate A receives \\( a \\) votes and candidate B receives \\( b \\) votes with \\( a > b \\), and the votes are counted in random order, what is the probability that A is always ahead?

For our problem, there is a known result that gives:

\\[
P(A > B) = \frac{1}{2}
\\]

This result follows from **symmetry**: Alice has one extra coin toss. For each possible configuration of Bob’s tosses, exactly half of Alice’s outcomes will result in **more heads**, due to the fair and independent nature of the coins.

---

### Conclusion

\\[
\boxed{P(\text{Alice gets more heads}) = \frac{1}{2}}
\\]

Despite the difference in number of tosses, the symmetry and fairness of the coins give this elegant result.

# Reference

* [1] [Coin Toss Game - Probability of H when unequal number of coins tossed](https://math.stackexchange.com/questions/1804013/coin-toss-game-probability-of-h-when-unequal-number-of-coins-tossed)