---
layout: post
title: "Research Paper Relative Strength Strategies for Investing"
date: 2025-06-16
category: trading
---

**Author**: Mebane T. Faber
**Affiliation**: Cambria Investment Management, Inc.
**Publication Year**: 2010

### Abstract Summary

This paper presents practical, quantitative methods aimed at enhancing risk-adjusted returns through momentum investing. The author tests a relative strength model using U.S. equity sector data dating back to the 1920s and global asset class data from 1973 onward. The models, which involve monthly rebalancing based on trailing returns, outperform traditional buy-and-hold strategies in roughly 70% of years. Additional techniques such as trend-following dynamic hedging further reduce volatility and drawdowns.

### Key Ideas and Comments (Pages 6–7 and 11–12)

#### Pages 6–7

* **Momentum Strategy Rules**:

  * Rank sectors monthly based on trailing total returns (including dividends).
  * Invest in the top 1, 2, or 3 ranked sectors (equal-weighted within the top group).
  * Rebalance monthly, replacing any sector that falls out of the top rankings.
* **Execution Details**:

  * Monthly rebalancing at month-end close prices.
  * Ignores intra-month movements.
  * Total returns include dividends.
  * Taxes, commissions, and slippage are excluded at this stage.
* **Comment**: The approach is straightforward and accessible, offering a clean rule-set for momentum investing. However, omission of trading costs and taxes suggests real-world results may vary slightly.

#### Pages 11–12

* **Primary Drawback**: Relative strength strategies are fully exposed to market risk due to being long-only and fully invested.
* **Two Solutions Proposed**:

  * **Dynamic Hedging**: Move to cash (T-Bills) when the S\&P 500 drops below its 10-month simple moving average (SMA). This reduces drawdowns and volatility.
  * **Diversification**: Incorporate non-correlated global asset classes to broaden exposure and reduce reliance on U.S. equities.
* **Comment**: These enhancements significantly improve the robustness of the strategy, especially for periods of market downturn.

### Data and Fields Used

* **US Sector Data**:

  * Source: French-Fama CRSP Data Library
  * Timeframe: July 1926 to December 2009 (monthly returns)
  * Fields: Sector names, total returns (with dividends)
  * Sectors: 10 industry groups (e.g., Consumer Durables, Technology, Utilities)
* **Global Asset Classes**:

  * Timeframe: 1973–2009
  * Asset Types: U.S. Stocks, Foreign Stocks, Bonds, Commodities, REITs
  * Data Fields: Monthly total returns, including dividends

### Potential Issues

1. **Overfitting and Lack of Out-of-Sample Testing**
   - Strategy is tailored to historical data without formal out-of-sample validation.
   - Heavy reliance on one data source (French-Fama) for equity sectors.

2. **Transaction Costs and Tax Implications**
   - Paper ignores taxes and commissions in base simulations.
   - Real-world implementations could face 70–100% portfolio turnover annually, reducing net returns.

3. **Assumes Perfect Execution**
   - Assumes exact execution at month-end prices, with no slippage or bid-ask spread.
   - Does not account for liquidity constraints in historical data, especially before ETFs existed.

4. **Risk of Regime Change**
   - The model assumes that momentum will continue to outperform into the future.
   - Structural changes in markets or regulations may impact strategy efficacy.

### Reflection

Faber’s work is notable for translating academic momentum concepts into clear, executable strategies for individual investors. The empirical rigor over long time periods across both U.S. sectors and global assets, combined with realistic strategy enhancements like dynamic hedging, make this paper both informative and practical. While the exclusion of real-world costs needs attention, the overall framework provides a solid foundation for further customization and implementation in live portfolios.

# Reference

* [1] [Relative Strength Strategies for Investing](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1585517)
