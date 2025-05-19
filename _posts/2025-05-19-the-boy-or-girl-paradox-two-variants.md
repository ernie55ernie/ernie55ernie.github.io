---
layout: post
title: "The Boy or Girl Paradox: Two Variants"
date: 2025-05-19
category: quantitative interview
---

This classic paradox explores how subtly different phrasing in probability problems can lead to distinct outcomes. We'll examine two versions involving two-child families.

---

## Part A: "At Least One Son"

**Given:** Ms. Jackson has two children. You are told that *at least one* is a boy.

**Question:** What is the probability that *both* children are boys?

### Analysis

There are four equally likely combinations of two children:

- Boy–Boy (BB)
- Boy–Girl (BG)
- Girl–Boy (GB)
- Girl–Girl (GG)

The "at least one is a boy" condition eliminates GG, leaving:

- BB
- BG
- GB

These remaining cases are equally likely, so:

- Only 1 out of 3 has both children as boys.

### Answer:

\\[
P(\text{both are boys} \mid \text{at least one is a boy}) = \boxed{\frac{1}{3}}
\\]

---

## Part B: "You See a Boy"

**Given:** Ms. Parker has two children, and you *see* one of them, a boy.

**Question:** What is the probability that *both* children are boys?

### Analysis

This is a subtler form of conditioning. You’re not told abstractly that “at least one is a boy.” Instead, you directly observe a boy—without knowing if he's the older or younger child.

Each family combination (BB, BG, GB, GG) is equally likely to begin with. Now consider the chance that you *see a boy* under each scenario:

- **BB**: Seeing a boy is guaranteed (either child is a boy).
- **BG**: 50% chance (you might see the boy or the girl).
- **GB**: 50% chance.
- **GG**: 0% chance (no boys to see).

Weight the likelihoods based on visibility:

- BB: 1
- BG: 0.5
- GB: 0.5
- GG: 0

Normalize:

- Total weight: \\( 1 + 0.5 + 0.5 = 2 \\)
- BB has weight 1 out of 2.

### Answer:

\\[
P(\text{both are boys} \mid \text{you see a boy}) = \boxed{\frac{1}{2}}
\\]

---

## Conclusion

These two problems differ in how the information is obtained:

- **Part A** conditions on a *fact* about the family.
- **Part B** conditions on a *specific observation*.

This small shift leads to very different probabilities: \\( \frac{1}{3} \\) versus \\( \frac{1}{2} \\).

## Reference

* [1] [Wikipedia: Boy or Girl paradox](https://en.wikipedia.org/wiki/Boy_or_girl_paradox)
