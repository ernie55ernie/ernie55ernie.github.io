---
layout: post
title: "Can Mulder Escape the Alien? A Circular Pursuit Problem"
date: 2025-05-28
category: quantitative interview
---

## Problem

Mulder is imprisoned in a **circular field** of radius \\( R \\), and an alien—**4 times faster**—is constrained to the **perimeter**. If Mulder reaches an unguarded point on the fence, he can instantly escape. Can he do it?

---

## Variables

- Let \\( v \\): Mulder’s speed
- Alien’s speed: \\( 4v \\)
- \\( C \\): center of the circle
- \\( A \\): alien’s initial position
- \\( M \\): Mulder’s current position inside the circle
- \\( x \\): the fraction of radius \\( R \\) that Mulder is from center toward the escape point \\( P \\)

---

## Strategy Overview

1. **Initial Phase**: Mulder spirals or moves inside the circle to **deceive the alien**, maintaining a central position where the alien must guess his trajectory.
2. **Escape Preparation**: Mulder moves to a point \\( M \\) that is **closer to the perimeter**, precisely at distance \\( xR \\) from center \\( C \\), along the line connecting \\( A \\) and the center.
3. **Straight Run**: Once \\( M, C, A \\) are collinear with \\( C \\) between \\( M \\) and \\( A \\), Mulder **sprints toward the point \\( P \\)** on the perimeter opposite the alien’s position.

---

## Timing Condition

Mulder's run from \\( M \\) to \\( P \\):  
\\[
\text{Time}_M = \frac{(1 - x)R}{v}
\\]

Alien’s run from \\( A \\) to \\( P \\) along the perimeter:  
\\[
\text{Time}_A = \frac{\pi R}{4v}
\\]

Mulder escapes **if**:
\\[
\frac{(1 - x)R}{v} < \frac{\pi R}{4v}
\Rightarrow x > 1 - \frac{\pi}{4}
\\]

This gives:
\\[
x > 1 - \frac{\pi}{4} \approx 0.2146
\\]

So, if Mulder is **at least ~21.5% of the way from the center to the edge**, the alien **cannot intercept** him in time.

---

## Angular Speed Constraint

Mulder must reach this point \\( xR \\) without being intercepted. To do that, he **orbits around the circle of radius \\( xR \\)**. The alien tries to rotate along the outer circle, but Mulder's **angular speed** exceeds that of the alien when:

\\[
\frac{v}{xR} > \frac{4v}{\pi R}
\Rightarrow x < \frac{1}{4}
\\]

So Mulder can safely **orbit at any radius less than \\( \frac{R}{4} \\)** to position himself.

---

## Final Strategy

- Mulder sets \\( x = 1 - \frac{\pi}{4} + \epsilon \\), e.g., \\( \epsilon = 0.01 \\).
- He orbits at radius \\( xR \\) until perfectly aligned opposite the alien.
- He then **sprints straight for the fence**.

---

## Conclusion

\\[
\boxed{\text{Yes, Mulder can escape by running smart—not just fast.}}
\\]

This problem elegantly combines **geometry**, **relative motion**, and **clever timing**.

# Reference

* [1] [Dan Stefanica - 150 Most Frequently Asked Questions On Quant Intetviews](https://www.scribd.com/document/748214685/Dan-Stefanica-150-Most-Frequently-Asked-Questions-on-Quant-Intetviews-2013-Fe-Press-Libgen-li-1)
