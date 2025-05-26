---
layout: post
title: "Solving the Ornstein–Uhlenbeck SDE"
date: 2025-05-26
category: quantitative interview
---

We are asked to solve the stochastic differential equation (SDE):

\\[
dr_t = \lambda(\theta - r_t)\,dt + \sigma\,dW_t,
\\]

where \\( r_0 \\) is the initial value, \\( \lambda, \theta, \sigma \in \mathbb{R} \\), and \\( W_t \\) is a standard Brownian motion.

---

### Step 1: Linearization and Integrating Factor

Rewriting the SDE:

\\[
dr_t + \lambda r_t\,dt = \lambda \theta\,dt + \sigma\,dW_t.
\\]

Multiply both sides by the integrating factor \\( e^{\lambda t} \\):

\\[
e^{\lambda t}dr_t + \lambda e^{\lambda t} r_t\,dt = \lambda \theta e^{\lambda t}\,dt + \sigma e^{\lambda t}\,dW_t.
\\]

Recognize the left-hand side as a total derivative:

\\[
d(e^{\lambda t} r_t) = \lambda \theta e^{\lambda t}\,dt + \sigma e^{\lambda t}\,dW_t.
\\]

---

### Step 2: Integration

Integrate both sides from 0 to \\( t \\):

\\[
e^{\lambda t} r_t - r_0 = \lambda \theta \int_0^t e^{\lambda s}\,ds + \sigma \int_0^t e^{\lambda s}\,dW_s.
\\]

Evaluate the deterministic integral:

\\[
\int_0^t e^{\lambda s}\,ds = \frac{1}{\lambda}(e^{\lambda t} - 1),
\quad \text{so} \quad
\lambda \theta \int_0^t e^{\lambda s}\,ds = \theta(e^{\lambda t} - 1).
\\]

Thus:

\\[
e^{\lambda t} r_t = r_0 + \theta(e^{\lambda t} - 1) + \sigma \int_0^t e^{\lambda s}\,dW_s.
\\]

---

### Step 3: Solve for \\( r_t \\)

Divide through by \\( e^{\lambda t} \\):

\\[
r_t = e^{-\lambda t} r_0 + \theta(1 - e^{-\lambda t}) + \sigma e^{-\lambda t} \int_0^t e^{\lambda s}\,dW_s.
\\]

Equivalently, this can be written using the convolution form:

\\[
r_t = e^{-\lambda t} r_0 + \theta(1 - e^{-\lambda t}) + \sigma \int_0^t e^{-\lambda(t - s)}\,dW_s.
\\]

---

## Mean Reversion Property

Taking expectations:

\\[
\mathbb{E}[r_t] = e^{-\lambda t} r_0 + \theta(1 - e^{-\lambda t}),
\\]

since the stochastic integral has mean zero.

As \\( t \to \infty \\), we have:

\\[
\lim_{t \to \infty} \mathbb{E}[r_t] = \theta.
\\]

This confirms that the Ornstein–Uhlenbeck process is **mean-reverting** to level \\( \theta \\), regardless of the initial value \\( r_0 \\).

---

## Final Result

The explicit solution to the Ornstein–Uhlenbeck SDE is:

\\[
r_t = e^{-\lambda t} r_0 + \theta(1 - e^{-\lambda t}) + \sigma \int_0^t e^{-\lambda(t - s)}\,dW_s.
\\]

# Reference

* [1] [Stochastic differential equation](https://en.wikipedia.org/wiki/Stochastic_differential_equation)