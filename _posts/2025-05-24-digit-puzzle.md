---
layout: post
title: "Digit Puzzle: What’s Missing in 2^29?"
date: 2025-05-24
category: quantitative interview
---

## Digit Puzzle: What’s Missing in \\( 2^{29} \\)?

### The Puzzle

The number \\( 2^{29} \\) is a 9-digit number where **each digit appears exactly once**, except **one digit is missing**.

**Question:** Without computing \\( 2^{29} \\) directly, which digit is missing?

---

## Key Insight: Sum of Digits from 0–9

The sum of all digits from 0 through 9 is:

\\[
0 + 1 + 2 + \dots + 9 = \frac{9 \cdot 10}{2} = 45
\\]

If \\( 2^{29} \\) contains 9 distinct digits, then **one digit is missing** from the complete set \\( \{0,1,\dots,9\} \\).

If we can compute the **sum of the digits** of \\( 2^{29} \\), then the **missing digit** is:

\\[
45 - \text{sum of digits of } 2^{29}
\\]

---

## Step 1: Compute \\( 2^{29} \mod 9 \\)

The **digital root** or digit sum modulo 9 is congruent to the number modulo 9:

- \\( 2^3 = 8 \Rightarrow 2^6 = 64 \Rightarrow 2^9 = 512 \)
- But easier: \\( 2^6 = 64 \equiv 1 \mod 9 \\), so the cycle repeats every 6

Now:

\\[
29 \equiv 5 \mod 6 \Rightarrow 2^{29} \equiv 2^5 = 32 \equiv 5 \mod 9
\\]

So, the sum of the digits of \\( 2^{29} \\) must be congruent to 5 modulo 9.

---

## Step 2: Find Which Digit to Remove

Let’s subtract each digit from 45 and check which result is \\( \equiv 5 \mod 9 \\):

- \\( 45 - 0 = 45 \equiv 0 \mod 9 \\)
- \\( 45 - 1 = 44 \equiv 8 \mod 9 \\)
- \\( 45 - 2 = 43 \equiv 7 \mod 9 \\)
- \\( 45 - 3 = 42 \equiv 6 \mod 9 \\)
- \\( 45 - 4 = 41 \equiv \boxed{5} \mod 9 \\)
- ...

Only \\( 45 - 4 = 41 \equiv 5 \mod 9 \\)

---

## Final Answer

\\[
\boxed{4}
\\]

The missing digit in \\( 2^{29} \\) is **4**.

---

## Reference

* [1] [Digit Sum and Modulo 9 Properties – Wikipedia](https://en.wikipedia.org/wiki/Digital_root)