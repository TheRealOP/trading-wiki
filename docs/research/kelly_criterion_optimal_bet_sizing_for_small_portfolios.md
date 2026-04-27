```markdown
---
topic: "Kelly criterion optimal bet sizing for small portfolios"
date: 2026-04-07
model: Pro
tags: [agent/research, metrics/drawdown]
---

# Kelly Criterion for Optimal Bet Sizing

## Key Insight
The [[Kelly Criterion]] provides a mathematical framework for determining the optimal fraction of a [[portfolio]] to allocate to a single trade, maximizing long-term geometric growth. It balances the probability of winning with the win/loss ratio, preventing [[risk of ruin]] while aiming for aggressive [[compounding]]. For [[small accounts]], this can be a powerful tool for rapid growth, but it requires precise parameter estimation.

## The Math
The core formula calculates the percentage of capital to allocate:

$ K\% = W - \frac{(1 - W)}{R} $

Where:
- $K\%$ = The [[Kelly Criterion]] percentage of the portfolio to risk on a trade.
- $W$ = The historical [[win rate]] of the trading strategy.
- $R$ = The historical average [[win/loss ratio]] (average gain of winning trades / average loss of losing trades).

A simplified version is often expressed as:
$ K\% = \frac{(b \cdot p) - q}{b} $
- $p$ = probability of winning
- $q$ = probability of losing ($1-p$)
- $b$ = odds (e.g., if you risk $1 to win $2, b=2)

## Strategy Logic
1.  Gather historical data for a specific [[trading strategy]] over a large number of trades.
2.  Calculate the [[win rate]] ($W$) by dividing the number of winning trades by the total number of trades.
3.  Calculate the average gain for winning trades and the average loss for losing trades to determine the [[win/loss ratio]] ($R$).
4.  Input $W$ and $R$ into the [[Kelly Criterion]] formula to find the optimal fraction ($K\%$) of capital to allocate.
5.  Systematically apply this position size to future trades.
6.  Periodically re-evaluate and update $W$ and $R$ to adapt to changing market conditions.

## Parameters
-   **Win Probability (W):** Must be a stable, statistically significant value derived from extensive [[backtesting]] or a long track record.
-   **Win/Loss Ratio (R):** Highly sensitive to [[outliers]] and changes in market [[volatility]].
-   **Fraction:** Many quants use a [[fractional Kelly]] (e.g., 0.5 * K% or 0.25 * K%) to reduce [[volatility]] and mitigate the impact of parameter estimation errors.

## Risks
-   **Parameter Estimation Error:** The formula is extremely sensitive to the inputs. Overestimating the [[win rate]] ($W$) or [[win/loss ratio]] ($R$) can lead to over-betting, catastrophic losses, and an increased [[risk of ruin]].
-   **Non-Stationarity:** Historical data does not guarantee future results. The underlying probability distribution of returns can change, making Kelly-derived sizes inappropriate.
-   **Volatility Drag:** Even with perfect parameters, the full Kelly fraction can lead to severe [[drawdowns]] that are psychologically and financially difficult to endure.
-   **Liquidity Constraints:** For very [[small accounts]], allocating the precise Kelly fraction may not be possible due to minimum trade sizes.

## Related
- [[kelly_criterion_optimal_bet_sizing_for_small_portfolios_3]] — Kelly criterion optimal bet sizing for small portfolios
- [[kelly_criterion_optimal_bet_sizing_for_small_portfolios_2]] — Kelly criterion optimal bet sizing for small portfolios
- [[backtest_earnings_momentum_post-earnings_drift_trading]] — Backtest: earnings momentum post-earnings drift trading

## Sources
-   "A New Interpretation of Information Rate" - J.L. Kelly, Jr. (1956)
-   "Fortune's Formula: The Untold Story of the Scientific Betting System That Beat Wall Street and Las Vegas" - William Poundstone
-   "The Kelly Capital Growth Investment Criterion" - Thorp, E. O.

## Next Steps
-   [ ] Compare the performance of a [[momentum_trading_strategies_for_small_accounts]] using fixed-fractional sizing versus Kelly Criterion sizing in a [[backtesting]] environment. # edited by gemini
-   [ ] Implement a [[backtest]] of a strategy like the one discussed in [[backtesting_a_100_percent_return_in_30_days_realistic_strate]] to derive the [[win rate]] and [[win/loss ratio]] inputs for the Kelly formula. # edited by gemini
-   [ ] Test the robustness of the Kelly Criterion by conducting a [[Monte Carlo simulation]] that introduces noise into the [[win rate]] and [[win/loss ratio]] parameters, as explored in general [[quantitative_risk_management_position_sizing]]. # edited by gemini
-   [ ] Investigate the impact of using a [[fractional Kelly]] (e.g., 50% or 25% of the calculated K%) on both [[drawdowns]] and overall geometric return, potentially linking to concepts in [[risk_of_ruin_calculations_for_aggressive_small_accounts]]. # edited by gemini
-   [ ] Explore how [[quantitative_risk_management_position_sizing]] frameworks integrate or contrast with the direct application of the Kelly Criterion, especially regarding practical implementation challenges. # edited by gemini
-   [ ] Analyze the effect of the Kelly Criterion on [[risk_of_ruin_calculations_for_aggressive_small_accounts]] when applied to strategies with varying levels of aggressiveness, using simulated trading scenarios. # edited by gemini
-   [ ] Apply the Kelly Criterion to optimize position sizing for a specific strategy like [[leveraged_etf_momentum_rotation_tqqq_soxl_weekly_rebalance]] and evaluate the impact on its long-term growth. # edited by gemini
-   [ ] Research methods for dynamically adjusting Kelly inputs ($W$ and $R$) to account for non-stationarity in market conditions, referencing concepts from [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]] for adaptive parameter estimation. # edited by gemini
```

## Related
- [[kelly_criterion_optimal_bet_sizing_for_small_portfolios_3]] — Kelly criterion optimal bet sizing for small portfolios
- [[kelly_criterion_optimal_bet_sizing_for_small_portfolios_2]] — Kelly criterion optimal bet sizing for small portfolios
- [[backtest_earnings_momentum_post-earnings_drift_trading]] — Backtest: earnings momentum post-earnings drift trading
