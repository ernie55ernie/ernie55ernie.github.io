---
layout: post
title: "Fisher–Yates Shuffle and Reservoir Sampling"
date: 2025-05-22
category: quantitative interview
---

Two classic algorithmic challenges in randomized computation are:

1. **Generating a perfect random permutation** (uniformly over all \\( n! \\) orderings).
2. **Sampling uniformly from a stream of unknown length**.

---

## 1. Perfect Shuffling: Fisher–Yates Algorithm

### Problem

Given a list of \\( n \\) items (e.g., a 52-card deck), generate a **random permutation** such that each of the \\( n! \\) possible orders is **equally likely**.

### Fisher–Yates Algorithm

Iterate backwards through the array and for each index \\( i \\), swap the element at \\( i \\) with a randomly chosen element from index \\( 0 \) to \\( i \\):

```python
import random

def fisher_yates_shuffle(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
```

### Properties

* **Time Complexity**: \\( O(n) \\)
* **Space Complexity**: \\( O(1) \\) (in-place)
* **Uniformity**: Ensures every permutation appears with probability \\( 1/n! \\)

---

## 2. Sampling from Unknown-Length Stream: Reservoir Sampling (\\( k = 1 \\))

### Problem

Given a stream of unknown length, return **one item uniformly at random**, using only \\( O(1) \\) space.

### Reservoir Sampling Algorithm (\\( k = 1 \\))

```python
import random

def reservoir_sample(stream):
    result = None
    for i, item in enumerate(stream, start=1):
        if random.random() < 1 / i:
            result = item
    return result
```

### Why It Works

At step \\( i \\), each previous item has a \\( 1/i \\) chance of being replaced. By induction, each item in the stream has probability \\( 1/n \\) of being selected after \\( n \\) items.

### Properties

* **Time Complexity**: \\( O(n) \\) for a stream of length \\( n \\)
* **Space Complexity**: \\( O(1) \\)
* **Uniformity**: Every item has equal chance of being chosen

---

## Summary

| Problem                               | Solution                           | Uniform? | Time         | Space        |
| ------------------------------------- | ---------------------------------- | -------- | ------------ | ------------ |
| Random permutation of \\( n \\) items | Fisher–Yates Shuffle               | Yes      | \\( O(n) \\) | \\( O(1) \\) |
| Sample one item from a stream         | Reservoir Sampling (\\( k = 1 \\)) | Yes      | \\( O(n) \\) | \\( O(1) \\) |

---

## Reference

* [1] [Fisher–Yates Shuffle – Wikipedia](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)
* [2] [Reservoir Sampling – Wikipedia](https://en.wikipedia.org/wiki/Reservoir_sampling)