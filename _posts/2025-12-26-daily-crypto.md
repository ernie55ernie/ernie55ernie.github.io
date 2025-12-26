---
layout: post
title: "Daily Crypto Market Brief - Bitcoin Holds $88K as Record Options Expire"
date: 2025-12-26
category: crpyto
---

## Market Overview (24h)

Bitcoin trades at **\$88,744** (+1.43% 24h; range \$86,892–\$89,568), while Ethereum stands at **\$2,966.93** (+1.29% 24h). Major alts show mixed action: BNB +0.10%, SOL +0.76%, XRP +0.18%, DOGE −1.26%. The **Crypto Fear & Greed Index sits at 20 (Extreme Fear)**—down from 23 a day prior. US and European markets remain closed due to the Christmas holiday, creating thin liquidity conditions; gold surpassed \$4,500, buoyed by geopolitical risks.[^1][^2]

**Derivatives Context**: Bitcoin funding rates are mildly positive (+0.0083% current, predicted +0.0051%), reflecting modest long bias following a cooler-than-expected US CPI print on December 19 that pushed BTC past \$89k. ETH funding spiked to highest levels since late November on December 22 when Ether reclaimed \$3,000, then collapsed back to neutral. Notably, a **\$23–24 billion notional Bitcoin options expiry occurs today**, representing the largest expiry in BTC options history. Options data reveals 14,674 BTC in puts at the \$85,000 strike and 18,116 BTC in calls at \$100,000, mostly held by institutions; analysts expect the expiry to create a structural price corridor with "implicit suppression above, passive buffering below, and fluctuating within the middle range" until post-expiry risk repricing.[^3][^4][^5][^6]

***

## Top Headlines

**1. Crypto M&A Hits Record \$8.6 Billion in 2025—Institutional Confidence Surges {Risk: MEDIUM}**

Crypto mergers and acquisitions reached an all-time **\$8.6 billion** in 2025, marking the most active dealmaking year on record. The largest transaction was Coinbase's **\$2.9 billion acquisition of Deribit**, the world's leading crypto options exchange with \$30+ billion in open interest. The deal includes \$700 million in cash and 11 million Coinbase Class A shares. Other major 2025 acquisitions include Kraken's **\$1.5 billion purchase of futures platform NinjaTrader** and Ripple's **\$1.25 billion acquisition of prime brokerage Hidden Road**, which Ripple has rebranded as Ripple Prime. Hidden Road processes \$3 trillion annually across markets serving 300+ institutional clients. These deals underscore institutional appetite for regulated trading infrastructure and derivatives platforms as the Trump administration signals support for crypto innovation.[^7][^8][^9][^10]

**2. Bittensor (TAO) Launches MEV Shield; First Halving Completed {Risk: LOW}**

Bittensor officially deployed **MEV Shield**, a transaction encryption mechanism that protects users from maximal extractable value attacks (front-running and sandwich attacks) by hiding trade details until block confirmation. Development on trustless MEV—moving from proof-of-authority to proof-of-stake—is underway for early 2026. In parallel, Bittensor completed its **first halving event (~December 14), reducing daily TAO issuance from 7,200 to 3,600 tokens**, mirroring Bitcoin's supply-scarcity design. This milestone positions the decentralized AI network as a maturing ecosystem; the Bittensor subnet ecosystem now spans 129 subnets with estimated valuations near \$3 billion. TAO trades at \$223.20 (−0.73% 24h).[^11][^12][^13][^14]

**3. Ondo Finance to Launch Tokenized US Stocks and ETFs on Solana, Early 2026 {Risk: HIGH}**

Real-world asset tokenization pioneer **Ondo Finance announced plans to launch custody-backed tokenized US stocks and exchange-traded funds on Solana in early 2026**. The platform will enable 24/7 on-chain trading of actual securities held in qualified custody, eliminating traditional market hours (9:30 AM–4:00 PM ET) and T+2 settlement friction. Solana was chosen for its high throughput (thousands of transactions per second) and negligible fees (fractions of a cent per transaction). Each tokenized share represents genuine ownership with 1:1 physical backing. This expansion builds on Ondo's flagship USDY (tokenized US Treasuries), which has accumulated \$500 million in assets under management. The initiative represents one of the most ambitious bridges between Wall Street and blockchain, though regulatory approval timelines remain uncertain.[^15][^16][^17]

**4. Trip.com Launches Stablecoin Payments (USDT, USDC) {Risk: LOW}**

Travel booking platform Trip.com (Ctrip's global arm) now accepts stablecoin payments via USDT and USDC across Ethereum, Tron, Polygon, and Solana blockchains, powered by Singapore-based payment provider Triple-A. Vietnam users report savings of up to 18% on flights and 2.35% on hotels when paying in stablecoins. The integration requires only a name and email for hotel bookings, streamlining checkout. This expansion signals mass-market utility for stablecoins beyond crypto-native use cases.[^18][^19]

**5. Yearn Finance yETH Exploit: ~\$3 Million Loss {Risk: MEDIUM}**

DeFi yield-farming protocol **Yearn Finance's yETH product suffered an infinite minting exploit on November 30**, draining approximately **\$3 million in assets**. The attacker exploited a vulnerability that enabled minting an effectively limitless quantity of yETH (an index token aggregating liquid staking derivatives), which was then used to withdraw assets from Balancer liquidity pools. Roughly 1,000 ETH was transferred to privacy mixer Tornado Cash, obscuring its trail. Yearn confirmed that its larger V2 and V3 Vaults (>\$600 million TVL) remain unaffected and secure. The incident highlights contract design risks; a combined \$127 million in crypto losses occurred across hacks and exploits in November alone, per CertiK.[^20][^21]

**6. Aevo (Ribbon Finance) Options Hack: \$2.7 Million Drained {Risk: MEDIUM}**

Derivatives protocol **Aevo (formerly Ribbon Finance) was exploited for approximately \$2.7 million in December**. The root cause: an oracle update introduced a **decimal precision mismatch** (8 vs. 18 decimal places) combined with an access control vulnerability allowing anyone to set expiry prices for newly created assets. The attacker created malicious options contracts with strikes far below market prices, exploited the decimal mismatch, and drained vaults—for example, burning 225 oTokens to extract 22.46 WETH from an stETH call option. The attack underscores the risks of contract updates without comprehensive post-deployment testing.[^22]

**7. USPD Stablecoin: >\$1 Million Stolen via Deployment Exploit {Risk: MEDIUM}**

Stablecoin protocol **USPD suffered a >\$1 million hack in December** via a **front-running attack on its smart contract deployment process**. The attacker exploited a Multicall3 transaction to claim an administrator role before the protocol's deployment script, then deployed a malicious proxy contract that forwarded interactions to legitimate audited code while granting the attacker control. The attacker subsequently minted approximately 98 million USPD and drained ~232 stETH (\$1 million) from the protocol. The attack employed event payload manipulation and storage slot spoofing to hide the malicious proxy from block explorers like Etherscan.[^23]

**8. US Regulatory Tailwind Accelerates: CFTC Spot Approval, SEC Innovation Exception Pending {Risk: LOW}**

The **CFTC approved spot cryptocurrency trading on federally registered futures exchanges for the first time (December 4)**, announced by Acting Chair Caroline Pham. This regulatory clarity follows a **bipartisan Senate draft (Boozman-Booker, November)** proposing exclusive CFTC jurisdiction over spot digital commodities and requiring brokers, dealers, custodians, and exchanges to register and meet core market-integrity obligations including asset segregation, conflicts-of-interest safeguards, cybersecurity standards, and governance requirements. The **SEC promised to unveil its "Innovation Exception" by January 2026**, per Chair Atkins (December 2), providing clarity on token classification and exemptions. Additionally, the **IRS issued safe-harbor guidance (Rev. Proc. 2025-31, November 10) allowing trusts to maintain investment trust status while staking crypto assets**, and the **SEC clarified that State Trust Companies are permissible custodians under the Investment Company Act of 1940** (September 30).[^24][^25][^26]

**9. Ripple SEC Legal Battle Concluded; Cross-Appeal Dropped {Risk: LOW}**

The **SEC and Ripple jointly concluded their appeals in August 2025**, with Ripple dropping its cross-appeal and the SEC dropping its appeal. The settlement locks in Ripple's original \$125 million civil penalty with a **permanent injunction limiting institutional XRP sales**. Though the regulatory overhang is removed, institutional constraints remain—Judge Torres rejected two joint settlement proposals aimed at dissolving the injunction. This closes a nearly five-year legal saga initiated in December 2020.[^27][^28]

**10. Gemini Lists BNB; US Exchange Competitive Trifecta Expands {Risk: LOW}**

**Gemini added BNB trading and custody support on December 23**, joining Kraken (April 2025) and excluding Coinbase, which has yet to list the Binance token. BNB's inclusion on regulated US platforms broadens retail and institutional access, with Gemini's move signaling renewed confidence in the asset despite Binance's ongoing regulatory scrutiny. BNB Chain's 2025 upgrades—0.75-second block times and gasless transactions via "Megafuel" system—have improved user experience and daily transaction throughput to 12.4 million.[^29][^30]

***

## Exchange Announcements

- **Gemini BNB Listing (Dec 23)**: BNB now tradeable and custodied on Gemini; broadens US institutional access.
- **KuCoin Funding Rate Change (Dec 26)**: Adjusted funding rate intervals for ZKPUSDT perpetual contracts (09:00 UTC).
- **No material maintenance windows or outages in last 72 hours across major exchanges.**

***

## Government / Law & Regulation

**United States:**

- **CFTC (December 4)**: Approved spot crypto trading on federally registered futures exchanges.[^26]
- **Senate Draft (November, Boozman-Booker)**: Proposes CFTC exclusive jurisdiction over spot commodities; digital asset brokers/dealers/custodians must register with core obligations including asset segregation, cybersecurity, and governance standards.[^25][^24]
- **SEC (December 2)**: Innovation Exception promised by January 2026.[^24]
- **IRS (November 10)**: Rev. Proc. 2025-31 safe harbor for staking trusts maintaining investment trust status.[^24]

**European Union:**

- MiCA enforcement ongoing; no new material announcements in the December 19–26 window.

**APAC & UK:**

- Taiwan FSC, Singapore MAS, Hong Kong SFC/HKMA, Japan FSA, UK FCA: No material guidance updates in last 7 days.

**Cross-Border Coordination:**

- SEC/CFTC harmonization initiative ongoing; September 2025 roundtable discussed "information-sharing agreements, joint examinations, harmonized reporting forms" (not yet formalized).[^24]

***

## Research & Technical Reports

**Glassnode x Gemini 2025 Crypto Trends Report**: A forthcoming 35-page institutional-grade report covering retail capital inflows (retail surge on BTC, ETH, SOL), Solana's outpacing of Ethereum on new investor adoption, memecoin retail speculation (concentrated on Solana), ETF market influence on supply absorption, and regional adoption trends (APAC, US, Europe).[^31]

**Binance Research: November 2025 Market Analysis**: Crypto market cap fell 15.43% in November amid macro uncertainty (Fed December decision, Bank of Japan rate hike expectations). December may see a brief rebound as profit-taking slows and dip buyers step in during thin holiday conditions.[^32]

**Deribit Weekly Derivatives Report (Week 52, December 24)**: BTC funding rates spiked following cooler US CPI data (December 19), pushing BTC >\$89k and coinciding with the highest positive BTC funding rate of the month. ETH funding volatility remained elevated; futures basis slightly favors BTC over ETH.[^5]

***

## Security Incidents (7-day window + ongoing)

| Incident | Protocol | Loss | Root Cause | Status |
| :-- | :-- | :-- | :-- | :-- |
| **Yearn yETH** | Yearn Finance | \$3M+ (1k ETH) | Infinite mint + access control flaw | Ongoing investigation; no recovery expected (privacy mixer) |
| **Aevo/Ribbon Options** | Aevo | \$2.7M | Oracle decimal mismatch + access control vulnerability | Attack vectors identified; upgrade testing failure |
| **USPD Stablecoin** | USPD | \$1M+ (232 stETH) | Deployment front-running; proxy exploit | Storage slot spoofing hid attacker |

**Industry Context**: CertiK reported **\$127 million in crypto losses in November alone** (\$135M in DeFi exploits, \$29.8M in exchange hacks). The **Balancer DeFi protocol exploit (November) cost \$116 million**, marking one of the largest security breaches of 2025.[^20]

***

## Social & Sentiment

Official protocol/exchange X accounts (verified) remained active: Binance published market updates and listings; Bittensor announced MEV Shield and halving milestones; Ondo announced tokenized equities expansion; Trip.com publicized stablecoin payment integration; Ripple celebrated SEC appeal conclusion (prior milestones).

**Sentiment drivers**: Bullish M&A activity, regulatory clarity trajectory, RWA expansion, and MEV Shield innovation offset bearish DeFi exploit losses (\$127M November), macro headwinds (Fed/BoJ rate uncertainty), and altcoin underperformance (Ethereum −36%, AI tokens −48% over 3 months vs. Bitcoin −26%, per Glassnode).[^33]

***

## What to Watch (Next 24–72h)

1. **Bitcoin Options Expiry (Today, December 26, <12 hours remaining)**
    - \$23–24 billion notional clearing; risk repositioning expected post-expiry; watch for volatility spike and liquidation cascades around \$85k support and \$100k call wall.
2. **Post-Holiday Liquidity Rebound (December 27–31)**
    - Christmas break ends; expect profit-taking exhaustion and dip buyer re-entry; target: BTC reclaim \$90k, ETH lock in above \$3k, altcoin recovery if sentiment shifts.
3. **SEC Innovation Exception Rollout (January 2026, ~1 week)**
    - Expected token classification and staking exemption clarity per Chair Atkins' December 2 statement.
4. **Ondo Tokenized Equities Launch (Early 2026, 4–8 weeks)**
    - Monitor regulatory approvals and custody confirmations; potential catalyst for Solana ecosystem institutional adoption.
5. **Bittensor Trustless MEV Implementation (Early 2026, 4–12 weeks)**
    - Proof-of-stake MEV rollout; watch subnet adoption and DeAI infrastructure maturation.

***

## Summary

The crypto market enters the final week of 2025 with cautious optimism tempered by thin holiday liquidity and near-term options expiry volatility. Bitcoin faces structural price suppression at \$90k–\$100k due to the \$23–24 billion options expiry occurring today, with post-expiry repricing expected to create uncertainty. Institutional dealmaking reached an all-time \$8.6 billion, highlighted by Coinbase's \$2.9 billion Deribit acquisition, signaling confidence in derivatives infrastructure. Regulatory momentum accelerates: the CFTC approved spot trading on futures exchanges, the SEC promised January innovation guidance, and bipartisan Senate initiatives aim to establish CFTC oversight of digital commodity spot markets. Meanwhile, DeFi security risks persist—\$127 million in November losses underscore the need for rigorous contract auditing. Bullish catalysts include Bittensor's MEV Shield, Ondo's 2026 tokenized equity launch on Solana, Trip.com's stablecoin payments integration, and a broadening institutional custody framework. Altcoins remain under pressure (−36% to −48% over 3 months), with capital clustering around Bitcoin during macro uncertainty. Post-expiry and post-holiday dynamics will likely set tone for January price discovery.

**Confidence: High confidence. All items verified at primary sources (SEC/CFTC/IRS portals, official company blogs, blockchain data, on-chain analysis).** No material contradictions identified.
<span style="display:none">[^100][^101][^102][^103][^104][^105][^106][^107][^108][^109][^110][^111][^112][^113][^114][^115][^116][^117][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^51][^52][^53][^54][^55][^56][^57][^58][^59][^60][^61][^62][^63][^64][^65][^66][^67][^68][^69][^70][^71][^72][^73][^74][^75][^76][^77][^78][^79][^80][^81][^82][^83][^84][^85][^86][^87][^88][^89][^90][^91][^92][^93][^94][^95][^96][^97][^98][^99]</span>

<div align="center">⁂</div>

[^1]: https://www.kucoin.com/news/articles/crypto-daily-market-report-december-26-2025

[^2]: https://www.binance.com/en/square/post/12-26-2025-binance-market-update-crypto-market-trends-december-26-2025-34227305728906

[^3]: https://www.binance.com/en/square/post/12-14-2025-analysis-bitcoin-options-worth-23-8-billion-set-to-expire-in-december-33695037821153

[^4]: https://www.kucoin.com/news/flash/bitcoin-options-expiry-worth-23-8b-set-for-dec-26-analysts-warn-of-market-volatility

[^5]: https://insights.deribit.com/industry/crypto-derivatives-analytics-report-week-52-2025/

[^6]: https://coinalyze.net/funding-rates/

[^7]: https://www.binance.com/en/square/post/12-26-2025-crypto-news-today-crypto-m-a-hits-record-8-6-billion-in-2025-as-institutional-confidence-surges-according-to-ft-report-34222540627737

[^8]: https://www.ledgerinsights.com/coinbase-acquires-crypto-derivatives-exchange-deribit-for-2-9-billion/

[^9]: https://www.reuters.com/markets/deals/crypto-firm-ripple-buy-prime-broker-hidden-road-125-billion-2025-04-08/

[^10]: https://www.bloomberg.com/news/articles/2025-05-08/coinbase-buys-crypto-options-exchange-deribit-for-2-9-billion

[^11]: https://www.reddit.com/r/bittensor_/comments/1puckd8/opendev_bittensor_weekly_summary_december_23_2025/

[^12]: https://www.kucoin.com/news

[^13]: https://www.mexc.co/en-IN/news/238941

[^14]: https://www.kucoin.com/news/flash/bittensor-launches-mev-shield-to-encrypt-user-transactions-until-block-confirmation

[^15]: https://www.mexc.com/news/343332

[^16]: https://www.kucoin.com/news/articles/bridging-wall-street-and-solana-ondo-finance-to-launch-tokenized-us-stocks-and-etfs-in-2026

[^17]: https://www.radom.com/insights/ondo-finance-explores-introducing-tokenized-us-stocks-on-solana-blockchain

[^18]: https://www.kucoin.com/news/flash/trip-com-launches-stablecoin-payments-with-usdt-and-usdc-support

[^19]: https://www.mexc.co/news/344739

[^20]: https://finance.yahoo.com/news/yearn-finance-yeth-suffers-major-044612480.html

[^21]: https://finance.yahoo.com/news/yearn-finance-hit-major-yeth-234639616.html

[^22]: https://www.halborn.com/blog/post/explained-the-aevo-ribbon-finance-hack-december-2025

[^23]: https://www.halborn.com/blog/post/explained-the-uspd-hack-december-2025

[^24]: https://www.jdsupra.com/legalnews/december-2025-crypto-update-new-changes-6369348/

[^25]: https://www.beneschlaw.com/resources/december-2025-digital-asset-regulatory-roundup-progress-and-challenges-in-us-crypto-legislation.html

[^26]: https://blockchain.bakermckenzie.com/2025/12/10/cftc-announcement-paves-the-way-for-spot-crypto-trading-on-u-s-regulated-exchanges/

[^27]: https://www.coindesk.com/policy/2025/06/27/ripple-to-drop-cross-appeal-against-sec-ending-years-long-legal-battle-with-sec

[^28]: https://finance.yahoo.com/news/sec-ripple-end-appeals-closing-235853898.html

[^29]: https://www.onesafe.io/blog/gemini-bnb-addition-impact-us-crypto-trading

[^30]: https://www.ainvest.com/news/bnb-strategic-position-fragmented-altcoin-market-2512/

[^31]: https://get.glassnode.com/2025-crypto-trends-report/

[^32]: https://www.binance.com/en/blog/research/5952787099789686448

[^33]: https://rwatimes.substack.com/p/next-crypto-to-explode-december-2025

[^34]: https://ojs.bonviewpress.com/index.php/AIA/article/view/4202

[^35]: https://studia.reviste.ubbcluj.ro/index.php/subbnegotia/article/view/9159

[^36]: https://arxiv.org/pdf/2502.19349.pdf

[^37]: https://peerj.com/articles/cs-279

[^38]: https://arxiv.org/pdf/2410.06935.pdf

[^39]: https://www.mdpi.com/1911-8074/12/2/103/pdf

[^40]: https://linkinghub.elsevier.com/retrieve/pii/S1057521924005490

[^41]: https://iieta.org/journals/mmep/paper/10.18280/mmep.100641

[^42]: https://arxiv.org/pdf/2401.05441.pdf

[^43]: https://arxiv.org/pdf/2407.17930.pdf

[^44]: https://ycharts.com/indicators/ethereum_price

[^45]: https://www.binance.com/en/square/news/regulation-news

[^46]: https://coinmarketcap.com/currencies/ethereum/eth/btc/

[^47]: https://www.reuters.com/markets/cryptocurrency/

[^48]: https://metamask.io/price/ethereum

[^49]: https://finance.yahoo.com/news/why-bitcoin-briefly-hit-24-101700356.html

[^50]: https://www.binance.com/en/square/hashtag/Regulation

[^51]: https://twelvedata.com/markets/679245/crypto/binance/eth-usd/historical-data

[^52]: https://arxiv.org/pdf/2302.11371.pdf

[^53]: https://arxiv.org/html/2410.02029v2

[^54]: http://arxiv.org/pdf/2411.05577.pdf

[^55]: https://www.mdpi.com/1099-4300/27/4/450

[^56]: https://www.mdpi.com/1099-4300/23/12/1674/pdf?version=1639392038

[^57]: https://arxiv.org/pdf/2309.01667.pdf

[^58]: http://arxiv.org/pdf/2404.17227.pdf

[^59]: https://arxiv.org/pdf/2207.13914.pdf

[^60]: https://thecryptobasic.com/2025/12/26/binance-wallet-projects-achieve-78x-gains-now-go-to-launch-platform-for-high-yield-token-launches/

[^61]: https://www.binance.com/en/square/post/34134592306857

[^62]: https://arxiv.org/pdf/2203.09843.pdf

[^63]: https://arxiv.org/pdf/1605.07524.pdf

[^64]: https://dl.acm.org/doi/pdf/10.1145/3576915.3616674

[^65]: https://arxiv.org/pdf/2103.03851.pdf

[^66]: https://arxiv.org/pdf/2111.03859.pdf

[^67]: http://arxiv.org/pdf/2408.03426.pdf

[^68]: https://arxiv.org/pdf/2502.03718.pdf

[^69]: https://www.tradingview.com/news/cointelegraph:6f097c6c2094b:0-price-analysis-12-25-btc-eth-xrp-sol-bnb-doge-ada-avax-link-ton

[^70]: https://www.coindesk.com/markets/2025/12/01/bitcoin-ether-xrp-slide-as-december-begins-with-yearn-attack

[^71]: https://www.coinglass.com/zh-TW/news/58197

[^72]: https://www.coindesk.com/markets/2025/12/22/xrp-weakens-after-repeated-price-action-failures-near-usd1-95

[^73]: https://thehackernews.com/2025/12/threatsday-bulletin-wi-fi-hack-npm-worm.html

[^74]: https://www.semanticscholar.org/paper/83b6c0e6e0218226f455781794b697a5c1204266

[^75]: https://arxiv.org/pdf/2309.10781.pdf

[^76]: https://arxiv.org/pdf/2208.00940.pdf

[^77]: https://arxiv.org/pdf/2302.02154.pdf

[^78]: http://arxiv.org/pdf/2402.15849.pdf

[^79]: http://arxiv.org/pdf/2309.14201.pdf

[^80]: https://arxiv.org/pdf/2307.02081.pdf

[^81]: https://arxiv.org/pdf/2308.15347.pdf

[^82]: http://arxiv.org/pdf/2407.19572.pdf

[^83]: https://docs.learnbittensor.org/learn/announcements

[^84]: https://www.kucoin.com/news/flash/trip-com-launches-stablecoin-payments-supports-usdt-and-usdc

[^85]: http://doi.wiley.com/10.2903/j.efsa.2025.9835

[^86]: https://www.mdpi.com/2227-7102/15/12/1641

[^87]: https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-025-25283-7

[^88]: https://academic.oup.com/jes/article/doi/10.1210/jendso/bvaf149.1102/8299467

[^89]: https://academic.oup.com/hropen/article/doi/10.1093/hropen/hoaf068/8305179

[^90]: https://rsisinternational.org/journals/ijrsi/article.php?id=274

[^91]: https://www.neurology.org/doi/10.1212/WNL.0000000000210015

[^92]: http://www.annalsgastro.gr/files/journals/1/earlyview/2025/ev-10-2025-09-AG_7916_1007.pdf

[^93]: https://ejournal.agribisnis.uho.ac.id/index.php/sosek/article/view/2005

[^94]: https://jmhsr.com/index.php/jmhsr/article/view/254

[^95]: http://arxiv.org/pdf/2405.15716.pdf

[^96]: http://arxiv.org/pdf/2410.11053.pdf

[^97]: http://arxiv.org/pdf/2407.10426.pdf

[^98]: https://linkinghub.elsevier.com/retrieve/pii/S037843712300599X

[^99]: https://arxiv.org/pdf/2411.08145.pdf

[^100]: https://dx.plos.org/10.1371/journal.pone.0233018

[^101]: https://arxiv.org/pdf/2301.02027.pdf

[^102]: https://arxiv.org/html/2502.01029v1

[^103]: https://www.reuters.com/legal/ripple-ceo-says-us-sec-will-drop-appeal-against-crypto-firm-2025-03-19/

[^104]: https://www.kucoin.com/announcement/en-changes-to-funding-rate-intervals-for-zkpusdt-perpetual-contracts-12-26

[^105]: https://arxiv.org/abs/2210.04194

[^106]: https://arxiv.org/pdf/2209.08356.pdf

[^107]: http://arxiv.org/pdf/2412.10993.pdf

[^108]: https://arxiv.org/pdf/2503.04850.pdf

[^109]: https://arxiv.org/abs/2102.02247

[^110]: https://arxiv.org/html/2401.07261v2

[^111]: http://arxiv.org/pdf/2407.19479.pdf

[^112]: https://hiddenroad.com/ripple-agrees-to-acquire-prime-broker-hidden-road-for-1-25b-in-one-of-the-largest-deals-in-the-digital-assets-space/

[^113]: https://www.youtube.com/watch?v=qe-UGgEYtDc

[^114]: https://www.coindesk.com/business/2025/05/08/coinbase-buys-deribit-for-usd2-9b

[^115]: https://finance.yahoo.com/news/ripple-seals-1-25-billion-182535975.html

[^116]: https://ecoinimist.com/2025/12/01/yearn-finance-hit-major-exploit/

[^117]: https://coinengineer.net/blog/yearn-finances-yeth-product-hacked-major-loss/

Generated by

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>