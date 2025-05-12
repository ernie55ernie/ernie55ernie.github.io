---
layout: post
title: "Bridge and Torch: Racing Against the Dark"
date: 2025-05-12
category: quantitative interview
---

## Bridge and Torch: Racing Against the Dark

This classic puzzle tests our ability to optimize under constraints. Four people—A, B, C, and D—need to cross a bridge at night. They have only one torch, and at most two can cross at a time. The crossing speed of any pair is determined by the **slower** person.

### Crossing Times:
- **A**: 10 minutes
- **B**: 5 minutes
- **C**: 2 minutes
- **D**: 1 minute

The goal: **get everyone across as quickly as possible**.

## Naive Approaches Don’t Work

It might seem intuitive to always try to send the fastest people back and forth, or to send the slowest people together—but that doesn't always minimize total time.

### Key Insight

To minimize time, we **minimize the number of slow crossings**, and use the two fastest people (C and D) as returners whenever possible.

## Optimal Strategy

Let’s use the **fastest-first return strategy**:

1. **D and C cross** → 2 minutes  
2. **D returns** → 1 minute  
3. **A and B cross** → 10 minutes  
4. **C returns** → 2 minutes  
5. **D and C cross again** → 2 minutes  

### Total Time = 2 + 1 + 10 + 2 + 2 = **17 minutes**

## Why It's Optimal

- We only send the slowest pair (A and B) together once.
- The fastest (C and D) handle all the return trips.
- Any alternative involves **multiple crossings with A or B**, pushing the total time above 17 minutes.

## Final Answer

**Minimum total time: 17 minutes**

# Reference

* [1] [Bridge and Torch Problem (River Crossing Puzzle)](https://en.wikipedia.org/wiki/Bridge_and_torch_problem)
