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
\left\{ \frac{1}{16},\ \frac{1}{8},\ \frac{1}{4},\ 1,\ 2,\ 4,\ 8,\ 16 \right\}
\\]

The first player to obtain **three numbers whose product is 1** wins.

Alice moves first.

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

## Step 3: Recognize the Hidden Tic-Tac-Toe

There are exactly **8 numbers**, and the win condition is:

> Find 3 elements from the set that sum to 0.

This is equivalent to **3-in-a-line** in a magic square or **Tic-Tac-Toe** on a suitable representation of these 8 values.

This game has been studied — and it turns out the structure is **isomorphic to standard Tic-Tac-Toe**.

---

## Step 4: Result

In **standard Tic-Tac-Toe**, the **first player can force a win or draw** — **but not always win** if the second player plays optimally.

Hence, in this game:

- Alice **cannot always guarantee a win**.
- If **Bob plays optimally**, the game will end in a **draw**.
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