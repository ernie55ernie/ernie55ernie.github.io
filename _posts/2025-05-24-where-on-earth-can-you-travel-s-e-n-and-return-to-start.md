---
layout: post
title: "Where on Earth Can You Travel S–E–N and Return to Start?"
date: 2025-05-24
category: quantitative interview
---

### The Puzzle

You're standing on a **perfectly spherical Earth**. You:

1. Travel **1 mile south**
2. Then **1 mile east**
3. Then **1 mile north**

...and you end up **exactly where you started**.

If you’re **not at the North Pole**, where else could you possibly be?
<iframe src="{{ site.baseurl }}/assets/where_else_can_you_start_besides_the_north_pole.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

---

## Solution 1: The Obvious Answer — The North Pole

If you start at the **North Pole**:

- Going 1 mile **south** puts you on a circle of latitude exactly 1 mile from the pole.
- Going 1 mile **east** moves you along that circle (your distance from the pole remains 1 mile).
- Going 1 mile **north** takes you straight back, because **all paths heading north converge at the North Pole**.

That’s the well-known solution.

---

## But You're *Not* at the North Pole?

There are **infinitely many** such points near the **South Pole**!

---

## Generalized Solution

Suppose there exists a parallel **circle of latitude** near the **South Pole** where the **eastward circumference is**:

\\[
\frac{1}{k} \text{ miles for some integer } k \ge 1
\\]

Then going 1 mile east will take you **around the circle exactly \\( k \\) times**, returning you to your original east-point.

If you're 1 mile **north** of that circle, then:

1. Going south puts you on that circle
2. Going east wraps around \\( k \\) times and returns you
3. Going north brings you back to the start

These circles lie increasingly close to the **South Pole**, and there are **infinitely many such latitudes**.

---

## Final Answer

Besides the **North Pole**, your starting point could be **1 mile north of any circle of latitude near the South Pole** where traveling 1 mile east makes a full \\( k \\)-loop around the Earth for any integer \\( k \ge 1 \\).

---

## Reference

* [1] [Did you solve it? Are you smart enough to work for Elon Musk?](https://www.theguardian.com/science/2022/jun/27/did-you-solve-it-are-you-smart-enough-to-work-for-elon-musk)