---
layout: post
title: "Probability That a Cube Ends in 11"
date: 2025-05-19
category: quantitative interview
---

We are given a uniform random integer \\( x \\) from \\( 1 \\) to \\( 10^{12} \\), and are asked to compute the probability that the decimal representation of \\( x^3 \\) ends in the digits "11".

This is equivalent to determining the number of integers \\( x \in \{1, 2, \dots, 10^{12}\} \\) for which

\\[
x^3 \equiv 11 \pmod{100}
\\]

and dividing that count by \\( 10^{12} \\).

## Modular Reduction Strategy

We aim to solve:

\\[
x^3 \equiv 11 \pmod{100}
\\]

Since \\( 100 = 4 \times 25 \\), we solve this congruence modulo 4 and modulo 25 separately, and then combine the solutions using the Chinese Remainder Theorem (CRT).

### Step 1: Modulo 4

We examine all residues \\( x \mod 4 \\):

- \\( 0^3 \equiv 0 \mod 4 \\)
- \\( 1^3 \equiv 1 \mod 4 \\)
- \\( 2^3 \equiv 8 \equiv 0 \mod 4 \\)
- \\( 3^3 \equiv 27 \equiv 3 \mod 4 \\)

So the possible cube residues mod 4 are \\( \{0, 1, 3\} \\). Thus, \\( x^3 \equiv 11 \equiv 3 \mod 4 \\) implies:

\\[
x \equiv 3 \mod 4
\\]

### Step 2: Modulo 25

We need:

\\[
x^3 \equiv 11 \mod 25
\\]

Try small values:

- \\( 1^3 = 1 \\)
- \\( 2^3 = 8 \\)
- \\( 3^3 = 27 \\)
- ...
- \\( 16^3 = 4096 \equiv 4096 \mod 25 = 4096 - 25 \times 163 = 4096 - 4075 = 21 \\)
- \\( 17^3 = 4913 \equiv 4913 - 25 \times 196 = 4913 - 4900 = 13 \\)
- \\( 18^3 = 5832 \equiv 5832 - 5825 = 7 \\)
- \\( 19^3 = 6859 \equiv 6859 - 6825 = 34 \mod 25 = 9 \\)
- \\( 20^3 = 8000 \equiv 8000 \mod 25 = 0 \\)
- \\( 21^3 = 9261 \equiv 9261 - 9250 = 11 \\)

Success! \\( x \equiv 21 \mod 25 \\) is a solution.

Verify uniqueness:
Since the cube map modulo 25 is not injective, we check if there are other solutions.

Try:
- \\( x = 71 \\): then \\( x = 25 \cdot 2 + 21 = 71 \\)
- \\( x^3 = 71^3 = (70 + 1)^3 = 343000 + 3 \cdot 4900 + 3 \cdot 70 + 1 = 357911 \\)
- Ends in 11 ✔️

So \\( x \equiv 21 \mod 25 \\) yields \\( x^3 \equiv 11 \mod 100 \\) if and only if \\( x \equiv 3 \mod 4 \\)

Use CRT to combine:

Find \\( x \mod 100 \\) such that:

- \\( x \equiv 3 \mod 4 \\)
- \\( x \equiv 21 \mod 25 \\)

Let \\( x = 25k + 21 \\). Plug into first congruence:

\\[
25k + 21 \equiv 3 \mod 4 \Rightarrow k \equiv 2 \mod 4
\\]

So \\( k = 4m + 2 \\), thus:

\\[
x = 25k + 21 = 25(4m + 2) + 21 = 100m + 71
\\]

Therefore, all solutions are:

\\[
x \equiv 71 \mod 100
\\]

## Final Probability

Among \\( 1 \\) to \\( 10^{12} \\), every 100th number satisfies \\( x \equiv 71 \mod 100 \\). Hence, there are:

\\[
\left\lfloor \frac{10^{12}}{100} \right\rfloor = 10^{10}
\\]

such integers, and the probability is:

\\[
\frac{10^{10}}{10^{12}} = \boxed{\frac{1}{100}}
\\]

## Reference

* [1] [Probability that cubic of integer ends with 11](https://math.stackexchange.com/questions/3988843/probability-that-cubic-of-integer-ends-with-11)
