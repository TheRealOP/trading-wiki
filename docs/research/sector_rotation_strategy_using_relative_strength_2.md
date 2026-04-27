```markdown
---
topic: "sector rotation strategy using relative strength"
date: 2026-04-07
model: Pro
tags: [agent/research, quant/momentum, instrument/etf]
---

# Advanced Sector Rotation: Dual Momentum

## Key Insight
This strategy refines basic [[sector_rotation_strategy_using_relative_strength]] by incorporating an absolute momentum filter, a concept core to [[Dual Momentum]]. The goal is to participate in the strongest trending sectors ([[relative momentum]]) but only when the overall market context is positive ([[absolute momentum]]), seeking to avoid major [[drawdown]] events. This combines the classic momentum research of [[Jegadeesh and Titman]] with a [[trend following]] overlay for risk management.

## The Math
1.  **Relative Momentum (Ranking):** Calculate the Rate of Change (ROC) for each sector ETF and a benchmark over a lookback period 'n'.
    $ROC_n = \frac{P_t - P_{t-n}}{P_{t-n}}$
    Where $P_t$ is the current price and $P_{t-n}$ is the price 'n' periods ago. Sectors are then ranked by their ROC.

2.  **Absolute Momentum (Trend Filter):** A timing filter to protect capital. The strategy only holds equity assets if their ROC is positive, or if a broad market index like [[SPY]] is trading above a long-term moving average.
    $Filter_{abs} = (ROC_n(Asset) > 0)$ OR $(P_t(SPY) > SMA_{200}(SPY))$
    If the condition is false, capital is allocated to a safe asset like short-term treasury bonds ([[AGG]] or [[SHY]]).

## Strategy Logic
1.  Define a universe of sector ETFs (e.g., [[XLK]], [[XLF]], [[XLE]], [[XLY]], [[XLP]], etc.).
2.  Define a broad market benchmark ([[SPY]]) and a safe asset ([[AGG]]).
3.  At each rebalancing period (e.g., end of month), calculate the [[absolute momentum]] filter for the benchmark ([[SPY]]).
4.  **IF** the filter is FALSE (i.e., negative momentum), liquidate all sector positions and invest 100% in the safe asset ([[AGG]]).
5.  **IF** the filter is TRUE (i.e., positive momentum), calculate the [[relative momentum]] (e.g., 6-12 month ROC) for all sector ETFs in the universe.
6.  Rank the sectors by their momentum score.
7.  Invest in the top N (e.g., 1-3) ranked sectors for the next period.

## Parameters
*   **Lookback Period (n):** Typically 6-12 months. Shorter periods can increase [[whipsaw]], longer periods may be slower to adapt.
*   **Top N:** Number of sectors to hold. A smaller N increases concentration, while a larger N provides more diversification.
*   **Rebalancing Frequency:** Typically monthly.
*   **Safe Asset:** [[AGG]], [[SHY]], or other short-term government bond ETFs.
*   **Absolute Momentum Trigger:** ROC > 0 or Price > SMA(200) are common.

## Risks
*   **[[Whipsaw]]:** The strategy can be hurt by frequent, short-lived reversals in the market trend.
*   **[[Momentum Crashes]]:** Historically, momentum strategies have experienced rare but severe crashes, often at market turning points.
*   **[[Tracking Error]]:** The strategy will have high [[tracking error]] relative to a passive benchmark, which can be psychologically difficult to manage.

## Related # edited by gemini
*   [[sector_rotation_strategy_using_relative_strength]] — This strategy refines the basic concepts of sector rotation using relative strength by adding an absolute momentum filter.
*   [[Dual Momentum]] — This document elaborates on the core principle of combining relative and absolute momentum for enhanced risk-adjusted returns, which is central to this strategy.
*   [[trend following]] — The absolute momentum filter employed in this strategy serves as a crucial trend-following overlay for effective risk management.
*   [[leveraged_etf_momentum_rotation_tqqq_soxl_weekly_rebalance]] — Provides a specific example of an ETF-based momentum rotation strategy with similar principles of selecting leading assets.
*   [[momentum_trading_strategies_for_small_accounts]] — This advanced sector rotation strategy is a type of momentum trading, applicable for various account sizes.
*   [[algorithmic_trading_with_moving_averages]] — Moving averages are frequently used to define trend and construct absolute momentum filters, a key component of this strategy.
*   [[combining_trend_following_with_volatility_filters_for_max_re]] — Explores methods to enhance trend-following strategies, which is relevant to the risk management and signal generation aspects here.
*   [[quantitative_risk_management_position_sizing]] — Essential for determining appropriate capital allocation to the selected sectors within this strategy.
*   [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] — Offers a mathematical framework for optimal position sizing, which could be applied to manage concentration in the top N sectors.
*   [[risk_of_ruin_calculations_for_aggressive_small_accounts]] — Crucial for understanding the potential downside and managing capital preservation when implementing any strategy, particularly one involving concentration.
*   [[Sharpe Ratio]] — A standard metric for evaluating the risk-adjusted performance of such strategies, providing a benchmark for comparison.

## Sources
*   "A Quantitative Approach to Tactical Asset Allocation" - Mebane Faber
*   "Dual Momentum Investing" - Gary Antonacci
*   "Returns to Buying Winners and Selling Losers" - Jegadeesh & Titman

## Next Steps # edited by gemini
- [ ] Backtest the impact of different [[lookback periods]] (e.g., 3, 6, 9, 12 months) on strategy performance.
- [ ] Explore adding international or factor ETFs to the universe, similar to approaches discussed in [[leveraged_etf_momentum_rotation_tqqq_soxl_weekly_rebalance]].
- [ ] Compare performance of different absolute momentum filters (e.g., ROC vs. SMA), potentially drawing insights from [[algorithmic_trading_with_moving_averages]] for SMA-based approaches.
- [ ] Investigate using [[volatility]] or [[correlation]] as part of the ranking mechanism, possibly referencing concepts from [[volatility_breakout_strategies]] or [[pairs_trading_statistical_arbitrage_methods]].
- [ ] Consider applying advanced position sizing techniques, such as those discussed in [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]], for improved capital allocation.
- [ ] Implement with backtesting frameworks (e.g., VectorBT, Zipline) to empirically validate the strategy.
```