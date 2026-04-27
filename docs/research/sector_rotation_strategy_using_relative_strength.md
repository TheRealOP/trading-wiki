```markdown
---
topic: "sector rotation strategy using relative strength"
date: 2026-04-07
model: Pro
tags: [agent/research, quant/momentum, instrument/etf]
---

# [[Relative Strength Sector Rotation]]

## Key Insight
[[Sector Rotation]] is a [[strategy]] that seeks to capitalize on the cyclical nature of the economy by overweighting sectors that are expected to outperform. By applying a [[quantitative momentum]] lens, we can systematically identify the strongest sectors using [[relative strength]], allocating capital to leaders and avoiding laggards. This approach attempts to capture the [[momentum]] premium, a well-documented market anomaly.

## The Math
[[Relative Strength]] can be measured in several ways. A common method is to calculate the percentage price change over a lookback period.

Let $P_i(t)$ be the price of asset $i$ at time $t$. The [[momentum]] score ($M$) over a lookback period of $N$ days is:
$M_i(t, N) = \frac{P_i(t)}{P_i(t-N)} - 1$

Alternatively, relative strength can be calculated as a ratio against a [[benchmark]] like [[SPY]]:
$RS_{ratio} = \frac{P_{sector\_ETF}}{P_{SPY}}$

A combined [[momentum]] score can also be used, weighting different lookback periods, as seen in the work of Andreas Clenow. For example, a simple blended score:
$M_{total} = (0.6 \times M_i(t, 90)) + (0.4 \times M_i(t, 180))$

## Strategy Logic
1.  Define a universe of assets, typically 9-11 US sector ETFs (e.g., [[XLE]], [[XLF]], [[XLK]], [[XLY]], [[XLI]], [[XLP]], [[XLV]], [[XLB]], [[XLU]]).
2.  Select a [[lookback period]] (e.g., $N=126$ trading days for 6 months).
3.  At the end of each month, calculate the [[momentum]] score $M_i$ for each ETF in the universe.
4.  Rank the ETFs from highest to lowest score.
5.  Invest equal capital into the top $K$ ranked ETFs (e.g., $K=3$).
6.  Hold these positions for the next month.
7.  Repeat the process at the end of each month, rotating capital into the new leaders.

## Parameters
*   **Universe:** The set of ETFs to be ranked.
*   **Lookback Period:** The timeframe for calculating [[momentum]] (e.g., 3, 6, 12 months). Shorter periods are more responsive but can lead to more [[whipsaw]].
*   **Holding Period:** How long to hold the top assets before re-evaluating (e.g., monthly, quarterly).
*   **Number of Positions (K):** The number of top ETFs to hold. Fewer positions increase [[concentration risk]] but may also increase returns.

## Risks
*   **[[Whipsaw]]:** Rapid changes in sector leadership can lead to frequent, unprofitable trades.
*   **[[Momentum Crash]]:** The [[momentum]] factor can experience rare but severe drawdowns, especially during market regime changes.
*   **[[Tracking Error]]:** The strategy will have performance that deviates significantly from the broad market [[benchmark]], which can be psychologically difficult to manage.

## Related
*   [[Dual Momentum]] — This strategy builds upon the concept of relative momentum by adding an absolute momentum filter to avoid market downturns. # edited by gemini
*   [[Trend Following]] — Sector rotation is a specific application of trend-following principles, aiming to ride the trends of outperforming sectors. # edited by gemini
*   [[Time Series Momentum]] — This concept, focusing on an asset's past returns to predict future returns, is fundamental to calculating the momentum scores used in sector rotation. # edited by gemini
*   [[Tactical Asset Allocation]] — Sector rotation is a form of tactical asset allocation where capital is dynamically shifted between different market segments based on perceived strength. # edited by gemini
*   [[Sharpe Ratio]] — A key performance metric used to evaluate the risk-adjusted returns of strategies like sector rotation. # edited by gemini
*   [[algorithmic_trading_with_moving_averages]] — Moving averages are often used as a simple measure of momentum or trend, which aligns with the relative strength calculations here. # edited by gemini
*   [[crypto_momentum_trading_btc_eth_4h_timeframe]] — Provides an example of applying momentum trading principles, which are core to sector rotation, in a different asset class. # edited by gemini
*   [[leveraged_etf_momentum_rotation_tqqq_soxl_weekly_rebalance]] — This file describes a specific, similar strategy involving momentum-based rotation of ETFs, reinforcing the concepts used here. # edited by gemini
*   [[momentum_trading_strategies_for_small_accounts]] — This broader category encompasses the momentum-driven approach to identifying strong sectors that is central to sector rotation. # edited by gemini
*   [[quantitative_risk_management_position_sizing]] — Essential for determining appropriate capital allocation to each sector ETF and managing overall portfolio risk within this strategy. # edited by gemini

## Sources
*   "A Quantitative Approach to Tactical Asset Allocation" - Mebane T. Faber
*   "Dual Momentum Investing" - Gary Antonacci
*   "Stocks on the Move" - Andreas F. Clenow

## Next Steps
- [ ] Explore adding an [[absolute momentum]] filter, as detailed in [[Dual Momentum]], to move to cash during broad market downturns. # edited by gemini
- [ ] Investigate optimal [[position sizing]] for this strategy by applying concepts from [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] or the broader principles in [[quantitative_risk_management_position_sizing]]. # edited by gemini
- [ ] Analyze the impact of incorporating [[volatility]] filters, potentially drawing insights from [[combining_trend_following_with_volatility_filters_for_max_re]], to enhance risk-adjusted returns. # edited by gemini
- [ ] Conduct thorough backtesting across different [[lookback period]]s to assess strategy robustness. # edited by gemini
- [ ] Evaluate the strategy's risk profile and potential [[risk_of_ruin_calculations_for_aggressive_small_accounts]] to ensure alignment with risk tolerance. # edited by gemini
- [ ] Compare performance against an equal-weight benchmark of the same ETF universe. # edited by gemini
```