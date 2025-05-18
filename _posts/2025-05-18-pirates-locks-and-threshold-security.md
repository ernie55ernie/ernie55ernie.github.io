---
layout: post
title: "Pirates, Locks, and Threshold Security"
date: 2025-05-18
category: quantitative interview
---

## Pirates, Locks, and Threshold Security

This puzzle explores a physical version of **threshold secret-sharing** using locks and keys:

> There are **11 pirates** and a safe containing treasure.  
> They want a **majority group (6 or more)** to be able to **open the safe**,  
> but **no group of 5 or fewer** should be able to do so.

The locksmith uses a number \\( L \\) of **distinct locks**.  
To open the safe, **all locks must be opened**, and each lock can have keys given to multiple pirates.

---

## Goal

Design a lock-and-key scheme such that:

- **Any 6 or more pirates** can open **every lock** (collectively hold all keys).
- **No group of 5 or fewer pirates** can open **all locks**.

We want to minimize:

- The **total number of locks \\(L\\)**
- The number of **keys held per pirate**

---

## Step 1: Strategy

For each group of **5 pirates** (the ones we want to block), introduce a **lock** that **only those 5 pirates do *not*** have keys for.

This ensures:

- Any group of **5 pirates** is missing at least one key (cannot open the safe).
- Any group of **6 or more pirates** contains **at least one** pirate with the key for every lock (they can open all).

---

## Step 2: Count the Combinations

The number of distinct groups of **5 pirates out of 11** is:

\\[
L = \binom{11}{5} = 462
\\]

So we need **462 locks**—one for each 5-pirate coalition to exclude.

---

## Step 3: Key Distribution

Each lock is **inaccessible to one specific group of 5 pirates**, so keys for that lock are given to the **remaining 6 pirates**.

Now ask: How many locks does **each pirate** hold a key for?

Each pirate is **excluded** from some 5-pirate groups, but **included** in many others.

Specifically, for each lock (i.e., for each 5-pirate group), a pirate has a key if they are **not** in that group.

So: For pirate \\(P\\), the number of 5-pirate groups they are **not** in is:

\\[
\binom{10}{5} = 252
\\]

Hence, each pirate holds **252 keys**.

---

## Final Answer

> - **Minimum number of locks** required: \\(\boxed{462}\\)  
> - **Each pirate holds** \\(\boxed{252}\\) **keys**

This is a physical realization of a **(6-of-11)** threshold access system.

# Reference

* [1] [Minimum number of locks and keys [duplicate]](https://math.stackexchange.com/questions/1316831/minimum-number-of-locks-and-keys)