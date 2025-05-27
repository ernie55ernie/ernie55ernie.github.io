---
layout: post
title: "Expected Flips Until First Head"
date: 2025-05-27
category: quantitative interview
---

We consider two versions of the problem:

1. The coin is **fair**.
2. The coin is **biased**, with probability \\( p \\) of heads.

---

### Part 1: Fair Coin

Let \\( X \\) be the number of flips until the first head. Since the coin is fair:

\\[
P(\text{Head}) = \frac{1}{2}
\\]

Then \\( X \sim \text{Geometric}(p = \frac{1}{2}) \\). The expectation is:

\\[
\mathbb{E}[X] = \frac{1}{p} = \frac{1}{1/2} = \boxed{2}
\\]

---

### Part 2: Biased Coin (Probability of Head = \\( p \\))

Now \\( X \sim \text{Geometric}(p) \\), where:

\\[
P(X = k) = (1 - p)^{k - 1} p
\\]

Then the expected number of flips is:

\\[
\mathbb{E}[X] = \frac{1}{p}
\\]

So the smaller \\( p \\) is, the longer you expect to wait for a head.

---

## Conclusion

- For a fair coin: \\( \boxed{2} \\) expected flips
- For a biased coin with \\( P(\text{Head}) = p \\): \\( \boxed{\frac{1}{p}} \\) expected flips

# Reference

* [1] [Geometric distribution](https://en.wikipedia.org/wiki/Geometric_distribution)