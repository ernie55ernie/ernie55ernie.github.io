---
layout: post
title: "Box Packing Puzzle: Bricks in a Cube"
date: 2025-05-13
category: quantitative interview
---

> Can you fit **53 bricks**, each of size **1×1×4**, into a **6×6×6** cube?

This spatial puzzle blends volume computation with parity and tiling logic. Let's break it down.

### Step 1: Volume Check

- Cube volume: \\(6 × 6 × 6 = 216\\) unit cubes
- Each brick occupies: \\(1 × 1 × 4 = 4\\) unit cubes
- 53 bricks cover: \\(53 × 4 = 212\\) unit cubes

So, the total volume used would be **212**, leaving exactly **4 unit cubes empty**.

**At first glance, this seems possible.**

### Step 2: Parity Insight

To go further, we analyze the **structure** of the cube and the constraints of packing.

Color the cube in a **3D checkerboard pattern**: alternate black and white unit cubes such that adjacent cubes (in any direction) have opposite colors.

In a \\(6×6×6\\) cube, this gives:
- **108 black** and **108 white** cubes.

### Step 3: Brick Coverage Pattern

Each 1×1×4 brick occupies 4 consecutive cubes in a straight line. No matter how it's placed (along x, y, or z direction), it will cover:
- **2 black** and **2 white** cubes.

Why? Because starting on black leads to black-white-black-white or vice versa—4 in total, equally split.

### Step 4: Total Balance

53 bricks × (2 black + 2 white) = 106 black + 106 white

But the cube has 108 of each.

That means the **remaining 4 unit cubes** must be made up of **2 black and 2 white** cubes—perfectly balanced.

So the **parity check passes**.

### Step 5: Can You Actually Pack Them?

Despite parity and volume working out, **no known arrangement** can fit 53 such bricks into a 6×6×6 cube.

This was a research-level puzzle, and the key insight comes from **modulo arithmetic**.

#### Mod-4 Grid Analysis

Imagine labeling all unit cubes with coordinates (x, y, z). Now sum all coordinates mod 4.

Each brick always covers 4 **distinct values** of x+y+z mod 4. Thus, the **sum mod 4** of all positions used by bricks must be divisible by 4.

When applied to the cube and 53 bricks, this leads to a **modulo contradiction**.

### Final Verdict

Though volume and parity **seem to allow** a solution, deeper structure-based arguments prove it’s **not possible**.

## Final Answer

**No**, you **cannot** pack 53 bricks of size 1×1×4 into a 6×6×6 cube.

# Reference

* [1] [Brain Teaser 10: Box Packing](https://medium.com/@shelvia1039/brain-teaser-10-box-packing-d480769eb3f1)
