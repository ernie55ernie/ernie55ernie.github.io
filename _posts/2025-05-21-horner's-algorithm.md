---
layout: post
title: "Efficient Polynomial Evaluation with Horner’s Rule"
date: 2025-05-21
category: quantitative interview
---

### Problem

Given a polynomial with coefficients \\( A_0, A_1, \dots, A_n \\) and an input value \\( x \\), evaluate:

\\[
y = A_0 + A_1 x + A_2 x^2 + \cdots + A_n x^n
\\]

**Goal:** Compute this efficiently using only \\( O(n) \\) operations.

---

## Horner’s Algorithm

Rather than computing each power \\( x^k \\) explicitly, Horner’s method rewrites the polynomial as:

\\[
y = A_0 + x(A_1 + x(A_2 + \cdots + x(A_{n-1} + x A_n) \cdots ))
\\]

This nested form enables linear-time evaluation with minimal multiplications.

---

### Python Implementation

```python
def horner(coeffs, x):
    result = 0
    for coeff in reversed(coeffs):
        result = result * x + coeff
    return result
```

**Example Usage:**

```python
# Polynomial: 2 + 3x + 5x^2 at x = 4
coeffs = [2, 3, 5]  # A_0 + A_1*x + A_2*x^2
x = 4
print(horner(coeffs, x))  # Output: 2 + 3*4 + 5*4^2 = 2 + 12 + 80 = 94
```

---

## Time Complexity

* **Time**: \\( O(n) \\) for a polynomial of degree \\( n \\)
* **Space**: \\( O(1) \\) extra space

---

## Final Takeaway

**Horner's Rule** is the gold standard for fast, stable polynomial evaluation and underpins numerous numerical algorithms.

---

## Reference

* [1] [Horner's Method – Wikipedia](https://en.wikipedia.org/wiki/Horner%27s_method)