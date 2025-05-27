---
layout: post
title: "C++ Implementations of the Fibonacci Function"
date: 2025-05-26
category: quantitative interview
---

We present three ways to compute the \\( n \\)-th Fibonacci number in C++:

---

### 1. Recursive Implementation

Simple but inefficient due to exponential time complexity and repeated computation.

```cpp
int fib_recursive(int n) {
    if (n <= 1) return n;
    return fib_recursive(n - 1) + fib_recursive(n - 2);
}
```

---

### 2. Iterative Implementation

Efficient, uses constant space and linear time.

```cpp
int fib_iterative(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; ++i) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}
```

---

### 3. Tail-Recursive Implementation

Tail recursion can be optimized by compilers into iteration.

```cpp
int fib_tail_helper(int n, int a, int b) {
    if (n == 0) return a;
    return fib_tail_helper(n - 1, b, a + b);
}

int fib_tail_recursive(int n) {
    return fib_tail_helper(n, 0, 1);
}
```

---

### Example Usage

```cpp
#include <iostream>

int main() {
    int n = 10;
    std::cout << "Recursive: " << fib_recursive(n) << "\n";
    std::cout << "Iterative: " << fib_iterative(n) << "\n";
    std::cout << "Tail-recursive: " << fib_tail_recursive(n) << "\n";
    return 0;
}
```

# Reference

* [1] [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)