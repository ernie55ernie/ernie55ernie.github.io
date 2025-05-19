---
layout: post
title: "Simulating a Fair Coin with a Biased One: The Von Neumann Extractor"
date: 2025-05-19
category: quantitative interview
---

Suppose you have a coin that comes up heads with **unknown** probability \\( p \ne \frac{1}{2} \\). Can you simulate a perfectly fair (50/50) coin using only this biased coin?

### Yes—Using a Clever Trick

This is known as the **Von Neumann extractor**, a classic example of extracting unbiased randomness from biased sources.

---

## The Procedure

1. **Flip the biased coin twice.**
2. If the result is **HT**, output “heads.”
3. If the result is **TH**, output “tails.”
4. If the result is **HH** or **TT**, **discard and repeat** from step 1.

---

## Why This Works

Let’s look at the probabilities of each pair:

- \\( \Pr(\text{HT}) = p(1 - p) \\)
- \\( \Pr(\text{TH}) = (1 - p)p \\)
- \\( \Pr(\text{HH}) = p^2 \\)
- \\( \Pr(\text{TT}) = (1 - p)^2 \\)

Notice:

\\[
\Pr(\text{HT}) = \Pr(\text{TH}) = p(1 - p)
\\]

So when we get **HT or TH**, we’re equally likely to be in either situation. This makes the outcome **unbiased**, even though we used a **biased** coin.

The process discards **HH** and **TT** because these do not yield symmetric outcomes.

---

## Efficiency

The expected number of coin flips per fair bit is:

\\[
\frac{2}{2p(1 - p)} = \frac{1}{p(1 - p)}
\\]

So if \\( p \\) is close to 0 or 1, the method becomes inefficient (since the chance of HH or TT increases). But it always produces unbiased results **eventually**.

---

## Conclusion

The von Neumann extractor is a beautifully simple and elegant method to simulate a fair coin using a biased one—by relying only on symmetric outcomes in consecutive trials.

## Reference

* [1] [Wikipedia: Von Neumann extractor](https://en.wikipedia.org/wiki/Randomness_extractor#Von_Neumann_extractor)
