---
layout: post
title: "Alice vs. Bob: Coin Toss Game"
date: 2025-05-27
category: quantitative interview
---

**Scenario**:

- Alice tosses \\( n + 1 \\) **fair coins**.
- Bob tosses \\( n \\) **fair coins**.
- What is the probability that **Alice gets strictly more heads** than Bob?

<iframe src="{{ site.baseurl }}/assets/alice_vs_bob_coin_probability.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

---

### Reformulation and Intuition

Let:
- \\( A \sim \text{Bin}(n+1, \frac{1}{2}) \\): number of heads Alice gets
- \\( B \sim \text{Bin}(n, \frac{1}{2}) \\): number of heads Bob gets

We want:

\\[
P(A > B)
\\]

Rather than summing over binomial probabilities directly, we can solve this using **symmetry**.

---

### Symmetry Argument

Let \\( A_n \\) be the number of heads Alice gets in her first \\( n \\) tosses, and let her last toss be \\( C \\) (which is 1 if heads, 0 if tails). 
So, \\( A = A_n + C \\).

By symmetry, since Alice and Bob both toss \\( n \\) fair coins:

\\[
P(A_n > B) = P(A_n < B)
\\]

Since the probabilities must sum to 1:

\\[
P(A_n > B) = \frac{1 - P(A_n = B)}{2}
\\]

Now, Alice gets strictly more heads than Bob (\\( A > B \\)) in two mutually exclusive cases:
1. \\( A_n > B \\): Alice already has more heads in the first \\( n \\) tosses. Regardless of her final toss \\( C \\), she wins.
2. \\( A_n = B \\) **and** \\( C = 1 \\): They are tied after \\( n \\) tosses, but Alice's final coin lands heads.

The total probability is:

\\[
P(A > B) = P(A_n > B) + P(A_n = B) \cdot P(C = 1)
\\]

Substitute \\( P(A_n > B) \\) and \\( P(C = 1) = \frac{1}{2} \\):

\\[
P(A > B) = \frac{1 - P(A_n = B)}{2} + P(A_n = B) \cdot \frac{1}{2} = \frac{1}{2}
\\]

---

### Conclusion

\\[
\boxed{P(\text{Alice gets more heads}) = \frac{1}{2}}
\\]

Despite the difference in number of tosses, the symmetry and fairness of the coins give this elegant result.

# Reference

* [1] [Coin Toss Game - Probability of H when unequal number of coins tossed](https://math.stackexchange.com/questions/1804013/coin-toss-game-probability-of-h-when-unequal-number-of-coins-tossed)