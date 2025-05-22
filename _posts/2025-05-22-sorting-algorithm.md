---
layout: post
title: "Five Classic Sorting Algorithms: Descriptions and Complexity"
date: 2025-05-22
category: quantitative interview
---

This post describes **five well-known sorting algorithms** that can sort a list of \\( n \\) distinct elements \\( A_1, A_2, \dots, A_n \\). We analyze each algorithm in terms of **time** and **space** complexity.

---

### 1. Insertion Sort

**Description**:
Builds the sorted array one item at a time. At each step, it inserts the next element into its correct position among the previously sorted elements.

**Pseudocode**:
```python
for i in range(1, n):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = key
```

**Complexity**:

* **Time**:

  * Worst-case: \\( O(n^2) \\)
  * Best-case (already sorted): \\( O(n) \\)
* **Space**: \\( O(1) \\)

---

### 2. Merge Sort

**Description**:
A divide-and-conquer algorithm. Splits the array into halves, recursively sorts each half, then merges the sorted halves.

**Pseudocode**:

```python
def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left, right)
```

**Complexity**:

* **Time**: \\( O(n \log n) \\) in all cases
* **Space**: \\( O(n) \\) extra space for merging

---

### 3. Quick Sort

**Description**:
A divide-and-conquer algorithm. Chooses a pivot, partitions the array into elements less than and greater than the pivot, then recursively sorts the partitions.

**Pseudocode**:

```python
def quick_sort(A):
    if len(A) <= 1:
        return A
    pivot = A[0]
    left = [x for x in A[1:] if x < pivot]
    right = [x for x in A[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
```

**Complexity**:

* **Time**:

  * Average: \\( O(n \log n) \\)
  * Worst-case: \\( O(n^2) \\) (e.g., already sorted and poor pivot)
* **Space**:

  * Average: \\( O(\log n) \\) for recursive calls

---

### 4. Bubble Sort

**Description**:
Repeatedly compares adjacent elements and swaps them if out of order. Continues until no swaps are needed.

**Pseudocode**:

```python
for i in range(n):
    for j in range(0, n - i - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
```

**Complexity**:

* **Time**:

  * Worst and Average: \\( O(n^2) \\)
  * Best (already sorted): \\( O(n) \\)
* **Space**: \\( O(1) \\)

---

### 5. Selection Sort

**Description**:
Repeatedly finds the smallest remaining element and swaps it into the next position.

**Pseudocode**:

```python
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if A[j] < A[min_index]:
            min_index = j
    A[i], A[min_index] = A[min_index], A[i]
```

**Complexity**:

* **Time**: \\( O(n^2) \\) in all cases
* **Space**: \\( O(1) \\)

---

## Summary Table

| Algorithm      | Time (Best)         | Time (Avg)          | Time (Worst)        | Space             |
| -------------- | ------------------- | ------------------- | ------------------- | ----------------- |
| Insertion Sort | \\( O(n) \\)        | \\( O(n^2) \\)      | \\( O(n^2) \\)      | \\( O(1) \\)      |
| Merge Sort     | \\( O(n \log n) \\) | \\( O(n \log n) \\) | \\( O(n \log n) \\) | \\( O(n) \\)      |
| Quick Sort     | \\( O(n \log n) \\) | \\( O(n \log n) \\) | \\( O(n^2) \\)      | \\( O(\log n) \\) |
| Bubble Sort    | \\( O(n) \\)        | \\( O(n^2) \\)      | \\( O(n^2) \\)      | \\( O(1) \\)      |
| Selection Sort | \\( O(n^2) \\)      | \\( O(n^2) \\)      | \\( O(n^2) \\)      | \\( O(1) \\)      |

---

## Reference

* [1] [Sorting Algorithm Comparison](https://en.wikipedia.org/wiki/Sorting_algorithm)
