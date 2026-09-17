---
layout: post
title: "The Meeting Problem: Will They Overlap?"
date: 2025-05-20
category: quantitative interview
---

### The Setup

Two people (say, bankers) independently arrive at a train station at a time **uniformly at random** between 5:00 AM and 6:00 AM. Upon arrival, each waits **exactly 5 minutes** before departing.

**Question:** What is the probability that their waiting intervals **overlap** so that they actually meet?

---

## Visualizing the Problem

Let:

- \\( X \\): arrival time of person A (in minutes after 5:00 AM)
- \\( Y \\): arrival time of person B (also in minutes after 5:00 AM)

Each variable \\( X, Y \\) is uniformly distributed on the interval \\( [0, 60] \\).

They **meet** if their arrival times are within 5 minutes of each other:

\\[
|X - Y| \leq 5
\\]

---

## Geometric Probability Approach

We represent all possible arrival pairs \\( (X, Y) \\) as points in the 60×60 square.

The region where \\( |X - Y| \leq 5 \\) forms a band of width 10 along the diagonal.

### Total Area:

\\[
60 \times 60 = 3600
\\]

### Favorable Area (meeting zone):

The area where they **do not** meet is where \\( |X - Y| > 5 \\). This region consists of two right triangles, each with a base and height of 55.

\\[
\text{Area outside band} = 2 \times \frac{1}{2}(55)^2 = 3025
\\]

\\[
\text{Area where } |X - Y| \leq 5 = 3600 - 3025 = 575
\\]

So:

\\[
P(\text{meeting}) = \frac{\text{favorable area}}{\text{total area}} = \frac{575}{3600} = \boxed{\frac{23}{144}} \approx 0.1597
\\]

---

## Final Answer

\\[
\boxed{\frac{23}{144}}
\\]

## Reference

* [1] [Probability of meeting](https://math.stackexchange.com/questions/2498359/probability-of-meeting)
