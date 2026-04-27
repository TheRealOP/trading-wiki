```markdown
---
topic: "mean reversion overnight gap fade strategy"
date: 2026-04-07
model: Pro
tags: [agent/research, quant/mean-reversion]
---

# Statistical Modeling of Overnight Gaps

## Key Insight
The tendency for an overnight [[gap]] to fade can be modeled more rigorously by treating the intraday price as a [[mean-reverting process]]. By applying stochastic calculus, specifically the [[Ornstein-Uhlenbeck process]], we can derive key parameters like the speed of reversion and an optimal holding time, adding a quantitative layer to the [[mean_reversion_overnight_gap_fade_strategy]]. This transforms the strategy from a heuristic to a model-driven approach.

## The Math
The [[Ornstein-Uhlenbeck process]] is a [[stochastic differential equation]] that describes the velocity of a particle under friction. In finance, it models a variable $X_t$ (e.g., price) that is pulled towards a long-term mean $\mu$.

The process is defined as:
$dX_t = \theta(\mu - X_t)dt + \sigma dW_t$

Where:
- $X_t$ is the price at time $t$.
- $\mu$ is the [[mean reversion]] level (e.g., previous day's close or a [[moving average]]).
- $\theta$ is the speed of reversion. A higher $\theta$ means the price reverts to the mean faster.
- $\sigma$ is the [[volatility]] of the process.
- $dW_t$ is a Wiener Process, representing the random "shocks" to the price.

From the speed of reversion, $\theta$, we can calculate the **half-life** of the mean reversion process, which gives a model-based estimate for the expected holding time.

**Half-Life of Mean Reversion ($\tau_{1/2}$):**
$\tau_{1/2} = \frac{\ln(2)}{\theta}$

A shorter half-life implies a stronger, more reliable reversion tendency, making the gap fade trade more attractive.

## Strategy Logic
1.  Identify a significant [[overnight gap]] in a high-[[liquidity]] asset like [[SPY]] or [[QQQ]].
2.  After the market opens, collect high-frequency (e.g., 1-minute) price data.
3.  Using a lookback window (e.g., the first 30 minutes of trading), perform a regression on the discretized OU process to estimate the parameter $\theta$ (speed of reversion).
4.  If the estimated $\theta$ is positive and statistically significant, it confirms a mean-reverting tendency.
5.  Calculate the [[half-life]] $\tau_{1/2} = \frac{\ln(2)}{\theta}$. This is the expected time for the gap to close by 50%.
6.  Initiate a fade trade (short a gap-up, long a gap-down) with a holding period informed by the calculated half-life.
7.  Exit the position based on the half-life-derived time target, or a pre-defined [[stop-loss]].

## Parameters
- **Lookback Period:** Window for estimating OU parameters (e.g., 30, 60 minutes).
- **Minimum Reversion Speed ($\theta_{min}$):** A threshold for $\theta$ to ensure the mean-reversion property is strong enough to trade.
- **Stationarity Test:** p-value threshold for a [[stationarity]] test like the [[Augmented Dickey-Fuller test|ADF test]] to confirm the process is mean-reverting.

## Risks
- **Model Risk:** Price action may not follow an [[Ornstein-Uhlenbeck process]]. The model assumes constant $\theta$ and $\mu$, which is not true in reality.
- **Parameter Instability:** The speed of reversion ($\theta$) can vary significantly, leading to incorrect half-life calculations and suboptimal exit timing.
- **News-Driven Gaps:** Fundamental news can invalidate the mean-reversion assumption, turning a fade into a loss as the price trends.

## Related
- [[mean_reversion_overnight_gap_fade_strategy]] — This document expands upon the core heuristic strategy by introducing a statistical modeling approach.
- [[stochastic calculus]] — Provides the mathematical framework for modeling price movements, including the Ornstein-Uhlenbeck process used here.
- [[Ornstein-Uhlenbeck process]] — The foundational stochastic process central to modeling the mean-reverting behavior of overnight gaps in this strategy.
- [[half-life]] — A key metric derived from the Ornstein-Uhlenbeck process, offering a model-based estimate for optimal holding times in this strategy.
- [[stationarity]] — A critical property of time series data assumed by the Ornstein-Uhlenbeck process, which needs to be confirmed for effective mean reversion.
- [[Augmented Dickey-Fuller test|ADF test]] — A statistical test used to verify the stationarity of the price series, a prerequisite for applying the mean-reverting model.
- [[vectorbt]] — A Python library that can be utilized for backtesting the performance and parameters of this statistically modeled strategy.
- [[volatility]] — A parameter ($\sigma$) within the Ornstein-Uhlenbeck process that quantifies the randomness of price movements and influences strategy risk.
- [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]] — The statistical modeling approach presented here aligns with advanced quantitative finance concepts discussed in this work.
- [[algorithmic_trading_with_moving_averages]] — Moving averages can serve as dynamic mean reversion levels ($\mu$) in the Ornstein-Uhlenbeck process, offering a flexible alternative to previous day's close.
- [[alpaca_api_algorithmic_order_types_bracket_orders_trailing_s]] — This document details algorithmic order types like bracket orders and trailing stops, essential for automated execution and risk management in this strategy.
- [[backtesting_a_100_percent_return_in_30_days_realistic_strate]] — This strategy, like any other, necessitates robust backtesting to validate its effectiveness, profitability, and parameter sensitivity.
- [[gap_trading_strategies_opening_range_breakout_intraday]] — This document explores other gap trading approaches, offering alternative perspectives on how gaps can be exploited, which could provide contextual understanding for the mean reversion strategy.
- [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] — The Kelly Criterion can be applied to this strategy to determine optimal position sizing, aiming to manage risk and maximize long-term account growth.
- [[mean_reversion_strategies_equities]] — This strategy represents a specific application of general mean reversion principles tailored for the equities market.
- [[order_flow_analysis_tape_reading_for_short_term_trades]] — Order flow analysis can complement this strategy by providing real-time insights into buying and selling pressure, aiding entry and exit decisions around the gap.
- [[pairs_trading_statistical_arbitrage_methods]] — Pairs trading often employs mean-reverting models conceptually similar to the Ornstein-Uhlenbeck process to identify and exploit temporary divergences.
- [[quantitative_risk_management_position_sizing]] — Effective risk management, including proper position sizing, is crucial for implementing and scaling this statistically modeled strategy.
- [[risk_of_ruin_calculations_for_aggressive_small_accounts]] — Understanding and calculating the risk of ruin is vital for managing capital when deploying potentially aggressive strategies, particularly for smaller trading accounts.
- [[scalping_high_volatility_stocks_with_tight_stop_losses]] — The short-term nature and emphasis on quick exits in this gap fade strategy share characteristics with scalping approaches, often necessitating tight stop losses.
- [[statistical_edge_in_short_term_mean_reversion_spy_qqq]] — This strategy specifically aims to quantify and exploit a statistical edge in short-term mean reversion, especially in highly liquid instruments like SPY and QQQ.
- [[vwap_anchored_to_earnings_events_strategy]] — Volume Weighted Average Price (VWAP) can be used as a dynamic mean reversion level ($\mu$) in the OU model, similar to its application in other strategies.
- [[vwap_and_volume_profile_day_trading_edge]] — VWAP and volume profile can enhance this strategy by providing additional context for market microstructure and potential support/resistance levels during the gap fade.

## Sources
- Chiu, C. C. (2014). *An Introduction to the Ornstein-Uhlenbeck Process*.
- Stübinger, J., & Schneider, A. (2019). *Statistical Arbitrage with Mean-Reverting Overnight Price Gaps*.

## Next Steps
- [ ] Backtest the statistical significance of the estimated $\theta$ parameter, leveraging insights from [[backtesting_a_100_percent_return_in_30_days_realistic_strate]].
- [ ] Explore using the [[Kalman Filter]] for dynamic estimation of OU parameters.
- [ ] Investigate the relationship between [[VIX]] levels and the speed of reversion $\theta$.
- [ ] Test the strategy on different asset classes, such as forex or futures.
- [ ] Implement a [[stationarity]] test (e.g., [[ADF test]]) as a filter before initiating a trade. # edited by gemini
```