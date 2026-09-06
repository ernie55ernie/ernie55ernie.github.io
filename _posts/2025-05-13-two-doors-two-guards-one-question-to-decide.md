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

<iframe src="{{ site.baseurl }}/assets/two_doors_two_guards.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

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

You are asking a nested question. By asking one guard what the *other* guard would say, you guarantee that the logical path passes through exactly **one truth-teller** and **one liar**. 

Because `True × False = False`, the final answer you receive will **always be a lie**.

Let's trace it:
- If you point to the **Job door**: The true answer is "Yes". The liar would lie and say "No". The truth-teller would honestly report that the liar would say "No". Thus, both guards will say **"No"**.
- If you point to the **Doom door**: The true answer is "No". The liar would lie and say "Yes". The truth-teller would honestly report that the liar would say "Yes". Thus, both guards will say **"Yes"**.

In **both cases**, the "Yes" or "No" you receive is exactly backward.

## Final Answer

> Ask **either guard**:  
> **“If I asked the other guard which door leads to the job offer, would they say this one?”**  
> - If they say **"Yes"**, go to the **other door**.
> - If they say **"No"**, go to **the door you pointed at**.

# Reference

* [1] [Knights and Knaves Puzzle (Wikipedia)](https://en.wikipedia.org/wiki/Knights_and_Knaves)
