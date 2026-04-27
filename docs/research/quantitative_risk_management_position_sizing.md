```markdown
---
topic: "quantitative risk management position sizing"
date: 2026-04-07
model: Pro
tags: [agent/research, metrics/drawdown]
---

# [[Position Sizing]] via [[Quantitative Risk Management]]

## Key Insight
[[Position sizing]] is not about predicting the future, but about managing [[risk]] and maximizing long-term [[compounding]]. The [[Kelly Criterion]] provides a mathematical framework for optimizing the fraction of capital to allocate to each trade, balancing the probability of success with the [[risk/reward ratio]]. However, pure [[Kelly Criterion]] can lead to extreme [[volatility]] and [[drawdown]], so practitioners often use a [[fractional Kelly]] approach.

## The Math
The core of the [[Kelly Criterion]] is to determine the optimal fraction `f*` of capital to risk.

Let:
- `p` = probability of a winning trade
- `q` = probability of a losing trade (`1 - p`)
- `b` = ratio of the average win to the average loss

The [[Kelly Criterion]] formula is:
$f^* = \frac{p \cdot b - q}{b} = p - \frac{q}{b}$

For a [[volatility]]-based approach, the position size can be determined by:

$PositionSize = \frac{AccountSize \times Risk\%}{StopLoss \times ATR Multiplier}$

where [[ATR]] is the [[Average True Range]].

## Strategy Logic
1.  Define the trading [[strategy]] and establish its historical performance to estimate `p` and `b`.
2.  Calculate the [[optimal f]] using the [[Kelly Criterion]] formula.
3.  Adjust `f*` downwards (e.g., to 50% or 25% of the calculated value) to create a [[fractional Kelly]] allocation to reduce [[risk of ruin]].
4.  For each trade, calculate the position size based on the chosen fraction of capital and the specific trade's [[stop-loss]].
5.  Continuously monitor and update the inputs `p` and `b` as market conditions change.

## Parameters
- **Win Probability (`p`):** The historical win rate of the [[strategy]].
- **Win/Loss Ratio (`b`):** The average gain of a winning trade divided by the average loss of a losing trade.
- **Kelly Fraction:** The percentage of the [[optimal f]] to use (e.g., 0.5 for half-Kelly).

## Risks
- **[[Overestimation of Win Probability]]**: A small overestimation of `p` can lead to a drastically oversized position and large [[drawdown]].
- **[[Black Swan Events]]**: The [[Kelly Criterion]] assumes a stable probability distribution, which may not hold during extreme market events.
- **[[Risk of Ruin]]**: Even with an edge, a series of losses can significantly impact capital if the position size is too large.

## Related
- [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] — This file provides a deeper dive into the Kelly Criterion, which is a fundamental component of position sizing. # edited by gemini
- [[risk_of_ruin_calculations_for_aggressive_small_accounts]] — Explores the calculation and implications of the risk of ruin, a critical consideration when determining position sizes. # edited by gemini
- [[algorithmic_trading_with_moving_averages]] — Represents a trading strategy that would benefit from proper position sizing techniques to manage risk effectively. # edited by gemini
- [[volatility_breakout_strategies]] — These strategies often involve higher risk and require careful position sizing, potentially using volatility-based methods like ATR. # edited by gemini
- [[vwap_and_volume_profile_day_trading_edge]] — A day trading strategy where precise position sizing is crucial for managing intraday risk and maximizing edge. # edited by gemini
- [[pairs_trading_statistical_arbitrage_methods]] — Statistical arbitrage often involves multiple concurrent positions, necessitating sophisticated position sizing to manage overall portfolio risk. # edited by gemini
- [[scalping_high_volatility_stocks_with_tight_stop_losses]] — A high-frequency strategy where position sizing based on tight stop-losses and volatility is paramount for risk control. # edited by gemini
- [[momentum_trading_strategies_for_small_accounts]] — These strategies for smaller accounts emphasize the importance of carefully managed position sizes to mitigate the risk of ruin. # edited by gemini
- [[compounding_daily_returns_math_behind_doubling_a_small_accou]] — Proper position sizing is essential for achieving sustainable compounding of returns while managing risk. # edited by gemini
- [[Optimal f]]
- [[Value at Risk (VaR)]]
- [[Conditional Value at Risk (CVaR)]]
- [[Sharpe Ratio]]
- [[Information Ratio]]

## Sources
- "A New Interpretation of Information Rate" by J. L. Kelly, Jr.
- "The Mathematics of Money Management" by Ralph Vince

## Next Steps
- [ ] Explore the impact of using [[fractional Kelly]] on [[drawdown]] and [[Sharpe Ratio]]. # edited by gemini
- [ ] Test a [[volatility]]-based [[position sizing]] model in the context of strategies like `[[volatility_breakout_strategies]]`. # edited by gemini
- [ ] Investigate how [[position sizing]] impacts [[portfolio]]-level [[risk]] in multi-asset strategies, such as `[[pairs_trading_statistical_arbitrage_methods]]` or `[[sector_rotation_strategy_using_relative_strength]]`. # edited by gemini
- [ ] Research alternative [[portfolio optimization]] techniques beyond the [[Kelly Criterion]]. # edited by gemini
```