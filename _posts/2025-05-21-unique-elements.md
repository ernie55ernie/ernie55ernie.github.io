---
layout: post
title: "Remove Duplicates from a Sorted Array"
date: 2025-05-21
category: quantitative interview
---

### Problem

Given a **sorted array**, remove duplicates so that each element appears **only once**. Return the result either as a **new list** or **in-place**.

**Example:**

Input:

```

[1, 1, 3, 3, 3, 5, 5, 5, 9, 9, 9, 9]

```

Output:

```

[1, 3, 5, 9]

````

---

## Solution: New List Approach

```python
def remove_duplicates_sorted(arr):
    if not arr:
        return []
    
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            result.append(arr[i])
    return result
````

---

## Solution: In-Place Modification (Optional Return Length)

If modifying the original array in place is desired:

```python
def remove_duplicates_in_place(arr):
    if not arr:
        return 0
    
    write = 1
    for read in range(1, len(arr)):
        if arr[read] != arr[read - 1]:
            arr[write] = arr[read]
            write += 1
    return arr[:write]  # or return write to get the new length
```

---

## Complexity

* **Time Complexity**: \\( O(n) \\)
* **Space Complexity**:

  * New list: \\( O(n) \\)
  * In-place: \\( O(1) \\) extra space

---

## Reference

* [1] [Leetcode 26: Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)