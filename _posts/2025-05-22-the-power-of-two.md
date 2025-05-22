---
layout: post
title: "The power of two"
date: 2025-05-22
category: quantitative interview
---

### 1. Power of 2

**Question**: How do you determine whether a given positive integer \\( x \\) is a power of 2?

**Answer**:

A number \\( x > 0 \\) is a power of 2 **if and only if** it has **exactly one bit set** in binary.

```python
def is_power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0
```

**Why it works**:
For a power of 2, say \\( x = 2^k \\), its binary is a 1 followed by \\( k \\) zeros. Subtracting 1 flips all bits after the leading 1. The bitwise AND of the two is zero.

---

### 2. Multiply by 7 Without Multiplication

**Question**: Multiply an integer \\( x \\) by 7 without using `*`.

**Answer**:

Use addition and bit-shifting:

```python
def multiply_by_7(x):
    return (x << 3) - x  # 8x - x = 7x
```

**Explanation**:

* `x << 3` computes \\( 8x \\)
* Subtracting \\( x \\) gives \\( 7x \\)

---

### 3. Probability Simulation with a Fair Coin

**Question**: Given a fair coin, simulate an event with arbitrary probability \\( 0 < p < 1 \\).

**Answer**: Use the **probability tree** method:

* Generate uniform \\( U \in [0,1] \\) using coin flips (binary digits)
* Accept if \\( U < p \\), else reject

Alternatively, if \\( p \\) is rational, say \\( p = \frac{m}{n} \\):

```python
import random

def simulate_p(m, n):
    return random.randint(1, n) <= m
```

This simulates probability \\( \frac{m}{n} \\) using only fair coin–based random integers.

---

### 4. Poisoned Wine with 10 Mice

**Question**: You have 1000 wine bottles, one poisoned. You have 10 mice and 20 hours. Poison kills **exactly** at 18 hours. How do you find the poisoned bottle?

**Answer**:

* Label bottles \\( 0 \\) to \\( 999 \\)
* Use each mouse to represent one binary digit (10 bits total)
* For each bottle:

  * Convert its number to 10-bit binary
  * If bit \\( i \\) is 1, give a drop to mouse \\( i \\)

After 18 hours:

* The dead mice correspond to the 1s in the poisoned bottle’s binary label
* Read the set of dead mice as a binary number: that’s the poisoned bottle!

**Efficient and guaranteed**.

---

## Summary

| Problem                  | Key Idea                                   |
| ------------------------ | ------------------------------------------ |
| Power of 2               | \\( x > 0 \\) and \\( x & (x - 1) == 0 \\) |
| Multiply by 7            | \\( (x << 3) - x \\)                       |
| Arbitrary Probability    | Simulate \\( U < p \\) via coin flips      |
| Poisoned Wine (1000, 10) | Use binary coding and 10 mice as bits      |

---

## Reference

* [1] [Bit manipulation tricks – Hacker’s Delight](https://graphics.stanford.edu/~seander/bithacks.html)
* [2] [Puzzle 19 | (Poison and Rat)](https://www.geeksforgeeks.org/puzzle-19-poison-and-rat/)