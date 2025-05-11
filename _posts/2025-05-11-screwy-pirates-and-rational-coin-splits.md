---
layout: post
title: "Screwy Pirates and Rational Coin Splits"
date: 2025-05-11
category: quantitative interview
---

## Screwy Pirates and Rational Coin Splits

A classic logic puzzle involves a crew of five perfectly rational pirates attempting to divide 100 gold coins under a strict voting system. Their priorities: survival first, personal wealth second, and finally, maximizing the number of crewmates overboard if indifferent.

### The Rules

1. The most senior pirate proposes a split.
2. All remaining pirates vote.
3. A proposal passes with at least 50% (rounding up in case of odd pirates).
4. If rejected, the proposer dies, and the next most senior pirate makes a new proposal.

Let’s label the pirates from A (most senior) to E (least senior).

## Working Backwards

To understand what proposal pirate A should make, we analyze from the smallest group upward.

### 1 Pirate Left: Pirate E
Only E remains. He keeps all **100 coins**. No vote needed.

### 2 Pirates Left: Pirates D and E
Pirate D must get one vote (his own) to pass a proposal. He gives **100 coins to himself**, **0 to E**.

Split:  
**D: 100, E: 0**

### 3 Pirates: C, D, E
C needs 2 votes. He has his own. He can **buy E’s vote** with 1 coin.

Split:  
**C: 99, D: 0, E: 1**

Why this works:
- D would prefer C to die and revert to the 2-pirate case where he gets everything.
- E gets 0 in the 2-pirate case, so 1 coin is better. He votes yes.

### 4 Pirates: B, C, D, E
B needs 2 votes beyond his own. He gives **1 coin to D** (who would get 0 if B dies) to secure his support.

Split:  
**B: 99, C: 0, D: 1, E: 0**

- C would prefer B dead, hoping for 99 coins in the 3-pirate scenario.
- D prefers 1 over 0.
- E gets nothing either way, but prefers B dead, so votes no.
- B gets yes from himself and D.

### 5 Pirates: A, B, C, D, E
A needs 3 votes. He gives **1 coin to C** and **1 to E** (both get 0 in the 4-pirate case), securing their votes.

Split:  
**A: 98, B: 0, C: 1, D: 0, E: 1**

- B would get 99 if A dies; votes no.
- C gets 0 if A dies; votes yes.
- D gets 1 if A dies; votes no.
- E gets 0 if A dies; votes yes.

With votes from A, C, and E, the proposal passes.

## Final Distribution

**A: 98 coins**  
**B: 0 coins**  
**C: 1 coin**  
**D: 0 coins**  
**E: 1 coin**

# Reference

* [1] [Screwy Pirates Problem (Classic Logic)](https://en.wikipedia.org/wiki/Pirate_game)