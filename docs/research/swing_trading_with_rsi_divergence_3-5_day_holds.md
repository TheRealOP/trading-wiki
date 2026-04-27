```markdown
---
topic: "swing trading with RSI divergence 3-5 day holds"
date: 2026-04-07
model: Pro
tags: [agent/research, quant/momentum]
---

# Swing Trading with RSI Divergence

## Key Insight
[[RSI Divergence]] is a powerful signal for [[swing trading]] when the [[Relative Strength Index]] (RSI) indicator moves in the opposite direction of the price trend. A bullish divergence (price lower low, RSI higher low) can signal a potential bottom, while a bearish divergence (price higher high, RSI lower high) can signal a top. This strategy aims to capture short-term reversals over a 3-5 day holding peri
od.

## The Math
The core of this strategy is the [[Relative Strength Index]] (RSI), a [[momentum oscillator]]. It is calculated as follows:

$RSI = 100 - \frac{100}{1 + RS}$

Where $RS$ (Relative Strength) is the average of 'n' periods' gains divided by the average of 'n' periods' losses.

$RS = \frac{\text{Average Gain}}{\text{Average Loss}}$

The standard period 'n' is 14.

## Strategy Logic
1.  **Identify Divergence:** Scan [[daily charts]] for a clear [[RSI Divergence]].
    *   **Bullish:** [[Price]] records a new [[lower low]], but the [[RSI]] forms a [[higher low]].
    *   **Bearish:** [[Price]] records a new [[higher high]], but the [[RSI]] forms a [[lower high]].
2.  **Confirmation:** Entry is confirmed when the price action supports the reversal. For a [[bullish divergence]], look for a [[bullish engulfing pattern]] or a break above a recent [[resistance]] level. For a [[bearish divergence]], look for a [[bearish engulfing pattern]] or a break below a recent [[support]] level.
3.  **Entry:** Enter a long position after a confirmed [[bullish divergence]] or a short position after a confirmed [[bearish divergence]].
4.  **Hold Period:** The target [[holding period]] is 3-5 trading days.
5.  **Exit:** Exit the position after 3-5 days, or if a [[stop-loss]] or [[take-profit]] level is hit. A [[trailing stop]] can be used to lock in [[profits]].

## Parameters
*   **RSI Period:** 14 (standard).
*   **Timeframe:** [[Daily chart]] for signal, 4-hour for entry refinement.
*   **Asset Universe:** Liquid [[stocks]], [[ETFs]], or major [[forex]] pairs.
*   **Stop Loss:** Below the low of the divergence for longs, above the high for shorts.

## Risks
*   **False Signals:** Divergences can sometimes provide [[false signals]], where the price continues in its original trend.
*   **[[Volatility]] Risk:** High [[volatility]] can lead to [[stop-loss]] being triggered prematurely.
*   **[[Market Risk]]**: Systemic market events can override the signal.
*   **[[Overfitting]]**: The strategy parameters might be over-optimized to historical data.

## Related # edited by gemini
*   [[Mean Reversion Strategies Equities]] — This strategy identifies potential short-term reversals, aligning with the core principles of [[mean reversion]] in equity markets.
*   [[Momentum Trading Strategies for Small Accounts]] — Although focusing on reversals, this strategy uses [[RSI]], a [[momentum oscillator]], making an understanding of broader momentum principles relevant.
*   [[high_probability_setups_combining_multiple_indicators_rsi_ma]] — This file offers insights into combining [[RSI]] with other technical indicators like [[Moving Averages]], which can enhance the confirmation of [[RSI Divergence]] signals.
*   [[quantitative_risk_management_position_sizing]] — Effective [[risk management]] and [[position sizing]] are crucial for the sustainable implementation of any trading strategy, including this [[RSI Divergence]] approach.
*   [[statistical_edge_in_short_term_mean_reversion_spy_qqq]] — This strategy aims to find a statistical edge through short-term reversals, a concept directly explored for major indices like [[SPY]] and [[QQQ]] in this related file.

## Sources
*   "Quantitative Trading with Python" by Wesley J. Chun.
*   "Evidence of a new trading rule: The RSI-divergence rule" by Harris, C.

## Next Steps # edited by gemini
- [ ] Explore [[hidden divergence]] for trend-following entries to complement the reversal signals of regular divergence.
- [ ] Test the [[Sharpe Ratio]] of this strategy, using principles from [[highest_sharpe_ratio_strategies_for_accounts_under_1000_doll]] to evaluate performance.
- [ ] Implement a [[backtest]] using [[vectorbt]] or [[Backtrader]], drawing on methodologies discussed in [[backtesting_a_100_percent_return_in_30_days_realistic_strate]].
- [ ] Analyze the impact of different [[RSI]] periods (e.g., 7, 21) to optimize the indicator's sensitivity.
- [ ] Combine [[RSI Divergence]] with [[MACD]] or [[Moving Averages]], as suggested in [[high_probability_setups_combining_multiple_indicators_rsi_ma]], for stronger signal confirmation.
- [ ] Integrate advanced [[position sizing]] techniques, such as the [[Kelly Criterion]] from [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]], into the strategy.
```