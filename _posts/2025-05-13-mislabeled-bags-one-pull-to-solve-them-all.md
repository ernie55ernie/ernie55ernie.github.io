---
layout: post
title: "Mislabeled Bags: One Pull to Solve Them All"
date: 2025-05-13
category: quantitative interview
---

This classic logic puzzle tests your deductive reasoning with minimal information:

> You have **three bags**:
> 1. One has only **apples**
> 2. One has only **oranges**
> 3. One has a **mix of both**
>
> Each is labeled (“apple,” “orange,” or “mix”) — but **all labels are wrong**.  
> You may reach into any bag and pull out **one fruit at a time (without looking)**.  
>
> **Goal:** Determine the correct contents of all three bags with the **fewest possible pulls**.

---

<iframe src="{{ site.baseurl }}/assets/mislabeled_bags_visualization.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

## Step-by-Step Strategy

### Step 1: Pick the Bag Labeled “Mix”

Since **all labels are wrong**, the bag labeled “mix” **must contain only apples or only oranges**.

Reach into the **bag labeled “mix”** and pull out **one fruit**.

Let’s say you pull out an **apple**.

Then you know:
- This bag cannot be the mix (because its label is wrong).
- Since it must be a single-fruit bag and you pulled an apple, it is the **apple-only** bag.

### Step 2: Deduce the Others

Now you know the bag labeled “mix” actually contains **only apples**. 

What about the bag labeled "apple"?
- It cannot contain apples (since all labels are wrong, and we already found the apple bag anyway).
- Could it contain the **mix**? If it did, the third bag (labeled "orange") would have to contain **only oranges**. But we know **all labels are wrong**, so that's impossible!
- Therefore, the bag labeled "apple" must contain **only oranges**.

By elimination, the third bag (labeled "orange") must contain the **mix**.

---

## Final Answer

> **Pull one fruit from the bag labeled “mix.”**  
> If it's an apple → that bag is apples.  
> Use the “all labels wrong” rule to deduce the other two.

# Reference

* [1] [Brain Teaser 18: Mislabeled Bags](https://medium.com/@shelvia1039/brain-teaser-18-mislabeled-bags-1581b1278173)
