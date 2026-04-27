```markdown
# Sharpe Ratio
## Key Insight
The [[Sharpe Ratio]] measures the [[risk-adjusted return]] of an investment or strategy. It quantifies the excess return (over the [[risk-free rate]]) per unit of [[volatility]] or total [[risk]], providing a standardized way to compare performance. A higher Sharpe Ratio indicates better performance for the amount of risk taken.

## The Math
The ex-ante Sharpe Ratio ($S_a$) is calculated as:
$S_a = \frac{E[R_a - R_b]}{\sigma_a} = \frac{E[R_a - R_b]}{\sqrt{Var[R_a - R_b]}}$
Where:
- $R_a$ is the asset or strategy return.
- $R_b$ is the [[risk-free rate]] of return.
- $E[R_a - R_b]$ is the expected value of the excess of the asset return over the risk-free return.
- $\sigma_a$ is the standard deviation of the asset's excess return (a measure of its [[volatility]]).

For historical data (ex-post), the formula uses realized returns.

## Strategy Logic
1.  Define a calculation period and frequency (e.g., daily returns over the past year).
2.  Gather the series of returns for the strategy ($R_a$) and the [[risk-free rate]] ($R_b$).
3.  Calculate the series of excess returns: $R_{excess} = R_a - R_b$.
4.  Compute the average of the excess returns, $\bar{R}_{excess}$.
5.  Compute the standard deviation of the excess returns, $\sigma_{excess}$.
6.  The Sharpe Ratio is $\frac{\bar{R}_{excess}}{\sigma_{excess}}$.
7.  To compare strategies, annualize the ratio. For daily data, this is often done by multiplying the calculated ratio by $\sqrt{252}$ (the approximate number of trading days in a year).

## Parameters
- **Asset/Strategy Returns**: The series of returns being evaluated. Must be accurately measured.
- **Risk-Free Rate**: The return of a theoretically risk-free asset. The choice of this rate (e.g., 3-month T-bill, SOFR) can significantly affect the result.
- **Time Period**: The frequency of returns (daily, weekly, monthly) and the total lookback period used for calculation.

## Risks
- **Assumes Normality**: The ratio is most effective for return distributions that are close to normal. It can be misleading for strategies with significant [[skewness]] or [[kurtosis]] (i.e., [[fat tails]] and assymetric risk).
- **Underestimates Tail Risk**: Because it uses standard deviation, it may not properly account for the risk of rare, extreme negative events.
- **Ignores Drawdowns**: The metric does not provide information about the magnitude or duration of potential losses ([[drawdown]]). A strategy can have a high Sharpe Ratio but still suffer from severe drawdowns. See [[Calmar Ratio]].
- **Sensitive to Time Period**: Can be "gamed" by selecting a favorable lookback period or by changing the measurement interval.

## Related
- [[quantitative_risk_management_position_sizing]] — The Sharpe Ratio is a key metric in evaluating the effectiveness of position sizing strategies, as it directly incorporates risk. # edited by gemini
- [[risk_of_ruin_calculations_for_aggressive_small_accounts]] — Understanding risk-adjusted returns, as measured by the Sharpe Ratio, is crucial when calculating the risk of ruin, especially for aggressive trading approaches. # edited by gemini
- [[volatility_breakout_strategies]] — Strategies like volatility breakout often entail significant price fluctuations, making the Sharpe Ratio essential for assessing their risk-adjusted performance. # edited by gemini
- [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] — The Kelly Criterion aims to optimize portfolio growth by considering risk and return, concepts central to evaluating performance with the Sharpe Ratio. # edited by gemini
- [[_cat_sizing_risk]] — This category covers methods and principles for managing risk and sizing positions, directly relating to the risk component and evaluation of the Sharpe Ratio. # edited by gemini
- [[_cat_volatility_options]] — Volatility, a core component of the Sharpe Ratio calculation, is a central theme in options trading and related strategies. # edited by gemini
- [[momentum_trading_strategies_for_small_accounts]] — The Sharpe Ratio is frequently used to compare the risk-adjusted returns of different momentum trading strategies. # edited by gemini
- [[mean_reversion_strategies_equities]] — Evaluating mean reversion strategies benefits from the Sharpe Ratio to understand their performance relative to the risk taken. # edited by gemini
- [[scalping_high_volatility_stocks_with_tight_stop_losses]] — For high-frequency, high-volatility strategies like scalping, the Sharpe Ratio provides a standardized measure of efficiency and risk-adjusted return. # edited by gemini
- [[highest_sharpe_ratio_strategies_for_accounts_under_1000_doll]] — This topic explores strategies specifically designed to achieve a high Sharpe Ratio, which is the primary metric discussed here. # edited by gemini
- [[compounding_daily_returns_math_behind_doubling_a_small_accou]] — While focusing on raw returns, understanding compounding returns is foundational for appreciating how the Sharpe Ratio adjusts these returns for associated risk. # edited by gemini
- [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]] — This resource likely delves into advanced quantitative techniques, including more sophisticated risk metrics and portfolio optimization methods that build upon or address limitations of the Sharpe Ratio. # edited by gemini
- [[backtesting_a_100_percent_return_in_30_days_realistic_strate]] — The Sharpe Ratio is a critical metric used in backtesting strategies to assess their historical risk-adjusted performance. # edited by gemini

## Sources
- "The Sharpe Ratio" by William F. Sharpe (1994), *The Journal of Portfolio Management*.

## Next Steps
- [ ] Compare the [[Sharpe Ratio]] of [[momentum_trading_strategies_for_small_accounts]] vs. [[mean_reversion_strategies_equities]] to identify which strategy offers better risk-adjusted returns. # edited by gemini
- [ ] Implement a rolling Sharpe Ratio calculation in Python to analyze how a strategy's risk-adjusted performance changes over time, potentially leveraging concepts from [[algorithmic_trading_with_moving_averages]]. # edited by gemini
- [ ] Explore the impact of using different [[risk-free rate]] benchmarks on the final ratio, considering resources like `_resources.md` for economic data sources. # edited by gemini
- [ ] Research modifications to the Sharpe Ratio for non-normal returns, such as the Cornish-Fisher modification, potentially looking into advanced topics found in `advances_in_financial_machine_learning_by_marcos_lopez_de_pr.md`. # edited by gemini
- [ ] Backtest a strategy that aims to optimize its [[Sharpe Ratio]], possibly using insights from `backtesting_a_100_percent_return_in_30_days_realistic_strate.md`. # edited by gemini
```