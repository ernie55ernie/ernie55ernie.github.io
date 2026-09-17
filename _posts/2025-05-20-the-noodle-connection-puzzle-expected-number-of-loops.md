---
layout: post
title: "The Noodle Connection Puzzle: Expected Number of Loops"
date: 2025-05-20
category: quantitative interview
---

### The Setup

You start with **100 noodles**, each with **2 loose ends**—so a total of **200 ends**.

You then repeatedly grab **two free ends at random** and tie them together. You do this blindly and continue until no free ends remain. By the end, you'll have formed several **closed loops** of various lengths.

---

### The Question

**What is the expected number of loops** you’ll have when all 200 ends have been tied?

---

## Key Insight: Random Pairings and Cycles

This problem is equivalent to the problem of forming a **random pairing** of 200 elements (the ends). Each such pairing corresponds to a decomposition of a **set of 100 edges** (or 200 nodes) into **disjoint cycles**.

Each tied pair reduces the number of free ends by 2, and eventually all 200 ends are paired.

This process results in a **random pairing** of the 200 endpoints into **100 edges**, and the resulting structure can be seen as a collection of cycles (loops of connected noodle segments).

---

## Known Result

This is a classic result in combinatorics: the **expected number of loops** (cycles) formed when randomly pairing **2n endpoints** is:

\\[
\boxed{\sum_{k=1}^{n} \frac{1}{2k - 1}} \approx \frac{1}{2}\ln(n) + \frac{\gamma}{2} + \ln(2)
\\]

where \\( \gamma \approx 0.577 \\) is the Euler-Mascheroni constant.

For \\( n = 100 \\), the expected number of loops is:

\\[
\sum_{k=1}^{100} \frac{1}{2k - 1}
= \frac{1}{1} + \frac{1}{3} + \frac{1}{5} + \cdots + \frac{1}{199}
\approx \frac{1}{2}\ln(100) + \frac{0.577}{2} + \ln(2)
\approx 2.302 + 0.288 + 0.693 \approx 3.284
\\]

---

## Final Answer

\\[
\boxed{\sum_{k=1}^{100} \frac{1}{2k - 1} \approx 3.284}
\\]

So on average, you will end up with **about 3.28 loops** after all the ends are tied.

---

## Reference

* [1] [Connecting noodles probability question](https://math.stackexchange.com/questions/1417274/connecting-noodles-probability-question)
