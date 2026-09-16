---
layout: post
title: "Self-Reinforcing Free Throw Probability: Exactly 50 Makes in 100 Shots"
date: 2025-05-19
category: quantitative interview
---

### The Puzzle

A basketball player takes **100 free throws** under the following conditions:

- She **makes** her first shot and **misses** her second.
- For each subsequent shot (from the 3rd to the 100th), her chance of making it equals:

  \\[
  \frac{\text{number of makes so far}}{\text{number of shots so far}}
  \\]

  For example, if after 40 shots she's made 23, then the 41st shot succeeds with probability \\( \frac{23}{40} \\).

**Question:** What is the probability that, after all 100 shots, she has made **exactly 50** baskets?

---

## Understanding the Process

This scenario describes a **self-reinforcing stochastic process**, where the probability of success at each step depends on the cumulative success rate up to that point. This is akin to a **Pólya urn model**, where the composition of the urn evolves based on previous outcomes, leading to a form of **reinforcement learning**.

In this specific case, the process starts with one make and one miss, and from the 3rd shot onwards, the success probability at each step is determined by the ratio of total successes to total attempts so far.

---

## Key Insight: Uniform Distribution of Final Scores

An intriguing property of this process is that, despite its self-reinforcing nature, the distribution of the total number of successful shots after 100 attempts (starting with 1 make and 1 miss) is **uniform** over the integers from 1 to 99. That is, each total number of makes from 1 to 99 is equally likely.

This uniformity arises because the reinforcement mechanism balances out over time, leading to an equal likelihood of ending up with any total number of successes in the specified range.

---

## Calculating the Desired Probability

Given the uniform distribution over the integers 1 through 99, there are \\( 99 \\) possible total make counts. Therefore, the probability of ending up with exactly 50 successful shots is:

\\[
\boxed{\frac{1}{99}}
\\]

---

## Reference

* [1] [Probability of scoring 66 points in 100 shots](https://math.stackexchange.com/questions/2426159/66-points-in-100-shots)