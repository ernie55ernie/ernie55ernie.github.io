---
layout: post
title: "How Many Digits Does 125^100 Have Without Using Logarithms?"
date: 2025-05-29
category: quantitative interview
---

## Problem

Find the number of digits in the number \\( 125^{100} \\), **without** using values like \\( \log_{10} 2 \\) or \\( \log_{10} 5 \\).

---

## Step-by-Step Derivation

### 1. Rewrite the Expression

\\[
125^{100} = \left(\frac{1000}{8}\right)^{100} = \frac{1000^{100}}{2^{300}}
\\]

Now use the fact:

\\[
2^{10} = 1024 \Rightarrow 2^{300} = 1024^{30}
\\]

So:

\\[
125^{100} = \frac{1000^{100}}{1024^{30}} = \frac{1000^{70}}{(1.024)^{30}}
\\]

---

### 2. Estimate the Denominator

We approximate:

\\[
1 < (1.024)^{30} < 10
\\]

Hence:

\\[
\frac{1000^{70}}{10} < 125^{100} < 1000^{70}
\\]

Since \\( 1000^{70} = 10^{210} \\), we obtain:

\\[
10^{209} < 125^{100} < 10^{210}
\\]

---

### 3. Count the Digits

The number of digits of a positive integer \\( N \\) is:

\\[
\lfloor \log_{10} N \rfloor + 1
\\]

Since:

\\[
125^{100} < 10^{210} \quad \text{and} \quad 125^{100} > 10^{209}
\\]

It follows:

\\[
\log_{10} (125^{100}) \in (209, 210)
\Rightarrow \lfloor \log_{10} (125^{100}) \rfloor = 209
\Rightarrow \text{Number of digits} = 209 + 1 = \boxed{210}
\\]

---

## Final Answer

\\[
\boxed{125^{100} \text{ has exactly } 210 \text{ digits.}}
\\]

# Reference

* [1] [How many digits are in 125^100](https://math.stackexchange.com/questions/2604337/how-many-digits-are-in-125100)