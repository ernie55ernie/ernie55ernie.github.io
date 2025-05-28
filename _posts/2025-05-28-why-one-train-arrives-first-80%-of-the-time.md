---
layout: post
title: "Why One Train Arrives First 80% of the Time"
date: 2025-05-28
category: quantitative interview
---

## Problem

You notice that at your subway station:

- Train A arrives first **80%** of the time
- Train B arrives first only **20%** of the time

Yet both trains are supposed to run with **equal frequency**

What’s going on?

---

## Key Explanation

### 1. Frequency Mismatch?

It could be that Train A actually **runs more frequently**, despite what's claimed. But that's not the only explanation.

---

### 2. Uniform Arrival + Scheduling Offset

Even if both trains run **every 10 minutes**, you might still observe one coming first more often due to **schedule offset**.

#### Example:

- Train A: 1:00, 1:10, 1:20, ...
- Train B: 1:12, 1:22, 1:32, ...

Your arrival is **uniformly random** over time. Between 1:00 and 1:10:

- You’ll see Train A first **8 out of 10 minutes** (1:00 to 1:11)
- Only during the **last 2 minutes** (1:12 to 1:14) will Train B come first

So:

\\[
P(\text{Train A arrives first}) = \frac{8}{10} = \boxed{80\%}
\\]

Even though both trains arrive every 10 minutes!

---

### Moral of the Story

Your **random arrival time** interacts with the train schedules in a way that **biases your observation** toward one train—even when both have equal frequency.

This is a real-world example of the **inspection paradox** or **sampling bias** due to scheduling structure.

---

## Conclusion

\\[
\boxed{
The train that arrives first 80% of the time may not be more frequent—it just benefits from a favorable timing offset when you arrive randomly.
}
\\]

# Reference

* [1] [The Waiting-Time Paradox](https://www.math.ucla.edu/~mason/papers/frym-WTP-published.pdf)