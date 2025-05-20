---
layout: post
title: "Minimum-Variance Hedge Ratio in Portfolio Theory"
date: 2025-05-20
category: quantitative interview
---

### The Setup

You are:

- **Long** one share of stock A
- Considering a **short** position of \\( h \\) shares in stock B

Let:

- \\( \mathrm{Var}(R_A) = \sigma_A^2 \\)
- \\( \mathrm{Var}(R_B) = \sigma_B^2 \\)
- \\( \mathrm{Corr}(R_A, R_B) = \rho \\)

### Objective

Choose \\( h \\) to **minimize the variance** of your net position:

\\[
\mathrm{Var}(R_A - h R_B)
\\]

---

## Step-by-Step Solution

We compute:

\\[
\mathrm{Var}(R_A - h R_B) = \sigma_A^2 + h^2 \sigma_B^2 - 2h \rho \sigma_A \sigma_B
\\]

To minimize, differentiate with respect to \\( h \\):

\\[
\frac{d}{dh} \mathrm{Var}(R_A - h R_B) = 2h \sigma_B^2 - 2 \rho \sigma_A \sigma_B
\\]

Set derivative to zero:

\\[
2h \sigma_B^2 = 2 \rho \sigma_A \sigma_B
\Rightarrow h = \frac{\rho \sigma_A}{\sigma_B}
\\]

---

## Final Answer

\\[
\boxed{h = \frac{\rho \sigma_A}{\sigma_B}}
\\]

This is the **minimum-variance hedge ratio**, the amount of B to short to optimally hedge your position in A.

---

## Reference

* [1] [Investopedia: Hedge Ratio](https://www.investopedia.com/terms/h/hedgeratio.asp)