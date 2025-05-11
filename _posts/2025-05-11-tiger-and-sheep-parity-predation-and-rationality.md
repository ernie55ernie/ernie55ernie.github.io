---
layout: post
title: "Tiger and Sheep: Parity, Predation, and Rationality"
date: 2025-05-11
category: quantitative interview
---

## Tiger and Sheep: Parity, Predation, and Rationality

Imagine 100 rational tigers and 1 lone sheep stranded on a magical island. The only food source is grass, which the sheep can eat, but the tigers prefer meat—and specifically, they’d love to eat the sheep. However, there's a catch:

- If a tiger eats the sheep, **it becomes a sheep itself**.
- Only one tiger can eat at any given moment.
- All tigers are **perfectly rational**, prioritizing their **own survival** above all else.
- If indifferent in outcome, a tiger prefers **fewer fellow survivors** (more tigers dead).

The question: *Will the sheep ever be eaten?*

## Backward Induction Solution

We solve this through **backward induction**, analyzing from smaller cases up:

### 1 Tiger, 1 Sheep
- The tiger eats the sheep, becomes a sheep.
- Now alone, no threat. **Survival guaranteed.**
- **Outcome**: Tiger eats the sheep.

### 2 Tigers, 1 Sheep
- If a tiger eats the sheep, it becomes a sheep.
- Left with 1 tiger and 1 sheep.
- From above, we know the lone tiger will eat the new sheep.
- **Result**: The first tiger dies.
- **No rational tiger acts.** The sheep survives.

### 3 Tigers, 1 Sheep
- If a tiger eats the sheep, it becomes a sheep.
- Left with 2 tigers, 1 sheep.
- From above, no one eats.
- First tiger-turned-sheep survives.
- **A rational tiger sees that eating leads to survival.** The sheep is eaten.

### 4 Tigers, 1 Sheep
- Eating leads to 3 tigers, 1 sheep.
- We know from above: a sheep will get eaten in a 3-tiger scenario.
- So the first tiger who eats will ultimately die.
- **No one eats.** The sheep survives.

This alternating pattern continues:

- **Odd number of tigers**: One will dare to eat the sheep.
- **Even number of tigers**: No tiger will eat—it’s suicidal.

### Case of 100 Tigers, 1 Sheep

100 is even. So, **no tiger will eat the sheep**.

## Final Answer

**The sheep survives.**

Rational tigers recognize that making the first move will ultimately lead to their own death, so none act.

# Reference

* [1] [Tigers & The Sheep](https://brainstellar.com/puzzles/strategy/7)