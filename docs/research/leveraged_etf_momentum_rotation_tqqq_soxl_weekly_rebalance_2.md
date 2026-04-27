```markdown
---
topic: "leveraged ETF momentum rotation TQQQ SOXL weekly rebalance"
date: 2026-04-07
model: Pro
tags: [agent/research, quant/momentum, instrument/etf]
---

# Risk-Adjusted Leveraged ETF Rotation

## Key Insight
This strategy refines [[leveraged_etf_momentum_rotation_tqqq_soxl_weekly_rebalance]] by incorporating a [[volatility]] filter and risk-adjusted momentum. Instead of simply holding the top performer between [[TQQQ]] and [[SOXL]], this model rotates into a risk-off asset (e.g., [[IEF]] or [[TLT]]) during high-volatility regimes. This aims to mitigate the severe [[drawdown]] inherent in leveraged ETFs and improve the overall [[Sharpe Ratio]].

## The Math
The core of this approach is to select assets based on risk-adjusted returns rather than raw momentum. We use the [[Sharpe Ratio]] for this.

1.  **Momentum (Rate of Change):**
    $Momentum = \frac{P_t - P_{t-n}}{P_{t-n}}$
    Where $P_t$ is the current price and $P_{t-n}$ is the price *n* periods ago.

2.  **Risk-Adjusted Momentum (Sharpe Ratio):**
    $S_a = \frac{R_a - R_f}{\sigma_a}$
    - $R_a$: Average return of the asset over the look-back period.
    - $R_f$: Risk-free rate (or return of a benchmark like [[BIL]]).
    - $\sigma_a$: Standard deviation of the asset's returns (a proxy for [[volatility]]).

## Strategy Logic
1.  Define the asset universe: [[TQQQ]], [[SOXL]], and a risk-off asset like [[IEF]] (7-10 Year Treasury Bond ETF).
2.  Calculate the 3-month [[Sharpe Ratio]] for both [[TQQQ]] and [[SOXL]] on a weekly basis.
3.  Measure the market regime using a broad market index [[volatility]] indicator, like the [[VIX]]. If VIX > 25 (or another threshold), the regime is considered "risk-off".
4.  **Rotation Rule:**
    - If in a "risk-off" regime (VIX > 25), allocate 100% to [[IEF]].
    - If in a "risk-on" regime (VIX <= 25), allocate 100% to the ETF ([[TQQQ]] or [[SOXL]]) with the highest 3-month [[Sharpe Ratio]].
5.  Rebalance the portfolio weekly based on this logic.

## Parameters
- **Momentum Look-back:** 3 months (approx. 63 trading days).
- **Volatility Look-back:** 1 month (approx. 21 trading days) for calculating $\sigma_a$.
- **Market Regime Filter:** [[VIX]] closing price.
- **Risk-off Threshold:** VIX > 25.
- **Rebalance Frequency:** Weekly.

## Risks
- **[[Volatility Decay]]:** The primary risk in holding leveraged ETFs, especially in choppy or sideways markets. The regime filter aims to mitigate this, but it's not foolproof.
- **[[Whipsaw]]:** Rapid changes in market regime can lead to frequent, and potentially loss-making, trades between risk-on and risk-off assets.
- **[[Overfitting]]:** The VIX threshold and look-back periods are parameters that can be curve-fit to historical data. They may not perform as well in the future.
- **[[Black Swan Events]]:** Sudden, extreme market shocks can cause massive losses that a weekly rebalancing schedule cannot react to quickly enough.

## Related
- [[leveraged_etf_momentum_rotation_tqqq_soxl_weekly_rebalance]] — This document is a refinement of this strategy, building upon its core concept with risk management. # edited by gemini
- [[Sharpe Ratio]] — The Sharpe Ratio is a key metric used in this strategy to evaluate risk-adjusted returns for asset selection. # edited by gemini
- [[quantitative_risk_management_position_sizing]] — This strategy incorporates risk management through volatility filtering and risk-off asset allocation, which is a key aspect of effective position sizing. # edited by gemini
- [[combining_trend_following_with_volatility_filters_for_max_re]] — This strategy utilizes a volatility filter to manage risk, similar to the principles discussed in combining trend following with volatility filters. # edited by gemini
- [[momentum_trading_strategies_for_small_accounts]] — This strategy is a specific application of momentum trading tailored for leveraged ETFs. # edited by gemini
- [[sector_rotation_strategy_using_relative_strength]] — The rotation between TQQQ and SOXL based on relative strength (Sharpe Ratio) shares conceptual similarities with sector rotation strategies. # edited by gemini
- [[risk_of_ruin_calculations_for_aggressive_small_accounts]] — The aim of mitigating drawdowns and improving risk-adjusted returns in this strategy directly addresses concerns related to the risk of ruin. # edited by gemini
- [[highest_sharpe_ratio_strategies_for_accounts_under_1000_doll]] — This strategy aims to achieve a high Sharpe Ratio, aligning with the principles discussed in strategies for maximizing this metric. # edited by gemini
- [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] — The Kelly Criterion provides a framework for optimal bet sizing, which can be integrated into the position sizing component of this strategy. # edited by gemini

## Sources
- "Optimal Rebalancing of Leveraged ETF Portfolios" - arXiv:1806.09503
- "Taming Momentum: A Risk-Managed Approach to Global Tactical Asset Allocation"

## Next Steps
- [ ] Explore using [[ATR]] (Average True Range) as an alternative to the [[VIX]] for the regime filter. # edited by gemini
- [ ] Backtest the performance of different risk-off assets (e.g., [[GLD]], [[UUP]]). # edited by gemini
- [ ] Implement a dynamic position sizing model based on the [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] instead of a 100% allocation. # edited by gemini
- [ ] Test a dual-momentum approach, comparing the ETF's momentum to a benchmark like [[SPY]] before entering a position. # edited by gemini
- [ ] Analyze the impact of different rebalancing frequencies (e.g., daily, monthly). # edited by gemini
```