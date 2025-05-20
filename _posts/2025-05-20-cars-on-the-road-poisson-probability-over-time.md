---
layout: post
title: "Cars on the Road: Poisson Probability Over Time"
date: 2025-05-20
category: quantitative interview
---

### The Puzzle

You’re told that the probability of seeing **at least one** car on a highway during **any 20-minute** interval is:

\\[
p_{20} = \frac{609}{625}
\\]

Assuming car arrivals are uniform and follow a **Poisson process**, what is the probability of seeing **at least one** car in a **5-minute** interval?

---

## Step 1: Use Poisson Properties

In a Poisson process, the number of arrivals in time \\( t \\) follows the distribution:

\\[
P(\text{no arrivals in } t) = e^{-\lambda t}
\\]

So:

\\[
P(\geq 1 \text{ in } t) = 1 - e^{-\lambda t}
\\]

Given:

\\[
1 - e^{-20\lambda} = \frac{609}{625}
\\]

Solve for \\( \lambda \\):

\\[
e^{-20\lambda} = 1 - \frac{609}{625} = \frac{16}{625}
\\]

Take logs:

\\[
-20\lambda = \ln\left(\frac{16}{625}\right)
\Rightarrow \lambda = -\frac{1}{20} \ln\left(\frac{16}{625}\right)
\\]

---

## Step 2: Compute \\( p_5 \\)

\\[
p_5 = 1 - e^{-5\lambda} = 1 - \left(e^{-20\lambda}\right)^{1/4}
= 1 - \left(\frac{16}{625}\right)^{1/4}
\\]

Calculate:

\\[
\left(\frac{16}{625}\right)^{1/4} = \frac{2}{5}
\\]

So:

\\[
p_5 = 1 - \frac{2}{5} = \boxed{\frac{3}{5}}
\\]

---

## Final Answer

\\[
\boxed{\frac{3}{5}}
\\]

---

## Reference

* [1] [Poisson Process in Continuous Time](https://en.wikipedia.org/wiki/Poisson_point_process)