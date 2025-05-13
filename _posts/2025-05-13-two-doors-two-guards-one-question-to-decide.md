---
layout: post
title: "Two Doors, Two Guards: One Question to Decide"
date: 2025-05-13
category: quantitative interview
---

You face a classic logic puzzle:

> Two doors stand before you:
> - One leads to your **dream job offer**.
> - The other leads to **certain doom** (rejection and exit).
>
> In front of each door is a **guard**:
> - One **always tells the truth**.
> - The other **always lies**.
>
> You may ask **one yes-or-no question** to **one guard**.  
> You must then choose a door.

## The Challenge

With only one question and no way to know which guard is truthful, how can you **guarantee** selecting the correct door?

## The Classic Logic Trick

Ask this question to **either guard**:

> **“If I asked the other guard which door leads to the job offer, would they say this one?”**  
> (Point to one of the doors.)

Then:

- If the guard says **yes**, go to the **other door**.
- If the guard says **no**, go to the **door you pointed at**.

### Why It Works

Let’s break down what happens:

#### Case 1: You're speaking to the **truth-teller**
- They will **honestly report** what the **liar** would say.
- Since the liar always lies, the answer the truth-teller reports is **false**.
- So, you **go to the opposite door** of what they indicate.

#### Case 2: You're speaking to the **liar**
- They will **lie** about what the **truth-teller** would say.
- The truth-teller would point you to the correct door; the liar lies and points to the wrong one.
- Again, you go to the **opposite door**.

In **both cases**, reversing the answer leads you to the correct door.

## Final Answer

> Ask **either guard**:  
> **“If I asked the other guard which door leads to the job offer, would they say this one?”**  
> Then **go through the opposite door** of what they say.

# Reference

* [1] [Knights and Knaves Puzzle (Wikipedia)](https://en.wikipedia.org/wiki/Knights_and_Knaves)
