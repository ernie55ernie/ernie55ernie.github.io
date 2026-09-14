---
layout: post
title: "All-Girl World Reproduction Puzzle"
date: 2025-05-19
category: quantitative interview
---

In this hypothetical society, every couple continues to have children until they have a girl, and then they stop. Each child is independently a girl with probability \\( \frac{1}{2} \\).

### Question:

**What fraction of the population will be girls in the long run?**

<iframe src="{{ site.baseurl }}/assets/girls_until_first_girl.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

---

## Intuitive Trap

At first glance, one might think there will be more girls than boys, since each family stops only after a girl is born. But let's explore this rigorously.

---

## Mathematical Analysis

Let’s suppose there are \\( N \\) couples.

### Births Per Family

Each family continues until a girl is born. The number of births per family follows a geometric distribution with success probability \\( p = \frac{1}{2} \\). The expected number of children per family is:

\\[
\mathbb{E}[\text{children per family}] = \sum_{k=1}^{\infty} k \cdot \left(\frac{1}{2}\right)^k = 2
\\]

So, for \\( N \\) families, there are \\( 2N \\) expected total children.

### Gender Distribution

Since each child is independently a girl with probability \\( \frac{1}{2} \\), the gender ratio among all births remains 1:1.

Hence, the expected number of girls is:

\\[
\mathbb{E}[\text{girls}] = N
\\]

And the expected number of boys is also:

\\[
\mathbb{E}[\text{boys}] = N
\\]

### Final Fraction

The fraction of the population that is girls is:

\\[
\frac{\text{girls}}{\text{girls} + \text{boys}} = \frac{N}{N + N} = \boxed{\frac{1}{2}}
\\]

---

## Conclusion

Despite the stopping rule that every family stops at the first girl, the fraction of girls in the population remains exactly **50%**. The key insight is that although every family guarantees a girl, the number of boys before that girl balances the overall ratio.

## Reference

* [1] [Geometric distribution in birth models](https://en.wikipedia.org/wiki/Geometric_distribution)
