---
layout: post
title: "Color Consensus: Expected Steps to Uniformity"
date: 2025-05-21
category: quantitative interview
---

### Problem Statement

You begin with a box containing \\( n \\) balls, each uniquely colored (i.e., \\( n \\) distinct colors). At each step:

1. Select two balls uniformly at random (ordered selection).
2. Repaint the first ball to match the color of the second.
3. Return both balls to the box.

This process repeats until all balls share the same color.

**Question:** What is the expected number of steps required to reach this monochromatic state?

---

### Solution

This problem is analogous to the **Moran process** in population genetics, where individuals reproduce and replace others, leading to fixation of a single type. In our scenario, the "types" are the colors of the balls.

In the standard Moran process with a population size of \\( n \\), the expected time to fixation (i.e., all individuals sharing the same type) is:

\\[
t^* = n(n - 1)
\\]

However, in our process, when both selected balls are of the same color, repainting has no effect. The probability that both selected balls are of the same color is \\( \frac{1}{n} \\), since each ball has an equal chance of being any color, and there are \\( n \\) colors.

Therefore, the expected number of **effective** steps (i.e., steps that change the state) is:

\\[
t = (1 - \frac{1}{n}) \cdot t^* = (1 - \frac{1}{n}) \cdot n(n - 1) = (n - 1)^2
\\]

Thus, the expected number of steps until all balls are the same color is:

\\[
\boxed{(n - 1)^2}
\\]

---

### Reference

* [1] [Compute the expectation of steps making $n$ different balls the same](https://math.stackexchange.com/questions/1214293/compute-the-expectation-of-steps-making-n-different-balls-the-same)
