---
layout: post
title: "Proof That the Standard Normal PDF Integrates to 1"
date: 2025-05-24
category: quantitative interview
---

The standard normal distribution has the probability density function (PDF):

\\[
f(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}
\\]

To show this is a **valid PDF**, we need to verify:

\\[
\int_{-\infty}^{\infty} f(x) \, dx = 1
\\]

---

## Step 1: Square the Integral

Let:

\\[
I = \int_{-\infty}^{\infty} e^{-x^2/2} \, dx
\\]

Then:

\\[
I^2 = \left( \int_{-\infty}^{\infty} e^{-x^2/2} \, dx \right)^2 = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} e^{-(x^2 + y^2)/2} \, dx \, dy
\\]

Switch to polar coordinates:

\\[
x = r \cos\theta,\quad y = r \sin\theta,\quad dx\,dy = r\,dr\,d\theta
\\]

So:

\\[
I^2 = \int_{0}^{2\pi} \int_{0}^{\infty} e^{-r^2/2} \cdot r \, dr \, d\theta
\\]

---

## Step 2: Evaluate the Inner Integral

\\[
\int_{0}^{\infty} r e^{-r^2/2} \, dr
\\]

Substitute \\( u = r^2/2 \Rightarrow du = r \, dr \\):

\\[
= \int_{0}^{\infty} e^{-u} \, du = 1
\\]

---

## Step 3: Evaluate the Full Integral

\\[
I^2 = \int_{0}^{2\pi} 1 \, d\theta = 2\pi
\Rightarrow I = \sqrt{2\pi}
\\]

Thus:

\\[
\int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} \, dx = \frac{1}{\sqrt{2\pi}} \cdot \sqrt{2\pi} = \boxed{1}
\\]

---

## Final Result

\\[
\int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} \, dx = \boxed{1}
\\]

So the standard normal PDF is **properly normalized**.

---

## Reference

* [1] [Gaussian Integral – Wikipedia](https://en.wikipedia.org/wiki/Gaussian_integral)