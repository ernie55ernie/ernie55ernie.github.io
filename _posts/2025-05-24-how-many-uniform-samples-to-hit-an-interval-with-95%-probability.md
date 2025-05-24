---
layout: post
title: "How Many Uniform Samples to Hit an Interval with 95% Probability?"
date: 2025-05-24
category: quantitative interview
---

### The Problem

You generate \\( n \\) independent random variables \\( X_1, X_2, \dots, X_n \\), each uniformly distributed over \\( [0,1] \\).

**Question**: How large must \\( n \\) be so that **at least one** sample falls in the interval \\( [0.7, 0.72] \\) with probability **at least 95%**?

---

## Step-by-Step Solution

### Step 1: Probability of a Single Hit

The probability that a single sample \\( X_i \\) lands in \\( [0.7, 0.72] \\) is:

\\[
P(\text{hit}) = 0.72 - 0.7 = 0.02
\\]

---

### Step 2: Probability None Hit

The probability that **none** of the \\( n \\) variables fall in \\( [0.7, 0.72] \\):

\\[
P(\text{no hits}) = (1 - 0.02)^n = 0.98^n
\\]

We want:

\\[
1 - 0.98^n \ge 0.95 \Rightarrow 0.98^n \le 0.05
\\]

---

### Step 3: Solve for \\( n \\)

Take logs:

\\[
\log(0.98^n) \le \log(0.05) \Rightarrow n \cdot \log(0.98) \le \log(0.05)
\\]

\\[
n \ge \frac{\log(0.05)}{\log(0.98)} \approx \frac{-1.3010}{-0.00877} \approx 148.36
\\]

Round up:

\\[
\boxed{n = 149}
\\]

---

## Final Answer

You need to generate at least:

\\[
\boxed{149}
\\]

independent \\( \mathrm{Uniform}(0,1) \\) variables to ensure with 95% confidence that **at least one** falls in \\( [0.7, 0.72] \\).

---

## Reference

* [1] [150 Most Frequently Asked Questions on Quant Interviews, Second Edition](https://www.amazon.com/Frequently-Questions-Interviews-Second-Pocket/dp/097975769X/ref=pd_bxgy_img_2/137-0455346-7624716?pd_rd_w=ToT77&pf_rd_p=6b3eefea-7b16-43e9-bc45-2e332cbf99da&pf_rd_r=N7K2PCZYEB7MDZQF5AZM&pd_rd_r=397c9cc6-a138-4110-bc7c-8f504f9add37&pd_rd_wg=q9K2T&pd_rd_i=097975769X&psc=1)