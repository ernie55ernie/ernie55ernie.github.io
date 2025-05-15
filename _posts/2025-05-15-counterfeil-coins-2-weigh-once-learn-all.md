---
layout: post
title: "Counterfeit Coins II: Weigh Once, Learn All"
date: 2025-05-15
category: quantitative interview
---

This clever puzzle combines weights, coin counting, and **ternary encoding**:

> You have **5 bags**, each with **100 coins**, and each bag's coins are **uniform in weight**, but either:
>
> - **9 g**, or  
> - **10 g**, or  
> - **11 g**
>
> You may use a **digital scale** that reports the **total weight** of any group of coins.
>
> **Goal:** Determine, with **as few weighings as possible**, the exact weight of coins in **each bag**.

---

## Step 1: Strategy Overview

We're told that each bag could be **light (9g)**, **normal (10g)**, or **heavy (11g)**.

That’s **three possible states per bag** → a **ternary** system!

With 5 bags, the total number of weight configurations is:

\[
3^5 = 243
\]

So, we need a strategy that can distinguish between **243 different outcomes**—and we can encode all 243 in a **single ternary number**.

---

## Step 2: Use Weighted Coin Counts

Take coins from each bag in these amounts:

- **Bag 1** → 1 coin  
- **Bag 2** → 3 coins  
- **Bag 3** → 9 coins  
- **Bag 4** → 27 coins  
- **Bag 5** → 81 coins

These counts correspond to the **powers of 3**: \(3^0, 3^1, 3^2, 3^3, 3^4\)

---

## Step 3: Calculate Expected Weight

If all coins were **10g**, then total weight would be:

\[
1×10 + 3×10 + 9×10 + 27×10 + 81×10 = 1210 \text{ g}
\]

Now suppose you perform a single weighing and get total weight \(W\).

Let the difference \(d = W - 1210\). Each 1g deviation corresponds to:

- -1 per light coin (9g)
-  0 per normal coin (10g)
- +1 per heavy coin (11g)

Because you took different **multiples of coins** from each bag, each weight deviation from 1210 reflects a **ternary digit** in base 3 centered at 10g.

---

## Step 4: Decode the Deviation

Write \(d\) as a number in **balanced ternary** (digits = -1, 0, +1), using the weights:
\[
d = a×1 + b×3 + c×9 + d×27 + e×81
\]

Each coefficient tells you whether that bag was:
- **-1** → 9g coins
- **0** → 10g coins
- **+1** → 11g coins

The powers (1, 3, 9, ...) uniquely identify which bag’s coins contributed which deviation.

---

## Final Answer

> **One weighing is enough.**  
> Take **1, 3, 9, 27, 81** coins from the 5 bags.  
> Compute the total.  
> Compare to **1210g**, and convert the difference into **balanced ternary** to identify each bag’s coin weight (9g, 10g, or 11g).

# Reference

* [1] [Defective coin weighing problem and ternary representation when number of coins is not a power of 3](https://math.stackexchange.com/questions/1687435/defective-coin-weighing-problem-and-ternary-representation-when-number-of-coins)
