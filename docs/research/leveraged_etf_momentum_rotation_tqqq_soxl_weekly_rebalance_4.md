---
topic: "leveraged ETF momentum rotation TQQQ SOXL weekly rebalance"
date: 2026-04-09
model: Pro
tags: [agent/research, quant/momentum, instrument/etf]
---

# Volatility-Managed Leveraged ETF Rotation

## Key Insight
This strategy refines a pure [[momentum]] approach by incorporating a [[volatility targeting]] mechanism. Instead of a binary "all-in" or "all-out" allocation, position size is dynamically adjusted based on the recent realized [[volatility]] of the selected ETF. This helps manage risk and mitigate the impact of [[volatility decay]], a significant drag on [[leveraged ETFs]] in choppy markets, creating a basic [[risk parity]] framework.

## The Math
The core of the strategy is the volatility-adjusted position sizing.

1.  **Momentum Score ($M_i$):** A standard rate-of-change formula is used to select the asset.
    $M_i = \frac{P_{i,t}}{P_{i, t-n}} - 1$
    Where $P_{i,t}$ is the price of asset $i$ at time $t$ and $n$ is the lookback period.

2.  **Realized Volatility ($\sigma_i$):** The annualized standard deviation of daily log returns over a lookback period $k$.
    $\sigma_i = \text{StDev}(\ln(\frac{P_{t}}{P_{t-1}})) \times \sqrt{252}$

3.  **Target Weight ($W_i$):** The allocation is inversely proportional to the asset's volatility.
    $W_i = \frac{\sigma_{target}}{\sigma_i}$
    Where $\sigma_{target}$ is the desired portfolio volatility level. The remainder of the portfolio ($1 - W_i$) is held in a low-volatility asset like cash or [[SHY]].

## Strategy Logic
1.  On a weekly basis (e.g., end-of-day Friday), calculate the $n$-period [[momentum]] score ($M_i$) for [[TQQQ]] and [[SOXL]].
2.  Select the ETF with the higher momentum score. If both scores are negative, move to the risk-off asset ([[SHY]]).
3.  Calculate the $k$-period realized [[volatility]] ($\sigma_i$) for the selected ETF.
4.  Determine the target weight ($W_i$) using the target volatility formula. The weight is capped at 100%.
5.  Allocate $W_i$ of the portfolio to the selected ETF and $1 - W_i$ to [[SHY]].
6.  Hold the position until the next weekly rebalancing signal.

## Parameters
*   **Asset Universe:** [[TQQQ]], [[SOXL]], [[SHY]] (or cash).
*   **Momentum Lookback ($n$):** 20-60 trading days (approx. 1-3 months).
*   **Volatility Lookback ($k$):** 20 trading days (approx. 1 month).
*   **Target Volatility ($\sigma_{target}$):** An annualized figure, e.g., 20-30%. This is a critical parameter requiring careful calibration.

## Risks
*   **[[Whipsaw]]:** Rapid changes in market leadership can lead to frequent, unprofitable trades.
*   **Parameter Sensitivity:** The strategy's performance is highly dependent on the chosen lookback periods and, most critically, the `$\sigma_{target}$`.
*   **[[Volatility decay]]:** While mitigated, the erosive effect of volatility on leveraged ETF returns is not eliminated.
*   **Black Swan Events:** Extreme market shocks can cause [[drawdown]]s that exceed the target volatility before the model can adjust.

## Related
*   [[leveraged_etf_momentum_rotation_tqqq_soxl_weekly_rebalance]]
*   [[leveraged_etf_momentum_rotation_tqqq_soxl_weekly_rebalance_2]]
*   [[leveraged_etf_momentum_rotation_tqqq_soxl_weekly_rebalance_3]]
*   [[quantitative_risk_management_position_sizing]]
*   [[risk parity]]
*   [[volatility_breakout_strategies]]
*   [[Sharpe Ratio]]
*   [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]]

## Sources
*   "Volatility Targeting: A Risk-Based Approach to Asset Allocation" - AQR Capital Management
*   "The Dangers of Leveraged ETFs" - Seeking Alpha

## Next Steps
- [ ] Backtest the strategy using `vectorbt` to analyze the impact of different `$\sigma_{target}$` values.
- [ ] Explore using implied volatility (e.g., [[VIX]], VXN) as a forward-looking risk input.
- [ ] Compare returns and [[drawdown]]s against a non-risk-managed momentum strategy.
- [ ] Introduce a market regime filter (e.g., based on a long-term [[moving average]] of [[SPY]]) to switch the entire strategy off during bear markets.
- [ ] Investigate alternative momentum calculations, such as dual momentum or ROC-weighted momentum.