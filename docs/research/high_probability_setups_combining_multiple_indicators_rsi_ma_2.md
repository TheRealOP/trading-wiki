```markdown
---
topic: "high probability setups combining multiple indicators RSI MACD Bollinger"
date: 2026-04-07
model: Pro
tags: [agent/research, quant/momentum]
---

# Bollinger Band Squeeze with MACD/RSI Confirmation

## Key Insight
This strategy advances beyond simple indicator-crossing by using [[Bollinger Bands]] to first identify a volatility regime—specifically, a low-volatility [[Squeeze]]. The "squeeze" acts as a setup, indicating potential for a large price move. [[MACD]] and [[RSI]] are then used as confirmation filters to validate the direction of the subsequent [[volatility breakout]], improving the probability of a successful trade over using any single indicator in isolation.

## The Math
The core of the setup is the [[Bollinger Bandwidth]], a measure of [[volatility]].

1.  **Typical Price (TP):** $TP_t = \frac{High_t + Low_t + Close_t}{3}$
2.  **Bollinger Bands:**
    *   Middle Band (MB): $MB_t = SMA(TP, n)$
    *   Upper Band (UB): $UB_t = MB_t + m \times \sigma(TP, n)$
    *   Lower Band (LB): $LB_t = MB_t - m \times \sigma(TP, n)$
    *   Where $\sigma(TP, n)$ is the n-period standard deviation of Typical Price.
3.  **Bollinger Bandwidth (BBW):** This normalizes the bandwidth. A low value signals the squeeze.
    *   $BBW_t = \frac{UB_t - LB_t}{MB_t}$

## Strategy Logic
1.  **Setup (The Squeeze):** Identify a period where [[Bollinger Bandwidth]] ($BBW_t$) falls to a multi-period low (e.g., the lowest value in the last 120 periods). This signals extreme consolidation.
2.  **Breakout Trigger:** The first bar that closes outside of the [[Bollinger Bands]] after a squeeze is identified.
3.  **Confirmation (Long Entry):**
    *   Price closes above the Upper Bollinger Band.
    *   [[MACD]] Line is above the MACD Signal Line.
    *   [[RSI]] is greater than 50.
4.  **Confirmation (Short Entry):**
    *   Price closes below the Lower Bollinger Band.
    *   [[MACD]] Line is below the MACD Signal Line.
    *   [[RSI]] is less than 50.
5.  **Exit:** A potential exit is when the price touches the opposite Bollinger Band, or when the [[MACD]] line crosses back over its signal line.

## Parameters
-   **Bollinger Bands Period (n):** Typically 20.
-   **Standard Deviation Multiplier (m):** Typically 2.0.
-   **Squeeze Lookback Period:** Typically 120 to 252.
-   **RSI Period:** Typically 14.
-   **MACD Periods:** Typically (12, 26, 9).

## Risks
-   **[[Whipsaw]]:** A false breakout where price quickly reverses and re-enters the bands.
-   **Squeeze Failure:** The squeeze can resolve with a fizzle rather than a strong directional move.
-   **[[Parameter Overfitting]]:** The chosen parameters may be too specific to historical data. See [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]].

## Related
-   [[volatility_breakout_strategies]] — This strategy is a specific type of volatility breakout strategy, using the Bollinger Band Squeeze as the entry trigger.
-   [[momentum_trading_strategies_for_small_accounts]] — This strategy identifies momentum following a consolidation, making it relevant for understanding general momentum trading approaches.
-   [[quantitative_risk_management_position_sizing]] — Effective position sizing, as discussed in this document, is crucial for managing the risks associated with this strategy.
-   [[swing_trading_with_rsi_divergence_3-5_day_holds]] — RSI is a key indicator in both strategies, offering potential confluence for swing trade setups.
-   [[algorithmic_trading_with_moving_averages]] — Bollinger Bands and MACD, central to this strategy, heavily rely on moving averages in their calculation and application.
-   [[earnings_momentum_post-earnings_drift_trading]] — This strategy could be applied to stocks exhibiting post-earnings drift, using the squeeze for entry timing.
-   [[crypto_momentum_trading_btc_eth_4h_timeframe]] — The principles of this strategy, particularly momentum and volatility analysis, are applicable to cryptocurrency markets, as explored in this file.
-   [[mean_reversion_strategies_equities]] — While this is a breakout strategy, understanding mean reversion helps differentiate it from and potentially combine with other market regimes, as outlined in this document.
-   [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]] — This work provides advanced techniques relevant for mitigating issues like parameter overfitting, a risk associated with this strategy.
-   [[backtesting_a_100_percent_return_in_30_days_realistic_strate]] — Insights from backtesting methodologies described in this document can be applied to validate the effectiveness of the Bollinger Band Squeeze strategy.
-   [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] — The Kelly Criterion, detailed in this file, offers a robust framework for optimal bet sizing that can be integrated into the risk management of this strategy.
-   [[vwap_and_volume_profile_day_trading_edge]] — This document discusses volume profile analysis, which could provide additional confirmation for the volatility breakout identified by the Bollinger Band Squeeze.
-   [[order_flow_analysis_tape_reading_for_short_term_trades]] — Concepts from order flow analysis could be used to fine-tune entry and exit points during the volatility breakout phase of this strategy.
-   [[gap_trading_strategies_opening_range_breakout_intraday]] — This file discusses gap trading and opening range breakouts, which are related to volatility and could offer complementary entry ideas to the Bollinger Band Squeeze.
-   [[scalping_high_volatility_stocks_with_tight_stop_losses]] — The short-term, high-volatility nature of scalping strategies discussed in this document aligns with the rapid price movements expected after a Bollinger Band Squeeze breakout.
-   [[sector_rotation_strategy_using_relative_strength]] — Incorporating concepts of relative strength from this document could help identify strong sectors or stocks likely to experience significant breakouts after a squeeze.
-   [[statistical_edge_in_short_term_mean_reversion_spy_qqq]] — The principles of identifying statistical edges, as discussed here, could be applied to further validate the breakout probability of the Bollinger Band Squeeze strategy.
-   [[combining_trend_following_with_volatility_filters_for_max_re]] — This document explores combining trend-following with volatility filters, a concept highly relevant to the Bollinger Band Squeeze which identifies trends after low volatility.
# edited by gemini

## Sources
-   "Bollinger on Bollinger Bands" by John Bollinger.
-   Academic studies on combining [[momentum]] and [[volatility]] indicators.

## Next Steps
-   [ ] Backtest the impact of different squeeze lookback periods on [[Sharpe Ratio]] and compare with results from [[backtesting_a_100_percent_return_in_30_days_realistic_strate]].
-   [ ] Explore adding a [[volume]] filter to the breakout confirmation logic, potentially linking to concepts in [[vwap_and_volume_profile_day_trading_edge]].
-   [ ] Test this strategy on various asset classes, such as [[crypto_momentum_trading_btc_eth_4h_timeframe]] and different equities as explored in [[mean_reversion_strategies_equities]].
-   [ ] Implement this strategy in Python for robust [[backtesting]].
-   [ ] Analyze optimal bet sizing for this strategy using concepts from [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]].
```