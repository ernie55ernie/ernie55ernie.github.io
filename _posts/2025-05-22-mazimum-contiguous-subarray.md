---
layout: post
title: "Maximum Contiguous Subarray: Kadane’s Algorithm"
date: 2025-05-22
category: quantitative interview
---

### Problem

Given a one-dimensional array \\( A[1..n] \\) of both positive and negative numbers, find the **contiguous subarray** \\( A[i..j] \\) such that the **sum**:

\\[
\sum_{k=i}^{j} A[k]
\\]

is **maximized**.

---

## Naive Approach

Try all possible \\( O(n^2) \\) subarrays and compute their sums.

- **Time complexity**: \\( O(n^2) \\) or \\( O(n^3) \\)
- **Space**: \\( O(1) \\)

Too slow for large inputs.

---

## Kadane’s Algorithm: Linear Time \\( O(n) \\)

**Key Insight**: Track the best sum ending at each position, and reset when the running sum becomes negative.

### Python Code

```python
def max_subarray(A):
    max_sum = curr_sum = A[0]
    start = end = temp_start = 0

    for i in range(1, len(A)):
        if curr_sum < 0:
            curr_sum = A[i]
            temp_start = i
        else:
            curr_sum += A[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i

    return max_sum, start, end
```

---

## Example

Input:

```python
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

Output:

```python
max_sum = 6, indices = (3, 6), subarray = [4, -1, 2, 1]
```

---

## Time and Space Complexity

* **Time**: \\( O(n) \\)
* **Space**: \\( O(1) \\) (if just returning sum) or \\( O(1) \\) extra for tracking indices

---

## Final Answer

Kadane’s algorithm computes the **maximum contiguous subarray sum** in:

$$
\boxed{O(n) \text{ time, } O(1) \text{ space}}
$$

---

## Reference

* [1] [Kadane’s Algorithm – Wikipedia](https://en.wikipedia.org/wiki/Maximum_subarray_problem)