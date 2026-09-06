---
layout: post
title: "Box Packing Puzzle: Bricks in a Cube"
date: 2025-05-13
category: quantitative interview
---

> Can you fit **53 bricks**, each of size **1×1×4**, into a **6×6×6** cube?

This spatial puzzle blends volume computation with parity and tiling logic. Let's break it down.

<iframe src="{{ site.baseurl }}/assets/box_packing_brain_teaser.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

### Step 1: Volume Check

- Cube volume: \\(6 × 6 × 6 = 216\\) unit cubes
- Each brick occupies: \\(1 × 1 × 4 = 4\\) unit cubes
- 53 bricks cover: \\(53 × 4 = 212\\) unit cubes

So, the total volume used would be **212**, leaving exactly **4 unit cubes empty**.

**At first glance, this seems possible.**

### Step 2: The Clever Coloring

To prove it's impossible, we use a special coloring scheme. 
Instead of coloring individual \\(1×1×1\\) cubes, imagine dividing the \\(6×6×6\\) cube into **27 smaller \\(2×2×2\\) sub-cubes**. 

Now, color these 27 sub-cubes in a 3D checkerboard pattern (alternating Black and White). 
Since 27 is an odd number, there won't be an equal amount of Black and White sub-cubes. Let's say we end up with:
- **14 Black sub-cubes** 
- **13 White sub-cubes**

Since each sub-cube contains exactly 8 unit cubes, our entire \\(6×6×6\\) cube has:
- \\(14 × 8 = \mathbf{112}\\) Black unit cubes
- \\(13 × 8 = \mathbf{104}\\) White unit cubes

### Step 3: Brick Coverage Parity

Now, think about placing a single \\(1×1×4\\) brick anywhere in this grid. 
Along its length, the axis is divided into three 2-unit segments (the sub-cubes). A brick of length 4 must cover 4 consecutive units.
It can either align perfectly with two segments (taking 2 units from each), or it can sit in the middle (taking 1 unit from the first segment, 2 from the middle, and 1 from the third).

Because the alternating sub-cubes have opposite colors, the outer segments in the middle scenario share the *same* color. 
- Aligned: 2 Black, 2 White.
- Middle: 1 Black + 2 White + 1 Black = 2 Black, 2 White.

Therefore, no matter where it's placed, **every single brick covers exactly 2 Black and 2 White unit cubes.**

### Step 4: The Contradiction

If we were to pack **53 bricks**, we would need:
- \\(53 × 2 = \mathbf{106}\\) Black unit cubes
- \\(53 × 2 = \mathbf{106}\\) White unit cubes

But look at our cube: **there are only 104 White unit cubes available!** 

Since 106 > 104, it is mathematically impossible to fit 53 bricks into the cube.

## Final Answer

**No**, you **cannot** pack 53 bricks of size 1×1×4 into a 6×6×6 cube.

# Reference

* [1] [Brain Teaser 10: Box Packing](https://medium.com/@shelvia1039/brain-teaser-10-box-packing-d480769eb3f1)
