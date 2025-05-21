---
layout: post
title: "Order Statistics of Uniform(0,1): Max and Min"
date: 2025-05-21
category: quantitative interview
---

Let \\( X_1, \dots, X_n \\) be **independent and identically distributed** \\( \mathrm{Uniform}(0,1) \\) random variables.

We define the **maximum** and **minimum** as:

\\[
Z_n = \max\{X_1, \dots, X_n\}, \quad Y_n = \min\{X_1, \dots, X_n\}
\\]

---

## Part 1: Maximum \\( Z_n \\)

### CDF of \\( Z_n \\)

\\[
F_{Z_n}(z) = \Pr(Z_n \le z) = \Pr(X_1 \le z, \dots, X_n \le z) = \Pr(X_1 \le z)^n = z^n, \quad 0 \le z \le 1
\\]

### PDF of \\( Z_n \\)

\\[
f_{Z_n}(z) = \frac{d}{dz}F_{Z_n}(z) = n z^{n-1}, \quad 0 \le z \le 1
\\]

### Expected Value of \\( Z_n \\)

\\[
E[Z_n] = \int_0^1 z \cdot f_{Z_n}(z)\,dz = \int_0^1 z \cdot n z^{n-1}\,dz = n \int_0^1 z^n\,dz = \frac{n}{n+1}
\\]

---

## Part 2: Minimum \\( Y_n \\)

### CDF of \\( Y_n \\)

\\[
F_{Y_n}(y) = \Pr(Y_n \le y) = 1 - \Pr(X_1 > y, \dots, X_n > y) = 1 - (1 - y)^n, \quad 0 \le y \le 1
\\]

### PDF of \\( Y_n \\)

\\[
f_{Y_n}(y) = \frac{d}{dy}F_{Y_n}(y) = n(1 - y)^{n-1}, \quad 0 \le y \le 1
\\]

### Expected Value of \\( Y_n \\)

\\[
E[Y_n] = \int_0^1 y \cdot f_{Y_n}(y)\,dy = n \int_0^1 y(1 - y)^{n-1}\,dy = \frac{1}{n+1}
\\]

(by the Beta integral identity)

---

## Final Answers

### For \\( Z_n = \max(X_1,\dots,X_n) \\):

- CDF: \\( F_{Z_n}(z) = z^n \\)
- PDF: \\( f_{Z_n}(z) = n z^{n-1} \\)
- Expected value: \\( \boxed{E[Z_n] = \frac{n}{n+1}} \\)

### For \\( Y_n = \min(X_1,\dots,X_n) \\):

- CDF: \\( F_{Y_n}(y) = 1 - (1 - y)^n \\)
- PDF: \\( f_{Y_n}(y) = n(1 - y)^{n-1} \\)
- Expected value: \\( \boxed{E[Y_n] = \frac{1}{n+1}} \\)

---

## Reference

* [1] [Wikipedia: Order statistics](https://en.wikipedia.org/wiki/Order_statistic#Order_statistics_from_the_uniform_distribution)