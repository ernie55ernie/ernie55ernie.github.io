---
layout: post
title: "Why √2 Is Irrational: A Classic Proof"
date: 2025-05-18
category: quantitative interview
---

One of the earliest known proofs in number theory tackles this elegant question:

> **Problem:** Show that \\( \sqrt{2} \\) **cannot** be written as a ratio of two integers.  
> In other words, **prove that \\( \sqrt{2} \\) is irrational**.

---

## Step-by-Step Proof (By Contradiction)

### Step 1: Assume the Opposite

Suppose, for contradiction, that \\( \sqrt{2} \\) **is rational**.

Then we can write:

\\[
\sqrt{2} = \frac{a}{b}
\\]

where \\( a \\) and \\( b \\) are integers with **no common factors** (i.e., the fraction is in **lowest terms**).

---

### Step 2: Square Both Sides

\\[
\left(\frac{a}{b}\right)^2 = 2 \Rightarrow \frac{a^2}{b^2} = 2 \Rightarrow a^2 = 2b^2
\\]

So \\( a^2 \\) is **even**, which means \\( a \\) must also be **even** (since the square of an odd number is odd).

Let \\( a = 2k \\) for some integer \\( k \\).

---

### Step 3: Substitute Back

\\[
(2k)^2 = 2b^2 \Rightarrow 4k^2 = 2b^2 \Rightarrow b^2 = 2k^2
\\]

So \\( b^2 \\) is also even → \\( b \\) is **even**.

---

### Step 4: Contradiction

Now we’ve concluded that **both \\( a \\) and \\( b \\) are even**, which means they share a common factor of 2.

But that contradicts our assumption that \\( \frac{a}{b} \\) was in **lowest terms**.

---

## Final Answer

> \\( \sqrt{2} \\) **cannot** be expressed as a ratio of two integers.  
> Therefore, \\( \sqrt{2} \\) is **irrational**.

# Reference

* [1] [Irrational Numbers (Number Theory)](https://en.wikipedia.org/wiki/Square_root_of_2#Proofs_of_irrationality)
