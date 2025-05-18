---
layout: post
title: "N Points on a Circle: When Do They Fit in a Semicircle?"
date: 2025-05-18
category: quantitative interview
---

Here’s a beautiful geometric probability puzzle:

> **Problem:** Place \\( N \\) points **independently and uniformly at random** on the circumference of a circle.  
> What is the probability that **all \\( N \\) points** lie within some **semicircle** (i.e., an arc of length \\(180^\circ\\))?

---

## Step 1: Understand the Event

We ask: What is the chance that all \\( N \\) random points can be "seen" within a **180° arc**?

Visually, this means you could take a semicircle "window" and rotate it around the circle to include all the points.

---

## Step 2: Strategy

We fix one of the points (say, point A) to be at angle \\(0^\circ\\) without loss of generality—because the circle is rotationally symmetric.

Then the rest of the \\(N-1\\) points are placed uniformly at random on the circle.

The configuration **fits inside a semicircle** **if and only if** all the other \\(N-1\\) points fall within an arc of \\(180^\circ\\) starting from point A.

We now ask: What's the probability that the angular **spread** between the largest and smallest of the \\(N\\) points is \\( \leq 180^\circ \\)?

---

## Step 3: Core Result

The probability that \\( N \\) points all lie in some semicircle is:

\\[
P(N) = \frac{N}{2^{N-1}}
\\]

### Examples:

- \\( P(2) = \frac{2}{2^1} = 1 \\)
- \\( P(3) = \frac{3}{4} \\)
- \\( P(4) = \frac{4}{8} = \frac{1}{2} \\)
- \\( P(5) = \frac{5}{16} \\)

This formula emerges from symmetry and combinatorics:  
For each point, consider whether the other \\(N - 1\\) points fall within a half-circle arc originating at that point.

---

## Final Answer

> The probability that \\( N \\) random points lie within **some semicircle** is:
>
> \\[
> \boxed{\frac{N}{2^{N-1}}}
> \\]

# Reference

* [1] [Probability that n points on a circle are in one semicircle](https://math.stackexchange.com/questions/325141/probability-that-n-points-on-a-circle-are-in-one-semicircle6)