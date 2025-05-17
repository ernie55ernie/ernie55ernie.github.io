---
layout: post
title: "The Party Problem: Ramsey’s Theorem in Action"
date: 2025-05-15
category: quantitative interview
---

You’re at a small gathering with a twist of mathematics:

> In a **party of 6 people**, every pair is either **acquainted** or **strangers**.
>
> **Prove:** No matter how these relationships are arranged, there is always:
>
> - A trio of **mutual acquaintances**, or  
> - A trio of **mutual strangers**.

This is a classic result from **Ramsey theory**, and specifically proves that:

\\[
R(3,3) = 6
\\]

---

## Step 1: Model the Problem

Think of the 6 people as **nodes in a graph**.

- Draw an edge between each pair.
- Color each edge:
  - **Red** for acquaintances
  - **Blue** for strangers

Goal: Prove that **some triangle** must be **monochromatic** (all red or all blue).

---

## Step 2: Use the Pigeonhole Principle

Pick any person—say, **Alice**. She has **5 edges** (to the 5 others).

By the pigeonhole principle:

- At least **3 edges** must be the **same color**.
- Suppose at least **3 red edges** (acquaintances): Alice is acquainted with **Bob, Carol, Dave**

Now look at Bob, Carol, and Dave.

- If **any pair among them** (say Bob–Carol) are also acquainted → **Bob–Carol–Alice** is a **red triangle** (mutual acquaintances).
- If **none of them** know each other → Bob–Carol–Dave form a **blue triangle** (mutual strangers).

Either way, a monochromatic triangle exists.

---

## Step 3: Generalization

The same argument applies if Alice has 3+ blue edges (to strangers).

You’d then find either:
- A blue triangle (among strangers), or
- A red triangle (mutual acquaintances).

---

## Final Answer

**In any group of 6 people**, there must exist **three mutual acquaintances** or **three mutual strangers**.

This elegant result is a special case of **Ramsey’s Theorem**:

\\[
R(3,3) = 6
\\]

# Reference

* [1] [Ramsey's theorem](https://en.wikipedia.org/wiki/Ramsey%27s_theorem#An_elementary_example)
