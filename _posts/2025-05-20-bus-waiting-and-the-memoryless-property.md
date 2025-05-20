---
layout: post
title: "Bus-Waiting and the Memoryless Property"
date: 2025-05-20
category: quantitative interview
---

### The Puzzle

Buses arrive according to a **Poisson process** with rate \\( \lambda = 0.1 \\) per minute. That means the **mean interarrival time** is:

\\[
\frac{1}{\lambda} = 10 \text{ minutes}
\\]

You show up at a **random time**.

---

### Questions:

1. What is your **expected waiting time** until the **next bus**?
2. On average, how long ago did the **last bus** depart?

---

## Key Concept: The Memoryless Property

In a Poisson process, the **interarrival times** are **exponentially distributed**. The exponential distribution has the **memoryless property**:

\\[
P(T > s + t \mid T > s) = P(T > t)
\\]

This implies that **given no event has occurred so far**, the distribution of the waiting time until the next event **remains the same**.

---

## Forward Recurrence Time (Next Bus)

Since arrivals follow a Poisson process, the time until the **next bus** from a random observation point is distributed:

\\[
\text{Waiting time} \sim \text{Exp}(\lambda)
\Rightarrow \mathbb{E}[\text{wait}] = \frac{1}{\lambda} = 10 \text{ minutes}
\\]

---

## Backward Recurrence Time (Last Bus)

Likewise, the **time since the last bus** is also distributed as:

\\[
\text{Time since last bus} \sim \text{Exp}(\lambda)
\Rightarrow \mathbb{E}[\text{elapsed time}] = \frac{1}{\lambda} = 10 \text{ minutes}
\\]

---

## Final Answers

1. Expected waiting time until next bus: \\( \boxed{10} \\) minutes  
2. Expected time since last bus: \\( \boxed{10} \\) minutes

---

## Reference

* [1] [Exponential distribution and the memoryless property](https://en.wikipedia.org/wiki/Exponential_distribution#Lack_of_memory)