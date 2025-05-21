---
layout: post
title: "Random Ants on a Stick: Expected Time Until All Fall Off"
date: 2025-05-21
category: quantitative interview
---

### The Setup

- A 1-foot string has **500 ants**, each placed uniformly at random in \\( [0, 1] \\).
- Each ant independently chooses to walk **left** or **right** with equal probability (\\( \frac{1}{2} \\)).
- Ants walk at a constant speed of **1 ft/min**.
- When two ants meet, they **reverse directions**—or equivalently, **pass through** one another unchanged.
- Ants fall off the string upon reaching either end.

---

## Key Insight

The reversal behavior upon meeting is **indistinguishable** (in terms of final outcomes) from the ants **passing through** each other. So we may treat each ant as continuing in its original direction without interaction.

Thus, the **last ant to fall off** is simply the ant that takes the **maximum time** to reach an endpoint.

---

## Time to Fall Off

Each ant:

- Starts at a position \\( x \in [0,1] \\)
- Goes left with probability \\( \frac{1}{2} \\): time to fall off = \\( x \\)
- Goes right with probability \\( \frac{1}{2} \\): time to fall off = \\( 1 - x \\)

So the time for a given ant to fall off is:

\\[
T = 
\begin{cases}
x & \text{with probability } \frac{1}{2} \\
1 - x & \text{with probability } \frac{1}{2}
\end{cases}
\\]

Thus, the time for all ants to fall off is:

\\[
\max_{i=1}^{500} T_i
\\]

Each \\( T_i \\) is uniformly distributed over \\( [0,1] \\) (as a symmetric combination of \\( x \\) and \\( 1 - x \\)).

---

## Expected Maximum of 500 Uniform(0,1) Variables

Let \\( T_i \sim \mathrm{Uniform}(0,1) \\). Then:

\\[
\mathbb{E}\left[\max_{i=1}^{500} T_i\right] = \frac{500}{501}
\\]

---

## Final Answer

\\[
\boxed{\frac{500}{501}} \text{ minutes}
\\]

This is the expected time until all ants have fallen off the string.

---

## Reference

* [1] [Expected falling time of all 500
 random ants](https://math.stackexchange.com/questions/3493757/expected-falling-time-of-all-500-random-ants)