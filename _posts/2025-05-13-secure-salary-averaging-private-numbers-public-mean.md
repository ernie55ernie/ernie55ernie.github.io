---
layout: post
title: "Secure Salary Averaging: Private Numbers, Public Mean"
date: 2025-05-13
category: quantitative interview
---

Eight quantitative analysts want to know the **average of their salaries**, but with a strict condition:

> **No one is willing to reveal their individual salary to anyone else.**

How can they **collaboratively compute the average** while keeping each person’s salary strictly private?

---

## The Goal

Let each person \\( Q_1, Q_2, \ldots, Q_8 \\) have a private salary \\( s_1, s_2, \ldots, s_8 \\).

They want to compute:

\\[
\text{Average} = \frac{s_1 + s_2 + \cdots + s_8}{8}
\\]

without revealing any \\( s_i \\).

---

## The Protocol: Secure Sum via Random Offsets

This method uses **secure masking** with random numbers.

### Step-by-Step:

1. **Q1 picks a random number** \\( r \\) and **adds it** to their salary:
   \\[
   T_1 = s_1 + r
   \\]

2. **Q1 sends \\( T_1 \\)** to Q2.

3. Each subsequent analyst \\( Q_i \\) (for \\( i = 2 \\) to \\( 8 \\)):

   - **Adds their own salary** \\( s_i \\) to the total they received:
     \\[
     T_i = T_{i-1} + s_i
     \\]

   - Then **passes \\( T_i \\)** to the next person.

4. **Q8 returns the final sum** \\( T_8 \\) to **Q1**.

5. **Q1 subtracts their random number \\( r \\)**:
   \\[
   \text{Total Sum} = T_8 - r = s_1 + s_2 + \cdots + s_8
   \\]

6. The group divides by 8 to compute the **average salary**.

---

## Why It Works

- Only Q1 knows the random \\( r \\), which protects their salary.
- Every participant only sees a **masked partial sum**.
- No one learns any individual salary.
- Only the **total sum** is ever revealed (to Q1), and then the **average** is shared.

---

## Final Answer

**Yes**, the quant team can compute the average securely.  
> Use a chained sum protocol with a random offset to mask individual values—revealing only the final average.

# Reference

* [1] [Secure Multiparty Computation (Wikipedia)](https://en.wikipedia.org/wiki/Secure_multi-party_computation)
