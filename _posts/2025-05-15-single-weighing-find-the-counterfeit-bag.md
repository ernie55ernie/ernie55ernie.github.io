---
layout: post
title: "Single Weighing: Find the Counterfeit Bag"
date: 2025-05-15
category: quantitative interview
---

You face a classic logic-and-weight puzzle:

> You have **10 bags**, each with **100 coins**.  
> All coins look identical.  
> - **9 bags** contain only **10g coins**.  
> - **1 bag** contains only **9g or 11g coins** (unknown which).
>
> You may use a **digital scale** **once** to determine **which bag is counterfeit**.

---

## Step-by-Step Solution

### Step 1: Assign a Unique Sample Pattern

Take coins from each bag in a **distinct count**:

- Take **1 coin from Bag 1**
- **2 coins from Bag 2**
- ...
- **10 coins from Bag 10**

Now you have **55 coins total**:
\\[
1 + 2 + \cdots + 10 = \frac{10 × 11}{2} = 55
\\]

---

## Step 2: Expected Weight if All Bags Are Genuine

If all coins were 10g:

\\[
55 × 10 = 550 \text{ grams}
\\]

Now place your 55 coins on the scale and **record the actual weight**.

---

## Step 3: Interpret the Difference

Let the measured weight be \\(W\\). Then:

- If one bag has **9g coins**, the total will be **less than 550**.
- If one bag has **11g coins**, the total will be **more than 550**.

Let the difference be \\(|W - 550|\\).  
This difference tells you **how many grams off** you are—i.e., **how many coins you took from the counterfeit bag**.

Because you took a unique number of coins from each bag, this difference directly identifies the counterfeit bag.

- If \\(W = 548\\), you're 2g short → Bag **2** is counterfeit (with 9g coins).
- If \\(W = 562\\), you're 12g over → Bag **6** is counterfeit (with 11g coins).

---

## Final Answer

> Take \\(n\\) coins from Bag \\(n\\) (1–10), weigh them all once.  
> Compare total to 550g.  
> The **difference (in grams)** tells you the **bag number** and whether it’s **lighter or heavier**.

# Reference

* [1] [Weighing](https://mathworld.wolfram.com/Weighing.html)
