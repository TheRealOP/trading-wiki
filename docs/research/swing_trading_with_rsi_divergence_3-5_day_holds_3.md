---
topic: "swing trading with RSI divergence 3-5 day holds"
date: 2026-04-09
model: Flash
tags: [agent/research, quant/momentum]
---

I will read the existing knowledge files `knowledge/swing_trading_with_rsi_divergence_3-5_day_holds.md`, `knowledge/swing_trading_with_rsi_divergence_3-5_day_holds_2.md`, and `knowledge/backtest_swing_trading_with_rsi_divergence_3-5_day_hol.md` to understand the previous research and identify new angles to explore.
# Quantitative Enhancements & Multi-Timeframe Divergence

## Key Insight
Expanding beyond static [[RSI Divergence]] detection, this research delves into the **quantitative validation** of divergence patterns through statistical methods and the integration of **multi-timeframe analysis** for robust signal generation. It explores adaptive [[RSI]] parameterization and introduces advanced [[risk management]] metrics to refine the 3-5 day [[swing trading]] hold strategy, aiming to reduce [[false signals]] and improve [[risk-adjusted returns]].

## The Math
The [[Relative Strength Index]] (RSI) is calculated as:
$RSI = 100 - \frac{100}{1 + RS}$
where $RS = \frac{\text{EMA of Average Gain}}{\text{EMA of Average Loss}}$ over $N$ periods, often using an [[Exponential Moving Average]] for smoothing.

**Quantitative Divergence Metric:**
To move beyond subjective visual identification, a divergence score can be computed. For a potential bullish divergence (price making a lower low, RSI making a higher low), we identify the two swing lows on price ($P_1, P_2$) and the corresponding RSI values ($R_1, R_2$). A divergence strength ($D$) can be defined as:
$D = \frac{(P_1 - P_2)}{|P_1|} \cdot \frac{(R_2 - R_1)}{|R_1|}$
A positive $D$ indicates a bullish divergence, negative for bearish. Thresholds for $D$ can be set based on historical backtesting to filter weak signals.

**Statistical Significance of Divergence:**
The null hypothesis ($H_0$) is that price and [[RSI]] move in the same direction. A [[t-test]] can be applied to the difference in slopes or a [[Pearson correlation coefficient]] ($\rho$) can be calculated between price change and [[RSI]] change over the divergence period. For a valid divergence, one would expect a low (e.g., negative for bullish divergence) and statistically significant $\rho$ over the identified peaks/troughs.

**Adaptive RSI Period:**
Instead of a fixed $N=14$, the [[RSI]] period can be made adaptive based on [[volatility]]. For example, using [[Average True Range]] (ATR) to adjust $N$:
$N_{adaptive} = \text{round}(\frac{\text{Constant}}{\text{ATR}_{normalized}})$
where `Constant` is an optimized value and `ATR_normalized` scales [[ATR]] to a range (e.g., 0-1). Higher [[volatility]] might lead to a shorter [[RSI]] period, increasing sensitivity.

## Strategy Logic
1.  **Multi-Timeframe Divergence Identification:**
    *   Identify potential [[RSI Divergence]] (Regular or Hidden) on a higher [[timeframe]] (e.g., [[Weekly Chart]] or [[Daily Chart]]) to establish the macro trend or reversal context.
    *   Confirm the divergence on a lower [[timeframe]] (e.g., [[4-hour chart]] or [[1-hour chart]]) for precise entry signals.
2.  **Quantitative Divergence Validation:** Apply a predefined quantitative metric ($D$) and a statistical significance test (e.g., [[t-test]] or [[correlation]]) to filter only statistically robust divergence signals.
3.  **Entry Confirmation with [[Volume]] and [[Price Action]]**:
    *   For bullish signals, look for increasing [[volume]] on buying [[candlesticks]] or a break above a short-term [[volume-weighted average price]] ([[VWAP]]).
    *   For bearish signals, look for increasing [[volume]] on selling [[candlesticks]] or a break below a short-term [[VWAP]].
4.  **Adaptive Stop-Loss and Take-Profit:** Adjust [[stop-loss]] and [[take-profit]] levels dynamically using [[ATR]] multiples, ensuring they adapt to current [[market volatility]].
5.  **Holding Period and Exit Management**: Maintain the 3-5 day [[holding period]] but allow for early exits if momentum significantly shifts or an alternative confirmed [[RSI Divergence]] signal appears in the opposite direction. Incorporate a [[trailing stop]] to lock in [[profits]].

## Parameters
*   **Adaptive RSI Period Logic:** Parameters for `Constant` in the adaptive [[RSI]] calculation.
*   **Divergence Lookback:** Max bars for identifying swing pivots (e.g., 20-50 bars).
*   **Quantitative Thresholds:** Minimum $D$ score, significance level for statistical tests (e.g., p-value < 0.05).
*   **Multi-Timeframe Ratios:** Define the ratio between higher and lower [[timeframes]] (e.g., 1:4 or 1:6).
*   **ATR Multiplier:** For dynamic [[stop-loss]] and [[take-profit]] (e.g., 1.5x [[ATR]] for stop, 3x [[ATR]] for profit).

## Risks
*   **Model Risk:** Over-reliance on quantitative models may lead to [[curve fitting]] if not validated on out-of-sample data.
*   **Complexity:** Increased complexity can introduce more potential points of failure and make debugging harder.
*   **Lagging Indicators:** Even with enhancements, [[RSI]] is a lagging indicator and can still generate [[false signals]] in fast-moving markets.
*   **[[Market Regime]] Sensitivity:** Adaptive parameters still need to be robust across varying [[market conditions]].

## Related
*   [[Mean Reversion Strategies Equities]]
*   [[Momentum Trading Strategies for Small Accounts]]
*   [[high_probability_setups_combining_multiple_indicators_rsi_ma]]
*   [[quantitative_risk_management_position_sizing]]
*   [[statistical_edge_in_short_term_mean_reversion_spy_qqq]]
*   [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]]
*   [[volatility_breakout_strategies]]
*   [[vwap_and_volume_profile_day_trading_edge]]
*   [[backtest_swing_trading_with_rsi_divergence_3-5_day_hol]]

## Sources
*   "Technical Analysis of the Financial Markets" by John J. Murphy.
*   "Quantitative Trading: How to Build Your Own Algorithmic Trading Business" by Dr. Ernie Chan.
*   "Evidence of a new trading rule: The RSI-divergence rule" by Harris, C.
*   "Algorithmic Trading & DMA: An Introduction to Direct Market Access Strategies" by H. James Poland.

## Next Steps
- [ ] Implement an algorithm for calculating the **Quantitative Divergence Metric** and integrating statistical tests.
- [ ] Research and implement methods for **Adaptive RSI Period** calculation based on [[volatility]] (e.g., using [[ATR]] or standard deviation).
- [ ] Backtest the **multi-timeframe divergence strategy** with entry confirmation using [[VWAP]] and [[volume]] on major [[ETFs]] like [[SPY]] and [[QQQ]].
- [ ] Evaluate strategy performance using advanced metrics: [[Sortino Ratio]], [[Calmar Ratio]], and [[Ulcer Index]], in addition to [[Sharpe Ratio]].
- [ ] Explore the potential of **Machine Learning** (e.g., [[LSTM]] networks) for predicting divergence validity or future price movements post-divergence.
# edited by gemini