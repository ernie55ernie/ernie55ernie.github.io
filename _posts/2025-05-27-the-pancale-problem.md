---
layout: post
title: "The Pancake Problem: Conditional Probability Puzzle"
date: 2025-05-27
category: quantitative interview
---

You have a bag containing 3 pancakes:

1. Golden on both sides (GG)
2. Burnt on both sides (BB)
3. Golden on one side and burnt on the other (GB)

You shake the bag, draw a pancake at random, **observe one side is golden**, and are asked:

> What is the probability that the other side is also golden?

---

### Step 1: Sample Space of Sides

Each pancake has **two sides**, so the total sample space of visible sides is:

- GG pancake: **2 golden sides**
- BB pancake: 2 burnt sides → irrelevant here
- GB pancake: **1 golden, 1 burnt side**

So among the 6 sides (2 per pancake), there are:

- 3 golden sides in total:
  - 2 from GG
  - 1 from GB

These 3 golden sides come from:

- **2 instances of GG**
- **1 instance of GB**

---

### Step 2: Conditional Probability

You're told a **golden side** is observed. So the sample space is restricted to:

- GG's 2 golden sides
- GB's 1 golden side

There are 3 equally likely golden-side observations:
- GG-side 1
- GG-side 2
- GB's golden side

In how many of these is the **other side also golden**?

- GG: yes, both sides golden (2 outcomes)
- GB: no (1 outcome)

So:

\\[
P(\text{other side is golden} \mid \text{observed golden}) = \frac{2}{3}
\\]

---

## Final Answer

\\[
\boxed{\frac{2}{3}}
\\]

# Reference

* [1] [Conditional probability](https://en.wikipedia.org/wiki/Conditional_probability)
