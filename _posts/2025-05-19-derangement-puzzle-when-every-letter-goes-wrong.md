---
layout: post
title: "Derangement Puzzle: When Every Letter Goes Wrong"
date: 2025-05-19
category: quantitative interview
---

This classic probability puzzle takes on a new face:

> You have **5 firms** and **5 personalized cover letters**, one for each.  
> The letters are **randomly placed** into the envelopes (each permutation equally likely).  
>
> **Question:** What is the probability that **no letter** ends up in the correct envelope?

This is a textbook case of the **derangement problem**—also known as the **hat-check puzzle**.

---

## Step 1: Total Permutations

There are:

\\[
5! = 120 \text{ total permutations}
\\]

Each represents a way to stuff the 5 letters into 5 envelopes.

---

## Step 2: Count Derangements

A **derangement** is a permutation with **no fixed points** (i.e., no item is in its correct position).

The number of derangements of \\(n\\) items is denoted by \\( !n \\), and for \\(n = 5\\):

\\[
!5 = 44
\\]

This can be computed by:

\\[
!n = n! \left(1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \cdots + (-1)^n \frac{1}{n!} \right)
\\]

For \\(n = 5\\):

\\[
!5 = 120 \left(1 - 1 + \frac{1}{2} - \frac{1}{6} + \frac{1}{24} - \frac{1}{120} \right) = 120 \times \frac{44}{120} = 44
\\]

---

## Step 3: Final Probability

\\[
P(\text{no letter in correct envelope}) = \frac{!5}{5!} = \frac{44}{120} = \boxed{\frac{11}{30}}
\\]

---

## Final Answer

> The probability that **none** of the 5 letters ends up in the correct envelope is:
>
> \\[
> \boxed{\frac{11}{30}}
> \\]

# Reference

* [1] [Derangement and Hat-Check Problem](https://en.wikipedia.org/wiki/Derangement)