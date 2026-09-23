---
layout: post
title: "Shortest Path for an Ant in a 10×10×10 Cube"
date: 2025-05-27
category: quantitative interview
---

## Problem

An ant is at one corner of a \\( 10 \times 10 \times 10 \\) cube-shaped room and wants to reach the **opposite corner**, traveling **only along the walls** (not diagonally through space). What is the **shortest path length** it can take?

<iframe src="{{ site.baseurl }}/assets/cube_shortest_path_visualization.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

---

### Key Insight

Though the room is 3D, the ant walks **only along the surfaces** of the cube. We "unfold" the cube's walls onto a **2D plane**, where the ant's path becomes a straight line.

---

### Unfolding the Cube

Imagine unfolding two adjacent faces (e.g., the floor and one wall) into a flat rectangle of size:

\\[
10 \times (10 + 10) = 10 \times 20
\\]

Now the ant moves from one corner to the diagonally opposite corner of this rectangle.

---

### Apply Pythagoras

The shortest path is the diagonal:

\\[
\text{Distance} = \sqrt{10^2 + 20^2} = \sqrt{100 + 400} = \sqrt{500} = \boxed{10\sqrt{5}} \approx 22.36
\\]

---

## Conclusion

The shortest path the ant can take along the surfaces of a \\( 10 \times 10 \times 10 \\) room is:

\\[
\boxed{10\sqrt{5}}
\\]

# Reference

* [1] [What Is the Shortest Path an Ant Can Take Across a Cube?](https://www.physicsforums.com/threads/what-is-the-shortest-path-an-ant-can-take-across-a-cube.820987/)