---
layout: post
title: "Probability of No Two Consecutive Heads in n Coin Tosses"
date: 2025-05-27
category: quantitative interview
---

## Problem

You toss a **fair coin** \\( n \\) times. What is the probability that **no two consecutive heads** appear in the sequence?

---

### Step 1: Count Valid Sequences

Let \\( a_n \\) be the number of valid length-\\( n \\) sequences with **no consecutive heads**.

We define a recurrence:

- Base cases:
  \\[
  a_0 = 1 \quad (\text{empty sequence})
  \\]
  \\[
  a_1 = 2 \quad (\text{H or T})
  \\]

- Recursive case:
  \\[
  a_n = a_{n-1} + a_{n-2}
  \\]

**Why?**
- If the \\( n \\)-th toss is T: append T to any valid \\( (n-1) \\)-sequence → \\( a_{n-1} \\)
- If the \\( n \\)-th toss is H: must be preceded by T → append TH to valid \\( (n-2) \\)-sequence → \\( a_{n-2} \\)

So the total number of valid sequences is:

\\[
a_n = \text{Fibonacci}(n+2)
\\]

---

### Step 2: Total Possible Sequences

Each coin toss has 2 outcomes, so total sequences of length \\( n \\):

\\[
2^n
\\]

---

### Step 3: Final Probability

\\[
P(\text{no two heads in a row}) = \frac{a_n}{2^n} = \frac{\text{Fibonacci}(n+2)}{2^n}
\\]

---

### Examples

- \\( n = 1 \\): \\( a_1 = 2 \\), \\( 2^1 = 2 \\) → \\( \frac{2}{2} = 1 \\)
- \\( n = 2 \\): \\( a_2 = 3 \\), \\( 2^2 = 4 \\) → \\( \frac{3}{4} \\)
- \\( n = 3 \\): \\( a_3 = 5 \\), \\( 2^3 = 8 \\) → \\( \frac{5}{8} \\)

---

## Conclusion

The probability that no two consecutive heads appear in \\( n \\) fair coin tosses is:

\\[
\boxed{P_n = \frac{F_{n+2}}{2^n}}
\\]

where \\( F_k \\) is the \\( k \\)-th Fibonacci number.

# Reference

* [1] [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)