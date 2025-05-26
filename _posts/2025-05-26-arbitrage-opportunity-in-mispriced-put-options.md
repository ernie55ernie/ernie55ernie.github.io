---
layout: post
title: "Arbitrage Opportunity in Mispriced Put Options"
date: 2025-05-26
category: quantitative interview
---

### Setup

We are given prices for European put options on the same underlying asset and maturity with the following strikes and prices:

\\[
P(30) = 6, \quad P(20) = 4, \quad P(0) = 0
\\]

Let \\( P(K) \\) be the price of the put option with strike \\( K \\). Then, the points \\( (K, P(K)) \\) lie on the line:

\\[
P(K) = \frac{2}{3}K
\\]

This implies a linear relationship, contradicting the convexity of put prices as a function of strike price. This leads to an **arbitrage opportunity**.

### Arbitrage Strategy

The arbitrage arises because the price of the put at strike 20 is **too high** compared to what convexity implies.

We can exploit this using the following **zero-cost portfolio**:

- **Long 2 puts** with strike 30
- **Short 3 puts** with strike 20

This results in **no initial cost**:

\\[
3 \cdot \$4 - 2 \cdot \$6 = \$12 - \$12 = \$0
\\]

### Payoff at Maturity

Let \\( S_T \\) be the underlying asset price at maturity. The portfolio payoff is:

- Long 2 puts at strike 30: \\( 2 \cdot \max(30 - S_T, 0) \\)
- Short 3 puts at strike 20: \\( -3 \cdot \max(20 - S_T, 0) \\)

So the net payoff is:

\\[
V(S_T) = 2 \cdot \max(30 - S_T, 0) - 3 \cdot \max(20 - S_T, 0)
\\]

Let's analyze key intervals:

- If \\( S_T \geq 30 \\): payoff = 0
- If \\( 20 \leq S_T < 30 \\): payoff = \\( 2(30 - S_T) - 3(20 - S_T) = 60 - 2S_T - 60 + 3S_T = S_T \\)
- If \\( S_T < 20 \\): payoff = \\( 2(30 - S_T) - 3(20 - S_T) = 60 - 2S_T - 60 + 3S_T = S_T \\)

Hence:

\\[
V(S_T) = 
\begin{cases}
0 & \text{if } S_T \geq 30 \\
S_T & \text{if } S_T < 30
\end{cases}
\\]

### Conclusion

This portfolio costs **nothing** to set up and yields a **non-negative payoff**, strictly **positive when \\( S_T < 30 \\)**. Thus, we have identified an **arbitrage opportunity** due to the violation of put price convexity.

# Reference

* [1] [Options Arbitrage Opportunities via Put-Call Parity](https://www.investopedia.com/articles/optioninvestor/05/011905.asp)
