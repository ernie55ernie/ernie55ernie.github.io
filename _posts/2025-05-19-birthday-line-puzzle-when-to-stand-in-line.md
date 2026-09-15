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

Let's define what needs to happen for the person in position \\( i \\) to win:

1. **No repeats among the first \\( i-1 \\) people.**  
   The probability that all \\( i-1 \\) people have distinct birthdays is:
   \\[
   P(\text{no repeats}) = \frac{365}{365} \times \frac{364}{365} \times \dots \times \frac{365 - (i-2)}{365}
   \\]

2. **Person \\( i \\) matches one of those \\( i-1 \\) distinct birthdays.**  
   Since there are exactly \\( i-1 \\) distinct birthdays before them, the probability that person \\( i \\)'s birthday is one of them is simply:
   \\[
   P(\text{match}) = \frac{i-1}{365}
   \\]

So we compute the total probability that position \\( i \\) wins:

\\[
P(i \text{ wins}) = P(\text{no repeats}) \times P(\text{match})
\\]

To maximize this, we check where \\( P(i+1) > P(i) \\). After simplifying the ratio \\( P(i+1)/P(i) \\), the probability is maximized at position:

\\[
\boxed{20}
\\]

---

## Conclusion

If you can choose your place in line, position **20** gives you the highest chance of being the first person with a matching birthday and winning the free ticket.

## Reference

* [1] [Birthday problem variations](https://en.wikipedia.org/wiki/Birthday_problem)
