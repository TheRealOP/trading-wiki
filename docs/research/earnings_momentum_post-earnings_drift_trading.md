```markdown
---
topic: "earnings momentum post-earnings drift trading"
date: 2026-04-07
model: Pro
tags: [agent/research, quant/momentum, macro/earnings]
---

# [[Post-Earnings Announcement Drift (PEAD)]]
## Key Insight
[[Post-Earnings Announcement Drift (PEAD)]] is a market anomaly where stock prices continue to drift in the direction of an earnings surprise for weeks or months after the announcement. This contradicts the [[Efficient Market Hypothesis]] and is often attributed to investor [[underreaction]] to the new information contained in earnings reports. This creates an opportunity for [[quantitative strategies]] that systematically trade on this persistent [[momentum]].

## The Math
The core of many [[PEAD]] strategies is quantifying the "earnings surprise." The most common metric is [[Standardized Unexpected Earnings (SUE)]].

The SUE for a quarter $q$ is calculated as:
$SUE_q = \frac{EQ_q - E[EQ_q]}{\sigma(EQ_q - E[EQ_q])}$

Where:
- $EQ_q$: Actual earnings per share for quarter $q$.
- $E[EQ_q]$: Expected (forecasted) earnings per share for quarter $q$. This can be from analyst consensus or a time-series model like ARIMA on past earnings.
- $\sigma(\dots)$: The standard deviation of the earnings surprise, calculated over a historical period (e.g., the prior 8 quarters).

A high positive [[SUE]] indicates a significant positive earnings surprise, while a large negative [[SUE]] signals a major miss.

## Strategy Logic
A classic [[PEAD]] strategy is a long-short portfolio based on [[SUE]] values.
1. At the end of each month/quarter, collect earnings announcement data for all stocks in the universe.
2. For each stock that announced earnings in the period, calculate its [[SUE]].
3. Rank all stocks by their [[SUE]] value.
4. Form quintiles. Buy the top quintile (highest [[SUE]]) and short-sell the bottom quintile (lowest [[SUE]]).
5. Hold the portfolio for a set period (e.g., 3-6 months) and rebalance.

## Parameters
*   **Surprise Metric:** [[Standardized Unexpected Earnings (SUE)]], Cumulative Abnormal Return ([[CAR]]) around the announcement.
*   **Universe:** e.g., Russell 1000. The effect is often stronger in [[small-cap]] stocks.
*   **Holding Period:** Typically 1 to 6 months.
*   **Rebalancing:** Monthly or Quarterly.
*   **Ranking:** Quintiles or Deciles.

## Risks
*   **[[Transaction Costs]]**: High turnover and trading frictions can erode profits, especially for the short leg.
*   **Anomaly Decay**: As more capital attempts to exploit [[PEAD]], its profitability may decline over time.
*   **[[Market Microstructure]]**: Impact of bid-ask spreads, especially for less liquid [[small-cap]] stocks.
*   **Short Squeeze**: The short side of the portfolio is vulnerable to [[short squeezes]].

## Sources
- Ball and Brown (1968), "An Empirical Evaluation of Accounting Income Numbers"
- Bernard and Thomas (1889), "Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium?"
- Chan, Jegadeesh, and Lakonishok (1996), "Momentum Strategies"

## Related
- [[momentum_trading_strategies_for_small_accounts]] — This file describes the broad category of momentum strategies, for which PEAD is a specific, fundamentals-driven example. # edited by gemini
- [[mean_reversion_strategies_equities]] — Represents a contrasting quant philosophy; PEAD bets on trend continuation post-earnings, while mean reversion bets on reversals from extremes. # edited by gemini
- [[quantitative_risk_management_position_sizing]] — Provides the essential framework for determining how much capital to allocate to a systematic PEAD strategy. # edited by gemini
- [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] — Offers a specific mathematical model for position sizing that can be applied to trades based on SUE scores to maximize long-term growth. # edited by gemini
- [[alpaca_api_algorithmic_order_types_bracket_orders_trailing_s]] — Details the practical execution mechanics, such as using bracket or trailing stop orders, relevant for implementing a PEAD portfolio. # edited by gemini
- [[combining_trend_following_with_volatility_filters_for_max_re]] — Introduces risk management techniques like volatility filters that can be applied to a PEAD strategy to improve its risk-adjusted returns. # edited by gemini
- [[risk_of_ruin_calculations_for_aggressive_small_accounts]] — Provides methods to assess the probability of capital loss, which is crucial for managing the inherent risks of aggressive PEAD strategies. # edited by gemini
- [[leveraged_etf_momentum_rotation_tqqq_soxl_weekly_rebalance]] — This file presents another application of momentum principles, but focused on different assets and rebalancing periods, offering a comparative context for PEAD. # edited by gemini
- [[sector_rotation_strategy_using_relative_strength]] — Describes a momentum strategy at a broader market level, complementing PEAD's stock-specific approach by illustrating momentum principles across different scales. # edited by gemini
- [[mean_reversion_overnight_gap_fade_strategy]] — This specific mean reversion strategy provides a direct counterpoint for performance comparison against a PEAD momentum strategy, especially around earnings events. # edited by gemini

## Next Steps
- [ ] Backtest a PEAD strategy, modeling realistic entries and exits using principles from [[backtesting_a_100_percent_return_in_30_days_realistic_strate]] and order types from [[alpaca_api_algorithmic_order_types_bracket_orders_trailing_s]]. # edited by gemini
- [ ] Determine optimal trade size for a PEAD strategy by applying the formula from [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] in conjunction with risk assessments from [[risk_of_ruin_calculations_for_aggressive_small_accounts]]. # edited by gemini
- [ ] Investigate adding a volatility filter to the screening process, as described in [[combining_trend_following_with_volatility_filters_for_max_re]], to avoid high-surprise but overly-risky stocks. # edited by gemini
- [ ] Compare the profitability of this momentum strategy against a [[mean_reversion_overnight_gap_fade_strategy]] that trades around the same earnings events. # edited by gemini
- [ ] Analyze the text of earnings call transcripts with NLP to quantify management sentiment as a supplemental factor to [[SUE]], potentially building upon concepts from [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]]. # edited by gemini
- [ ] Research the [[Earnings Announcement Return (EAR)]] metric as an alternative to [[SUE]] for quantifying earnings surprise. # edited by gemini
```