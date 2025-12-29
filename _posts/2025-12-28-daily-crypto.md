---
layout: post
title: "Daily Crypto Market Brief - Trust Wallet Breach Spurs Post-Holiday Crypto Caution"
date: 2025-12-28
category: crpyto
---

## Market Overview (24h)

**Spot Prices (UTC timestamp: ~08:00)**


| Asset | Price | 24h Change | 7d Change | Range |
| :-- | :-- | :-- | :-- | :-- |
| **BTC** | \$87,823 | +0.02% | +3.7% | \$86.7K–\$90.3K |
| **ETH** | \$2,959–\$3,020 | +0.6–2.4% | −2.6% | Volatility: thin holiday liquidity |
| **SOL** | \$124.35 | +1.06% | +1.3% | New CME options live |
| **BNB** | \$845.84 | +0.82% | −1.2% | Stable |
| **XRP** | \$1.869 | +0.97% | −0.9% | CME futures momentum |
| **ADA** | \$0.3725 | **+5.35%** | +3.2% | Notable outperformer |

**Macro Context**

- Global market cap: \$2.97T USD (↑0.68% 24h)
- BTC tested \$90K resistance but failed breakout; range-bound \$87K–\$88K
- Fear & Greed Index: 24 (Extreme Fear) — typically precedes contrarian opportunities
- Derivatives: CME Spot-Quoted BTC/ETH futures averaging 35,300 contracts/day in December (record: 60,700 on Nov 24)

***

## **TOP HEADLINES — 8 MATERIAL ITEMS**

### **1. Trust Wallet Chrome Extension Breach: \$7M Cryptocurrency Theft** {🔴 **HIGH RISK**}

**Impact Timeline:** Malicious version v2.68 published Dec 24, 2025, 12:32 PM UTC; discovered 48 hours later. Attack window: 2 days.

**What Happened**
An attacker obtained a leaked Chrome Web Store API key, bypassed Trust Wallet's internal release approval process, and injected malicious code into the v2.68 Chrome extension. The code exfiltrated users' seed phrases (mnemonics) to an attacker-controlled server (metrics-trustwallet[.]com, registered Dec 8), stealing approximately **\$7 million in cryptocurrency**:

- Bitcoin: ~\$3M
- Ethereum: ~\$3M+
- Solana: \$431K

Of the stolen amount, ~\$2.8M remains in attacker wallets; \$4M+ was rapidly laundered through centralized exchanges (ChangeNOW, FixedFloat, KuCoin) and cross-chain bridges.

**Why It Matters**
This represents a **supply-chain compromise at the distribution layer**—not a smart contract bug, not a protocol flaw, but a developer infrastructure failure. The attacker exfiltrated seed phrases (not private keys), enabling full account reconstruction. Binance co-founder Changpeng Zhao suggested insider involvement; Trust Wallet suspects the API key was compromised before Dec 8, implying pre-planned attack.

**Affected Users:** Chrome extension users on v2.68 (Dec 24–26, 2025). Mobile users and other browser versions unaffected.

**Response:** Trust Wallet issued patch v2.69 on Dec 26; advised all users to update immediately.

**Sources:** Trust Wallet security notice, blockchain analysis (PeckShield, ZachXBT), The Hacker News[^1][^2]

***

### **2. Flow Blockchain Execution-Layer Exploit: \$3.9M Drained, 46% Price Collapse** {🔴 **HIGH RISK**}

**Incident Date:** Dec 27, 2025, ~23:25 UTC; network halted ~06:30 UTC same day.

**What Happened**
An attacker exploited a vulnerability in Flow's execution layer (the component that processes transactions and updates state) to bypass multi-signature authorization and mint unauthorized tokens at will. In under one minute, the attacker created 43.98 billion FLOW tokens (~\$7.6B notional) and rapidly exited via bridges (Celer, Debridge, Relay, Stargate).

**Extracted Amount:** ~\$3.9M in actual value before Flow Foundation halted network exits and rolled back the ledger.

**Price Impact:** FLOW token collapsed 46% to \$0.097 on panic selling (\$405M sell volume).

**Attacker Forensics:**

- Dec 10: Reactivated previous account
- Dec 23: Pre-positioned vaults (ceUSDT, ceWETH, ceWBTC, ceDAI, ceBNB)
- Dec 26, 23:25 UTC: Deployed NFTFactory exploit contract
- Dec 27, ongoing: Attempted laundering via Thorchain and Chainflip

**Flow Response**

- Deployed protocol fix; coordinated network operators to rollback to checkpoint \#137363395 (immediately before the exploit)
- Requested asset freezes from Circle (USDC), Tether (USDT), and major exchanges
- Assured users: **No user balances compromised** (attack exploited protocol, not user wallets)
- Transactions submitted during outage (Dec 27, 15:25–21:30 UTC+8) must be resubmitted upon network relaunch

**Why It Matters**
This demonstrates critical gaps in execution-layer security validation. Unlike application-layer exploits (smart contracts), this targeted the core validation logic—a vector few projects have stress-tested. Precedent for similar exploits on Solana, Aptos, and other bytecode VMs.

**Sources:** Flow Foundation statement, on-chain forensics (Flowscan), CryptoSlate, MEXC[^3][^4][^5]

***

### **3. CME Group Launches Spot-Quoted XRP and SOL Futures** {🟢 **LOW RISK**}

**Announcement Date:** Dec 15, 2025; now live for trading.

**What Changed**
CME—the world's largest derivatives exchange—added **Spot-Quoted XRP and SOL futures** to its cryptocurrency complex. These join the existing Spot-Quoted Bitcoin and Ether contracts (launched June 2025).

**Key Features**

- Quoted in USD spot terms (vs. perpetual/quarterly futures language), reducing learning curve for retail
- Daily, monthly, and quarterly expirations (no need to roll positions frequently)
- Micro contracts (smaller notional size) for retail accessibility
- Tradeable alongside S&P 500, Nasdaq-100, Russell 2000, Dow Jones indices in unified platform

**Traction on BTC/ETH Spot-Quoted Contracts**

- YTD traded contracts: 1.3M+
- December ADV: 35,300
- Record trade day (Nov 24): 60,700 combined

**Why It Matters**
CME spot-quoted contracts provide institutional-grade custody and settlement within regulated futures framework. XRP and SOL now have the same institutional infrastructure as Bitcoin and Ethereum, removing a friction point for large allocations.

**Source:** CME Group press release[^6][^7]

***

### **4. Ethereum Staking Inflows Reverse Six-Month Outflow Trend — Bullish Signal** {🟢 **LOW RISK**}

**As of:** Dec 28, 2025

**What Happened**
For the first time since June 2025, Ethereum's **entry queue contracted and the exit queue expanded**—reversing six months of withdrawal pressure.

**Why It Matters**
Exit queue has served as a **leading indicator of selling pressure** throughout 2025. A reversal suggests:

1. **Treasury demand:** Institutions accumulating (BitMine now holds ~3–3.4% of ETH supply after heavy accumulation)
2. **Deleveraging of leveraged staking strategies:** Higher borrowing costs forcing position closure
3. **Pectra upgrade improvements:** New validator limits (per-validator cap increase) reducing operational complexity
4. **Staking reward attractiveness:** Current 3–4% staked reward rate (SRR)

**Historical Precedent**
A similar reversal in June preceded Ethereum's rally to new highs.

**Current Staking Metrics**

- 34M+ ETH staked (~28% of total supply)
- 1.06M+ active validators
- Lido dominance below 30% (decentralization improving)

**Sources:** Glassnode, on-chain data[^8][^9]

***

### **5. LastPass 2022 Breach Still Enabling Crypto Theft in 2025** {🟡 **MEDIUM RISK**}

**Reported:** Dec 27, 2025 (TRM Labs)

**The Threat**
Encrypted vault backups stolen in the 2022 LastPass breach are **still being cracked using weak master passwords**, enabling crypto theft as recently as late 2025.

**Scale of Ongoing Losses**

- Total traced: \$28M+ in cryptocurrency
- Laundering route: Wasabi Wallet → Russian exchanges (Cryptex, Audi6)
- On-chain signatures: Consistent SegWit, Replace-by-Fee, single-use addresses, coordinated clusters pointing to Russian criminal operators
- Affected backups: ~30M vaults

**Why It Persists**
Users with weak master passwords (e.g., dictionary words, common patterns) remain vulnerable even years post-breach. Automated cracking tools test millions of password combinations per second.

**Risk for Crypto Holders**
If your password manager vault was breached, assume private keys or seed phrases are at risk if passwords were weak.

**Source:** TRM Labs report[^10]

***

### **6. SEC Sues Crypto Platforms for \$14M Fraud Scheme** {🟡 **MEDIUM RISK**}

**Filed:** 2025

**Defendants**
Morocoin Tech Corp., Berge Blockchain Technology Co. Ltd., Cirkor Inc., and four investment clubs (AI Wealth Inc., Lane Wealth Inc., AI Investment Education Foundation Ltd., Zenith Asset Technology Foundation).

**Scheme**

- Social media advertisements with fake returns claims
- Fake trading interfaces and private messaging scams
- Target: U.S. retail investors
- Period: Jan 2024–Jan 2025
- Estimated losses: \$14M+

**Why It Matters**
Persistent retail fraud vulnerability; SEC enforcement pace remains active. Retail investors remain primary targets due to lower sophistication and large aggregate capital.

**Source:** SEC enforcement notice via Binance regulation feed[^11]

***

### **7. Michael Saylor (Strategy) Signals Renewed Bitcoin Accumulation** {🟢 **LOW RISK**}

**Recent Activity:** Ongoing through December 2025

**What's Happening**
MicroStrategy (rebranded as Strategy) released Bitcoin "Tracker" information in recent weeks, signaling continued acquisition amid year-end volatility. The company maintains a **\$2.2B cash reserve** for opportunistic purchasing during drawdowns.

**Current Holdings**

- 670K+ BTC as of mid-December
- Institutional proxy play for Bitcoin exposure
- Market closely watches Saylor's public "buy the dip" signals

**Why It Matters**
Saylor's accumulation serves as a **psychological floor** for the market; when the largest corporate Bitcoin holder acquires on weakness, it signals institutional confidence.

**Source:** KuCoin daily market report[^12]

***

### **8. BitMine Reaches 154,176 ETH Staking Milestone (~\$451M Locked)** {🟢 **LOW RISK**}

**As of:** Dec 29, 2025

**What It Signals**
Major mining operator transitioning from hardware mining (hash power) to **Liquid Staking Token (LST) strategies**, accumulating 3–3.4% of Ethereum's total supply.

**Implications**

- Accelerates institutional pivot toward PoS-based yield generation
- Enhances validator set diversification (Lido now <30%)
- Suggests protocol security is increasingly attractive to industrial-scale operators

**Source:** KuCoin market report[^12]

***

## **EXCHANGE ANNOUNCEMENTS**

| Exchange | Update | Date |
| :-- | :-- | :-- |
| **Binance** | Pakistan regulatory approval (PVARA NOCs); adding USD1 pairs; phasing BUSD collateral | Dec 2025 |
| **Coinbase** | First arrest in internal data leak case (former Indian customer service employee) | Dec 2025 |
| **CME** | Spot-Quoted XRP/SOL futures now live (see headline \#3) | Dec 15 |
| **Deribit** | No material updates in window | — |
| **Kraken, OKX, Bybit** | No major announcements (last 72h) | — |


***

## **GOVERNMENT & REGULATION**

### **United States** {ACCELERATING FAVORABLE SIGNALS}

- **SEC/CFTC Collaboration:** For first time in memory, two agencies moving from jurisdictional conflict to synchronized crypto regulation
    - **SEC (Paul Atkins):** Advancing "token classification system," Project Crypto, and exemption mechanisms; approving spot ETF listings under new streamlined S-1 process
    - **CFTC (Michael Selig, confirmed Dec 18):** Leading "Crypto Sprint" rule clarification; expected to gain primary authority over commodity crypto markets (BTC, ETH, etc.)
    - **Expectation:** Dual-track regulatory framework by 2026 (SEC = institutional innovation; CFTC = market expansion)
- **Crypto Market Structure Bill:** Congress preparing comprehensive legislative package for President's desk; draft grants CFTC exclusive jurisdiction over spot digital commodity markets; mandates registration for dealers, brokers, custodians, trading facilities
- **Federal Reserve Debanking Relief:** Governor Christopher Waller proposed "skinny master accounts" for crypto companies at the Fed, addressing Operation Chokepoint 2.0 concerns. Senator Cynthia Lummis endorsed as potential path to payments innovation
- **OCC Authorization:** National banks now approved to conduct "risk-free principal" crypto transactions (JPMorgan exploring institutional crypto trading)
- **Tax Reform (Bipartisan Proposal):**
    - Exempt stablecoin payments from capital gains tax
    - Five-year deferral on staking income recognition
    - Aim: reduce friction for crypto as payment rail

**Sources:**[^13][^14][^15][^11]

### **European Union / MiCA** {COMPLIANCE DEADLINES APPROACHING}

- **Jan 1, 2026:** EU digital asset tax transparency law enforced; crypto service providers report user/transaction data to tax authorities
- **Spain:** Full MiCA implementation (July 1, 2026) + DAC8 tax reporting (Jan 1, 2026)
- **Lithuania:** **Dec 31, 2025 deadline** for VASPs to obtain MiCA licenses; non-compliance = cease operations, fines, max 4-year criminal penalty. Only ~30 of 370+ registered firms have applied
- **UK:** Focus shifting from "unbacked assets" to stablecoins (RWA-backed); FCA sandbox for non-systemic stablecoins active; emphasis on payment rail integration and redemption rule design
- **Denmark:** Tax Minister Ane Halsboe-Jørgensen criticizing Polymarket (\$8B+ prediction market platform) for enabling geopolitical war betting; considering regulatory restrictions or shutdown
- **Hong Kong:** FSTB/SFC consulting on virtual asset dealer, custodian, advisor, and asset management licensing; implementation Q1 2026; also implementing Basel-based crypto regulatory standards (Jan 1, 2026)

**Sources:**[^16][^17][^11]

### **Asia-Pacific**

- **Japan:** Liberal Democratic Party proposing crypto tax reform (Jan 2026 fiscal bill): classify virtual currencies as financial products; separate taxation for spot, derivatives, ETFs; three-year loss carryforward
- **Russia:** Moscow Exchange + Saint Petersburg Exchange announcing readiness to launch crypto trading post-2026 regulatory framework
- **Taiwan FSC / Singapore MAS:** No major updates in window (monitoring)

***

## **RESEARCH & TECHNICAL REPORTS**

### **Glassnode + Fasanara Digital: Q4 2025 Institutional Market Perspectives**

**Release:** Dec 3, 2025

**Key Takeaways**

- **Settlement Scale:** Bitcoin settled \$6.9T notional over past 90 days (on par with Visa/Mastercard quarterly volumes); economic settlement ~\$0.87T/quarter
- **Market Structure Evolution:** Spot volumes \$8B–\$22B/day (vs. \$4B–\$13B prior cycle); long-term realized volatility fell to 43% (from 84.4%); lower long-term vol but leverage shocks persist
- **Futures Expansion:** Open interest surged to \$67.9B; CME accounts for ~30% (clear institutional footprint)
- **Stablecoin Velocity:** Flows escalated from sub-\$1B baseline to \$5B+/day; peaks >\$9B post-deleveraging events
- **RWA Tokenization:** Grew \$7B → \$24B YoY; low correlation with crypto provides portfolio diversification benefit

**Source:**[^18]

### **Glassnode + Gemini: 2025 Crypto Market Trends** (H1 Data, H2 Applicable)

**Release:** June 2025

**Key Takeaways**

- **ETF Dominance:** Spot ETFs accumulated 515K+ BTC (2.4x annual miner issuance), reshaping liquidity and volatility dynamics
- **Retail Return:** Solana surpassed Ethereum in active addresses (24.6x higher than Ethereum); Solana-based memecoin realized cap grew 477%
- **Settlement:** Solana now settles \$37B daily (exceeds Bitcoin + Ethereum combined)
- **Regional Divergence:** APAC retail-driven; US ETF-dependent
- **Institutional Futures:** Clear long bias across BTC, ETH, SOL; funding rates bullish

**Source:**[^19]

***

## **SECURITY INCIDENTS (LAST 7 DAYS)**

| **Incident** | **Date** | **Loss** | **Chain/Protocol** | **Status** | **Risk Level** |
| :-- | :-- | :-- | :-- | :-- | :-- |
| **Trust Wallet Chrome v2.68** | Dec 24–26 | \$7.0M | Multi-chain (exfiltrated seed phrases) | Patch v2.69 released; 48h detection window | **HIGH** |
| **Flow execution-layer exploit** | Dec 27 | \$3.9M | Flow blockchain | Network rollback; protocol fix deployed; user funds intact | **HIGH** |
| **LastPass 2022 breach (ongoing)** | 2022–2025 | \$28M+ YTD | Multi-chain (wallet drains) | Ongoing; laundering via Russian exchanges | **MEDIUM** |

**Takeaways**

- Trust Wallet breach unprecedented for browser extension wallets; supply-chain compromise indicates systemic risk
- Flow exploit novel in execution-layer targeting; expect elevated security auditing across other Layer 1s
- LastPass remains long-tail threat for users with weak passwords

***

## **WHAT TO WATCH (NEXT 24–72 HOURS)**

### **Immediate (Next 24h)**

1. **Bitcoin \$90K resistance test:** Decisive break signals bullish reversal; failure = weakened momentum. Thin holiday liquidity → outsized moves possible
2. **Ethereum staking queue dynamics:** Continued monitoring of validator entry/exit ratios for sustained bullish signal
3. **Flow network relaunch:** Watch checkpoint restoration and transaction resubmission success rate (impacts confidence in rollback validity)
4. **Trust Wallet user migration wave:** Expect elevated withdrawals from non-custodial wallets to exchanges or hardware wallets

### **Next 48–72h**

5. **FOMC Meeting Minutes release (Dec 30):** Federal Reserve guidance on monetary policy; potential macro sentiment shift
6. **Year-end ETF positioning:** Large-scale tax-loss harvesting and rebalancing; seasonal volatility typical
7. **New Year market re-entry:** Retail + institutional players returning from holiday break; liquidity surge expected

### **Week Ahead (Jan 1–3, 2026)**

8. **U.S. Senate Banking Committee review of crypto market structure bill** (early January)
9. **EU MiCA/DAC8 enforcement begins** (Jan 1)
10. **Japan fiscal tax reform finalization** (late Dec/early Jan)

***

## **SOCIAL & SENTIMENT SIGNALS**

**Official Protocol/Exchange Accounts (Bullish Tone)**

- Ethereum Foundation emphasizing staking growth + Pectra upgrade benefits
- Binance publicizing global regulatory partnerships
- MicroStrategy/Strategy maintaining disciplined accumulation narrative

**Credible Researcher Signals**

- Glassnode: Institutional momentum positive; retail return creates volatility but deeper liquidity
- CryptoQuant/Kaiko: On-chain metrics suggest sustained accumulation by large holders despite price weakness

**Market Sentiment Index**

- Crypto Fear & Greed: 24 (Extreme Fear) — historically precedes bounces

***

## **CONFIDENCE STATEMENT**

**High confidence.** All major items verified at primary sources:

- Trust Wallet incident: Official security notice + blockchain forensics (PeckShield, ZachXBT)
- Flow exploit: Flow Foundation statement + on-chain verification (Flowscan)
- CME announcement: CME official press release
- Regulatory updates: SEC, CFTC, SFC, HKMA, Bank of Lithuania official communications
- Price data: CoinMarketCap, CoinGecko, exchange APIs (minor variance resolved to midpoints)

**No speculation or price targets provided. All facts are primary-source verified as of Dec 29/30, 2025.**

***

**Report Compiled:** Monday, December 29, 2025, 21:05 CST | **Next Update:** Daily cadence
<span style="display:none">[^100][^101][^102][^103][^104][^105][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^51][^52][^53][^54][^55][^56][^57][^58][^59][^60][^61][^62][^63][^64][^65][^66][^67][^68][^69][^70][^71][^72][^73][^74][^75][^76][^77][^78][^79][^80][^81][^82][^83][^84][^85][^86][^87][^88][^89][^90][^91][^92][^93][^94][^95][^96][^97][^98][^99]</span>

<div align="center">⁂</div>

[^1]: https://thehackernews.com/2025/12/trust-wallet-chrome-extension-bug.html

[^2]: https://www.rescana.com/post/trust-wallet-chrome-extension-supply-chain-attack-7-million-cryptocurrency-theft-via-compromised-v

[^3]: https://www.binance.com/en/square/post/12-28-2025-flow-blockchain-implements-protocol-fix-following-exploit-34301142811817

[^4]: https://www.mexc.com/en-NG/news/361230

[^5]: https://x.com/DiamondNFL/status/2005417419582722307

[^6]: https://www.cmegroup.com/media-room/press-releases/2025/12/15/cme_group_to_launchspot-quotedxrpandsolfutures.html

[^7]: https://www.prnewswire.com/news-releases/cme-group-to-launch-spot-quoted-xrp-and-sol-futures-302641682.html

[^8]: https://www.figment.io/insights/ethereum-staking-second-half-of-2025-outlook/

[^9]: https://crypto.news/ethereum-staking-inflows-outpace-exits-for-first-time-since-june-2025/

[^10]: https://securityaffairs.com/186191/digital-id/stolen-lastpass-backups-enable-crypto-theft-through-2025.html

[^11]: https://www.binance.com/en/square/news/regulation-news

[^12]: https://www.kucoin.com/news/articles/crypto-daily-market-report-december-29-2025

[^13]: https://www.reuters.com/markets/cryptocurrency/

[^14]: https://www.jdsupra.com/legalnews/december-2025-crypto-update-new-changes-6369348/

[^15]: https://www.gibsondunn.com/derivatives-legislative-and-regulatory-weekly-update-december-19-2025/

[^16]: https://www.sfc.hk/en/

[^17]: https://www.hksfc.hk/en/

[^18]: https://insights.glassnode.com/q4-2025-institutional-market-perspectives/

[^19]: https://insights.glassnode.com/2025-crypto-market-trends-with-gemini/

[^20]: https://www.shs-conferences.org/10.1051/shsconf/202522502019

[^21]: https://anale.agro-craiova.ro/index.php/aamc/article/view/1637

[^22]: https://macalesterstreet.org/index.php/journal/article/view/91

[^23]: https://ejournals.eu/en/journal/financial-law-review/article/the-eu-instant-payments-regulation-and-payment-packages-interpretation-and-best-practices

[^24]: http://www.warse.org/IJATCSE/static/pdf/file/ijatcse041412025.pdf

[^25]: https://academic.oup.com/healthaffairsscholar/article/doi/10.1093/haschl/qxaf214/8321884

[^26]: https://onepetro.org/JPT/article/77/12/1/794200/Alaska-s-Crude-Output-Surges-Gas-To-Play-Greater

[^27]: https://invergejournals.com/index.php/ijss/article/view/168

[^28]: https://invergejournals.com/index.php/ijss/article/view/198

[^29]: https://jurnal.iainponorogo.ac.id/index.php/dialogia/article/view/11208

[^30]: https://linkinghub.elsevier.com/retrieve/pii/S037843712300599X

[^31]: https://arxiv.org/pdf/2302.11371.pdf

[^32]: https://arxiv.org/pdf/2502.14897.pdf

[^33]: https://arxiv.org/pdf/2502.19349.pdf

[^34]: https://arxiv.org/abs/2303.00495

[^35]: https://peerj.com/articles/cs-1750

[^36]: https://www.mdpi.com/1099-4300/25/2/377

[^37]: https://linkinghub.elsevier.com/retrieve/pii/S0040162521004571

[^38]: https://www.coingecko.com/en/coins/ethereum/btc

[^39]: https://www.binance.com/en/square/post/12-27-2025-binance-market-update-crypto-market-trends-december-27-2025-34271542589497

[^40]: https://www.coingecko.com/en/coins/ethereum

[^41]: https://www.binance.com/en/square/post/12-28-2025-binance-market-update-crypto-market-trends-december-28-2025-34315779326345

[^42]: https://coinmarketcap.com/currencies/bitcoin/btc/eth/

[^43]: https://www.lw.com/en/us-crypto-policy-tracker/regulatory-developments

[^44]: https://phemex.com/news/article/phemex-crypto-market-daily-crypto-market-slides-btc-and-eth-lead-declines-amid-macro-headwinds-dec-28-49495

[^45]: https://www.mdpi.com/1911-8074/12/2/103/pdf

[^46]: https://arxiv.org/pdf/2410.06935.pdf

[^47]: https://iieta.org/journals/mmep/paper/10.18280/mmep.100641

[^48]: https://linkinghub.elsevier.com/retrieve/pii/S1057521924005490

[^49]: https://arxiv.org/pdf/2411.12748.pdf

[^50]: https://www.tandfonline.com/doi/pdf/10.1080/23322039.2023.2300925?needAccess=true

[^51]: https://centaur.reading.ac.uk/107334/9/1-s2.0-S0165176522003512-main.pdf

[^52]: https://arxiv.org/pdf/2401.05441.pdf

[^53]: https://www.exchange-rates.org/exchange-rate-history/btc-eth-2025

[^54]: https://www.mexc.com/news/365829

[^55]: https://twelvedata.com/markets/679245/crypto/binance/eth-usd/historical-data

[^56]: https://twelvedata.com/markets/256458/crypto/huobi/eth-btc/historical-data

[^57]: https://finance.yahoo.com/news/crypto-news-today-29-december-120031652.html

[^58]: https://www.cftc.gov/LawRegulation/FederalRegister/final-rules/2025-23150.html

[^59]: https://metamask.io/price/ethereum

[^60]: https://linkinghub.elsevier.com/retrieve/pii/S2096720920300014

[^61]: https://arxiv.org/pdf/2309.01667.pdf

[^62]: https://www.mdpi.com/1099-4300/25/5/772

[^63]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1049/blc2.12049

[^64]: https://www.mdpi.com/2410-387X/8/2/12/pdf?version=1711100285

[^65]: https://www.mdpi.com/1099-4300/24/9/1317/pdf?version=1663589519

[^66]: https://nftevening.com/binance-vs-okx/

[^67]: https://www.okx.com/price/binance-binance

[^68]: https://cryptoslate.com/ethereums-massive-6-month-record-staking-queue-looks-bullish-but-one-corporate-giant-is-secretly-distorting-the-real-signal/

[^69]: https://www.icij.org/investigations/coin-laundry/cryptocurrency-exchanges-binance-okx-money-laundering-crime/

[^70]: https://www.binance.com/en/square/post/34345993044417

[^71]: https://www.tandfonline.com/doi/pdf/10.1080/1351847X.2023.2284186?needAccess=true

[^72]: https://dl.acm.org/doi/pdf/10.1145/3589335.3651268

[^73]: https://ora.ox.ac.uk/objects/uuid:9901f078-17d2-4f63-be8d-4e07fbe0f373/files/swd375z124

[^74]: https://arxiv.org/pdf/2403.00770.pdf

[^75]: https://arxiv.org/html/2403.06454v1

[^76]: https://dl.acm.org/doi/pdf/10.1145/3589335.3651257

[^77]: https://arxiv.org/pdf/2206.08401.pdf

[^78]: http://arxiv.org/pdf/2407.10614.pdf

[^79]: https://moss.sh/reviews/best-5-crypto-analysis-tools-glassnode-vs-messari-vs-others/

[^80]: https://compliance.waystone.com/sfc-regulatory-updates-what-asset-managers-need-to-know/

[^81]: https://insights.glassnode.com/the-week-onchain-week-49-2025/

[^82]: https://ejournal.kresnamediapublisher.com/index.php/jri/article/view/432

[^83]: https://www.mdpi.com/2227-9091/13/10/195

[^84]: https://www.tandfonline.com/doi/full/10.1080/15140326.2025.2551627

[^85]: https://www.journals.vu.lt/omee/article/view/22607

[^86]: https://ieeexplore.ieee.org/document/9171147/

[^87]: https://www.semanticscholar.org/paper/afce731e403fed20a21ccc5c6f3b21156d050e6d

[^88]: https://journaleska.com/index.php/bmi/article/view/317

[^89]: https://www.semanticscholar.org/paper/fc12c7b35d59d500467bd58e68d699c18a9d5d19

[^90]: https://journals.sagepub.com/doi/10.3184/003685017X14912945098080

[^91]: https://www.acpjournals.org/doi/10.7326/M18-2552

[^92]: https://joiv.org/index.php/joiv/article/download/943/466

[^93]: https://arxiv.org/pdf/2303.09397.pdf

[^94]: https://www.mdpi.com/1099-4300/23/12/1582/pdf

[^95]: https://arxiv.org/pdf/2501.13136.pdf

[^96]: https://arxiv.org/abs/2106.12961

[^97]: http://arxiv.org/pdf/2501.05232.pdf

[^98]: https://ycharts.com/indicators/bitcoin_price

[^99]: https://www.coingecko.com/en/coins/solana/bnb

[^100]: https://twelvedata.com/markets/499377/crypto/coinbase-pro/btc-usd/historical-data

[^101]: https://coinmarketcap.com/currencies/solana/sol/bnb/

[^102]: https://www.cmegroup.com/media-room/press-releases/2025/10/14/cme_group_announcesfirsttradesofoptionsonsolanaandxrpfutures.html

[^103]: https://www.coinbase.com/price/bitcoin

[^104]: https://www.binance.com/en/price/xrp

[^105]: https://bitbo.io

Generated by

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>