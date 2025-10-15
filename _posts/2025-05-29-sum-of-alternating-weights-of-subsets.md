---
layout: post
title: "Sum of Alternating Weights of Subsets of {1, 2, ..., 2013}"
date: 2025-05-29
category: quantitative interview
---

## Problem

Let \\( S = \{1, 2, \dots, 2013\} \\).  
For each subset \\( A = \{a_1 < a_2 < \dots < a_k\} \subseteq S \\), define the **weight** of \\( A \\) as:

\\[
w(A) = a_1 - a_2 + a_3 - a_4 + \dots + (-1)^{k+1} a_k
\\]

What is the **sum of the weights** over all subsets of \\( S \\)?

---

## Insight: Pairing Trick

- Consider subsets **without** the number 1.
- There are \\( 2^{2012} \\) such subsets.
- For each such subset \\( S \\), pair it with \\( \{1\} \cup S \\).
- For each pair \\( (S, \{1\} \cup S) \\), the total weight is:

\\[
w(S) + w(\{1\} \cup S) = 1
\\]

#### Example:

\\[
w({2,5,8}) = 2 - 5 + 8 = 5
\\]
\\[
w({1,2,5,8}) = 1 - 2 + 5 - 8 = -4
\\]
\\[
\Rightarrow \text{Total} = 1
\\]

---

## Final Calculation

There are \\( 2^{2012} \\) such disjoint pairs, each contributing 1 to the total sum:

\\[
\boxed{\sum w(A) = 2^{2012}}
\\]

---

## Conclusion

The sum of the weights of all subsets of \\( \{1, 2, \dots, 2013\} \\) is:

\\[
\boxed{2^{2012}}
\\]

# Reference

* [1] [1983 AIME Problems/Problem 13](https://artofproblemsolving.com/wiki/index.php/1983_AIME_Problems/Problem_13)