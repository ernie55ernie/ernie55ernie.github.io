---
layout: post
title: "Bayes' Theorem and the Double-Headed Coin"
date: 2025-05-19
category: quantitative interview
---

### The Puzzle

You have 1,000 coins in a bag:

- 1 is **double-headed** (always lands heads)
- 999 are **fair** (heads with probability \\( \frac{1}{2} \\))

You draw one coin uniformly at random and flip it **10 times**. It lands **heads every time**.

### Question:

What is the probability that the coin you picked is the **double-headed** one?

---

## Solution Using Bayes' Theorem

We define:

- \\( D \\): the event that you picked the double-headed coin
- \\( F \\): the event that you picked a fair coin
- \\( H^{10} \\): the event that you observed 10 heads in a row

We want to compute:

\\[
P(D \mid H^{10}) = \frac{P(H^{10} \mid D) \cdot P(D)}{P(H^{10})}
\\]

### Step 1: Prior Probabilities

- \\( P(D) = \frac{1}{1000} \\)
- \\( P(F) = \frac{999}{1000} \\)

### Step 2: Likelihoods

- \\( P(H^{10} \mid D) = 1 \\) (always heads)
- \\( P(H^{10} \mid F) = \left(\frac{1}{2}\right)^{10} = \frac{1}{1024} \\)

### Step 3: Total Probability of 10 Heads

\\[
P(H^{10}) = P(H^{10} \mid D) \cdot P(D) + P(H^{10} \mid F) \cdot P(F) = 1 \cdot \frac{1}{1000} + \frac{1}{1024} \cdot \frac{999}{1000}
\\]

\\[
P(H^{10}) = \frac{1}{1000} + \frac{999}{1024000}
= \frac{1024 + 999}{1024000} = \frac{2023}{1024000}
\\]

### Step 4: Apply Bayes' Theorem

\\[
P(D \mid H^{10}) = \frac{1 \cdot \frac{1}{1000}}{\frac{2023}{1024000}} = \frac{1024}{2023}
\\]

---

## Final Answer

\\[
\boxed{\frac{1024}{2023}} \approx 0.506
\\]

So, given 10 consecutive heads, there's slightly more than a 50% chance that you picked the double-headed coin.

## Reference

* [1] [Wikipedia: Bayes' theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem)
