---
layout: post
title: "Screwy Pirates and Rational Coin Splits"
date: 2025-05-11
category: Quantitative interview
---

## Screwy Pirates and Rational Coin Splits

This is a classic logic puzzle rooted in game theory and rational behavior. The pirates are perfectly rational beings who prioritize survival, personal wealth, and, finally, a bloodthirsty preference for seeing others perish if all else is equal. The goal is to determine the final coin distribution that will be accepted under these rules.

## Setup

- **Pirates A, B, C, D, E** — listed in order of seniority, with A being the most senior.
- **100 gold coins** to be distributed.
- Each pirate votes; a proposal needs **at least 3 votes** to be accepted.
- If rejected, the proposer dies and the next in seniority proposes a new split.
- Each pirate prefers: 1) staying alive > 2) maximizing coins > 3) seeing others die.

## Step-by-Step Reasoning

We work **backwards**, starting from the smallest group of pirates to build up a solution.

### 1 Pirate: Pirate E
If only Pirate E is left, he gets **all 100 coins**. There's no one else.

**Split**:  
- E: 100

### 2 Pirates: Pirates D and E
Pirate D must convince E. But E knows if D dies, he gets all 100. So D gives himself **0**, E **100**.

E votes **no**, D dies.

**Resulting Split**:
- E: 100

### 3 Pirates: Pirates C, D, E
Pirate C must get at least 2 votes. His own vote is 1; he needs **one more**.

C knows that if he's thrown overboard, the split becomes:
- D: 0
- E: 100

So C bribes pirate D with **1 coin** (better than D's 0). E gets nothing.

**Split**:
- C: 99  
- D: 1  
- E: 0

C and D vote yes.

### 4 Pirates: Pirates B, C, D, E
Pirate B needs 2 more votes.

If B dies, the split becomes:
- C: 99  
- D: 1  
- E: 0

So B bribes two pirates who would otherwise get nothing: E and D.

Give:
- D: 1 (same as before, no incentive change — maybe not helpful)
- E: 1 (improvement from 0)

Instead, to **minimize payment**, B can offer **1 coin to E** and **1 to C** (who gets nothing if B dies), because D already gets 1 if B dies, but C gets 99 and will be hard to sway. So B needs to pick the right 2 out of C, D, E.

Actually, best to bribe E and C, who get 0 if B dies.

**Split**:
- B: 98  
- C: 1  
- D: 0  
- E: 1

B, C, E vote yes.

### 5 Pirates: Pirates A, B, C, D, E
A needs 2 more votes.

If A dies, the split is:
- B: 98  
- C: 1  
- D: 0  
- E: 1

So A must bribe 2 pirates who get 0 if he dies — i.e., D and C.

Offer:
- D: 1 (better than 0)
- C: 2 (better than 1)
- E gets 0 either way

**Split**:
- A: 97  
- B: 0  
- C: 2  
- D: 1  
- E: 0

Votes yes: A, C, D → 3 votes — proposal passes.

## Final Split Accepted

- A: 97  
- B: 0  
- C: 2  
- D: 1  
- E: 0

# Reference

* [1] [Pirate Game - Wikipedia](https://en.wikipedia.org/wiki/Pirate_game)
