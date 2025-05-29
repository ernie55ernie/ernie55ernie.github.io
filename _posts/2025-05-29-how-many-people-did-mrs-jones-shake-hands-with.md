---
layout: post
title: "How Many People Did Mrs. Jones Shake Hands With?"
date: 2025-05-29
category: quantitative interview
---

## Problem

Mr. and Mrs. Jones host a party and invite **4 other couples** — 10 people total.  
At the end, Mr. Jones asks the **other 9 people** how many hands they shook.  
Each person gives a **different answer**: 0, 1, 2, ..., 8.  
People don’t shake hands with themselves or their spouse.

**Question**: How many people did **Mrs. Jones** shake hands with?

---

## Step-by-Step Analysis

Let’s label the 9 people **excluding Mr. Jones** as:

\\[
P_1, P_2, \dots, P_9
\\]

They each report a **distinct handshake count** from 0 to 8.  
This means the set of answers is:  
\\[
\{0, 1, 2, \dots, 8\}
\\]

---

### Key Observations

- There are **exactly 9 answers**, so every number from 0 to 8 appears once.
- No one shakes hands with their own spouse.
- The person who shook hands with **8 people** must have shaken hands with everyone **except their spouse**.
- The person who shook hands with **0 people** shook hands with **no one**, not even their spouse.

So the person with **8 handshakes** must have **not shaken hands with exactly one person**: their spouse.  
Likewise, the person with **0 handshakes** must be the **spouse** of the 8-handshake person.

This pairing logic continues:

- 1 and 7 must be spouses
- 2 and 6 must be spouses
- 3 and 5 must be spouses

Leaving the person who shook hands with **4 people** unpaired — this must be **Mrs. Jones**!

---

## Final Answer

\\[
\boxed{\text{Mrs. Jones shook hands with } 4 \text{ people.}}
\\]

# Reference

* [1] [Handshakes](https://quantnet.com/threads/handshakes.6311/)