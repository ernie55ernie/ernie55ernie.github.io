---
layout: post
title: "Trailing Zeros in 100!: Factorial Fun"
date: 2025-05-13
category: quantitative interview
---

A classic number theory puzzle asks:

> **How many zeros are at the end of $100!$ when written in base 10?**

These trailing zeros come from **factors of 10** in the factorial. Each 10 comes from a factor pair of **2 and 5**. Since multiples of 2 are more frequent than multiples of 5, we only need to count how many times **5** appears as a factor.

## Step-by-Step Count

To count the number of factors of 5 in $100!$:

\[
\left\lfloor \frac{100}{5} \right\rfloor + \left\lfloor \frac{100}{25} \right\rfloor + \left\lfloor \frac{100}{125} \right\rfloor + \cdots
\]

Calculate:

- \(\left\lfloor \frac{100}{5} \right\rfloor = 20\)
- \(\left\lfloor \frac{100}{25} \right\rfloor = 4\)
- \(\left\lfloor \frac{100}{125} \right\rfloor = 0\)

### Total:  
\[
20 + 4 = 24
\]

## Final Answer

**There are 24 trailing zeros in \(100!\)**

This technique generalizes to finding the number of trailing zeros in any factorial.

# Reference

* [1] [Trailing Zeros in Factorials (Number Theory)](https://en.wikipedia.org/wiki/Trailing_zero#In_factorials)
