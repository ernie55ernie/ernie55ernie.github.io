---
layout: post
title: "The Birthday Problem: Probability of Shared Birthdays"
date: 2025-05-19
category: quantitative interview
---

The **birthday problem** explores the counterintuitive probability that in a relatively small group of people, some pair will share the same birthday. While there are 365 possible birthdays (ignoring leap years), it doesn't take a large group for the chances of a shared birthday to surpass 50%.

### Problem Statement

> **Given:** Birthdays are uniformly distributed over 365 days.  
> **Find:** The smallest number \( n \) such that the probability of **at least two** people sharing a birthday is **greater than 50%**.

## Solution

Rather than directly computing the probability that *at least two* people share a birthday, we take the complementary approach. We compute the probability that **no two** people share a birthday and subtract it from 1.

Let:

- \( P(n) \): Probability that all \( n \) people have unique birthdays.
- \( Q(n) = 1 - P(n) \): Probability that **at least two** share a birthday.

### Step-by-step Computation

Assuming birthdays are independent and uniformly distributed:

\[
P(n) = \frac{365}{365} \cdot \frac{364}{365} \cdot \frac{363}{365} \cdot \cdots \cdot \frac{365 - n + 1}{365}
\]

This can be expressed compactly as:

\[
P(n) = \prod_{k=0}^{n-1} \left( \frac{365 - k}{365} \right)
\]

We evaluate \( Q(n) = 1 - P(n) \) for increasing values of \( n \) until \( Q(n) > 0.5 \).

### Result

By computing or looking up standard values:

- \( Q(22) \approx 0.475 \)
- \( Q(23) \approx 0.507 \)

Hence, **23 people** are sufficient for the probability of shared birthdays to exceed 50%.

## Conclusion

Surprisingly, with just 23 people in a room, there's a better than even chance that at least two share a birthday — a striking result that showcases the unintuitive nature of probability.

# Reference

* [1] [Wikipedia: Birthday problem](https://en.wikipedia.org/wiki/Birthday_problem)
