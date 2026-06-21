---
layout: post
title: "Sharpe Ratio: Definition, Formula, and Examples"
date: 2026-06-21
category: trading
------

## Executive Summary

The Sharpe Ratio is one of the most widely used measures of risk-adjusted investment performance. Its core idea is simple: first subtract the risk-free rate from an investment's return to obtain excess return, then divide that excess return by the volatility of returns. In other words, it asks: **how much excess return does an investor receive for each unit of total risk taken?**

When William F. Sharpe introduced the concept in 1966, he called it the **reward-to-variability ratio**. In 1994, Sharpe further clarified its ex ante and ex post uses. The reason the metric has remained so influential is that it compresses both return and risk into one comparable number, making it especially useful for comparing funds, strategies, and portfolios.

However, the Sharpe Ratio is useful only when interpreted carefully. It treats risk as standard deviation, which means it penalizes upside and downside volatility symmetrically. This can be misleading for skewed returns, fat-tailed distributions, option-like payoffs, illiquid assets, smoothed returns, and strategies with nonlinear downside risk.

A particularly important caveat is that **a monthly Sharpe Ratio cannot generally be annualized simply by multiplying it by $$\sqrt{12}$$**. That shortcut is valid only under restrictive assumptions, especially independent and identically distributed returns. When returns are serially correlated, annualized Sharpe can be materially overstated. Andrew Lo's classic work shows that some hedge fund Sharpe Ratios may be overstated by as much as 65% when serial correlation is ignored.

The practical conclusion is straightforward: **the Sharpe Ratio is a good first-pass screening tool, but it should not be the sole basis for investment judgment**. For long-tail, nonlinear, actively managed, or benchmark-relative strategies, it should be combined with other metrics such as Sortino Ratio, Treynor Ratio, Information Ratio, Jensen's Alpha, maximum drawdown, and rolling-window stability analysis.

## Definition and Intuition

The standard intuition behind the Sharpe Ratio is to split investment performance into two parts.

First, how much of the return exceeds the return of a relatively safe asset? Second, how much volatility did the investor have to endure to earn that excess return?

If two portfolios have similar returns, the one with lower volatility has the higher Sharpe Ratio. If two portfolios have similar volatility, the one with higher excess return has the higher Sharpe Ratio.

So the Sharpe Ratio does not merely ask:

> How much money did you make?

It asks:

> **Was the return worth the risk?**

Historically, Sharpe introduced the concept in the context of mutual fund performance evaluation. His 1966 paper emphasized that performance should not be judged by average return alone; risk must also be considered. The original term, reward-to-variability ratio, describes the same basic structure: reward divided by return variability.

By 1994, Sharpe had clarified two important versions of the measure:

* **Ex ante Sharpe Ratio**: based on expected future excess return and expected volatility.
* **Ex post Sharpe Ratio**: based on historical realized excess return and historical volatility.

In practice, the Sharpe Ratios seen in fund reports, backtests, and asset allocation dashboards are usually historical, ex post estimates. They are not true population values. They are sample estimates.

Another important point is that the Sharpe Ratio measures **total risk**, not only market risk. This makes it more appropriate for evaluating a complete portfolio, a standalone fund, or a full strategy. By contrast, metrics such as the Treynor Ratio focus on systematic market risk through beta.

## Mathematical Formula and Calculation Method

Unless stated otherwise, the formulas and examples below use the following assumptions:

1. Returns are simple discrete returns, not log returns.
2. Historical estimates use arithmetic averages and sample standard deviations.
3. The risk-free rate is converted to the same frequency as the return data.
4. Examples ignore transaction costs, taxes, and slippage.
5. All numerical examples are for educational illustration only.

The core variable is the period-by-period excess return:

$$
x_t = r_{p,t} - r_{f,t}
$$

where:

* $$r_{p,t}$$ is the portfolio or asset return in period $$t$$,
* $$r_{f,t}$$ is the risk-free rate in the same period, currency, and frequency.

If the risk-free rate is treated as constant over the sample, the excess return is often written as:

$$
x_t = r_{p,t} - r_f
$$

### Population Formula

The theoretical population Sharpe Ratio can be written as:

$$
SR = \frac{\mu_x}{\sigma_x}
= \frac{E[r_p-r_f]}{\sqrt{\mathrm{Var}(r_p-r_f)}}
$$

If the risk-free asset is treated as having zero volatility during the measurement period, this is often simplified to:

$$
SR = \frac{E[r_p-r_f]}{\sigma_p}
$$

This is the theoretical or population Sharpe Ratio. In practice, this true value is unknown and must be estimated from historical data.

### Sample Formula

Given historical excess returns $$x_1, x_2, \ldots, x_n$$, the sample mean excess return is:

$$
\bar{x}=\frac{1}{n}\sum_{t=1}^{n}x_t
$$

The sample standard deviation is:

$$
s_x=\sqrt{\frac{1}{n-1}\sum_{t=1}^{n}(x_t-\bar{x})^2}
$$

The historical sample Sharpe Ratio is:

$$
\widehat{SR}=\frac{\bar{x}}{s_x}
$$

This is the most common historical Sharpe Ratio estimator used in practice.

If the observed data are treated as the full finite population rather than a sample from an unknown process, one may instead use the population standard deviation:

$$
\sigma_{x,\text{pop}}=
\sqrt{\frac{1}{N}\sum_{t=1}^{N}(x_t-\mu_x)^2}
$$

The corresponding finite-population-style Sharpe Ratio would be:

$$
SR_{\text{pop-like}}=\frac{\bar{x}}{\sigma_{x,\text{pop}}}
$$

In investment practice, however, historical data are usually treated as a sample from an uncertain return-generating process. Therefore, the sample Sharpe Ratio is far more common.

## Annualization and Data Frequency

If excess returns are approximately independent and identically distributed, and compounding effects are ignored for simplicity, the Sharpe Ratio can be annualized as:

$$
SR_{\text{ann}} \approx \sqrt{m}, SR_{\text{per}}
$$

where $$m$$ is the number of periods per year.

Common values are:

| Data Frequency | Common Periods Per Year $$m$$ |   Approximate Annualized Sharpe |
| -------------- | ----------------------------: | ------------------------------: |
| Daily          |       Around 252 trading days |  $$\sqrt{252},SR_{\text{day}}$$ |
| Weekly         |               Around 52 weeks |  $$\sqrt{52},SR_{\text{week}}$$ |
| Monthly        |                     12 months | $$\sqrt{12},SR_{\text{month}}$$ |
| Quarterly      |                    4 quarters |       $$2,SR_{\text{quarter}}$$ |

This shortcut is common, but it depends heavily on the assumption that returns are not serially correlated.

Andrew Lo showed that when returns exhibit autocorrelation, the correct scaling should be adjusted. A general form is:

$$
SR_T
====

\frac{q}{\sqrt{q+2\sum_{k=1}^{q-1}(q-k)\rho_k}}
, SR_t
$$

where:

* $$q=T/t$$,
* $$\rho_k$$ is the $$k$$-th order autocorrelation of excess returns.

When all autocorrelations are zero, the formula collapses back to the familiar $$\sqrt{q}$$ rule. But when autocorrelation is positive, simple square-root annualization may overstate the true annualized Sharpe Ratio.

## Converting the Risk-Free Rate

The risk-free rate must be converted to the same frequency as the return data.

If the annual risk-free rate is $$y_f$$, the equivalent per-period risk-free rate is:

$$
r_{f,\text{per}} = (1+y_f)^{1/m}-1
$$

Conversely, if the per-period risk-free rate is $$r_{f,\text{per}}$$, its annualized equivalent is:

$$
r_{f,\text{ann}} = (1+r_{f,\text{per}})^m-1
$$

The purpose is to ensure that returns and risk-free rates are comparable in the same currency, same horizon, and same compounding convention.

## Simple Returns vs. Log Returns

If simple returns $$R_t$$ are used, multi-period returns compound multiplicatively:

$$
1+R_t(k)=\prod_{j=0}^{k-1}(1+R_{t-j})
$$

So simple returns are not additive over time.

If log returns are used:

$$
g_t=\ln(1+R_t)
$$

then multi-period log returns are additive:

$$
g_t(k)=\sum_{j=0}^{k-1} g_{t-j}
$$

This makes log returns mathematically convenient for time aggregation. However, a Sharpe Ratio calculated using log returns is not exactly the same object as a Sharpe Ratio calculated using simple returns.

At the portfolio level, simple returns are usually more intuitive because portfolio simple return is a weighted average of asset simple returns. Portfolio log return, however, is not simply the weighted average of individual asset log returns.

For this reason, the examples below use simple returns.

## Calculation Workflow

```mermaid id="f57ayg"
flowchart TD
A[Choose data frequency and sample window] --> B[Convert risk-free rate to the same frequency]
B --> C[Calculate excess return: x_t = r_p,t - r_f,t]
C --> D[Calculate average excess return]
C --> E[Calculate volatility of excess returns]
D --> F[Sharpe Ratio = Average Excess Return / Volatility]
E --> F
F --> G{Annualize?}
G --> H[If approximately i.i.d.: multiply by sqrt(m)]
G --> I[If serially correlated: use autocorrelation adjustment]
```

## Example 1: Historical Sharpe Ratio for a Single Asset

Assume:

* Monthly data with 12 observations.
* Monthly risk-free rate is fixed at 0.2%.
* Transaction costs and taxes are ignored.

| Month | Asset Monthly Return $$r_t$$ | Excess Return $$x_t=r_t-r_f$$ |
| ----: | ---------------------------: | ----------------------------: |
|     1 |                         3.0% |                          2.8% |
|     2 |                         1.5% |                          1.3% |
|     3 |                        -1.0% |                         -1.2% |
|     4 |                         2.5% |                          2.3% |
|     5 |                         0.5% |                          0.3% |
|     6 |                         1.8% |                          1.6% |
|     7 |                        -1.2% |                         -1.4% |
|     8 |                         2.2% |                          2.0% |
|     9 |                         1.0% |                          0.8% |
|    10 |                         1.7% |                          1.5% |
|    11 |                        -0.5% |                         -0.7% |
|    12 |                         2.0% |                          1.8% |

First calculate the average excess return:

$$
\bar{x}=\frac{1}{12}\sum_{t=1}^{12}x_t
=\frac{0.1110}{12}=0.00925
$$

So the average monthly excess return is:

$$
0.925%
$$

Next calculate the sample standard deviation:

$$
s_x=0.01389
$$

The sample Sharpe Ratio is:

$$
\widehat{SR}=\frac{0.00925}{0.01389}=0.666
$$

If the 12 observations are treated as a finite population, the population standard deviation is approximately:

$$
\sigma_{x,\text{pop}}=0.01330
$$

The corresponding population-style ratio is:

$$
\frac{0.00925}{0.01330}=0.696
$$

Under the i.i.d. approximation, the annualized Sharpe Ratio is:

$$
SR_{\text{ann}}\approx \sqrt{12}\times 0.666 = 2.307
$$

This example shows two important points.

First, sample and population standard deviations produce slightly different results. Second, with only 12 monthly observations, even a strong annualized Sharpe Ratio should be interpreted cautiously. A short sample can easily overstate the true quality of a strategy.

## Example 2: Multi-Asset Portfolio Sharpe Ratio

Assume:

* Three assets: $$A$$, $$B$$, and $$C$$.
* Six months of return data.
* Portfolio weights are:

$$
w=(0.5,;0.3,;0.2)^\top
$$

* Monthly risk-free rate is 0.15%.
* The portfolio is fully invested, so weights sum to 1.

| Month | $$A$$ | $$B$$ | $$C$$ | Portfolio Return $$r_{p,t}$$ | Excess Return $$x_t$$ |
| ----: | ----: | ----: | ----: | ---------------------------: | --------------------: |
|     1 |  2.0% |  1.2% |  3.0% |                        1.96% |                 1.81% |
|     2 |  1.0% |  0.8% | -1.0% |                        0.54% |                 0.39% |
|     3 | -1.5% |  0.4% |  2.0% |                       -0.23% |                -0.38% |
|     4 |  1.8% |  1.1% |  1.5% |                        1.53% |                 1.38% |
|     5 |  1.2% | -0.6% |  0.5% |                        0.52% |                 0.37% |
|     6 |  0.5% |  0.7% | -1.2% |                        0.22% |                 0.07% |

The portfolio return in each period is:

$$
r_{p,t}=\sum_{i=1}^{3} w_i r_{i,t}=w^\top r_t
$$

For month 1:

$$
r_{p,1}=0.5(0.020)+0.3(0.012)+0.2(0.030)=0.0196=1.96%
$$

The sample covariance matrix of the three assets is:

$$
\Sigma=
\begin{bmatrix}
0.0001603 & 0.0000242 & 0.0000140\
0.0000242 & 0.0000428 & 0.0000246\
0.0000140 & 0.0000246 & 0.0002820
\end{bmatrix}
$$

The portfolio variance is:

$$
\sigma_p^2=w^\top \Sigma w
=0.00006821
$$

So the portfolio sample standard deviation is:

$$
\sigma_p=\sqrt{0.00006821}=0.008259
$$

The average monthly excess return is:

$$
\bar{x}=0.006067
$$

Therefore, the sample Sharpe Ratio is:

$$
\widehat{SR}=\frac{0.006067}{0.008259}=0.735
$$

Under the i.i.d. annualization approximation:

$$
SR_{\text{ann}}\approx \sqrt{12}\times 0.735=2.545
$$

The key lesson is that the denominator of the portfolio Sharpe Ratio comes from the **entire covariance structure**, not simply the average of individual asset volatilities.

Two portfolios with the same expected return can have very different Sharpe Ratios if their assets have different correlations. This is where Markowitz diversification and Sharpe Ratio analysis connect directly.

## Example 3: Negative Sharpe Ratio

Assume:

* Six months of return data.
* Monthly risk-free rate is 0.2%.
* Fees and leverage are ignored.

| Month | Asset Monthly Return $$r_t$$ | Excess Return $$x_t$$ |
| ----: | ---------------------------: | --------------------: |
|     1 |                        -3.0% |                 -3.2% |
|     2 |                         1.0% |                  0.8% |
|     3 |                        -2.0% |                 -2.2% |
|     4 |                        -1.5% |                 -1.7% |
|     5 |                         0.5% |                  0.3% |
|     6 |                        -1.0% |                 -1.2% |

The average monthly excess return is:

$$
\bar{x}=-0.0120
$$

The sample standard deviation is:

$$
s_x=0.01517
$$

Therefore:

$$
\widehat{SR}=\frac{-0.0120}{0.01517}=-0.791
$$

A negative Sharpe Ratio means that, over the sample period, the investment earned less than the risk-free rate on average.

However, negative Sharpe Ratios are often less informative for ranking than positive Sharpe Ratios. Once a strategy has failed to beat the risk-free asset, the more important question is usually not whether $$-0.6$$ is better than $$-0.8$$. The more important question is why the strategy lost money, whether the sample window is representative, and whether the risk structure has changed.

## Practical Interpretation

A Sharpe Ratio greater than zero means average excess return is positive. A Sharpe Ratio equal to zero means the investment roughly matched the risk-free return. A Sharpe Ratio below zero means the investment underperformed the risk-free asset over the sample period.

For positive Sharpe Ratios, higher is generally better. For negative Sharpe Ratios, rankings are usually less meaningful.

A common market rule of thumb is:

| Annualized Sharpe Ratio | Common Interpretation      | Practical View                                                |
| ----------------------- | -------------------------- | ------------------------------------------------------------- |
| < 0                     | Worse than risk-free asset | Investigate losses, sample window, and risk source            |
| 0–0.99                  | Weak to ordinary           | Limited risk-adjusted attractiveness                          |
| 1.00–1.99               | Good                       | Worth considering, but stability should be verified           |
| 2.00–2.99               | Very strong                | Be cautious if sample is short or returns are smoothed        |
| ≥ 3.00                  | Excellent and rare         | Check for overfitting, smoothing, illiquidity, or sample bias |

These thresholds are not theoretical laws. They are practical heuristics.

The same strategy may produce different Sharpe Ratios depending on:

* data frequency,
* sample window,
* risk-free rate choice,
* return smoothing,
* serial correlation,
* transaction cost assumptions,
* whether returns are simple or log returns,
* whether the calculation uses sample or population standard deviation.

## Practical Limitations

| Issue                      | Why It Matters                                                                                                                               | Practical Suggestion                                                                            |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Risk-free rate choice      | The numerator is excess return. If the risk-free rate uses the wrong currency, maturity, or compounding convention, the result is distorted. | Use a risk-free rate that matches the investment currency, horizon, and measurement convention. |
| Standard deviation as risk | Sharpe treats upside and downside volatility symmetrically.                                                                                  | Add downside and tail-risk measures when losses matter more than upside volatility.             |
| Non-normal returns         | Skewness, fat tails, and option-like payoffs can make Sharpe misleading.                                                                     | Combine Sharpe with drawdown, skewness, kurtosis, Sortino Ratio, or stress tests.               |
| Serial correlation         | Smoothed or autocorrelated returns can understate volatility and overstate Sharpe.                                                           | Do not blindly annualize by $$\sqrt{m}$$; use autocorrelation-adjusted scaling.                 |
| Estimation error           | Sharpe is an estimate, not a true value.                                                                                                     | Use longer samples, confidence intervals, bootstrapping, and out-of-sample validation.          |
| Small-sample bias          | Short samples can produce inflated Sharpe estimates.                                                                                         | Treat high Sharpe from small samples with skepticism.                                           |
| Measurement window         | Different windows can produce very different Sharpe Ratios.                                                                                  | Compare strategies using the same sample period and frequency.                                  |

These limitations do not make the Sharpe Ratio useless. They simply mean it should be treated as a compact summary statistic, not a complete description of risk.

## Comparison with Other Risk-Adjusted Metrics

The Sharpe Ratio is important, but it is not the only risk-adjusted performance measure.

Some metrics, such as Sharpe and Sortino, focus on whether an investment is attractive on its own. Others, such as Treynor Ratio, Information Ratio, and Jensen's Alpha, focus more on benchmark-relative performance or market risk exposure.

| Metric                | Formula                                                            | Risk in Denominator                        | Main Benchmark                              | Best Used For                                               | Main Limitation                                                                                     |
| --------------------- | ------------------------------------------------------------------ | ------------------------------------------ | ------------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Sharpe Ratio**      | $$\dfrac{R_p-r_f}{\sigma_p}$$ or $$\dfrac{\bar{x}}{s_x}$$          | Total risk, measured by standard deviation | Risk-free asset                             | Comparing portfolios, funds, or standalone strategies       | Penalizes upside and downside volatility equally; sensitive to skew, fat tails, and autocorrelation |
| **Sortino Ratio**     | $$\dfrac{R_p-MAR}{DD}$$, or commonly $$\dfrac{R_p-r_f}{\sigma_d}$$ | Downside risk                              | Minimum acceptable return or risk-free rate | When downside deviations matter more than upside volatility | Sensitive to the choice of MAR and downside deviation method                                        |
| **Treynor Ratio**     | $$\dfrac{R_p-r_f}{\beta_p}$$                                       | Systematic market risk                     | Risk-free asset and market portfolio        | Well-diversified portfolios where beta is the relevant risk | Ignores idiosyncratic risk                                                                          |
| **Information Ratio** | $$\dfrac{R_p-R_B}{\sigma_{p-B}}$$                                  | Active risk, or tracking error             | Passive benchmark                           | Evaluating active managers relative to a benchmark          | Highly sensitive to benchmark choice                                                                |
| **Jensen's Alpha**    | $$\alpha_p=R_p-\left[r_f+\beta_p(R_m-r_f)\right]$$                 | Not a ratio                                | Market portfolio                            | Measuring excess return relative to CAPM prediction         | Depends heavily on CAPM and benchmark assumptions                                                   |

The key question is not:

> Which metric is best?

The better question is:

> **Which metric answers the question I actually care about?**

If the goal is to compare standalone strategies or funds, the Sharpe Ratio is often appropriate. If the investor mostly cares about downside losses, the Sortino Ratio may be more relevant. If evaluating an active manager relative to a benchmark, Information Ratio is often more directly useful. If the portfolio is already well diversified and market beta is the key risk, Treynor Ratio and Jensen's Alpha can be more informative.

## Interpretation of Related Metrics

| Metric            | How to Interpret                                                                               | Common Practical Reading                                                                 |
| ----------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Sharpe Ratio      | Higher is better, assuming same frequency, window, and risk-free rate convention               | 1, 2, and 3 are often used as rough benchmarks, but they are not theoretical thresholds  |
| Sortino Ratio     | Higher is better, but only comparable when the same MAR and downside deviation method are used | Best used for relative comparison                                                        |
| Treynor Ratio     | Higher is better if the portfolio is sufficiently diversified and beta is meaningful           | No universal fixed threshold                                                             |
| Information Ratio | Higher means more active return per unit of tracking error                                     | 0.20–0.30 may already be good in competitive markets; 0.50 is strong; 1.0 is exceptional |
| Jensen's Alpha    | Positive alpha means return exceeded CAPM expectation                                          | Measured in return units, not as a ratio                                                 |

The broader lesson is that absolute thresholds should be used carefully. Metrics are most informative when compared within the same strategy universe, benchmark framework, and measurement convention.

## Rolling Sharpe Ratio

One commonly overlooked issue is that the Sharpe Ratio changes with the sample window.

A single full-sample Sharpe Ratio can hide instability across market regimes. A strategy may look excellent over the full sample but perform poorly in a particular subperiod. For this reason, **rolling Sharpe Ratio** is often more informative than a single static Sharpe estimate.

Rolling Sharpe calculates the Sharpe Ratio over a moving window, such as the most recent 12 months, 36 months, or 252 trading days.

For example:

![Illustrative chart: monthly returns and 12-month rolling Sharpe Ratio](sandbox:/mnt/data/sharpe_rolling_example_en.png)

In this type of chart, the bars represent monthly returns and the line represents rolling annualized Sharpe. The point is not to draw a conclusion from the illustrative data, but to show how quickly Sharpe can shift when recent returns, volatility, or loss patterns change.

Rolling Sharpe helps answer questions such as:

* Is performance stable?
* Did Sharpe depend on one lucky period?
* Did risk-adjusted performance deteriorate recently?
* Is the strategy regime-dependent?
* Does the full-sample Sharpe hide a major drawdown period?

If returns are serially correlated, even rolling annualized Sharpe should be interpreted with caution.

## Conclusion

The Sharpe Ratio is valuable because it provides a simple and comparable starting point:

$$
\text{Sharpe Ratio} = \frac{\text{Excess Return}}{\text{Total Risk}}
$$

When comparing investments with the same frequency, same currency, same risk-free rate convention, same sample window, and similar return distributions, it is a powerful first-pass measure of risk-adjusted performance.

But it is not a complete investment decision framework.

For short samples, smoothed returns, nonlinear payoffs, skewed distributions, benchmark-relative strategies, or strategies with meaningful tail risk, the Sharpe Ratio should be supplemented with other tools.

A practical workflow is:

1. Use Sharpe Ratio as the first screening metric.
2. Use rolling Sharpe to check stability across time.
3. Use Sortino Ratio to focus on downside risk.
4. Use Information Ratio for benchmark-relative active performance.
5. Use Jensen's Alpha or Treynor Ratio when market beta is central.
6. Use maximum drawdown, tail-risk metrics, and stress tests to understand path risk.
7. For very high Sharpe Ratios, demand out-of-sample validation or statistical confidence analysis.

The best way to use Sharpe Ratio is not to worship the number, but to treat it as the first question:

> Did this return adequately compensate me for the risk?

## References

* Sharpe, William F. (1966), "Mutual Fund Performance," *The Journal of Business*, 39(1), 119–138.
* Sharpe, William F. (1994), "The Sharpe Ratio," *The Journal of Portfolio Management*, 21(1), 49–58.
* Markowitz, Harry (1952), "Portfolio Selection," *The Journal of Finance*, 7(1), 77–91.
* Lo, Andrew W. (2002), "The Statistics of Sharpe Ratios," *Financial Analysts Journal*, 58(4), 36–52.
* Jensen, Michael C. (1968), "The Performance of Mutual Funds in the Period 1945–1964," *The Journal of Finance*, 23(2), 389–416.
* Kidd, Deborah, CFA (2011), "The Sharpe Ratio and the Information Ratio," CFA Institute.
* Kidd, Deborah, CFA (2011), "Measures of Risk-Adjusted Return: Let's Not Forget Treynor and Jensen," CFA Institute.
* Kidd, Deborah, CFA (2012), "The Sortino Ratio: Is Downside Risk the Only Risk that Matters?", CFA Institute.
* Damodaran, Aswath (2008), "What is the Riskfree Rate? A Search for the Basic Building Block," New York University Stern School of Business.
* Riondato, Matteo (2018), "Sharpe Ratio: Estimation, Confidence Intervals, and Hypothesis Testing," Two Sigma Technical Report.
* Morningstar (2016), "Custom Calculation Data Points," Morningstar Direct Methodology Document.
* Zivot, Eric (2015), "Return Calculations," University of Washington.
* Zivot, Eric (2013), "Portfolio Theory with Matrix Algebra," University of Washington.
* Charles Schwab (2026), "How to Calculate the Sharpe Ratio to Gauge Risk."
