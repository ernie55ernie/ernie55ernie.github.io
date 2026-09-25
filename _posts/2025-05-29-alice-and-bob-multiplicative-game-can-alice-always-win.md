---
layout: post
title: "Alice and Bob Multiplicative Game: Can Alice Always Win?"
date: 2025-05-29
category: quantitative interview
---

## Game Description

Players: Alice and Bob  
They take turns choosing one number at a time from the following set, **without replacement**:

\\[
{ \frac{1}{16},\ \frac{1}{8},\ \frac{1}{4},\ 1,\ 2,\ 4,\ 8,\ 16}
\\]

The first player to obtain **three numbers whose product is 1** wins.

Alice moves first.

<iframe src="{{ site.baseurl }}/assets/can_alice_always_win.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

---

## Step 1: Change the Problem to Additive

Take the **base-2 logarithm** of all numbers:

| Number     | \\( \log_2 \\) value |
|------------|-------------------|
| \\( \frac{1}{16} \\) | \\( -4 \\)            |
| \\( \frac{1}{8} \\)  | \\( -3 \\)            |
| \\( \frac{1}{4} \\)  | \\( -2 \\)            |
| \\( 1 \\)           | \\( 0 \\)             |
| \\( 2 \\)           | \\( 1 \\)             |
| \\( 4 \\)           | \\( 2 \\)             |
| \\( 8 \\)           | \\( 3 \\)             |
| \\( 16 \\)          | \\( 4 \\)             |

So instead of finding three numbers whose **product** is 1, we're now finding three numbers whose **sum of logs** is:

\\[
\log_2(a) + \log_2(b) + \log_2(c) = \log_2(abc) = \log_2(1) = 0
\\]

---

## Step 2: Reformulate

The problem becomes:

> Alice and Bob take turns choosing one number from the set  
> \\[
> \{-4, -3, -2, 0, 1, 2, 3, 4\}
> \\]  
> without replacement.  
> Whoever gets **three numbers that sum to 0** wins.

---

## Step 3: Analyze the Winning Lines

Let's list all the possible triplets from this set that sum to 0:

1. \\( \{-4, 0, 4\} \\)
2. \\( \{-3, 0, 3\} \\)
3. \\( \{-2, 0, 2\} \\)
4. \\( \{-4, 1, 3\} \\)
5. \\( \{-3, 1, 2\} \\)

There are exactly **5 winning lines**. 

*(Note: This is often confused with the game of choosing numbers from 1 to 9 that sum to 15, which has 9 numbers, 8 winning lines, and is isomorphic to Tic-Tac-Toe. Our game here is much sparser!)*

---

## Step 4: Result

Because this game has only 8 numbers and 5 winning lines, it is significantly harder to form winning combinations than in Tic-Tac-Toe. 

- Alice **cannot force a win**. She has too few winning lines to easily set up an unblockable "double threat" if Bob plays optimally.
- By the **strategy-stealing argument** (having an extra number is never a disadvantage), Alice can guarantee at least a draw.
- If **Bob plays optimally** (e.g., picking central numbers like \\( -3 \\) or \\( 0 \\) to block multiple lines), the game will end in a **draw**.
- But if **Bob makes a mistake**, Alice **can win**.

---

## Conclusion

\\[
\boxed{
\text{Alice cannot always win, but she can force at least a draw with optimal play.}
}
\\]

# Reference

* [1] [Bob and Alice are playing the following game: Each of them chooses a number between 1 and 9 without replacement. The first one to get 3 numbers which sum to 15 wins. Does any of them have a winning strategy?](https://www.quora.com/Bob-and-Alice-are-playing-the-following-game-Each-of-them-chooses-a-number-between-1-and-9-without-replacement-The-first-one-to-get-3-numbers-which-sum-to-15-wins-Does-any-of-them-have-a-winning-strategy#:~:text=There%20are%20precisely%208%20ways,x%203%20grid%20as%20follows.)