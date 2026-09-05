---
layout: post
title: "Bridge and Torch: Racing Against the Dark"
date: 2025-05-12
category: quantitative interview
---

This classic puzzle tests our ability to optimize under constraints. Four people—A, B, C, and D—need to cross a bridge at night. They have only one torch, and at most two can cross at a time. The crossing speed of any pair is determined by the **slower** person.

### Crossing Times:
- **A**: 10 minutes
- **B**: 5 minutes
- **C**: 2 minutes
- **D**: 1 minute

The goal: **get everyone across as quickly as possible**.

<iframe src="{{ site.baseurl }}/assets/bridge_and_torch_problem.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

## The Naive Approach

It might seem intuitive to always use the absolute fastest person (D) to ferry everyone else across. Let's see what happens if we do that:

1. **D and A cross** (10 mins), **D returns** (1 min)
2. **D and B cross** (5 mins), **D returns** (1 min)
3. **D and C cross** (2 mins)

**Total Time = 19 minutes.** We can do better!

## Key Insight

To minimize time, we must overlap the largest time penalties by sending the two **slowest** people (A and B) across together. To facilitate this without stranding our fast people on the wrong side, we use the two fastest people (C and D) to stage the return trips.

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
