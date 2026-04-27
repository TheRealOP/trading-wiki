---
topic: "earnings momentum post-earnings drift trading"
date: 2026-04-09
model: Pro
tags: [agent/research, quant/momentum, macro/earnings]
---

# PEAD: Surprise Metrics and Risk-Adjusted Implementation

## Key Insight
The profitability of a [[Post-Earnings Announcement Drift]] (PEAD) strategy is highly dependent on the metric used to quantify the "surprise" and the risk environment. Research indicates that using the initial market reaction, or [[Earnings Announcement Return]] (EAR), can be a more robust signal than traditional [[Standardized Unexpected Earnings]] (SUE). Furthermore, the anomaly's strength is concentrated in smaller, less-analyzed firms and can be moderated by filtering for [[liquidity]] and market [[volatility]] regimes.

## The Math
A common method for quantifying an earnings surprise is the Standardized Unexpected Earnings (SUE). It measures the surprise relative to its historical volatility.

$SUE_i = \frac{EPS_i - E[EPS_i]}{\sigma(EPS_i - E[EPS_i])}$

Where:
- $EPS_i$: Actual reported Earnings Per Share for company *i*.
- $E[EPS_i]$: Analyst consensus expected EPS for company *i*.
- $\sigma(\dots)$: The standard deviation of the earnings surprise ($EPS_i - E[EPS_i]$) over a trailing lookback period (e.g., 8 quarters).

A high positive SUE indicates a significant positive surprise, while a large negative SUE indicates a significant negative surprise.

## Strategy Logic
1.  **Universe Selection**: At the start of each period (e.g., monthly), filter for stocks that announced earnings in the prior period. Focus on a specific market cap range, such as the Russell 2000, where the PEAD anomaly is historically more pronounced.
2.  **Surprise Calculation**: For each stock, calculate the earnings surprise. A superior alternative to [[SUE]] can be the cumulative abnormal return around the announcement day (e.g., days `[-1, +1]`), also known as the [[Earnings Announcement Return]] (EAR). This captures the market's immediate interpretation of all information in the release, not just the EPS number.
3.  **Liquidity Filter**: Exclude stocks with very low average daily trading volume to mitigate [[transaction costs]] and slippage. For example, remove the bottom 20% of the universe by liquidity.
4.  **Portfolio Formation**: Sort the remaining stocks into deciles based on their EAR. Construct a dollar-neutral portfolio by going long the top decile (highest EAR) and shorting the bottom decile (lowest EAR).
5.  **Holding Period**: Hold the portfolio for a set period, typically 60-90 days, to capture the drift. The portfolio is rebalanced at the end of the holding period.
6.  **Risk Management**: Consider adding a market regime filter. For instance, pause new entries or reduce position sizes when a broad market stress indicator, like the VIX, is above a certain threshold (e.g., 30). This is a form of [[quantitative_risk_management_position_sizing]].

## Parameters
- **Surprise Metric**: [[Earnings Announcement Return]] (EAR) over `[-1, +1]` window.
- **Universe**: Small-to-mid cap stocks (e.g., Russell 2000).
- **Liquidity Filter**: Remove bottom 20% by 30-day Average Daily Volume.
- **Quantiles**: Long top decile, Short bottom decile.
- **Holding Period**: 60 trading days.
- **Rebalancing**: Monthly or quarterly.

## Risks
- **Anomaly Decay**: As more capital exploits the PEAD anomaly, its magnitude may decline, a sign of increasing [[market efficiency]].
- **Transaction Costs**: High turnover and the focus on less liquid small-caps can lead to significant trading costs that erode profits.
- **Factor Crowding**: The strategy has implicit exposure to [[momentum]] and [[size]] (small-cap) factors. A downturn in these factors will negatively impact the strategy.
- **Short Squeezes**: Shorting stocks with negative earnings surprises can be risky, as these can be volatile and prone to short squeezes.

## Related
- [[earnings_momentum_post-earnings_drift_trading]]
- [[earnings_momentum_post-earnings_drift_trading_2]]
- [[earnings_momentum_post-earnings_drift_trading_3]]
- [[momentum_trading_strategies_for_small_accounts]]
- [[quantitative_risk_management_position_sizing]]
- [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]]

## Sources
- Ball, Ray, and Philip Brown. "An empirical evaluation of accounting income numbers." Journal of accounting research (1968).
- DellaVigna, Stefano, and Joshua M. Pollet. "Investor attention and the pricing of earnings news." Journal of Financial Economics (2009).
- Frazzini, Andrea. "The post-earnings announcement drift: A behavioral puzzle, a rational anomaly, or both?." AQR Capital Management (2015).

## Next Steps
- [ ] Backtest the performance difference between [[SUE]] and [[EAR]] as the primary signal.
- [ ] Explore using machine learning models to predict the magnitude and duration of the drift based on earnings call transcripts and other alternative data.
- [ ] Investigate the impact of different market [[volatility]] regimes on the PEAD strategy's performance.
- [ ] Analyze the transaction costs and implement a cost-aware optimization for the strategy.
- [ ] Test the strategy on different international markets and asset classes.