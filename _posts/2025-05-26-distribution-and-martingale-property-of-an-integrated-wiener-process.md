---
layout: post
title: "Distribution and Martingale Property of an Integrated Wiener Process"
date: 2025-05-26
category: quantitative interview
---

Let \\( W\sb{t} \\) be a standard Wiener process (Brownian motion), and define

\\[
X\sb{t} = \int\sb{0}^t W\sb{\tau}\,d\tau.
\\]

We answer two questions:

<iframe src="{{ site.baseurl }}/assets/integrated_brownian_motion.html" width="100%" height="800px" style="border:none; border-radius: 12px; margin: 20px 0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"></iframe>

---

### 1. Distribution of \\( X\sb{t} \\)

The process \\( X\sb{t} \\) is a stochastic integral of Brownian motion with respect to Lebesgue measure (not Itô). It can be evaluated in distribution as follows:

- \\( X\sb{t} \\) is a **Gaussian** random variable (being a linear transformation of a Gaussian process).
- We compute its **mean** and **variance**.

#### Mean:

\\[
\mathbb{E}[X\sb{t}] = \mathbb{E}\left[\int\sb{0}^t W\sb{\tau}\,d\tau\right] = \int\sb{0}^t \mathbb{E}[W\sb{\tau}]\,d\tau = \int\sb{0}^t 0\,d\tau = 0.
\\]

#### Variance:

Using the covariance of Brownian motion:

\\[
\text{Var}(X\sb{t}) = \mathbb{E}[X\sb{t}^2] = \mathbb{E}\left[ \left( \int\sb{0}^t W\sb{\tau}\,d\tau \right)^2 \right] = \int\sb{0}^t\int\sb{0}^t \mathbb{E}[W\sb{s} W\sb{u}]\,ds\,du.
\\]

Since \\( \mathbb{E}[W\sb{s} W\sb{u}] = \min(s, u) \\), we compute:

\\[
\text{Var}(X\sb{t}) = \int\sb{0}^t \int\sb{0}^t \min(s, u)\,ds\,du = \frac{t^3}{3}.
\\]

Thus,

\\[
X\sb{t} \sim \mathcal{N}\left(0, \frac{t^3}{3} \right).
\\]

---

### 2. Is \\( \{X\sb{t}\}_{t \ge 0} \\) a martingale?

We check whether \\( X\sb{t} \\) satisfies the martingale property with respect to the natural filtration \\( \mathcal{F}\sb{t} = \sigma(W\sb{s}: s \le t) \\):

We evaluate \\( \mathbb{E}[X\sb{t} \mid \mathcal{F}\sb{s}] \\) for \\( s < t \\). Note that:

\\[
X\sb{t} = \int\sb{0}^t W\sb{\tau}\,d\tau = \int\sb{0}^s W\sb{\tau}\,d\tau + \int\sb{s}^t W\sb{\tau}\,d\tau = X\sb{s} + \int\sb{s}^t W\sb{\tau}\,d\tau.
\\]

Then, taking the conditional expectation:

\\[
\mathbb{E}[X\sb{t} \mid \mathcal{F}\sb{s}] = X\sb{s} + \mathbb{E}\left[ \int\sb{s}^t W\sb{\tau}\,d\tau \mathrel{\Big\vert} \mathcal{F}\sb{s} \right].
\\]

By Fubini's theorem (or moving the expectation inside the integral), and using the martingale property of Brownian motion (\\( \mathbb{E}[W\sb{\tau} \mid \mathcal{F}\sb{s}] = W\sb{s} \\) for \\( \tau > s \\)):

\\[
\mathbb{E}\left[ \int\sb{s}^t W\sb{\tau}\,d\tau \mathrel{\Big\vert} \mathcal{F}\sb{s} \right] = \int\sb{s}^t \mathbb{E}[W\sb{\tau} \mid \mathcal{F}\sb{s}]\,d\tau = \int\sb{s}^t W\sb{s}\,d\tau = (t - s)W\sb{s}.
\\]

Therefore,

\\[
\mathbb{E}[X\sb{t} \mid \mathcal{F}\sb{s}] = X\sb{s} + (t - s)W\sb{s} \ne X\sb{s}.
\\]

So \\( X\sb{t} \\) is **not** a martingale.

---

## Conclusion

- \\( X\sb{t} = \int\sb{0}^t W\sb{\tau}\,d\tau \sim \mathcal{N}(0, t^3/3) \\)
- \\( X\sb{t} \\) is **not** a martingale with respect to the natural filtration of \\( W\sb{t} \\)

# Reference

* [1] [Wiener process](https://en.wikipedia.org/wiki/Wiener_process)
