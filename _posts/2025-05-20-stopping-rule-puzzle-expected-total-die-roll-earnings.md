---
layout: post
title: "Stopping Rule Puzzle: Expected Total Die Roll Earnings"
date: 2025-05-20
category: quantitative interview
---

### The Setup

You roll a fair 6-sided die repeatedly. The rules are:

- After each roll, you **earn** an amount equal to the face value shown.
- If you roll a **4, 5, or 6**, you get to **roll again**.
- If you roll a **1, 2, or 3**, the game **ends immediately**.

### Question:

What is the **expected total payout** from this process?

---

## Let the Expected Total Be \\( E \\)

We compute \\( E \\) using a recursive expectation. Consider the expected value of the first roll:

\[
E = \sum_{i=1}^{6} \frac{1}{6} \left[\text{earn } i + \text{continue or stop}\right]
\]

Break it into two parts:

- For rolls 1, 2, 3: the game ends after this roll
- For rolls 4, 5, 6: you earn the value and then continue with expectation \\( E \\)

### Compute Explicitly:

\[
E = \frac{1}{6}(1 + 2 + 3) + \frac{1}{6}[(4 + E) + (5 + E) + (6 + E)]
\]

\[
E = \frac{6}{6} + \frac{1}{6}(15 + 3E) = 1 + \frac{15}{6} + \frac{3E}{6}
= \frac{21}{6} + \frac{1}{2}E
\]

Now solve for \\( E \\):

\[
E = \frac{21}{6} + \frac{1}{2}E
\Rightarrow \frac{1}{2}E = \frac{21}{6}
\Rightarrow E = \frac{42}{6} = \boxed{7}
\]

---

## Final Answer

\[
\boxed{7}
\]

So the **expected total payout** under this stopping rule is **7 dollars**.

---

## Reference

* [1] [Expected payoff of dice game](https://math.stackexchange.com/questions/4122166/expected-payoff-of-dice-game)