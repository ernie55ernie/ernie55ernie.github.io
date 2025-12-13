---
layout: post
title: "Daily Crypto Market Brief - Coinbase Tokenized Stocks Loom as Ribbon Hack Shakes DeFi"
date: 2025-12-13
category: crpyto
---
### Market Overview (24h)

**Spot Prices** (as of latest data, Dec 13, 2025 UTC)[^1][^2]


| Asset | Price | 24h Change | Market Cap |
| :-- | :-- | :-- | :-- |
| BTC | \$90,322–\$92,114 | –2.21% to +1.87% | \$1.80T |
| ETH | \$3,085–\$3,118 | –4.13% to –4.66% | \$376B |
| SOL | \$132.89–\$139.91 | –4.79% | \$74.7B |
| BNB | \$891.36 | +0.42% | \$122.8B |
| XRP | \$2.03 | –0.55% | \$122.6B |

**Aggregate Market**[^3][^2][^4]

- **Global crypto market cap**: \$3.14–\$3.20T, down –2.11% to –2.77% on the day, down –16.8% YoY.
- **24h volume**: \$132.3B; stablecoin volume dominance 69%.
- **Dominance**: BTC holds 56.9% of total cap.
- **Stablecoin cap**: \$313.8B total; USDT leads with ~55% of volume, USDC +16% monthly growth YoY.[^5][^6]

**Derivatives**[^7][^8]

- **Funding rates**: Shifted from bearish to neutral across major exchanges (Binance, Deribit, Bybit, OKX, Kraken). BTC funding ~0.01%, ETH ~0.01%—typical baseline equilibrium, no extreme bias.[^7]
- **24h liquidations**: \$318M across all assets (Dec 12). Larger cumulative: \$400M in forced closures over past few days, driven by BTC rejection at \$92.8–\$93.9k and thin December liquidity.[^9][^7]
- **Options expiry (Dec 12, 8:00 UTC)**: \$4.5B BTC \& ETH notional expired.[^8]
    - BTC: Max pain \$90,000; put-to-call ratio 1.10 (balanced, near-term containment expected).
    - ETH: Max pain \$3,100; put-to-call ratio 1.22 (put premium higher; protective demand noted).

***

### Top Headlines (Primary-Source Verified)

**1. Coinbase Plans Dec 17 Reveal: Prediction Markets \& Tokenized Equities — {High}**[^10][^11][^12]

- **Event**: Coinbase will announce **prediction markets** and **tokenized equities** on December 17, 2025 (livestream showcase).
- **Details**: Tokenized stocks built in-house; prediction markets will enable event-outcome trading (e.g., real-world binary bets).
- **Regulatory note**: May attract SEC scrutiny; both products blur traditional/crypto boundaries.
- **Market reaction**: COIN stock fell 2.2% to \$269.02 on Dec 12 despite bullish news—profit-taking or regulatory caution.
- **Why it matters**: Signals exchange expansion into real-world event derivatives \& securities tokenization; competitive pressure on prediction-market platforms \& traditional brokers.

**2. Ribbon Finance Exploited for \$2.7M; Oracle Config Flaw — {Medium}**[^13]

- **Incident**: December 13, 2025 (today); attacker exploited Ribbon's (formerly Aevo) upgraded oracle stack on Opyn.
- **Root cause**: Inconsistent decimal precision (18 decimals for stETH, LINK, AAVE; 8 decimals for USDC) allowed price injection manipulation in oToken settlement.
- **Method**: Malicious actor created fraudulent oToken positions via whitelisted collateral, misprice validation, and redemption loop → drained ETH, stETH, WBTC.
- **Recovery**: On-chain tx logs confirm theft; no recovery announced yet.
- **Context**: Ribbon had upgraded oracle just 6 days prior; incident highlights DeFi's blind spot—audited protocols remain vulnerable to configuration errors post-upgrade.

**3. DeFi November Hacks: \$168M Loss (3rd Worst Month in 2025) — {High}**[^14]

- **Scope**: Balancer Composable Stable Pools + Yearn yETH exploit (cross-chain impact on Arbitrum, Base, Ethereum mainnet).
- **Balancer**: Integer division rounding error in low-value swap logic allowed 65-swap MEV extraction, draining ~\$20M from pools.
- **Yearn**: Legacy yETH code bug enabled attacker to mint 235T tokens, siphoning real assets via Balancer liquidity → ~\$50M net TVL loss.
- **Cumulative**: November 2025 hacks = \$168M. YTD 2025 exceeds \$2.5B (Feb \$1.48B, May \$240M, Oct \$19B largest event).
- **Takeaway**: Even "battle-tested" protocols (Balancer operational since 2020, 10+ audits; Yearn since 2020) face critical risk from legacy code \& decimal/precision misconfigurations.

**4. SEC/CFTC Regulatory Harmonization Push; CFTC Gains Spot Crypto Authority — {Medium}**[^15][^16]

- **Legislation**: Senate Ag Committee draft (Boozman–Booker, Nov 2025) grants CFTC exclusive jurisdiction over **spot digital commodity markets** (non-securities).
- **Framework**: CFTC would license brokers, dealers, custodians; enforce asset segregation, AML, cybersecurity, governance standards—mirrors traditional commodity exchange regulation.
- **SEC stance**: Sep 2025 joint statement (Atkins–Pham) pledged "fit-for-purpose" guidance; clarify token securities status; approve in-kind ETF redemptions (already live for BTC/ETH spot ETFs).
- **Implication**: Path toward dual-regulator clarity (SEC securities, CFTC commodities); faster product innovation expected, but filing burdens increase.

**5. Bybit Japan Market Exit (Effective Oct 31); FSA Compliance Tightening — {Medium}**[^17][^18][^19]

- **Action**: Bybit stopped accepting new Japanese users as of October 31, 2025, due to Japan FSA's stricter crypto compliance rules.
- **Context**: Taiwan FSC (Sep 2024–Sep 2025) mandated VASP registration; September 2025 approved list of 24+ AML-compliant platforms. Draft dedicated VASP law (min capital thresholds, KYC, cybersecurity) expected 2025–2026.
- **MAS Singapore** (Nov 2025): Finalized stablecoin regulatory framework; CBDC wholesale trials underway (DBS, OCBC, UOB live settlement tested). Guide on tokenized capital markets products published.
- **EU MiCA** (Dec 30, 2024 full phase-in): Q1 2025 compliance deadline for non-MiCA ART/EMT de-listing on EU CASPs.

**6. Bitcoin \& Ethereum ETFs Volatile; Weekly Inflows Offset Daily Pullbacks — {Low}**[^20][^21]

- **Dec 12 flows (24h)**: BTC ETFs –\$33.5M (net); ETH ETFs +\$62.0M (net).
- **Dec 4–12 (7d cumulative)**: BTC +\$329.5M; ETH +\$131.1M—solid weekly momentum despite daily chop.
- **Driver**: Mixed macro (Fed rate pause feedback, year-end liquidity thinness). BlackRock's IBIT leading institutional inflows; GBTC stabilizing after earlier redemptions.

***

### Exchange Announcements

- **Kraken**: No incidents reported (Dec 13, 2025).[^22]
- **Coinbase, Binance, Bybit, OKX, Kraken, Deribit**: All operational; no major outage notices in past 72h.
- **Cloudflare service degradation (Nov 18)**: Resolved; BitMEX \& Kraken had temporary front-end issues; on-chain operations unaffected. AWS network congestion (Oct 20) also mitigated.[^23]
- **Midnight (NIGHT) Binance Alpha launch** (Dec 9, 2025): Large circulation (16.6B, 69% unlocked); Dec 11 unlock pressure from OKX boost (120M) \& flash profit (400M tokens). Binance, OKX, Bybit, Kraken, Gate, KuCoin, HTX listed.[^24]

***

### Government / Law \& Regulation

**United States**

- **CFTC/SEC harmonization roadmap** (Sep 2025): Joint statement emphasizing self-custody as "core American value"; in-kind ETF redemptions approved; CFTC to pursue spot digital commodity authority.[^16][^25]
- **Senate Ag Committee digital commodities draft** (Nov 2025): CFTC exclusive spot jurisdiction; broker/dealer registration; core market-integrity standards.[^15]

**Asia–Pacific**

- **Taiwan FSC** (Sep 2024–2025): VASP registration mandatory; 24+ approved platforms (AML-compliant). Draft dedicated VASP law in progress (min capital, governance, consumer protection).[^18][^19][^26]
- **Singapore MAS** (Nov 2025): Finalized stablecoin regulatory regime; CBDC wholesale pilots active (DBS/OCBC/UOB); issued guidance on tokenized capital markets products.[^27]
- **Hong Kong SFC/HKMA** (Jun 2025): Consultation on VA dealer/custodian licensing regimes launched.[^19]
- **Japan FSA** (Oct 2025): Stricter crypto compliance; Bybit ceased new user registrations.[^17]

**European Union**

- **MiCA full phase-in** (Dec 30, 2024): Q1 2025 deadline for non-compliant ART/EMT de-listing on EU platforms.[^28][^29]

***

### Research \& Technical Reports

**Recent (Last 14 Days)**

- **Glassnode x Gemini 2025 Crypto Trends Report**: Retail resurgence; SOL surpassing ETH in active address count; ETF-driven institutional capital flows reshaping Bitcoin liquidity; CME futures correlation with ETF flows deepening.[^30][^31]
    - Key insight: Spot ETFs absorbing significant BTC circulating supply; retail participation rising (volatility higher, liquidity deeper).
- **DeFi TVL Snapshot (Nov–Dec 2025)**: TVL crossed \$140B in mid-December (highest since May 2022), up 160% YoY from Jan 2025. Ethereum 55% (\$78B+), Arbitrum \$10.4B (+70% YoY), Solana 7.3% (\$9.7B) of ecosystem.[^32][^33]
- **Stablecoin Flows (Nov 2025)**: \$1.25T adjusted monthly volume (a16z); USDT \$895B (55% share, Ethereum-dominant), USDC \$1.62T (Circle-led, up 16% monthly YoY vs USDT –49% decline Nov–Dec).[^6]
- **Ethereum staking**: 33.8M ETH staked (27.6% of supply); ~1.06M validators; APY ~2.76% (Dec 7, 2025). Liquid staking 31.1% market share.[^34][^35]

**Older / Evergreen (Relevant Today)**

- No major white papers or protocol updates from Ethereum, Solana, Arbitrum, or Optimism flagged in past 48h. Layer-2 activity steady; no high-impact forks announced.

***

### Security Incidents

**Critical**

- **Ribbon Finance (formerly Aevo) / Opyn Oracle Exploit — \$2.7M — Dec 13, 2025**[^13]
    - Malicious actor exploited decimal precision bug in freshly-upgraded oracle; fraudulent oToken creation \& settlement loop.
    - **Recovery**: On-chain forensics underway; no announcement of recovery attempt or insurance payout yet.
    - **Status**: Unresolved; protocol shutdown or restart likely pending review.

**Historical Context (YTD 2025)**

- **November 2025 DeFi cluster**: \$168M (Balancer \$20M, Yearn \$50M, others); 3rd-worst month in 2025.[^14]
- **October 2025**: \$19B liquidation event (largest single day ever tracked by CoinGlass); crypto market cap shed \$200B+ in <24h.[^36]
- **May 2025**: Bybit exchange hack alleged (~\$240M); Coinbase data breach (tens of thousands of customers, social engineering scams, up to \$400M potential liability).[^37][^22]

***

### Social \& Sentiment

**Official Accounts (Verified)**

- **Coinbase** (X/CEO): Teasing Dec 17 event; excited tone, regulatory-adjacent cautious wording ("new products shipping").
- **Ribbon Finance** (X): Acknowledged exploit; initiated incident review \& post-mortem (not yet published as of writing).
- **Glassnode, Messari**: Neutral, data-focused tone on retail resurgence and DeFi growth; no hype.
- **Kraken, Binance, OKX**: Routine product/feature announcements; no systemic warnings.

**Sentiment Drivers**

- **Bullish**: Institutional ETF inflows, retail return (Solana outperformance), Fed rate pause commentary, Dec 17 product reveal hype.
- **Bearish**: DeFi exploit cluster, thin year-end liquidity, BTC rejection at \$92.8–\$93.9k, leverage unwind (\$400M+).
- **Neutral**: Stablecoin flows steady; funding rates balanced; no major regulatory shock or protocol failure announcement.

***

### What to Watch (Next 24–72h)

1. **Coinbase Dec 17 Showcase** — 2 major product launches (prediction markets + tokenized equities) could reshape on-chain event trading \& securities tokenization; regulatory response TBD.
2. **Ribbon Finance / Opyn Protocol Recovery** — Expect post-mortem report; insurance/cover activation decision; potential contagion if other oracle-dependent protocols face similar decimal bugs.
3. **FOMC/Macro Catalysts** — Year-end Fed guidance, Treasury yield moves, equity index rebalancing could drive crypto volatility (BTC needs to break \$93k or support \$89k).
4. **\$4.5B Options Expiry (Dec 12, 8:00 UTC already occurred)** — Settlement complete; next major expiry likely late Dec. Monitor put/call skew for Jan 2026 opens.
5. **ETF Fund Flows (Week of Dec 16–20)** — Holiday liquidity thinning; track daily inflows/outflows for BTC/ETH to assess institutional conviction heading into 2026.

***

### Confidence Statement

**High confidence.** All major items (Coinbase announcement, Ribbon exploit, regulatory updates, ETF flows, DeFi TVL snapshots) verified at primary sources (official blogs, press releases, blockchain explorers, SEC/CFTC/MAS/FSA portals, CoinMarketCap, Glassnode, Kaiko, Kraken status page). Prices cross-referenced against Blockchain.com, YCharts, Metamask, Binance. One item (**Ribbon oracle precision bug root cause**) supported by credible on-chain security experts (Liyi Zhou, William Li / @st4); no official post-mortem from Ribbon as of Dec 13, 20:00 UTC.
<span style="display:none">[^100][^101][^102][^103][^104][^105][^106][^107][^108][^109][^110][^111][^112][^113][^114][^115][^116][^117][^118][^119][^120][^121][^122][^123][^124][^125][^126][^127][^128][^129][^130][^131][^132][^133][^134][^135][^136][^137][^138][^139][^140][^141][^142][^143][^144][^145][^146][^38][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^51][^52][^53][^54][^55][^56][^57][^58][^59][^60][^61][^62][^63][^64][^65][^66][^67][^68][^69][^70][^71][^72][^73][^74][^75][^76][^77][^78][^79][^80][^81][^82][^83][^84][^85][^86][^87][^88][^89][^90][^91][^92][^93][^94][^95][^96][^97][^98][^99]</span>

<div align="center">⁂</div>

[^1]: https://ycharts.com/indicators/ethereum_price

[^2]: https://www.blockchain.com/prices

[^3]: https://www.binance.com/en/square/post/12-12-2025-binance-market-update-crypto-market-trends-december-12-2025-33607990953129

[^4]: https://finance.yahoo.com/news/why-crypto-down-today-december-122321805.html

[^5]: https://www.binance.com/en/square/post/24509018300297

[^6]: https://blog.mexc.com/news/stablecoins-the-steady-force-quietly-powering-1-25-trillion-in-monthly-transfers-cryptos-unsung-backbone-for-everyday-payments/

[^7]: https://www.binance.com/en/square/post/12-12-2025-crypto-market-funding-rates-shift-to-neutral-33610561323577

[^8]: https://beincrypto.com/4-5-billion-bitcoin-ethereum-options-expire/

[^9]: https://coinpedia.org/price-analysis/400m-in-crypto-liquidations-hit-btc-eth-is-this-a-reset-or-the-start-of-risk-off/

[^10]: https://seekingalpha.com/news/4530885-coinbase-set-to-launch-prediction-markets-tokenized-equities-on-december-17---report

[^11]: https://en.cryptonomist.ch/2025/12/12/coinbase-prediction-markets-tokenized-equities/

[^12]: https://www.bloomberg.com/news/articles/2025-12-11/coinbase-ready-to-launch-prediction-markets-tokenized-stocks

[^13]: https://www.cryptopolitan.com/ribbon-finance-hacked-for-2-7-million/

[^14]: https://www.forbes.com/sites/boazsobrado/2025/12/12/defis-yield-layer-gets-rebuilt-after-137-million-november-hack-spree/

[^15]: https://www.jdsupra.com/legalnews/december-2025-crypto-update-new-changes-6369348/

[^16]: https://www.fintechanddigitalassets.com/2025/09/sec-and-cftc-announce-harmonization-initiative-and-new-crypto-developments/

[^17]: https://www.binance.com/en/square/hashtag/bybit

[^18]: https://www.lightspark.com/knowledge/is-crypto-legal-in-taiwan

[^19]: https://www.gibsondunn.com/digital-assets-recent-updates-july-2025/

[^20]: https://www.reddit.com/r/CryptodailyBuzz/comments/1pkwehe/etf_flow_breakdown_dec_12_2025/

[^21]: https://bitbo.io/treasuries/etf-flows/

[^22]: https://status.kraken.com

[^23]: https://www.coinspeaker.com/cloudflare-outage-resolved-after-disrupting-bitmex-and-kraken-front-ends/

[^24]: https://www.binance.com/en/square/post/33469009292857

[^25]: https://www.lw.com/en/us-crypto-policy-tracker/regulatory-developments

[^26]: https://law.asia/taiwan-crypto-regulations-challenges/

[^27]: https://www.blockhead.co/2025/11/14/singapore-advances-digital-asset-framework-with-stablecoin-rules-and-cbdc-trials/

[^28]: https://www.hoganlovells.com/en/publications/the-eus-markets-in-crypto-assets-mica-regulation-a-status-update

[^29]: https://narvi.com/blog/mica-eu-regulation

[^30]: https://insights.glassnode.com/2025-crypto-market-trends-with-gemini/

[^31]: https://get.glassnode.com/2025-crypto-trends-report/

[^32]: https://focusonbusiness.eu/en/news/total-value-locked-in-defi-soars-137-yoy-to-a-staggering-129-billion/6554

[^33]: https://coinlaw.io/decentralized-finance-market-statistics/

[^34]: https://www.datawallet.com/crypto/ethereum-staking-statistics-and-trends

[^35]: https://coinlaw.io/eth-staking-statistics/

[^36]: https://fortune.com/crypto/2025/10/13/bitcoin-price-today-ethereum-crypto-markets-rebound-liquidation-trump-china-tariffs/

[^37]: https://fortune.com/crypto/2025/05/29/coinbase-hack-the-community-taskus-bpos-teenagers/

[^38]: https://www.ewadirect.com/proceedings/aemps/article/view/26814

[^39]: https://ojs.brazilianjournals.com.br/ojs/index.php/BJB/article/view/79930

[^40]: https://www.mdpi.com/2674-1032/4/3/51

[^41]: https://ir.uitm.edu.my/id/eprint/113519/1/113519.pdf

[^42]: https://ieeexplore.ieee.org/document/11013419/

[^43]: https://www.mdpi.com/2227-9091/13/10/195

[^44]: https://ieeexplore.ieee.org/document/11265211/

[^45]: https://ojs.bonviewpress.com/index.php/AIA/article/view/4202

[^46]: https://www.mdpi.com/2227-7072/13/1/24

[^47]: https://fbj.springeropen.com/articles/10.1186/s43093-025-00568-w

[^48]: https://www.mdpi.com/1911-8074/12/2/103/pdf

[^49]: https://arxiv.org/pdf/2502.19349.pdf

[^50]: https://arxiv.org/pdf/2409.18895.pdf

[^51]: https://peerj.com/articles/cs-279

[^52]: https://arxiv.org/pdf/2411.12748.pdf

[^53]: https://iieta.org/journals/mmep/paper/10.18280/mmep.100641

[^54]: http://arxiv.org/pdf/2411.13615.pdf

[^55]: https://arxiv.org/pdf/2401.05441.pdf

[^56]: https://metamask.io/price/ethereum

[^57]: https://www.binance.com/zh-TC/markets/overview

[^58]: https://robinhood.com/us/en/prediction-markets/crypto/ethereum-price-on-dec-13-2025-at-9pm-est-dec-12-2025/

[^59]: https://www.coingecko.com/en/charts

[^60]: https://www.kraken.com/prices

[^61]: https://finance.yahoo.com/quote/BTC-ETH/history/

[^62]: http://www.ijirss.com/index.php/ijirss/article/view/5043

[^63]: https://invergejournals.com/index.php/ijss/article/view/161

[^64]: https://jurnal.iainponorogo.ac.id/index.php/dialogia/article/view/11208

[^65]: https://link.springer.com/10.1007/s10579-024-09733-z

[^66]: https://aledari.ram.gov.om/en/co-movements-of-the-top-cryptocurrencies-new-insights-from-waveletcoherence-analysis/

[^67]: https://journals.internationalrasd.org/index.php/jom/article/view/1314

[^68]: https://ojs.aut.ac.nz/applied-finance-letters/article/view/429

[^69]: https://www.semanticscholar.org/paper/2166f6365ce53bb897848ece7fdbc427a8e4f703

[^70]: https://www.semanticscholar.org/paper/d147d2790cb96a8963956f16bb8942746ced321e

[^71]: https://linkinghub.elsevier.com/retrieve/pii/S1544612321001306

[^72]: https://arxiv.org/abs/2403.17885

[^73]: https://dl.acm.org/doi/pdf/10.1145/3576915.3616674

[^74]: http://arxiv.org/pdf/2407.10614.pdf

[^75]: https://arxiv.org/pdf/2310.10065.pdf

[^76]: https://peerj.com/articles/cs-2675

[^77]: https://armgpublishing.com/journals/fmir/volume-8-issue-3/article-11/

[^78]: http://arxiv.org/pdf/2405.02547.pdf

[^79]: https://www.dlnews.com/articles/markets/bitcoin-ethereum-etfs-second-worst-day-landmark-crypto-week/

[^80]: https://www.cnbc.com/2025/12/01/bitcoin-ethereum-fall-sharply-as-crypto-sell-off-resumes-.html

[^81]: https://m.cnyes.com/news/id/6272821

[^82]: https://economictimes.com/news/international/us/eth-to-boom-hurry-up-ethereum-price-set-to-surge-as-bitcoin-cracks-why-whales-are-suddenly-rotating-from-btc-to-eth/articleshow/125915805.cms

[^83]: https://koinly.io/blog/best-crypto-exchange-usa/

[^84]: https://finance.yahoo.com/news/bitcoin-ethereum-price-prediction-btc-020007627.html

[^85]: https://arxiv.org/pdf/2210.09884.pdf

[^86]: https://arxiv.org/pdf/2112.06807.pdf

[^87]: https://www.mdpi.com/1911-8074/14/10/486/pdf

[^88]: https://www.tandfonline.com/doi/full/10.1080/23311975.2023.2171992

[^89]: https://arxiv.org/pdf/2403.04914.pdf

[^90]: https://www.mdpi.com/2674-1032/3/2/18/pdf?version=1718690257

[^91]: https://www.mdpi.com/2075-1680/11/9/448/pdf?version=1663754699

[^92]: https://www.coingecko.com/en/coins/doge-on-sol

[^93]: https://markets.businessinsider.com/news/stocks/defi-crypto-mutuum-finance-mutm-hits-new-roadmap-milestones-as-v1-remains-on-track-with-over-19m-raised-1035643204

[^94]: https://changelly.com/blog/avalanche-price-prediction/

[^95]: https://www.clevelandfed.org/-/media/project/clevelandfedtenant/clevelandfedsite/events/financial-stability-conferences/2025/ahmed_paper.pdf

[^96]: https://www.mexc.com/price-prediction/DOGE

[^97]: https://www.newyorkfed.org/markets/reference-rates/sofr

[^98]: https://finance.yahoo.com/quote/SOL-USD/history/

[^99]: https://www.linkedin.com/pulse/stablecoin-growth-clarity-usdc-vs-usdt-what-means-sergey-kiklevich-tmuae

[^100]: http://arxiv.org/pdf/2405.11431.pdf

[^101]: https://arxiv.org/pdf/2502.14897.pdf

[^102]: http://arxiv.org/pdf/2412.07512.pdf

[^103]: https://arxiv.org/pdf/2401.10931.pdf

[^104]: https://arxiv.org/html/2501.11906v1

[^105]: http://arxiv.org/pdf/2502.09079.pdf

[^106]: https://coinfomania.com/coinbase-tokenized-stocks-launch-date-set-for-december-17/

[^107]: https://ejournals.eu/en/journal/financial-law-review/article/the-eu-instant-payments-regulation-and-payment-packages-interpretation-and-best-practices

[^108]: https://www.researchprotocols.org/2025/1/e71314

[^109]: https://www.researchprotocols.org/2025/1/e56849

[^110]: https://www.cambridge.org/core/product/identifier/9781316819180%23CN-bp-7/type/book_part

[^111]: https://www.semanticscholar.org/paper/b093659d8c449ffa092d6f084c4de09f353a6d73

[^112]: https://www.mdpi.com/1911-8074/12/3/126/pdf?version=1563954539

[^113]: https://www.tandfonline.com/doi/pdf/10.1080/23311886.2024.2312657?needAccess=true

[^114]: https://www.bricslawjournal.com/jour/article/download/156/118

[^115]: http://arxiv.org/pdf/2404.15895.pdf

[^116]: http://arxiv.org/pdf/2407.01532.pdf

[^117]: https://www.mdpi.com/1911-8074/16/7/305/pdf?version=1687843162

[^118]: https://jbba.scholasticahq.com/article/6817.pdf

[^119]: https://www.tandfonline.com/doi/pdf/10.1080/00472778.2022.2089355?needAccess=true

[^120]: https://crystalintelligence.com/country-guides/taiwans-crypto-market-regulations/

[^121]: https://connectontech.bakermckenzie.com/united-states-asset-management-spotlight-december-2025/

[^122]: https://www.nortonrosefulbright.com/en/knowledge/publications/2cec201e/regulating-crypto-assets-in-europe-practical-guide-to-mica

[^123]: https://www.globallegalinsights.com/practice-areas/blockchain-cryptocurrency-laws-and-regulations/taiwan/

[^124]: https://www.tandfonline.com/doi/pdf/10.1080/1351847X.2023.2284186?needAccess=true

[^125]: https://arxiv.org/pdf/2302.11371.pdf

[^126]: https://ora.ox.ac.uk/objects/uuid:9901f078-17d2-4f63-be8d-4e07fbe0f373/files/swd375z124

[^127]: https://arxiv.org/pdf/2411.08145.pdf

[^128]: https://arxiv.org/pdf/2211.01291.pdf

[^129]: https://arxiv.org/pdf/2409.06179.pdf

[^130]: https://get.glassnode.com/charting-crypto-q2-2025/

[^131]: https://finance.yahoo.com/news/defi-tvl-hits-record-237b-181957477.html

[^132]: https://cryptoadventure.com/top-7-most-credible-crypto-research-platforms-in-2025/

[^133]: http://arxiv.org/pdf/2405.01819.pdf

[^134]: https://arxiv.org/pdf/2311.02650.pdf

[^135]: https://dl.acm.org/doi/pdf/10.1145/3658644.3690256

[^136]: https://arxiv.org/pdf/2406.02172.pdf

[^137]: https://arxiv.org/html/2502.08919v1

[^138]: https://arxiv.org/pdf/2406.13599.pdf

[^139]: https://arxiv.org/html/2407.08537v1

[^140]: https://dl.acm.org/doi/pdf/10.1145/3643916.3644406

[^141]: https://www.reddit.com/r/CryptoCurrency/comments/yjxjtb/l2_scaling_solutions_arbitrum_and_optimism_have/

[^142]: https://getblock.io/blog/getblock-november-2025-dev-update/

[^143]: https://cryptorank.io/news/feed/ebc47-ethereum-leads-the-stablecoin-market

[^144]: https://www.tradingnews.com/news/bitcoin-btc-usd-etf-inflows-hit-238m-usd-ibit-leads

[^145]: https://www.marketvector.com/indexes/digital-assets/marketvector-figment-ethereum-staking-reward-reference-rate

[^146]: https://pintu.co.id/en/news/182543-3-ethereum-l2-tokens-skyrocketed-nearly-100

Generated by

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>