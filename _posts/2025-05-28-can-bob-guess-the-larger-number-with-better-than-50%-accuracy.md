---
layout: post
title: "Can Bob Guess the Larger Number with Better Than 50% Accuracy?"
date: 2025-05-28
category: quantitative interview
---

## Problem

Alice writes **two distinct real numbers between 0 and 1** on separate sheets. Bob:

1. Randomly selects and looks at one number.
2. Must guess whether the number he sees is **the larger or the smaller** of the two.

Can Bob devise a strategy that gives him **more than a 50% chance of being correct**?

---

## Naïve Strategy

If Bob has **no information** and randomly guesses "larger" or "smaller," he will be correct with probability:

\\[
\boxed{\frac{1}{2}}
\\]

But **can he do better**?

---

## Clever Strategy: Use a Random Threshold

Bob chooses a random number \\( r \\) from a known continuous distribution on \\( (0,1) \\), say **uniformly at random**.

Then his strategy is:

> If the number he sees is **less than \\( r \\)**, guess it is the **smaller** number.  
> If it is **greater than \\( r \\)**, guess it is the **larger** number.

---

### Why This Works

Let the two hidden numbers be \\( a < b \\). Bob randomly picks one of them to inspect. There are two cases:

- If he sees \\( a \\):
  - He guesses **"smaller"** if \\( a < r \\) — which is correct.
- If he sees \\( b \\):
  - He guesses **"larger"** if \\( b > r \\) — which is also correct.

Each has probability \\( \frac{1}{2} \\), so:

\\[
P(\text{correct}) = \frac{1}{2}P(r > b) + \frac{1}{2}P(r < a)
\\]

Because \\( r \sim \text{Uniform}(0,1) \\), these probabilities are \\( 1 - b \\) and \\( a \\), so:

\\[
P(\text{correct}) = \frac{1}{2}(1 - b + a)
\\]

Since \\( a < b \\), we have:

\\[
P(\text{correct}) > \frac{1}{2}
\\]

Thus, **Bob beats 50% accuracy**, regardless of what numbers Alice chooses!

---

## Conclusion

Yes — by comparing the revealed number to a random threshold, Bob can win more than 50% of the time.

This works because the strategy **introduces external randomness** to exploit the structure of the problem.

# Reference

* [1] [Puzzle: Guessing the bigger number!](https://math.stackexchange.com/questions/179897/puzzle-guessing-the-bigger-number)