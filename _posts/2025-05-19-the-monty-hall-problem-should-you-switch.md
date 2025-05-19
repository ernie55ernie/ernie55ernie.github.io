---
layout: post
title: "The Monty Hall Problem: Should You Switch?"
date: 2025-05-19
category: quantitative interview
---

This is one of the most famous puzzles in probability, highlighting how intuition can be misleading.

---

### The Setup

- There are **3 doors**:
  - 1 hides a **car**.
  - The other 2 hide **goats**.
- You pick one door (say, Door A).
- The host, who **knows** what’s behind each door, opens **another** door, revealing a **goat**.
- You are then asked: **Do you want to stay with your original pick or switch to the other unopened door?**

---

## Key Insight

Let’s examine the probabilities:

- **Initial pick** (before any doors are opened): Probability your door has the car is \\( \frac{1}{3} \\).
- Therefore, the probability the car is **behind one of the other two doors** is \\( \frac{2}{3} \\).

Now, the host opens one of the other two doors and shows a **goat**. Because the host **always avoids the car**, he effectively tells you **nothing new about your door**, but removes the uncertainty about **one of the losing doors**.

So the entire \\( \frac{2}{3} \\) probability **transfers** to the one remaining unopened door.

---

## Conclusion

If you **switch**, your chance of winning is:

\\[
\boxed{\frac{2}{3}}
\\]

If you **stay**, your chance is only:

\\[
\frac{1}{3}
\\]

### So you should **always switch**.

## Reference

* [1] [Wikipedia: Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)
