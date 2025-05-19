---
layout: post
title: "Cubic Ending in 11"
date: 2025-05-19
category: quantitative interview
---

We are given a problem of modular arithmetic involving probability:

> Let \\( x \\) be chosen uniformly at random from the integers \\( 1 \\) through \\( 10^{12} \\). What is the probability that the decimal representation of \\( x^3 \\) ends in the digits “11”?

This is equivalent to computing:

\\[
\Pr(x^3 \equiv 11 \pmod{100}) = \frac{\#\{x \in \{1,\dots,10^{12}\} : x^3 \equiv 11 \pmod{100} \}}{10^{12}}
\\]

## Step 1: Reduce the Problem Modulo 100

We must determine how many integers \\( x \in \{1, \dots, 10^{12}\} \\) satisfy:

\\[
x^3 \equiv 11 \pmod{100}
\\]

By the Chinese Remainder Theorem, we split this into two congruences:

- \\( x^3 \equiv 11 \pmod{4} \\)
- \\( x^3 \equiv 11 \pmod{25} \\)

## Step 2: Solve \\( x^3 \equiv 11 \pmod{4} \\)

Compute all cubes modulo 4:

- \\( 0^3 = 0 \\)
- \\( 1^3 = 1 \\)
- \\( 2^3 = 8 \equiv 0 \\)
- \\( 3^3 = 27 \equiv 3 \\)

So cube residues mod 4 are {0, 1, 3}. Since 11 ≡ 3 mod 4, this is possible.

## Step 3: Solve \\( x^3 \equiv 11 \pmod{25} \\)

Try all residues mod 25 (or use computational aid). Only one solution exists:

\\[
x \equiv 21 \pmod{25} \Rightarrow x^3 \equiv 11 \pmod{25}
\\]

## Step 4: Use Chinese Remainder Theorem

We want \\( x \equiv a \pmod{100} \\) such that:

- \\( x^3 \equiv 3 \pmod{4} \\)
- \\( x \equiv 21 \pmod{25} \\)

We check which \\( x \equiv 21 \pmod{25} \\) gives \\( x^3 \equiv 3 \pmod{4} \\). Try:

- \\( x = 21 \\Rightarrow x \equiv 1 \pmod{4}, x^3 \equiv 1 \pmod{4} \\)
- \\( x = 46 \\Rightarrow x \equiv 2 \pmod{4}, x^3 \equiv 0 \pmod{4} \\)
- \\( x = 71 \\Rightarrow x \equiv 3 \pmod{4}, x^3 \equiv 3 \pmod{4} \\) ✅

So only \\( x \equiv 71 \pmod{100} \\) satisfies \\( x^3 \equiv 11 \pmod{100} \\).

## Step 5: Count the Solutions

In \\( 1 \leq x \leq 10^{12} \\), every 100 integers will contain exactly one that satisfies \\( x \equiv 71 \pmod{100} \\).

So there are:

\\[
\frac{10^{12}}{100} = 10^{10}
\\]

satisfying values. Therefore, the probability is:

\\[
\frac{10^{10}}{10^{12}} = \boxed{\frac{1}{100}}
\\]

## Final Answer

\\[
\boxed{\frac{1}{100}}
\\]

# Reference

* [1] [Probability that cubic of integer ends with 11](https://math.stackexchange.com/questions/3988843/probability-that-cubic-of-integer-ends-with-11)
