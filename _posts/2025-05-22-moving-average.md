---
layout: post
title: "Sliding-Window Average in O(m) Time"
date: 2025-05-22
category: quantitative interview
---

### Problem

Given:

- A large array \\( A \\) of length \\( m \\)
- A window size \\( n \\)

Compute a new array \\( B \\) of length \\( m - n + 1 \\), where each entry is the average of a sliding window of \\( n \\) consecutive elements of \\( A \\):

\\[
B_i = \frac{A_{i-n+1} + A_{i-n+2} + \cdots + A_i}{n}
\\]

for \\( i = n, n+1, \dots, m \\).

---

## Naive Approach: \\( O(mn) \\)

Iterate over every window and sum \\( n \\) elements per window:

```python
for i in range(n - 1, m):
    B[i - n + 1] = sum(A[i - n + 1 : i + 1]) / n
```

This takes \\( O(mn) \\) time—not efficient for large \\( m \\).

---

## Efficient Solution: \\( O(m) \\) Time Using Sliding Sum

Maintain a running sum of the current window:

### Python Code

```python
def sliding_average(A, n):
    m = len(A)
    B = []
    window_sum = sum(A[:n])
    B.append(window_sum / n)

    for i in range(n, m):
        window_sum += A[i] - A[i - n]
        B.append(window_sum / n)
    
    return B
```

### Explanation

* Start with the sum of the first \\( n \\) elements
* For each new step:

  * Add the incoming element
  * Subtract the outgoing element
* This maintains the sum in constant time per step

---

## Complexity

* **Time**: \\( O(m) \\)
* **Space**: \\( O(m - n + 1) \\)

---

## Final Thoughts

The sliding-window trick is powerful for turning a brute-force \\( O(mn) \\) problem into a linear-time \\( O(m) \\) solution—ideal for streaming and real-time applications.

---

## Reference

* [1] [Moving average – Wikipedia](https://en.wikipedia.org/wiki/Moving_average)
