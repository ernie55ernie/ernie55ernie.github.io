---
layout: post
title: "Ant Collisions on a Line: Who Reaches Whom?"
date: 2025-05-24
category: quantitative interview
---

### The Setup

- A straight line segment connects **Alice** and **Bob**.
- **Bob** sends **50 ants** toward Alice.
- **Alice** sends **20 ants** toward Bob.
- All ants move at equal speed along the segment.
- **Whenever two ants collide**, they **bounce back** and reverse direction.

---

## Question

1. **How many ants reach Alice?**
2. **How many ants reach Bob?**
3. **How many collisions occur?**

---

## Key Insight: Collisions Are Indistinguishable

When two ants collide and bounce back, it's as if they **pass through each other**.

- Because ants are **indistinguishable**, we can **pretend they don't bounce**—they just **keep moving** in their original directions.

### So:

- Every ant continues along its path unless it collides—but we **treat them as if they don't**.
- That means:
  - **All 50 ants from Bob** continue to Alice.
  - **All 20 ants from Alice** continue to Bob.

---

## Final Answers

- **Ants reaching Alice**: \\( \boxed{50} \\)
- **Ants reaching Bob**: \\( \boxed{20} \\)

---

## How Many Collisions?

Each pair of ants traveling in opposite directions will **collide once**.

- 50 ants from Bob × 20 ants from Alice = \\( 50 \times 20 = \boxed{1000} \\) total collisions

---

## Summary

| Quantity              | Value      |
|-----------------------|------------|
| Ants reaching Alice   | \\( \boxed{50} \\) |
| Ants reaching Bob     | \\( \boxed{20} \\) |
| Total collisions      | \\( \boxed{1000} \\) |

---

## Reference

* [1] [Chapter 1](https://www.fepress.org/wp-content/uploads/2013/10/150iqs-ten_questions_solutions.pdf)