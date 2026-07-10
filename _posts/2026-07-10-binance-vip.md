---
layout: post
title: "Binance VIP"
date: 2026-07-10
category: trading
---

# Executive Summary  
Binance’s VIP program has **10 levels (VIP0–VIP9)**, each offering progressively lower trading fees and enhanced privileges.  Tiers are set by *dual criteria*: a user’s 30-day trading volume (across Spot, Margin, etc.) and average BNB holdings.  To reach a tier, one must meet **both** the volume (in USD) and BNB thresholds listed below (recently lowered for VIP1–3 in Mar 2026).  VIP status updates daily at 08:00 UTC based on the rolling 30‑day window.  For example, a trader with $2 million 30‑day volume and ≥5 BNB qualifies as VIP1 (maker fee 0.090%/taker 0.100%), whereas meeting VIP9’s requirements (≥$4 billion + 5,500 BNB) yields a flat 0.011%/0.023% fee.  Holding/borrowing/OTC tracks also exist (e.g. ≥$100k average assets + 5 BNB for VIP1).  Non-fee perks include higher withdrawal limits (e.g. VIP0–3 ≈8 M BUSD/day vs. VIP9 ≈96 M BUSD/day), more sub-accounts, raised API/margin limits, 24/7 priority support, and VIP-only events/swags.  The tables below summarize the numeric thresholds/fees and tier benefits; charts illustrate fee vs. volume and the tier-evaluation timeline.  (See *Sources* at end for Binance’s official details.)  

## VIP Qualification Criteria  
- **Trading Volume (30d)**: Binance measures each user’s cumulative 30-day trading volume (all Spot+Margin trades in USD).  Each VIP level has a minimum volume threshold (see table below).  
- **BNB Holding**: A daily average BNB balance (on all accounts) must meet a tier-specific minimum.  (March 2026 updates lowered VIP1–3 BNB requirements from 25→5, 100→25, 250→100.)  BNB counts toward overall asset criteria in the new “Holder” program.  
- **Asset/Holdings Track**: Long-term holders can qualify by total assets (Spot, Futures, Earn, etc.).  E.g. previously ≥$500k+25 BNB (VIP1) was needed; now only $100k+5 BNB.  The expanded “Holder Program” lets users reach up to VIP9 by holdings.  
- **Borrower/Loan Track**: Borrowing ≥$100k (via crypto or VIP loans) + 5 BNB also grants VIP status (borrower VIP).  
- **OTC and Options**: ≥$200k OTC volume + 5 BNB yields VIP; options volume ≥$100M fast-tracks to VIP4 (no BNB needed).  (These are supplementary tracks.)  
- **Daily Update**: Binance **recalculates VIP daily (08:00 UTC)** using the past 30 days of activity.  If a user meets multiple tracks, they receive the highest VIP.  Once gained, benefits apply immediately.  Falling below thresholds will downgrade VIP at the next 08:00 recalculation.  

>*Example:* A trader with 3 million USD 30d volume and holding 10 BNB meets VIP1’s criteria (≥1M USD + ≥5 BNB) but not VIP2 (needs ≥5M + 25 BNB).  His maker/taker fees are thus 0.090%/0.100%.  If he instead held 30 BNB, he’d reach VIP2 (fees 0.080%/0.100%).  Enabling “BNB fee payment” gives an additional 25% discount (e.g. VIP1 taker 0.0750%).  

```mermaid
gantt
    title VIP Tier Recalculation (Daily, rolling window)
    dateFormat  YYYY-MM-DD
    axisFormat  %d\n%b
    section Rolling Window
    Last 30 days of trading (volume & holdings) : 2026-06-01, 30d
    section VIP Update
    Daily Tier Eval @ 08:00 UTC: 2026-06-02, 2026-06-31
```

## Maker/Taker Fees by VIP Level  

| VIP Level      | 30d Volume (USD)      | BNB Balance      | Maker Fee (spot) | Taker Fee (spot) | Maker Fee (with 25% BNB) | Taker Fee (with 25% BNB) |
|---------------|------------------------|------------------|------------------|------------------|---------------------------|---------------------------|
| VIP 0 (Regular) | < $1,000,000          | ≥ 0              | 0.100%           | 0.100%           | 0.07500%                  | 0.07500%                  |
| VIP 1         | ≥ $1,000,000           | ≥ 5              | 0.090%           | 0.100%           | 0.06750%                  | 0.07500%                  |
| VIP 2         | ≥ $5,000,000           | ≥ 25             | 0.080%           | 0.100%           | 0.06000%                  | 0.07500%                  |
| VIP 3         | ≥ $20,000,000          | ≥ 100            | 0.040%           | 0.060%           | 0.03000%                  | 0.04500%                  |
| VIP 4         | ≥ $75,000,000          | ≥ 500            | 0.040%           | 0.052%           | 0.03000%                  | 0.03900%                  |
| VIP 5         | ≥ $150,000,000         | ≥ 1,000          | 0.025%           | 0.031%           | 0.01875%                  | 0.02325%                  |
| VIP 6         | ≥ $400,000,000         | ≥ 1,750          | 0.020%           | 0.029%           | 0.01500%                  | 0.02175%                  |
| VIP 7         | ≥ $800,000,000         | ≥ 3,000          | 0.019%           | 0.028%           | 0.01425%                  | 0.02100%                  |
| VIP 8         | ≥ $2,000,000,000       | ≥ 4,500          | 0.016%           | 0.025%           | 0.01200%                  | 0.01875%                  |
| VIP 9         | ≥ $4,000,000,000       | ≥ 5,500          | 0.011%           | 0.023%           | 0.00825%                  | 0.01725%                  |

*Source: Binance Spot/Margin fee schedule.  BNB discount (25%) is optional if “Pay with BNB” is enabled.  (USDC fees shown on Binance site are similar; we omit them here.)*  

The chart below illustrates how maker/taker fees drop with rising volume (assuming BNB criteria met):

  

```mermaid
%%{init: {"themeVariables": {"lineColor": "#ff7f0e", "textColor": "#000000", "fontSize": "12px"}}}%%
gantt
    title Tiered Fee Schedule vs Volume
    dateFormat  YYYY
    axisFormat  %Y
    2020 : 2025
    section Maker Fee (%)
    VIP 0 at 0.100%        : a1, 2020, 2025
    VIP 1 drops to 0.090%   : a2, 2020, 2025
    VIP 2 drops to 0.080%   : a3, 2020, 2025
    VIP 3 drops to 0.040%   : a4, 2020, 2025
    VIP 4+ at 0.025–0.011%  : a5, 2020, 2025
    section Taker Fee (%)
    VIP 0 at 0.100%        : b1, 2020, 2025
    VIP 1 remains 0.100%    : b2, 2020, 2025
    VIP 3 drops to 0.060%   : b3, 2020, 2025
    VIP 4 drops to 0.052%   : b4, 2020, 2025
    VIP 9 at 0.023%        : b5, 2020, 2025
```

*(Simplified illustration of VIP fee levels; see table above for exact rates.)*  

### Fee Examples  
- **Low-volume trader:** $1000 spot trade at VIP0 costs 0.1%×$1000 = $1.  Paying with BNB yields 25% off (fee $0.75).  A 20% referral rebate can further lower it to $0.60.  
- **Medium-volume trader:** $5M monthly volume, 50 BNB held ⇒ VIP2 (maker 0.080%, taker 0.100%).  Taker fee = $0.10 per $100 traded.  With BNB discount, maker/taker become 0.0600%/0.0750%.  
- **High-volume trader:** $3B volume, 6,000 BNB held ⇒ VIP9 (maker 0.011%, taker 0.023%).  A $100k trade costs $11 maker / $23 taker.  (Even lower with BNB.)  

## Non-Fee VIP Benefits (by Tier)  

| Benefit                     | Details & VIP Level                                             |
|-----------------------------|-----------------------------------------------------------------|
| **Withdrawal Limits** (24h) | VIP0–3: ~8 million BUSD; VIP4: ~16 M; VIP5: ~24 M; VIP6: ~40 M; VIP7: ~64 M; VIP8: ~80 M; VIP9: ~96 M.  (BNB=Binance USD; 1 BUSD≈1 USD.) |
| **24/7 Priority Support**   | All VIPs (1+) get 24/7 priority support.  At higher tiers (typically VIP3+), dedicated account managers (“key coverage”) are assigned. |
| **API & Sub-Accounts**      | VIPs enjoy higher API weight limits and can create more sub-accounts.  (For example, institutional VIPs often use dozens or up to ~200 sub-accounts, far above regular limits.) |
| **Margin/Borrow Limits**    | VIP tiers have elevated margin and loan limits.  For instance, Binance raised *isolated* margin borrowing caps ≈4× for VIP1 (see example BTC/USDT table).  Generally, each VIP level allows successively higher loan and margin exposures. |
| **VIP Perks & Events**      | Starting VIP1, users gain access to exclusive research, VIP-only insights, and special events.  Higher tiers receive VIP swag, invites to private gatherings, and tailored onboarding. |
| **Other Privileges**        | Customizable futures/spot rate limits, launchpad staking priority (unofficial), and sometimes private OTC trading desks are hallmarks of high-tier VIPs.  (Exact details may vary by region and product.) |

*These benefits (cited above) grow with tier.  For example, Binance notes that **withdrawal limits, sub-accounts, and API thresholds all increase** for higher VIPs.  The VIP program is designed for “high-volume” users and institutions, offering **tailored limits and support** as tier benefits.*

## Tier Calculation and Maintenance  
Binance uses a **rolling 30-day window** (including the current day) to evaluate volume and holdings.  Each day at 08:00 UTC, it recalculates every account’s VIP level based on the past 30 days of trades (Spot, Margin, COIN/USDT futures, Convert, etc.) and asset balances.  If a user met VIP2 criteria yesterday, they keep VIP2 benefits immediately (even before 08:00) and will continue only if their trailing metrics remain ≥ VIP2 by the next calculation.  Falling below either threshold causes a downgrade at the next 08:00 update.

Specifically, the **volume threshold** uses the higher of *rolling 30-day total* or *previous-day total* (whichever is larger).  Similarly, **asset holdings** (for the “Holder” track) use either the 30-day average net assets or the last-day net assets.  (This ensures stability: short dips don’t immediately drop a user’s VIP.)  In practice, active traders simply watch their 30-day volume and BNB balance, since any VIP tier requires *both* conditions.  Users can track their status via Binance’s *VIP portal* or app hub. 

>*Example timeline:* Suppose today is July 31.  Binance will sum your trades from July 1–31 and check your BNB balance; then at 08:00 UTC on Aug 1 it assigns your new tier.  That tier holds until 08:00 UTC Aug 2, when Binance again slides the window (now July 2–Aug 1) and updates your VIP accordingly. 

## Regional & Product Notes  
- **Global (Binance.com)**: The above applies to the main Binance platform.  In **Binance.US** (and other restricted jurisdictions), fee structures and limits differ; the VIP program as described is only on Binance’s international sites.  
- **Spot vs. Futures vs. Others**: A user’s VIP level is *universal* across products.  Tiered spot fees are shown above; futures and margin follow similar tier discounts.  (E.g. after the Mar 2026 update, USDⓈ-M futures VIP1 taker fee is 0.05% (maker 0.018%), and higher VIPs get even lower rates.)  However, qualification thresholds for **futures volume** are higher (e.g. VIP1 futures vol ≥$5M instead of $1M).  *Options* trading has its own fast-track rule (see above).  **P2P** crypto trading usually has no trading fee and isn’t tiered by VIP (VIP mainly affects fees in Spot/Margin/Futures).  
- **Other Products**: Benefits like higher launchpad allocations or staking yields for VIPs are not officially documented per tier (they often depend on promotions).  OTC trading desks and institutional loans are generally more accessible at VIP1+, but details are by Binance OTC policy, not public thresholds.  

**Unspecified Details:** Binance’s official disclosures do not enumerate every perk by tier.  For example, API weight limits and sub-account maximums are referenced qualitatively.  Similarly, “support coverage” and non-trading rewards are described broadly (e.g. “key account manager at higher tiers”) without exact VIP thresholds.  Where possible we cited concrete figures (e.g. withdrawal limits, margin limits). 

## Sources and Further Reading  
- Binance Support – **Fee Schedule (Spot/Margin)** (Official fee table used above)  
- Binance Announcements (Mar 2026) – **VIP Program Threshold Updates** (BNB holding and futures thresholds lowered; new Holder VIP criteria; Rising Star program)  
- Binance Blog – *What Is Binance VIP?* (Jan 2026) (benefits overview and qualification tracks)  
- Binance Announcement (Jun 2023) – **Margin Borrow Limits Increased for VIPs**  
- Binance Square (blog) – **Withdrawal Limits by VIP**  
- Binance Futures FAQ – **API/Rate Limits by VIP** (sub-account & rate-limit policy)  

Additional crypto news and community sources confirm the above changes (e.g. PR Newswire’s summary of Mar 2026 updates). The data above reflects the latest Binance policies (as of mid-2026) and may evolve; always refer to Binance’s official pages for updates. 

