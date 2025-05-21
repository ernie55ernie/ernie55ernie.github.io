---
layout: post
title: "In-Place Variable Swap: No Temp Needed"
date: 2025-05-21
category: quantitative interview
---

### Problem

You have two integer variables, `i` and `j`. How can you **swap** their values **without using any extra storage**, i.e., no temporary variable?

---

## Solution Using Arithmetic

You can swap `i` and `j` in-place using arithmetic operations:

```python
i = i + j
j = i - j
i = i - j
```

### Example:

Suppose initially `i = 3` and `j = 5`:

* Step 1: `i = 3 + 5 = 8`
* Step 2: `j = 8 - 5 = 3` (original `i`)
* Step 3: `i = 8 - 3 = 5` (original `j`)

Now `i = 5`, `j = 3` — swap complete!

**Note**: This method works reliably for integers as long as there's no overflow in the arithmetic operations.

---

## Alternative: Bitwise XOR Method

You can also use the XOR bitwise operation (which is common in low-level programming):

```python
i = i ^ j
j = i ^ j
i = i ^ j
```

### Explanation:

* XOR is reversible: \\( a \oplus b \oplus b = a \\)

This version avoids potential overflow, making it safer for bounded integer types in systems languages like C.

---

## Conclusion

There are two common in-place swap techniques:

* **Arithmetic swap**: `i = i + j; j = i - j; i = i - j`
* **Bitwise XOR swap**: `i = i ^ j; j = i ^ j; i = i ^ j`

Both accomplish the swap **without any temporary storage**.

---

## Reference

* [1] [In-place swapping algorithms](https://en.wikipedia.org/wiki/XOR_swap_algorithm)