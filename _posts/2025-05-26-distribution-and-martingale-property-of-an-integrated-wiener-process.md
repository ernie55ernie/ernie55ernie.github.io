---
layout: post
title: "Distribution and Martingale Property of an Integrated Wiener Process"
date: 2025-05-26
category: quantitative interview
---

Let \\( W_t \\) be a standard Wiener process (Brownian motion), and define

\\[
X_t = \int_0^t W_\tau\,d\tau.
\\]

We answer two questions:

<iframe src="{{ site.baseurl }}/assets/integrated_brownian_motion.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

---

### 1. Distribution of \\( X_t \\)

The process \\( X_t \\) is a stochastic integral of Brownian motion with respect to Lebesgue measure (not Itô). It can be evaluated in distribution as follows:

- \\( X_t \\) is a **Gaussian** random variable (being a linear transformation of a Gaussian process).
- We compute its **mean** and **variance**.

#### Mean:

\\[
\mathbb{E}[X_t] = \mathbb{E}\left[\int_0^t W_\tau\,d\tau\right] = \int_0^t \mathbb{E}[W_\tau]\,d\tau = \int_0^t 0\,d\tau = 0.
\\]

#### Variance:

Using the covariance of Brownian motion:

\\[
\text{Var}(X_t) = \mathbb{E}[X_t^2] = \mathbb{E}\left[ \left( \int_0^t W_\tau\,d\tau \right)^2 \right] = \int_0^t\int_0^t \mathbb{E}[W_s W_u]\,ds\,du.
\\]

Since \\( \mathbb{E}[W_s W_u] = \min(s, u) \\), we compute:

\\[
\text{Var}(X_t) = \int_0^t \int_0^t \min(s, u)\,ds\,du = \frac{t^3}{3}.
\\]

Thus,

\\[
X_t \sim \mathcal{N}\left(0, \frac{t^3}{3} \right).
\\]

---

### 2. Is \\( \{X_t\}_{t \ge 0} \\) a martingale?

We check whether \\( X_t \\) satisfies the martingale property with respect to the natural filtration \\( \mathcal{F}_t = \sigma(W_s: s \le t) \\):

We evaluate \\( \mathbb{E}[X_t \mid \mathcal{F}_s] \\) for \\( s < t \\). Note that:

\\[
X_t = \int_0^t W_\tau\,d\tau = \int_0^s W_\tau\,d\tau + \int_s^t W_\tau\,d\tau = X_s + \int_s^t W_\tau\,d\tau.
\\]

Then, taking the conditional expectation:

\\[
\mathbb{E}[X_t \mid \mathcal{F}_s] = X_s + \mathbb{E}\left[ \int_s^t W_\tau\,d\tau \mathrel{\Big\vert} \mathcal{F}_s \right].
\\]

By Fubini's theorem (or moving the expectation inside the integral), and using the martingale property of Brownian motion (\\( \mathbb{E}[W_\tau \mid \mathcal{F}_s] = W_s \\) for \\( \tau > s \\)):

\\[
\mathbb{E}\left[ \int_s^t W_\tau\,d\tau \mathrel{\Big\vert} \mathcal{F}_s \right] = \int_s^t \mathbb{E}[W_\tau \mid \mathcal{F}_s]\,d\tau = \int_s^t W_s\,d\tau = (t - s)W_s.
\\]

Therefore,

\\[
\mathbb{E}[X_t \mid \mathcal{F}_s] = X_s + (t - s)W_s \ne X_s.
\\]

So \\( X_t \\) is **not** a martingale.

---

## Conclusion

- \\( X_t = \int_0^t W_\tau\,d\tau \sim \mathcal{N}(0, t^3/3) \\)
- \\( X_t \\) is **not** a martingale with respect to the natural filtration of \\( W_t \\)

# Reference

* [1] [Wiener process](https://en.wikipedia.org/wiki/Wiener_process)
