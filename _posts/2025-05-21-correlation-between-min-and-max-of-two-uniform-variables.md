---
layout: post
title: "Correlation of Min and Max of Two Uniform Variables"
date: 2025-05-21
category: quantitative interview
---

Let \\( X_1, X_2 \sim \mathrm{Uniform}(0,1) \\) be **independent**. Define:

\\[
Y = \min(X_1, X_2), \quad Z = \max(X_1, X_2)
\\]

---

### Part 1: Conditional Probability \\( P(Y \ge y \mid Z \le z) \\)

We are interested in computing:

\\[
P(Y \ge y \mid Z \le z), \quad \text{for } 0 \le y \le z \le 1
\\]

#### Step 1: Joint Probability

Let’s compute the joint event:

\\[
P(Y \ge y, Z \le z) = P(y \le X_1, X_2 \le z, X_1 \ne X_2)
\\]

Since \\( X_1 \\) and \\( X_2 \\) are iid, we can write:

\\[
P(Y \ge y, Z \le z) = \text{Area of the square } [y, z]^2 = (z - y)^2
\\]

#### Step 2: Marginal Probability

\\[
P(Z \le z) = P(X_1 \le z, X_2 \le z) = z^2
\\]

#### Final Result

\\[
P(Y \ge y \mid Z \le z) = \frac{P(Y \ge y, Z \le z)}{P(Z \le z)} = \frac{(z - y)^2}{z^2}
\\]

---

### Part 2: Correlation \\( \mathrm{Corr}(Y, Z) \\)

We use known results from order statistics of Uniform(0,1).

For two iid Uniform(0,1) variables:

- \\( \mathbb{E}[Y] = \frac{1}{3} \\)
- \\( \mathbb{E}[Z] = \frac{2}{3} \\)
- \\( \mathrm{Var}(Y) = \mathrm{Var}(Z) = \frac{1}{18} \\)
- \\( \mathbb{E}[YZ] = \frac{1}{4} \\)

So:

\\[
\mathrm{Cov}(Y, Z) = \mathbb{E}[YZ] - \mathbb{E}[Y] \cdot \mathbb{E}[Z] = \frac{1}{4} - \frac{1}{3} \cdot \frac{2}{3} = \frac{1}{4} - \frac{2}{9} = \frac{1}{36}
\\]

Now compute the correlation:

\\[
\mathrm{Corr}(Y, Z) = \frac{\mathrm{Cov}(Y, Z)}{\sqrt{\mathrm{Var}(Y)\mathrm{Var}(Z)}} = \frac{1/36}{\sqrt{(1/18)(1/18)}} = \frac{1/36}{1/18} = \boxed{\frac{1}{2}}
\\]

---

## Final Answers

1. Conditional probability:

\\[
\boxed{P(Y \ge y \mid Z \le z) = \frac{(z - y)^2}{z^2}}
\\]

2. Correlation:

\\[
\boxed{\mathrm{Corr}(Y, Z) = \frac{1}{2}}
\\]

---

## Reference

* [1] [Order statistic](https://en.wikipedia.org/wiki/Order_statistic#Distribution_of_the_minimum_and_maximum)
