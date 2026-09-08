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

This is a classic result from **Ramsey theory**, and famously demonstrates the Ramsey number:

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

This rigorously proves that any group of 6 people guarantees a trio, meaning \\( R(3,3) \le 6 \\).

---

## Bonus: Why Not 5 People?

To fully prove \\( R(3,3) = 6 \\), we must show that 5 people is **not enough**. 

Imagine 5 people sitting in a circle, where everyone is acquainted **only** with their two immediate neighbors. 
- The acquaintances form a **pentagon boundary** (no triangles).
- The strangers form a **star inside** the pentagon (no triangles).

Since a group of 5 can avoid both trios, 6 is the absolute minimum!

---

## Final Answer

**In any group of 6 people**, there must exist **three mutual acquaintances** or **three mutual strangers**.

This perfectly illustrates the core principle of **Ramsey’s Theorem**: complete disorder is impossible!

# Reference

* [1] [Ramsey's theorem](https://en.wikipedia.org/wiki/Ramsey%27s_theorem#An_elementary_example)
