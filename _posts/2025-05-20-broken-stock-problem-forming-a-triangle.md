---
layout: post
title: "Broken Stick Problem: Forming a Triangle"
date: 2025-05-20
category: quantitative interview
---

### The Puzzle

You take a stick of **unit length** and break it at **two points**, chosen **uniformly at random** and independently along the stick. This produces **three segments**.

**Question:** What is the probability that these three segments can form a **triangle**?

---

## Triangle Inequality Condition

Let the lengths of the three resulting segments be:

- \\( a \\), \\( b \\), and \\( c \\), with \\( a + b + c = 1 \\)

To form a triangle, the sum of the lengths of **any two sides** must be **greater** than the third:

\\[
a + b > c,\quad b + c > a,\quad c + a > b
\\]

Using \\( a + b + c = 1 \\), these inequalities become:

\\[
a < \frac{1}{2},\quad b < \frac{1}{2},\quad c < \frac{1}{2}
\\]

So **each piece must be less than 1/2** in length.

---

## Modeling the Cuts

Let the two cut points \\( X, Y \\) be chosen uniformly and independently from \\( [0,1] \\). We can assume \\( 0 < X < Y < 1 \\) by ordering them.

Then the lengths of the segments are:

- \\( L_1 = X \\)
- \\( L_2 = Y - X \\)
- \\( L_3 = 1 - Y \\)

We seek the probability that all of these are less than \\( \frac{1}{2} \\).

---

## Geometric Probability

This corresponds to the area of the region in the unit square \\( [0,1]^2 \\) where:

\\[
0 < X < Y < 1,\quad \text{and } X < \frac{1}{2},\quad Y - X < \frac{1}{2},\quad 1 - Y < \frac{1}{2}
\\]

This region forms a triangle within the unit square with area:

\\[
\boxed{\frac{1}{4}}
\\]

---

## Final Answer

\\[
\boxed{\frac{1}{4}}
\\]

So, there is a 25% chance the three segments can form a triangle.

## Reference

* [1] [Probability of forming a triangle - solution seems to be wrong?](https://math.stackexchange.com/questions/3655437/probability-of-forming-a-triangle-solution-seems-to-be-wrong)
