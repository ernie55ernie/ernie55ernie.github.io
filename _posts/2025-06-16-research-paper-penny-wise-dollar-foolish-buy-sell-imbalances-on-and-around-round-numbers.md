---
layout: post
title: "Research Paper Penny Wise, Dollar Foolish: Buy-Sell Imbalances On and Around Round Numbers"
date: 2025-06-16
category: trading
---

### Authors

- **Utpal Bhattacharya** – Kelley School of Business, Indiana University  
- **Craig W. Holden** – Kelley School of Business, Indiana University  
- **Stacey E. Jacobsen** – Cox School of Business, Southern Methodist University  

### Publication Year: 2011

---

## Abstract Summary

This paper investigates how stock traders use round numbers as cognitive reference points. By analyzing over 100 million stock transactions, the authors show that there is consistent excess buying just below round numbers (e.g., $6.99) and excess selling just above them (e.g., $7.01). This behavior leads to significant buy-sell imbalances and suboptimal trading outcomes, including an estimated $1 billion annual wealth loss due to these biases. The study explores three main effects — the **left-digit effect**, the **threshold trigger effect**, and **cluster undercutting** — which together explain this round number phenomenon.

---

## Key Ideas and Comments

### Page 3 Paragraph 1
- **Key Idea**: Traders treat round numbers as psychological thresholds, triggering distinctive trading actions when prices approach these levels.
- **Comment**: Fundamental behavioral finance insight ideal for designing D0 alphas that exploit price movement patterns near integers.

### Page 3 Paragraph 2
- **Key Idea**: Empirical confirmation of three effects — left-digit, threshold trigger, and cluster undercutting — using a massive trade dataset.
- **Comment**: These effects offer actionable frameworks for building trading rules that generalize well across markets and geographies.

### Page 5 Paragraph 2
- **Key Idea**: Quantifies the economic cost of these behavioral biases at approximately $1 billion per year in lost wealth.
- **Comment**: Highlights the real-world profitability of trading strategies that anticipate and exploit round number behaviors.

---

## Data and Fields Used

- **Source**: NYSE Trade and Quote (TAQ) database (2001–2006)
- **Sample**: 137 million trades from 100 randomly selected firms per year
- **Fields**:
  - Trade price and volume
  - Bid and ask quotes
  - Time-stamped trade sequences
  - Market capitalization, institutional ownership (from CRSP and CDA Spectrum)
  - Price path conditions (e.g., bid/ask hitting or crossing integers)

---

## Potential Issues in Implementing Strategies Based on This Paper

### 1. **Market Microstructure Evolution**
- Tick size has changed post-2006 (e.g., sub-pennying, fragmentation), possibly diluting round-number clustering.
- Increased use of algorithms and HFT may reduce manual trader biases, affecting strategy longevity.

### 2. **Data Latency and Real-Time Execution**
- Identifying and executing trades near round numbers requires real-time quote processing.
- Latency in data feeds or order placement can erode potential profit margins, especially in high-volume stocks.

### 3. **Order Classification Ambiguity**
- Buy/sell classification based on quote midpoint can introduce noise due to mid-quote trades or stale quotes.
- Misclassification risk increases in volatile markets or during quote flickering.

### 4. **Cross-Market Generalization**
- Effects observed in U.S. equity markets may not fully translate to emerging markets or assets with different tick sizes.
- Cultural or institutional differences (e.g., retail vs. institutional dominance) can affect trader psychology and round number sensitivity.

---

## Reflection

This paper is a classic in behavioral finance and market microstructure. It not only diagnoses a widespread trader bias but also demonstrates its systematic, measurable impact on market behavior and returns. The authors' rigorous approach and practical implications make this a foundational reference for anyone developing short-term trading signals based on behavioral patterns. Its insights are easily translatable into algorithmic strategies and applicable across asset classes and regions.

---

# Reference

* [1] Penny Wise, Dollar Foolish: Buy-Sell Imbalances On and Around Round Numbers (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1569922)
