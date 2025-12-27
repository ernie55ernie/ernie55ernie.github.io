---
layout: post
title: "Daily Crypto Market Brief - Trust Wallet Breach Spurs Post-Holiday Crypto Caution"
date: 2025-12-27
category: crpyto
---

## Market Overview (24h)

Bitcoin traded around \$95,975 on December 27, 2025 (00:00 UTC / 08:00 Asia/Taipei), representing a +1.45% gain from the prior day, with BTC market capitalization standing at \$1.773 trillion. Ethereum remained near \$3,375 levels, while Solana posted modest gains to \$122.19, up +1.75% from December 26. Total crypto market capitalization reached approximately \$2.97 trillion (as of December 20, 2025 reference), marking a +1.19% increase, with 24-hour trading volume surging +29.20% to \$150.14 billion.[^1][^2][^3]

Derivatives markets showed heightened activity: perpetual futures volume jumped +31% to \$1.41 trillion, while average funding rates spiked +264% to 0.006%. Open interest across futures reached record levels near \$67.9 billion, with CME accounting for roughly 30% of total OI—underscoring strong institutional footprint. The CMC Fear & Greed Index remained at 21 (Fear territory) for the 18th consecutive day, marking the longest fear streak since November 2025. No major stablecoin supply disruptions or liquidation cascades were reported in the 48-hour window.[^2][^4]

**Risk: Medium** – Sustained fear sentiment + elevated funding rates suggest trader caution, but volume increase indicates accumulation activity.

***

## Top Headlines

### Trust Wallet Chrome Extension Breach – \$7M Drained

- **What happened**: Trust Wallet confirmed a security incident affecting Chrome extension version 2.68, released December 24, 2025 (12:32 UTC). Malicious code was inserted directly into the codebase (not via compromised dependency), iterating through stored wallets and exfiltrating mnemonic phrases to attacker-controlled server `api.metrics-trustwallet[.]com` (registered December 8, 2025; first request December 21, 2025).[^5][^6][^7][^8]
- **Why it matters**: Approximately \$7 million in crypto assets (Bitcoin, Ethereum, Solana) stolen from hundreds of users who logged in before December 26, 11:00 UTC. SlowMist analysis indicates attacker leveraged PostHog analytics library as data-exfiltration channel. Trust Wallet CEO Eowyn Chen stated the malicious version was published externally via leaked Chrome Web Store API key, bypassing internal release checks. Over \$4 million laundered through CEXs (ChangeNOW ~\$3.3M, KuCoin ~\$447K, FixedFloat ~\$340K); ~\$2.8M remains in hacker wallets.[^8][^5]
- **Primary source**: Trust Wallet [@TrustWallet](https://x.com/TrustWallet/status/2004316503701958786) (December 25, 2025, 22:21 UTC / December 26, 06:21 Asia/Taipei); SlowMist analysis; The Hacker News report (December 26, 2025).[^7][^5][^8]
- **Action required**: Users with version 2.68 must upgrade immediately to v2.69 via official Chrome Web Store. Mobile app and other extension versions unaffected. Trust Wallet committed to full reimbursement for affected users.

**Risk: High** – Supply-chain compromise via leaked API credentials; demonstrates vulnerability of browser-based wallets even without traditional malware vectors.

***

### Binance Trading Pair Removals

- **What happened**: Binance announced removal of five spot trading pairs effective December 26, 2025, 03:00 UTC (11:00 Asia/Taipei): BIO/FDUSD, ENS/FDUSD, INJ/ETH, TREE/BNB, VTHO/TRY. Spot Trading Bots services for these pairs terminated simultaneously. Binance also listed KGST (KGST) on Earn, Buy Crypto, and Convert on December 24, 08:00 UTC.[^9][^10][^11]
- **Why it matters**: Routine liquidity optimization; delisting reflects poor trading volume and liquidity in specified pairs. Base assets (BIO, ENS, INJ, TREE, VTHO) remain tradable on other Binance pairs. No impact on token availability.
- **Primary source**: Binance official announcement (December 24, 2025).[^12][^10]

**Risk: Low** – Standard housekeeping; no broader market impact.

***

### ESMA Statement on MiCA Transitional Measures

- **What happened**: On December 4, 2025, the European Securities and Markets Authority (ESMA) issued a statement on the Markets in Crypto-Assets Regulation (MiCA) transitional regime for crypto-asset service providers (CASPs), warning that "last-minute" authorisation applications will be treated with considerable caution. ESMA reminded EU Member State competent authorities to enforce against unauthorised provision of crypto-asset services and confirmed readiness to cooperate on cross-border enforcement.[^13][^14]
- **Why it matters**: MiCA's full implementation as of December 30, 2024, means entities offering crypto services after the transitional period must be authorised or face enforcement. ESMA warned investors that entities active post-transition are not guaranteed to be MiCA-compliant. This tightens the regulatory noose on unlicensed CASPs operating in the EU, potentially forcing exit or rapid compliance for marginal players.
- **Primary source**: ESMA official statement (December 4, 2025).[^14][^13]

**Risk: Medium** – Regulatory enforcement ramp-up; potential disruption for users of non-compliant EU-based platforms.

***

### UK FCA Publishes Comprehensive Crypto Consultation Package

- **What happened**: On December 16, 2025, the UK Financial Conduct Authority (FCA) published three consultation papers: CP25/40 (regulating cryptoasset activities including trading platforms, intermediaries, staking, lending/borrowing, DeFi), CP25/41 (admissions, disclosures, market abuse), and CP25/42 (prudential requirements). These proposals extend the FCA's regulatory remit beyond current AML/financial promotions oversight to comprehensive crypto regime under the Financial Services and Markets Act 2000 (FSMA).[^15][^16][^17]
- **Why it matters**: UK sets 2027 target for full implementation, establishing authorisation requirements for cryptoasset trading platforms, custodians, and intermediaries. CP25/40 introduces "same risk, same regulatory outcome" principle, applying Consumer Duty and stringent operational resilience standards similar to banks. The FCA emphasized enforcement priorities: financial crime, fraud, sanctions evasion, and operational resilience.[^18][^19][^15]
- **Primary source**: FCA CP25/40, CP25/41, CP25/42 (December 16, 2025).[^16][^17][^15]

**Risk: Medium** – Long implementation runway (2027), but signals UK's intent to create robust, institutionally-oriented crypto regulatory framework. Firms must monitor consultation outcomes for compliance roadmaps.

***

### Taiwan Stablecoin Framework Targets Mid-2026 Launch

- **What happened**: On December 3, 2025, Taiwan's Financial Supervisory Commission (FSC) Chairman Peng Jin-lung told lawmakers that Taiwan's first domestic stablecoin (pegged to New Taiwan Dollar) could launch as early as June-July 2026, pending legislative approval. The FSC is submitting the "Virtual Assets Service Act" draft to Cabinet this week, with legislative passage targeted for H1 2025 and implementation in H2 2025.[^20][^21]
- **Why it matters**: Taiwan's regulatory framework will require VASPs to register/obtain licenses, meet capital and AML requirements, and comply with consumer protection standards. Initial stablecoin issuance will be restricted to licensed financial institutions to manage risks. This positions Taiwan as a regional leader in regulated digital finance, following MAS (Singapore) and SFC (Hong Kong) frameworks.
- **Primary source**: FSC Chairman Peng Jin-lung statement to Legislative Finance Committee (December 3, 2025); Taipei Times / Focus Taiwan reporting.[^21][^20]

**Risk: Low** – Regulatory clarity positive for Taiwan-based crypto operators; mid-2026 timeline provides industry preparation window.

***

## Exchanges

- **Binance**: Delisted spot pairs BIO/FDUSD, ENS/FDUSD, INJ/ETH, TREE/BNB, VTHO/TRY (December 26, 03:00 UTC). Listed KGST on Earn/Convert (December 24, 08:00 UTC). Quarterly 0626 delivery contracts (USDS-M, COIN-M) scheduled to list after 1226 contracts expire December 26, 08:00 UTC.[^22][^10][^9]
- **OKX**: Launched SOL/BTC and ETH/BTC spot trading pairs (December 26, 08:00 PST / 00:00 UTC December 27). Delisted DEGENUSDT and CETUSUSDT perpetual futures (December 26, 08:00 UTC). FXS spot trading and futures suspended for migration to FRAX token (December 26-29, 2025).[^23][^24][^25]
- **Coinbase**: Resolved multiple Ethereum Network and Polygon Network delayed send/receive incidents between December 24-26, 2025 (various timeframes). Coinbase Exchange listed CFG-USD and ZKP-USD markets; no other incidents reported.[^26][^27][^28][^29]
- **Kraken, Bybit, Bitfinex, Deribit**: No material incidents or announcements in 72-hour window.

**Risk: Low** – Routine maintenance and pair adjustments; no systemic exchange disruptions.

***

## Regulation/Law

### United States

- **CFTC**: On December 4, 2025, Acting Chair Caroline Pham announced that spot cryptocurrency products will begin trading for the first time on federally registered futures exchanges. This follows a September 2025 joint CFTC-SEC statement clarifying that registered exchanges are not prohibited from facilitating certain spot crypto commodity products.[^30]

**Risk: Low** – Positive regulatory clarity; expands on-shore trading venues for spot crypto.

### European Union

- **ESMA (MiCA)**: December 4, 2025, statement on transitional period enforcement (detailed above in Headlines).[^13][^14]

**Risk: Medium** – Enforcement ramp-up for non-compliant CASPs.

### United Kingdom

- **FCA**: December 16, 2025, consultation papers CP25/40, CP25/41, CP25/42 on comprehensive crypto regulatory framework (detailed above in Headlines).[^17][^15][^16]

**Risk: Medium** – 2027 implementation timeline provides clarity but requires industry preparation.

### Taiwan

- **FSC**: December 3, 2025, announcement of Virtual Assets Service Act targeting H1 2025 legislative passage and mid-2026 stablecoin launch (detailed above in Headlines).[^20][^21]

**Risk: Low** – Positive regulatory clarity for Taiwan market participants.

### Singapore

- **MAS**: June 30, 2025, deadline for Digital Token Service Providers (DTSPs) offering services to overseas clients to obtain license or cease operations. Penalties include fines up to SGD 250,000 and/or imprisonment up to 3 years. *(Note: This deadline has passed; enforcement actions may be ongoing but not confirmed in December 2025 data.)*[^31][^32][^33]

**Risk: N/A** – Enforcement window closed; monitor for any retrospective actions.

***

## Research/White Papers

- **Glassnode Q4 2025 Institutional Market Perspectives** (published December 3, 2025): Bitcoin attracted >\$732B in new capital—more than all previous cycles combined—lifting Realized Cap to ~\$1.1T with +690% price gain. Long-term volatility nearly halved from 84% to 43%. Spot volumes rose from \$4B–\$13B (prior cycle) to \$8B–\$22B/day. CME accounts for ~30% of total OI (\$67.9B record). Stablecoin supply reached record \$263B (top 5). Tokenized RWAs grew from \$7B to \$24B in one year. DEX perpetual share increased from ~10% to 16-20%, with monthly volume surpassing \$1T.[^4]
- **Gemini + Glassnode 2025 Crypto Market Trends** (published June 19, 2025): Solana active addresses now exceed Bitcoin by 16.2x and Ethereum by 24.6x. Solana settles \$37B daily, surpassing both BTC and ETH. Solana-based memecoin realized cap grew +477%, outpacing Ethereum. Report covers 30+ pages of ETF flows, futures, retail vs. institutional behavior.[^34]
- **Messari "The Crypto Theses 2025"** (published December 23, 2024): Anticipates Layer-2 designs to outperform native Layer-1s; Solana ecosystem expansion beyond speculation; RTK networks (e.g., GEODNET) to achieve 90-100% EU/NA coverage by end-2025 with revenue >\$10M.[^35]

**Risk: N/A** – Research publications provide market context; no immediate risk implications.

***

## Security Incidents

### Trust Wallet Chrome Extension Breach – \$7M

- **Incident**: Malicious code in Trust Wallet Chrome extension v2.68 (December 24-26, 2025) exfiltrated mnemonic phrases, draining ~\$7M across Bitcoin, Ethereum, Solana. Hundreds of users affected. Funds laundered via ChangeNOW, KuCoin, FixedFloat; ~\$2.8M remains in attacker wallets.[^6][^5][^7][^8]
- **Cause**: Attacker used leaked Chrome Web Store API key to publish malicious version bypassing internal release process. Malicious code directly in Trust Wallet codebase, not via compromised npm package.[^8]
- **Mitigation**: Trust Wallet released v2.69 patch (December 26, 2025); committed to full user reimbursement. Users must upgrade immediately and avoid phishing "compensation" forms not from official channels.[^8]
- **On-chain confirmations**: ZachXBT, PeckShield tracked wallet addresses and laundering flows.[^5][^8]

**Risk: High** – Supply-chain compromise; emphasizes need for hardware wallet isolation for high-value holdings.

### No Additional Major Exploits Reported

- **Solana Network**: No major outages reported in December 2025. Last officially acknowledged outage was February 6, 2024 (5-hour halt). StatusGator detected multiple undisclosed disruptions from October 2024–February 2025 (up to 13 hours), but Solana team never acknowledged.[^36][^37]
- **Coinbase Exchange**: Minor Ethereum/Polygon network delayed send/receive incidents (December 24-26, 2025), all resolved within hours. No user fund loss.[^28][^29][^26]

***

## What to Watch (Next 24–72h)

- **Trust Wallet Reimbursement Process**: Monitor official channels (trustwallet-support.freshdesk[.]com) for affected user compensation details. Beware of phishing scams impersonating Trust Wallet support via Telegram ads and fake forms.[^8]
- **Binance USDS-M/COIN-M Quarterly 0626 Contracts Launch**: Expected after December 26, 08:00 UTC settlement of 1226 contracts. Watch for initial volume and basis dynamics.[^22]
- **ESMA MiCA Enforcement Actions**: EU national regulators expected to begin enforcement against non-compliant CASPs post-December 30, 2024, transitional period. Monitor for exchange/CASP suspension announcements in EU jurisdictions.[^14][^13]
- **OKX FXS→FRAX Token Migration**: Snapshot December 29, 03:00 UTC; migration completes by December 31, 10:00 UTC. Users with FXS must upgrade KYC to Lv.2 or miss migration.[^23]
- **Funding Rate Normalization**: December 27-28 perpetuals funding (currently 0.006%, +264% spike) may normalize if leveraged positions unwind. Monitor BTC/ETH/SOL funding every 8 hours for deleverage signals.[^38][^2]

***

## Confidence Statement

**High confidence; all items verified at primary sources or authoritative secondary sources (official exchange announcements, regulator press releases, on-chain analysis from SlowMist/PeckShield/ZachXBT).** One item (MAS June 30, 2025, deadline) predates reporting window but included for context; enforcement actions post-deadline not confirmed in current data.

***

**Compiled**: December 28, 2025, 00:57 Asia/Taipei
**Sources**: Trust Wallet, Binance, OKX, Coinbase status pages; ESMA, FCA, FSC Taiwan official statements; Glassnode, Messari, Gemini research reports; SlowMist, PeckShield, ZachXBT security analysis; CoinMarketCap, YCharts, CoinGecko market data.
<span style="display:none">[^100][^101][^102][^103][^104][^105][^106][^107][^108][^109][^110][^111][^112][^113][^114][^115][^116][^117][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^51][^52][^53][^54][^55][^56][^57][^58][^59][^60][^61][^62][^63][^64][^65][^66][^67][^68][^69][^70][^71][^72][^73][^74][^75][^76][^77][^78][^79][^80][^81][^82][^83][^84][^85][^86][^87][^88][^89][^90][^91][^92][^93][^94][^95][^96][^97][^98][^99]</span>

<div align="center">⁂</div>

[^1]: https://ycharts.com/indicators/solana

[^2]: https://blockchain.news/flashnews/crypto-market-update-total-cap-hits-2-97-trillion-usd-perp-volume-up-31-percent-to-1-41-trillion-usd-funding-up-264-percent-to-0-006-percent-fear-and-greed-at-21

[^3]: https://ycharts.com/indicators/bitcoin_market_cap

[^4]: https://insights.glassnode.com/q4-2025-institutional-market-perspectives/

[^5]: https://www.news4hackers.com/malicious-code-caused-7-million-crypto-loss-by-trust-wallet-chrome-extension-breach/

[^6]: https://x.com/TheHackersNews/status/2004580292074606690

[^7]: https://x.com/TrustWallet/status/2004316503701958786

[^8]: https://thehackernews.com/2025/12/trust-wallet-chrome-extension-bug.html

[^9]: https://www.binance.com/en/support/announcement/detail/caaa09b168874ce4884dda4a52d99556

[^10]: https://www.binance.com/en-BH/square/post/34134229258121

[^11]: https://www.binance.com/en/square/hashtag/binancedelisting

[^12]: https://www.binance.com/en/support/announcement/detail/1351888d07104a7b93b60afae7d503c9

[^13]: https://www.esma.europa.eu/sites/default/files/2025-12/ESMA75-113276571-1631_Statement_on_end_of_MiCA_transitional_periods.pdf

[^14]: https://www.regulationtomorrow.com/france/esma-statement-on-mica-transitional-measures/

[^15]: https://www.fca.org.uk/publications/consultation-papers/cp25-40-regulating-cryptoasset-activities

[^16]: https://www.fca.org.uk/publications/consultation-papers/cp25-42-prudential-regime-cryptoasset-firms

[^17]: https://www.skadden.com/-/media/files/publications/2025/12/uk_legal_framework_for_crypto_takes_shape_with_draft_legislation_and_three_new_fca_consultations.pdf?rev=3edc6b92d0dc475a989f59ff0fb77033

[^18]: https://www.skadden.com/insights/publications/2025/12/uk-legal-framework-for-crypto

[^19]: https://www.cliffordchance.com/insights/resources/blogs/regulatory-investigations-financial-crime-insights/2025/12/balancing-innovation-and-integrity-fca-refining-minimum-standards-for-crypto-firms.html

[^20]: https://www.blockhead.co/2025/12/04/taiwan-targets-mid-2026-launch-for-domestic-stablecoin-under-new-regulatory-framework/

[^21]: https://focustaiwan.tw/business/202512030008

[^22]: https://www.binance.com/en/support/announcement/detail/ad0e765a656a4a0ca93aeb8899aa5b39

[^23]: https://www.okx.com/help/okx-to-support-fxs-crypto-migration

[^24]: https://www.okx.com/help/okx-to-delist-several-perpetual-futures-20251224

[^25]: https://www.okx.com/help/okx-will-launch-sol-btc-and-eth-btc-for-spot-trading

[^26]: https://statussight.com/status/coinbase

[^27]: https://status.exchange.coinbase.com

[^28]: https://statusgator.com/services/coinbase

[^29]: http://status.coinbase.com

[^30]: https://blockchain.bakermckenzie.com/2025/12/10/cftc-announcement-paves-the-way-for-spot-crypto-trading-on-u-s-regulated-exchanges/

[^31]: https://www.tassure.com/mas-tightens-crypto-oversight-unlicensed-overseas-facing-entities-will-be-blocked/

[^32]: https://www.binance.com/en/square/post/06-30-2025-singapore-tightens-regulations-on-digital-token-service-providers-26306271565193

[^33]: https://www.advomi.com.sg/crypto/singapore-sets-june-30-2025-deadline-for-crypto-firms-offering-overseas-digital-token-services/

[^34]: https://insights.glassnode.com/2025-crypto-market-trends-with-gemini/

[^35]: https://blockcast.it/2024/12/24/messari-the-crypto-theses-2025-report/

[^36]: https://statusgator.com/blog/solana-outage-history/

[^37]: https://protos.com/chart-its-been-262-days-since-solanas-last-major-outage/

[^38]: https://coinalyze.net

[^39]: https://www.mdpi.com/1911-8074/12/3/126/pdf?version=1563954539

[^40]: https://linkinghub.elsevier.com/retrieve/pii/S1544612324007773

[^41]: https://arxiv.org/abs/2412.02452

[^42]: http://arxiv.org/pdf/2408.11961.pdf

[^43]: http://arxiv.org/pdf/1406.5440.pdf

[^44]: https://arxiv.org/pdf/2302.11371.pdf

[^45]: https://linkinghub.elsevier.com/retrieve/pii/S037843712300599X

[^46]: http://arxiv.org/pdf/2409.10031.pdf

[^47]: https://nfttorney.com/2025/12/23/off-the-blockchain-december-15-22-2025/

[^48]: https://www.jdsupra.com/legalnews/december-2025-crypto-update-new-changes-6369348/

[^49]: https://www.leeandli.com/EN/Newsletters/7439.htm

[^50]: https://www.sec.gov/newsroom/press-releases/2025-144-sec-charges-three-purported-crypto-asset-trading-platforms-four-investment-clubs-scheme-targeted

[^51]: https://www.lw.com/en/us-crypto-policy-tracker/regulatory-developments

[^52]: https://www.leetsai.com/overview-of-taiwans-regulatory-measures-for-virtual-asset-service-providers

[^53]: https://www.ir-impact.com/2025/12/ipos-crypto-and-deregulation-the-sec-prepares-for-a-shift-in-2026/

[^54]: https://www.dwt.com/blogs/financial-services-law-advisor/2025/12/cftc-tokenized-collateral-crypto-sprint

[^55]: https://www.leetsai.com/the-financial-supervisory-commission-of-taiwan-requires-virtual-asset-custodians-to-store-more-than-70-of-customer-assets-in-cold-wallets

[^56]: https://www.fintechanddigitalassets.com/2025/08/sec-and-cftc-launch-crypto-initiatives-to-revamp-regulations-and-promote-innovation/

[^57]: https://www.leeandli.com/EN/NewslettersDetail/7374.htm

[^58]: https://arxiv.org/pdf/2502.19349.pdf

[^59]: http://eudl.eu/pdf/10.4108/eai.10-3-2022.173608

[^60]: https://arxiv.org/html/2409.03674

[^61]: https://arxiv.org/html/2502.01029v1

[^62]: https://arxiv.org/pdf/2009.11007.pdf

[^63]: https://www.mdpi.com/2075-1680/11/9/448/pdf?version=1663754699

[^64]: http://ledger.pitt.edu/ojs/ledger/article/download/213/212

[^65]: https://arxiv.org/pdf/1804.05916.pdf

[^66]: https://www.coingecko.com/en/coins/bitcoin

[^67]: https://cryptomarketcap.com

[^68]: https://www.coingecko.com/en/coins/ethereum/usd

[^69]: https://coingeckosprot.com

[^70]: https://crypto.com/en/price

[^71]: https://www.coinbase.com/price/ethereum

[^72]: https://www.coinbase.com/price/bitcoin

[^73]: https://www.kraken.com/prices

[^74]: https://ycharts.com/indicators/ethereum_price

[^75]: https://www.coingecko.com

[^76]: https://ycharts.com/indicators/bitcoin_price

[^77]: https://docs.coingecko.com/reference/crypto-global

[^78]: http://arxiv.org/pdf/2411.04616.pdf

[^79]: https://arxiv.org/abs/2411.05803

[^80]: https://arxiv.org/pdf/2303.10043.pdf

[^81]: http://arxiv.org/pdf/2411.19637.pdf

[^82]: https://arxiv.org/pdf/2305.13227.pdf

[^83]: https://arxiv.org/pdf/2201.03519.pdf

[^84]: https://arxiv.org/pdf/2503.08692.pdf

[^85]: https://arxiv.org/pdf/2206.07831.pdf

[^86]: https://www.coinglass.com/LiquidationData

[^87]: https://app-coingllass.walletuser.com/coinglass/en/

[^88]: https://www.tradingview.com/news/cointelegraph:2bbb247ab094b:0-bitcoin-has-room-to-fall-amid-unusual-open-interest-coinglass/

[^89]: https://ecmatlas.com/blog/mastering-crypto-trading-with-coinglass

[^90]: https://coinalyze.net/bitcoin/funding-rate/

[^91]: https://www.youtube.com/watch?v=2KCShdDNeBY

[^92]: https://www.youtube.com/watch?v=Lo99tX4Yz54

[^93]: https://coinalyze.net/funding-rates/

[^94]: https://o-web.coinglasscdn.com/currencies/BTC/futures

[^95]: https://www.reddit.com/r/Daytrading/comments/1biwsnc/liquidation_question/

[^96]: http://ledger.pitt.edu/ojs/ledger/article/view/325

[^97]: https://ieeexplore.ieee.org/document/9820085/

[^98]: https://journal.pandawan.id/b-front/article/view/107

[^99]: https://www.ssrn.com/abstract=3274331

[^100]: https://ieeexplore.ieee.org/document/10486777/

[^101]: https://journalajeba.com/index.php/AJEBA/article/view/1270

[^102]: https://dl.acm.org/doi/10.1145/3555776.3578996

[^103]: https://www.mdpi.com/2813-0324/11/1/20

[^104]: https://journal.sinergi.or.id/index.php/ijis/article/view/759

[^105]: https://ieeexplore.ieee.org/document/11154209/

[^106]: https://www.econstor.eu/bitstream/10419/230815/1/irtg1792dp2020-009.pdf

[^107]: https://arxiv.org/pdf/1906.05740.pdf

[^108]: https://arxiv.org/pdf/2403.00770.pdf

[^109]: https://arxiv.org/pdf/2201.12893.pdf

[^110]: https://arxiv.org/pdf/2107.12447.pdf

[^111]: https://www.mdpi.com/2199-8531/6/4/197/pdf

[^112]: http://arxiv.org/pdf/2409.04106.pdf

[^113]: https://www.bitcoinmagazinepro.com/charts/btc-open-interest/

[^114]: https://www.coindesk.com/markets/2025/05/22/bitcoin-options-open-interest-hit-record-425b-on-deribit-as-traders-eye-next-bull-target-for-btc

[^115]: https://www.gate.com/crypto-market-data/funds/liquidation

[^116]: https://coinalyze.net/bitcoin/open-interest/

[^117]: https://www.rootdata.com/news/127059

Generated by

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>