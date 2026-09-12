---
layout: post
title: "N Points on a Circle: When Do They Fit in a Semicircle?"
date: 2025-05-18
category: quantitative interview
---

Here’s a beautiful geometric probability puzzle:

> **Problem:** Place \\( N \\) points **independently and uniformly at random** on the circumference of a circle.  
> What is the probability that **all \\( N \\) points** lie within some **semicircle** (i.e., an arc of length \\(180^\circ\\))?

<iframe src="{{ site.baseurl }}/assets/probability_that_n_random_points_lie_in_some_semicircle.html" width="100%" height="900px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

---

## Step 1: Understand the Event

We ask: What is the chance that all \\( N \\) random points can be "seen" within a **180° arc**?

Visually, this means you could take a semicircle "window" and rotate it around the circle to include all the points.

---

## Step 2: Strategy

For all \\( N \\) points to fit inside a semicircle, exactly one of the points must act as the "starting" or "leading" edge of that semicircle (e.g., the counter-clockwise most point).

Let's calculate the probability that a specific point, say point A, is this leading edge.
For A to be the leading edge, all the other \\(N-1\\) points must fall within the \\(180^\circ\\) arc immediately following point A.

Since the points are placed independently and uniformly, the probability of any given point landing in that specific \\(180^\circ\\) arc is \\(1/2\\). Therefore, the probability that **all** \\(N-1\\) remaining points fall into this arc is \\((1/2)^{N-1}\\).

---

## Step 3: Core Result

Since any of the \\( N \\) points could be the leading edge, and these \\( N \\) events are mutually exclusive (probability of a tie is 0), we can add their probabilities together.

The probability that \\( N \\) points all lie in some semicircle is:

\\[
P(N) = N \times \left(\frac{1}{2}\right)^{N-1} = \frac{N}{2^{N-1}}
\\]

### Examples:

- \\( P(2) = \frac{2}{2^1} = 1 \\)
- \\( P(3) = \frac{3}{4} \\)
- \\( P(4) = \frac{4}{8} = \frac{1}{2} \\)
- \\( P(5) = \frac{5}{16} \\)

---

## Final Answer

> The probability that \\( N \\) random points lie within **some semicircle** is:
>
> \\[
> \boxed{\frac{N}{2^{N-1}}}
> \\]

# Reference

* [1] [Probability that n points on a circle are in one semicircle](https://math.stackexchange.com/questions/325141/probability-that-n-points-on-a-circle-are-in-one-semicircle)