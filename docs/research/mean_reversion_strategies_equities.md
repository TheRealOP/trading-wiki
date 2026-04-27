```markdown
---
topic: "mean reversion strategies equities"
date: 2026-04-07
tags: [agent/research, quant/mean-reversion]
---

# Mean Reversion Strategies: Equities

## Key Insight
[[Mean reversion]] is the theory that prices and returns eventually move back towards the mean or average. This tendency can be exploited through strategies that bet on the convergence of prices, such as [[Pairs Trading]], which has been shown to generate excess returns, although [[transaction costs]] can impact profitability.

## Strategy Logic
A common [[mean reversion]] strategy is [[Pairs Trading]]:
1.  Identify two [[S&P 500]] stocks with a historically high correlation (e.g., [[KO]] and [[PEP]]).
2.  Calculate the spread between their normalized prices.
3.  When the spread widens beyond a certain threshold (e.g., 2 standard deviations), short the outperforming stock and long the underperforming one.
4.  Close the position when the spread reverts to the mean.

## Parameters
*   **Lookback Period:** Window for calculating historical correlation and spread (e.g., 60 days).
*   **Entry/Exit Thresholds:** Standard deviation level to trigger trades (e.g., 2.0 for entry, 0.5 for exit).
*   **Universe:** The pool of stocks to select pairs from (e.g., [[S&P 500]], [[NASDAQ 100]]).

## Risks
*   **[[Drawdown]]**: The spread may continue to diverge, leading to significant losses.
*   **[[Position Sizing]]**: Incorrectly sized positions can lead to excessive risk.
*   **Regime Change**: The historical correlation between the pair may break down.

## Related
*   [[pairs_trading_statistical_arbitrage_methods]] — This document elaborates on the statistical arbitrage techniques that underpin pairs trading, a core mean reversion strategy. # edited by gemini
*   [[mean_reversion_overnight_gap_fade_strategy]] — Describes a specific mean reversion strategy focusing on overnight gaps, offering another application of the mean reversion principle. # edited by gemini
*   [[statistical_edge_in_short_term_mean_reversion_spy_qqq]] — Explores mean reversion specifically for short-term trading in major indices like SPY and QQQ, providing concrete examples. # edited by gemini
*   [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] — Provides a quantitative framework for optimal position sizing, directly addressing a risk factor of mean reversion strategies. # edited by gemini
*   [[quantitative_risk_management_position_sizing]] — Offers broader concepts and methods for managing the size of trading positions to control risk, crucial for mean reversion strategies. # edited by gemini
*   [[risk_of_ruin_calculations_for_aggressive_small_accounts]] — This article discusses calculations related to risk of ruin, directly tied to managing drawdown and overall risk in any trading strategy. # edited by gemini
*   [[algorithmic_trading_with_moving_averages]] — Provides foundational knowledge on moving averages, which can be used as filters or components in mean reversion entry/exit signals. # edited by gemini
*   [[high_probability_setups_combining_multiple_indicators_rsi_ma]] — Demonstrates how RSI and moving averages can be combined for trade setups, relevant for refining mean reversion signals. # edited by gemini
*   [[Bollinger Bands]] # edited by gemini
*   [[Ornstein-Uhlenbeck Process]] # edited by gemini
*   [[Volatility]] # edited by gemini

## Sources
*   "Pairs Trading: Quantitative Methods and Analysis" by Ganapathy Vidyamurthy
*   "Mean Reversion and Cointegration" by Alexander, Carol, and Dimitriu, O.

## Next Steps
- [ ] Explore [[cointegration]] as a more robust statistical test for pair selection, building upon the foundations of [[pairs_trading_statistical_arbitrage_methods]]. # edited by gemini
- [ ] Test the effectiveness of mean reversion strategies, potentially by reviewing concepts in `[[backtesting_a_100_percent_return_in_30_days_realistic_strate]]`. # edited by gemini
- [ ] Investigate the impact of [[transaction costs]] on strategy performance, considering practical execution aspects discussed in `[[alpaca_api_algorithmic_order_types_bracket_orders_trailing_s]]` for real-world trading. # edited by gemini
- [ ] Analyze the [[Sharpe Ratio]] and other performance metrics for different [[mean reversion]] strategies, relating to concepts in `[[highest_sharpe_ratio_strategies_for_accounts_under_1000_doll]]`. # edited by gemini
- [ ] Research the use of [[RSI]] and [[moving average]] as filters for mean reversion signals, leveraging insights from `[[high_probability_setups_combining_multiple_indicators_rsi_ma]]` and `[[algorithmic_trading_with_moving_averages]]`. # edited by gemini
- [ ] Consider [[position sizing]] strategies using frameworks like `[[kelly_criterion_optimal_bet_sizing_for_small_portfolios]]` to manage risk. # edited by gemini
```