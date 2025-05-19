---
layout: post
title: "Birthday-Line Puzzle: When to Stand in Line"
date: 2025-05-19
category: quantitative interview
---

In this intriguing probability problem, your goal is to **maximize** your chance of winning a free movie ticket based on birthdays.

---

### The Setup

- A line forms at a movie theater.
- The **first** person whose birthday matches someone **earlier in line** wins a free ticket.
- You can choose your **position** in the line.
- Everyone’s birthday is uniformly and independently distributed over 365 days.
- You **don’t know anyone else’s birthday**.

### Question:

**Which position in line should you choose to maximize your chance of being the winner?**

---

## Key Insight

You want to be the **first person** whose birthday matches someone earlier in line. This is related to the classic **birthday paradox**, but with a twist: you win only if **your birthday matches someone before you**, and **you are the first such person**.

---

## Probabilistic Structure

Let’s define:

- For position \\( i \\), the probability that **no one before** has your birthday is:

\\[
P(\text{no match before}) = \left( \frac{364}{365} \right)^{i-1}
\\]

- The probability that **someone before you has** your birthday is:

\\[
1 - \left( \frac{364}{365} \right)^{i-1}
\\]

- But for you to win, **no one before you** can have matched someone **before them**—you must be the **first** repeater.

So we compute:

\\[
P(i \text{ wins}) = \left[\text{probability no repeats among first } i-1\right] \times \left[\text{probability person } i \text{ matches someone before}\right]
\\]

This is maximized at position:

\\[
\boxed{20}
\\]

---

## Conclusion

If you can choose your place in line, position **20** gives you the highest chance of being the first person with a matching birthday and winning the free ticket.

## Reference

* [1] [Birthday problem variations](https://en.wikipedia.org/wiki/Birthday_problem)
