---
layout: post
title: "Choosing Fairly Between Three Options Using a Coin"
date: 2025-05-27
category: quantitative interview
---

Alice wants to pick **one of three desserts**, each with **equal probability**, using **only a coin**. We consider two versions:

1. The coin is **fair**.
2. The coin is **biased**, but the **bias is unknown**.

---

### Part 1: Using a Fair Coin

A fair coin gives two outcomes: H (heads) or T (tails). Here's one strategy:

**Step 1: Encode the outcomes**
- Toss the coin **twice**:
  - HT → choose dessert 1
  - TH → choose dessert 2
  - HH → choose dessert 3
  - TT → **discard** and retry

**Why it works**:
- Each of HT, TH, HH, TT has probability \\( \frac{1}{4} \\).
- By discarding TT and re-tossing, you ensure that each valid outcome has equal probability \\( \frac{1}{3} \\).

**Expected number of tosses**:
- Probability of success per trial = \\( \frac{3}{4} \\)
- Expected tosses per success ≈ \\( \frac{2}{3/4} = \frac{8}{3} \\)

---

### Part 2: Using a Biased Coin (Bias Unknown)

Now the coin is biased, with unknown \\( p = P(H) \\), \\( 0 < p < 1 \\). We need a method that’s **unbiased regardless of \\( p \\)**.

**Von Neumann’s Trick**:
- Toss the coin twice:
  - HT → output 1
  - TH → output 0
  - HH or TT → discard and retry

This gives a **fair bit**.

#### Step-by-Step:

1. **Generate fair bits** using Von Neumann's method.
2. Use **two fair bits** to generate numbers 0–3:
   - 00 → dessert 1
   - 01 → dessert 2
   - 10 → dessert 3
   - 11 → **discard** and retry

Now each dessert has probability \\( \frac{1}{3} \\), using **only a biased coin** with unknown bias.

---

## Conclusion

- With a **fair coin**: Use 2 tosses; map 3 outcomes, reject the 4th.
- With a **biased coin**: Use **Von Neumann's method** to extract fair bits, then proceed as above.

Both strategies ensure each dessert has probability:

\\[
\boxed{\frac{1}{3}}
\\]

# Reference

* [1] [Most efficient way to decide between three options using only coin flips](https://www.reddit.com/r/math/comments/otx3w/most_efficient_way_to_decide_between_three/)