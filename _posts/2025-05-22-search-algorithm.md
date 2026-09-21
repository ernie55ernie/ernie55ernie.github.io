---
layout: post
title: "Three Classic Search Problems: Min/Max, Sparse Array, and Matrix Search"
date: 2025-05-22
category: quantitative interview
---

### A. Min & Max in \\( \frac{3n}{2} \\) Comparisons

**Problem**: Given \\( n \\) elements, find **both** the minimum and maximum using as few comparisons as possible.

#### Naive Method

- \\( n-1 \\) comparisons to find min
- \\( n-1 \\) comparisons to find max  
⟶ Total: \\( 2n - 2 \\) comparisons

#### Optimized Solution (Tournament Pairing)

Group elements into **pairs** and compare each pair:
- For each pair, one comparison identifies the local min and max.
- Then:
  - Compare local mins to find global min (\\( n/2 - 1 \\) comparisons)
  - Compare local maxes to find global max (\\( n/2 - 1 \\) comparisons)

For even \\( n \\), the number of comparisons is:

\\[
\frac{n}{2} + \left( \frac{n}{2} - 1 \right) + \left( \frac{n}{2} - 1 \right) = \frac{3n}{2} - 2
\\]

For odd \\( n \\), the unpaired element is tested against the local mins and maxes, bringing the total to \\( \frac{3(n-1)}{2} \\). 

In general, the worst-case number of comparisons is exactly:

\\[
\boxed{\left\lceil \frac{3n}{2} \right\rceil - 2}
\\]

---

### B. First Nonzero in 0→Nonzero Array of Unknown Length

**Problem**: The array starts with a run of zeros, then switches to nonzeros. Find the index of the **first nonzero**, without knowing the array length.

#### Strategy: Exponential Search + Binary Search

1. **Exponential Search**:
   - Test indices: 1, 2, 4, 8, ... until you find a nonzero (say at index \\( 2^k \\))
2. **Binary Search**:
   - Between \\( 2^{k-1} \\) and \\( 2^k \\)

This narrows down the transition point in \\( O(\log n) \\) time.

---

### C. Searching a Row- and Column-Sorted Matrix

**Problem**: Matrix is sorted left-to-right and top-to-bottom. Find a target value.

#### Strategy: Staircase Search

Start at the **top-right** element.

At each step:

- If the current element is **equal**, return true.
- If it’s **greater**, move **left**
- If it’s **less**, move **down**

#### Time Complexity

- Each step eliminates a row or a column
- Maximum \\( m + m = 2m \\) steps for \\( m \times m \\) matrix

\\[
\boxed{O(m)}
\\]

---

## Summary

| Problem                                | Strategy                          | Time Complexity         |
|----------------------------------------|-----------------------------------|--------------------------|
| Min & Max from \\( n \\) elements         | Tournament pairing                | \\( \boxed{\left\lceil \frac{3n}{2} \right\rceil - 2} \\) comparisons |
| First nonzero in sparse array          | Exponential + binary search       | \\( O(\log n) \\)         |
| Search in sorted matrix                | Staircase (top-right traversal)   | \\( O(m) \\)              |

---

## Reference

* [1] [Finding the maximum and minimum elements using 3n / 2 comparisons? [closed]](https://stackoverflow.com/questions/35052270/finding-the-maximum-and-minimum-elements-using-3n-2-comparisons)
* [2] [Exponential Search – Wikipedia](https://en.wikipedia.org/wiki/Exponential_search)
