---
layout: post
title: "The Momentum of News"
date: 2025-06-17
category: trading
---

### Summary

This paper, *The Momentum of News* by **Ying Wang**, **Bohui Zhang**, and **Xiaoneng Zhu** (2018), investigates a novel phenomenon termed **"news momentum"**—the tendency of firm-specific news sentiment to persist over time. By constructing monthly firm-level sentiment scores from a large dataset of real-time news articles (2000–2016), the authors demonstrate that firms with more positive (or negative) news tend to generate similar sentiment news in subsequent periods.

The research evaluates three hypotheses to explain this persistence:
- **Stale Information Hypothesis**
- **Strategic Disclosure Hypothesis**
- **Fundamental Persistence Hypothesis**

The results strongly support the **Fundamental Persistence Hypothesis**: news sentiment mirrors enduring firm fundamentals rather than merely being a product of repeated stories or manipulated disclosures.

A trading strategy exploiting this momentum—going long on firms with positive sentiment and short on those with negative—produces an annualized risk-adjusted return of **7.45%**, indicating **mispricing** due to investor underreaction.

### Key Ideas

**Page 1, Paragraph 3**  
The paper sets the stage by emphasizing a key question: is news itself predictable in a cross-sectional sense? If so, understanding news dynamics could deepen insights into stock return anomalies and investor behavior.

**Page 19, Paragraph 2**  
Strategic disclosure is evaluated as a potential driver of news momentum. However, empirical results show that firms' disclosure behaviors, even when strategically managed, do not significantly explain the persistent pattern in news sentiment.

**Page 44, Paragraph 1**  
The authors apply a trading strategy based on news sentiment scores and find that it yields strong returns not explainable by standard risk models. This reinforces the notion of **market inefficiency** due to **investor underreaction** to news patterns.

### Data and Methodology

- **Source**: RavenPack News Analytics (2000–2016)
- **Sample**: ~2,600 firms/month across NYSE, Amex, Nasdaq
- **Articles**: Over 6.7 million firm-specific news items
- **Fields Used**:
  - News sentiment scores (scaled -1 to 1)
  - Firm fundamentals: ROA, earnings surprises (SUE)
  - Market data: returns, beta, size, analyst coverage, institutional holdings
  - Categorization into hard vs. soft news

### Reflection

This study presents compelling evidence that market participants do not fully incorporate information from news patterns into prices. It bridges behavioral finance and information theory by showing that **predictable patterns in news**—rooted in real firm fundamentals—are **not efficiently priced**, providing both a **trading edge** and a deeper understanding of financial market anomalies.

### Reference

* [1] [The Momentum of News - Ying Wang, Bohui Zhang, Xiaoneng Zhu (2018)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3267337)
