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

We can elegantly solve this by looking at the process **backwards in time** using coalescent theory. 

Instead of tracking colors forward, track the "ancestor" of each ball. When the first ball is repainted to match the second, its lineage merges with the second ball's lineage. The game ends when all \\( n \\) balls trace back to a single common ancestor.

At any point, if there are \\( k \\) distinct lineages, a step will merge two of them if we select two balls belonging to these \\( k \\) lineages. Since we select two distinct balls uniformly at random (ordered selection without replacement), there are \\( n(n-1) \\) possible pairs. The number of pairs that result in two of the \\( k \\) lineages merging is \\( k(k-1) \\).

Thus, the probability of a merger in a single step is:

\\[
P_k = \frac{k(k-1)}{n(n-1)}
\\]

The expected number of steps to reduce the number of lineages from \\( k \\) to \\( k-1 \\) is the reciprocal of this probability:

\\[
E_k = \frac{n(n-1)}{k(k-1)}
\\]

To find the total expected time to reach 1 lineage from \\( n \\) lineages, we sum these expectations:

\\[
E[\text{Total Steps}] = \sum_{k=2}^{n} \frac{n(n-1)}{k(k-1)} = n(n-1) \sum_{k=2}^{n} \left( \frac{1}{k-1} - \frac{1}{k} \right)
\\]

The sum is a telescoping series:

\\[
\sum_{k=2}^{n} \left( \frac{1}{k-1} - \frac{1}{k} \right) = \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \dots + \left(\frac{1}{n-1} - \frac{1}{n}\right) = 1 - \frac{1}{n} = \frac{n-1}{n}
\\]

Multiplying this by \\( n(n-1) \\):

\\[
E[\text{Total Steps}] = n(n-1) \cdot \frac{n-1}{n} = (n-1)^2
\\]

Thus, the expected number of steps until all balls are the same color is:

\\[
\boxed{(n - 1)^2}
\\]

---

### Reference

* [1] [Compute the expectation of steps making $n$ different balls the same](https://math.stackexchange.com/questions/1214293/compute-the-expectation-of-steps-making-n-different-balls-the-same)
