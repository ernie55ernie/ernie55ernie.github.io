---
layout: post
title: "Counting 1″ and 2″ Jump Sequences Using Matrix Exponentiation"
date: 2025-05-27
category: quantitative interview
---

We define \\( a_n \\) as the number of sequences of 1″ and 2″ jumps summing to \\( n \\). The recurrence is:

\\[
a_n = a_{n-1} + a_{n-2}, \quad \text{with } a_0 = 1, \; a_1 = 1.
\\]

This is identical to the Fibonacci sequence shifted by one index. That is,

\\[
a_n = F_{n+1}, \quad \text{where } F_n \text{ is the Fibonacci number with } F_0 = 0, F_1 = 1.
\\]

---

## Matrix Formulation

The Fibonacci sequence satisfies:

\\[
\begin{pmatrix}
F_{n+1} \\
F_n
\end{pmatrix}
=
\begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}^n
\begin{pmatrix}
1 \\
0
\end{pmatrix}.
\\]

Thus, to compute \\( a_{100} = F_{101} \\), we need to compute the top-left entry of:

\\[
\begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}^{100}
\begin{pmatrix}
1 \\
0
\end{pmatrix}.
\\]

Let \\( M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \\). Then,

\\[
\begin{pmatrix}
F_{101} \\
F_{100}
\end{pmatrix}
= M^{100}
\begin{pmatrix}
1 \\
0
\end{pmatrix}.
\\]

---

## Final Answer

Hence, the number of jump sequences (paths) the flea can take to cover 100 inches is:

\\[
a_{100} = F_{101}.
\\]

Using known values of Fibonacci numbers:

\\[
F_{101} = 573147844013817084101.
\\]

# Reference

* [1] [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)