---
layout: post
title: "Naive Recursive Fibonacci: Why It Explodes and How to Fix It"
date: 2025-05-22
category: quantitative interview
---

### The Classic Pitfall

Here’s the textbook recursive implementation of the Fibonacci function:

```cpp
int Fibonacci(int n) {
    if (n <= 0)   return 0;
    else if (n == 1) return 1;
    else
        return Fibonacci(n-1) + Fibonacci(n-2);
}
```

---

## 1. Exponential Running Time

Let \\( T(n) \\) be the time it takes to compute \\( F(n) \\). The recurrence:

$$
T(n) \approx T(n-1) + T(n-2) + O(1)
$$

has the same structure as the Fibonacci sequence itself. The growth rate is governed by the **golden ratio**:

$$
\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618
$$

Thus,

$$
T(n+1) \approx \varphi \cdot T(n)
$$

For instance, if \\( T(n) = 100 \\) seconds, then:

$$
T(n+1) \approx 1.618 \times 100 \approx 162 \text{ seconds}
$$

This exponential growth makes the naive approach intractable even for moderately large \\( n \\).

---

## 2. Is It Efficient?

**No.** The naive recursion performs **exponentially redundant work**. It recomputes the same subproblems over and over.

* **Time Complexity**: \\( O(\varphi^n) \\)
* **Space Complexity**: \\( O(n) \\) (due to call stack)

---

## 3. Faster Alternatives

### a. Dynamic Programming (Bottom-Up)

```python
def fibonacci_dp(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

* **Time**: \\( O(n) \\)
* **Space**: \\( O(1) \\)

---

### b. Memoized Recursion

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
```

* **Time**: \\( O(n) \\)
* **Space**: \\( O(n) \\)

---

### c. Matrix Exponentiation / Fast Doubling

Use:

$$
\begin{pmatrix}
F_{n+1} \\
F_n
\end{pmatrix}
=
\begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}^{\!n}
\begin{pmatrix}
1 \\
0
\end{pmatrix}
$$

Or the **fast doubling formulas**:

$$
F_{2k} = F_k(2F_{k+1} - F_k), \quad F_{2k+1} = F_{k+1}^2 + F_k^2
$$

These compute \\( F(n) \\) in \\( O(\log n) \\) time.

---

## Conclusion

Avoid the naive recursion at all costs. For serious applications, use:

* **Dynamic Programming** for clarity and simplicity
* **Fast Doubling** for large \\( n \\) and logarithmic performance

---

## Reference

* \[1] [Fibonacci Number Algorithms – Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number#Efficient_computation)