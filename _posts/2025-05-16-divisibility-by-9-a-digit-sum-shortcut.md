---
layout: post
title: "Divisibility by 9: A Digit-Sum Shortcut"
date: 2025-05-16
category: quantitative interview
---

Here's a classic puzzle with a beautiful answer rooted in modular arithmetic:

> **Problem:** Devise a simple rule to test if any number is divisible by **9**, and **prove** why it works.

---

## The Rule

> A number is divisible by **9** **if and only if** the **sum of its digits** is divisible by 9.

For example:

- 729 → \\(7 + 2 + 9 = 18\\), and \\(18\\) is divisible by 9 → ✅
- 1234 → \\(1 + 2 + 3 + 4 = 10\\), and \\(10\\) is **not** divisible by 9 → ❌

But **why** does this work?

---

## Step-by-Step Proof (Base 10)

Let a number \\(N\\) be written in decimal as:

\\[
N = a_k \cdot 10^k + a_{k-1} \cdot 10^{k-1} + \cdots + a_1 \cdot 10 + a_0
\\]

We want to analyze \\(N \mod 9\\). Notice:

\\[
10 \equiv 1 \pmod{9},\quad 10^n \equiv 1^n \equiv 1 \pmod{9}
\\]

So:

\\[
N \equiv a_k + a_{k-1} + \cdots + a_1 + a_0 \pmod{9}
\\]

That is, \\(N\\) and the **sum of its digits** are congruent modulo 9.

---

## Therefore:

- \\(N \equiv \text{digit sum} \mod 9\\)
- So, \\(N \equiv 0 \mod 9 \iff \text{digit sum} \equiv 0 \mod 9\\)

---

## Final Answer

> A number is divisible by **9** if and only if the **sum of its digits** is divisible by **9**.

# Reference

* [1] [Divisibility Rules and Modular Arithmetic](https://en.wikipedia.org/wiki/Divisibility_rule)
