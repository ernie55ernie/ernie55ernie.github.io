---
layout: post
title: "Sock Drawer Puzzle: Matching by the Pigeonhole Principle"
date: 2025-05-15
category: quantitative interview
---

You're faced with a cozy yet classic problem in logic:

> Your drawer holds:
> - 2 red socks  
> - 20 yellow socks  
> - 31 blue socks  
>
> You pick socks **at random**, **without looking**.
>
> **Question:** What’s the **minimum number** of socks you must pull out to guarantee a matching pair in the **same color**?

---

## Step 1: Understand the Worst-Case Scenario

This is a classic case for the **pigeonhole principle**, which states:

> If you have more items than containers, **at least one container must hold more than one item**.

In this context:

- There are **3 colors** (red, yellow, blue) — think of these as "pigeonholes".
- You want to be **guaranteed** that at least **one color repeats** — i.e., a pair.

### Worst Case

You could pick:

- 1 red sock  
- 1 yellow sock  
- 1 blue sock  

That's **3 socks**, all different colors—no match yet.

---

## Step 2: One More Guarantees a Match

Once you pull a **4th sock**, it **must** match one of the previous three (since there are only 3 colors available).

### Therefore:

> **Minimum number of socks = 4**

This guarantees **at least one matching pair** in the same color.

---

## Final Answer

**You must pull out at least 4 socks** to guarantee a matching pair of the same color.

# Reference

* [1] [Pigeonhole Principle](https://en.wikipedia.org/wiki/Pigeonhole_principle)
