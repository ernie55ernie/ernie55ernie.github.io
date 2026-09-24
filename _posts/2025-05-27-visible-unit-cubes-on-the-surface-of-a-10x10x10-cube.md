---
layout: post
title: "Visible Unit Cubes on the Surface of a 10×10×10 Cube"
date: 2025-05-27
category: quantitative interview
---

## Problem

A \\( 10 \times 10 \times 10 \\) cube is made up of \\( 1000 \\) unit cubes. How many of these unit cubes are **visible on the outside**?

<iframe src="{{ site.baseurl }}/assets/visible_cubes_10x10x10.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

---

### Step 1: Total Number of Cubes

\\[
10 \times 10 \times 10 = 1000 \quad \text{unit cubes}
\\]

---

### Step 2: Hidden Interior Cubes

The cubes that are **not visible** are the ones fully inside the cube, not on any face.

These form an interior cube of size:

\\[
(10 - 2)^3 = 8^3 = 512
\\]

These are the cubes that are **not visible** from any side.

---

### Step 3: Visible Cubes

The visible unit cubes are all those **not fully enclosed**, i.e., those **not in the 8×8×8 cube**:

\\[
1000 - 512 = \boxed{488}
\\]

---

## Conclusion

There are \\( \boxed{488} \\) unit cubes visible on the surface of a \\( 10 \times 10 \times 10 \\) cube.

# Reference

* [1] [painted cube brain teaser. Alternative solutions](https://math.stackexchange.com/questions/654889/painted-cube-brain-teaser-alternative-solutions)
