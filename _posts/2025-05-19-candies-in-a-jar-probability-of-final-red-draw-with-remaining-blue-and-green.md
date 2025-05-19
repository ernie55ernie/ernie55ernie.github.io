---
layout: post
title: "Candies in a Jar: Probability of Final Red Draw with Remaining Blue and Green"
date: 2025-05-19
category: quantitative interview
---

### The Puzzle

You have a jar containing:

- 10 red candies
- 20 blue candies
- 30 green candies

You draw candies one at a time at random **without replacement**.

**Question:** What is the probability that, **at the moment you remove the last red candy**, there is **still at least one blue** and **one green** candy remaining in the jar?

---

## Total Candies

Total number of candies: \\( 10 + 20 + 30 = 60 \\)

---

## Approach

We aim to find the probability that when the **last red candy** is drawn, **both blue and green candies** are still present in the jar. This is equivalent to computing the probability that the **last red candy** is drawn **before** the last blue and last green candies.

Let:

- \\( T_r \\): position (draw number) of the **last red** candy
- \\( T_b \\): position of the **last blue** candy
- \\( T_g \\): position of the **last green** candy

We are interested in:

\\[
P(T_r < T_b \text{ and } T_r < T_g)
\\]

This event can occur in two mutually exclusive ways:

1. \\( T_r < T_b < T_g \\)
2. \\( T_r < T_g < T_b \\)

Therefore:

\\[
P(T_r < T_b \text{ and } T_r < T_g) = P(T_r < T_b < T_g) + P(T_r < T_g < T_b)
\\]

---

## Calculating the Probabilities

### First Scenario: \\( T_r < T_b < T_g \\)

- Probability that the last candy drawn is green: \\( \frac{30}{60} \\)
- Given that, the probability that the last blue candy is drawn before the last green candy: \\( \frac{20}{30} \\)

So:

\\[
P(T_r < T_b < T_g) = \frac{30}{60} \cdot \frac{20}{30} = \frac{1}{2} \cdot \frac{2}{3} = \frac{1}{3}
\\]

### Second Scenario: \\( T_r < T_g < T_b \\)

- Probability that the last candy drawn is blue: \\( \frac{20}{60} \\)
- Given that, the probability that the last green candy is drawn before the last blue candy: \\( \frac{30}{40} \\)

So:

\\[
P(T_r < T_g < T_b) = \frac{20}{60} \cdot \frac{30}{40} = \frac{1}{3} \cdot \frac{3}{4} = \frac{1}{4}
\\]

---

## Final Probability

Adding both scenarios:

\\[
\frac{1}{3} + \frac{1}{4} = \frac{4}{12} + \frac{3}{12} = \frac{7}{12}
\\]

---

## Answer

\\[
\boxed{\frac{7}{12}}
\\]

## Reference

* [1] [Candies withdrawal probability for a particular subsequence](https://math.stackexchange.com/questions/1805078/candies-withdrawal-probability-for-a-particular-subsequence)