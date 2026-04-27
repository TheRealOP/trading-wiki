```markdown
---
topic: "earnings momentum post-earnings drift trading"
date: 2026-04-07
model: Pro
tags: [agent/research, quant/momentum, macro/earnings]
---

# PEAD: Factor Interactions & Advanced Metrics

## Key Insight
The [[Post-Earnings Announcement Drift (PEAD)]] anomaly's profitability can be enhanced by considering its interaction with other risk factors and by employing more sophisticated measures of earnings surprise. The strength of the drift is not uniform across all stocks and is often stronger in stocks with high [[information asymmetry]] and low investor attention, which are typically [[small-cap]] stocks. Combining [[PEAD]] with factors like [[value]] and [[momentum]] can create more robust portfolios.

## The Math
Beyond the classic [[Standardized Unexpected Earnings (SUE)]], other metrics can capture the earnings surprise and subsequent drift more effectively.

1.  **Cumulative Abnormal Return (CAR)**: The market's immediate reaction is a powerful predictor of future drift.
    $CAR_i = \sum_{t=-1}^{t=+1} (R_{it} - R_{mt})$
    Where $R_{it}$ is the return of stock $i$ on day $t$ (relative to the announcement) and $R_{mt}$ is the market return. A portfolio long high CAR stocks and short low CAR stocks often shows significant drift.

2.  **Analyst Forecast Dispersion**: High dispersion in analyst forecasts before an announcement is linked to a stronger drift, as it signals higher uncertainty.
    $\sigma_{forecasts} = \text{std. dev. of analyst EPS forecasts}$

## Strategy Logic
A more refined [[PEAD]] strategy incorporates additional factors.
1.  **Universe Selection**: Focus on a universe where [[PEAD]] is historically strongest, e.g., Russell 2000 stocks, excluding stocks with very high institutional ownership or analyst coverage.
2.  **Surprise Metric**: Calculate both [[SUE]] and announcement-period [[CAR]] for each stock. Create a composite score by ranking and combining them.
3.  **Factor Overlay**: Filter the long/short candidates based on other factors. For longs, favor stocks that also have attractive [[value]] (e.g., high Book-to-Market) or existing price [[momentum]] characteristics. For shorts, do the opposite.
4.  **Portfolio Construction**: Create a market-neutral portfolio, long the top decile and short the bottom decile of the composite rank. Use [[quantitative_risk_management_position_sizing]] to weigh positions.
5.  **Holding Period**: Hold positions for 3-6 months, with staggered, overlapping portfolios to reduce timing luck.

## Parameters
*   **Surprise Metrics**: [[SUE]], [[CAR]], Analyst Dispersion.
*   **Factor Filters**: Book-to-Market Ratio, 12-month [[momentum]], [[Analyst Coverage]].
*   **Universe**: [[Small-cap]] stocks (e.g., Russell 2000).
*   **Portfolio Style**: Market-Neutral, sector-neutral.
*   **Rebalancing**: Monthly, with overlapping portfolios.

## Risks
*   **Factor Crowding**: As more quant funds combine [[PEAD]] with common factors like [[value]] and [[momentum]], the combined premium may diminish.
*   **Regime Shifts**: The relationship between [[PEAD]] and other factors may not be stable over time.
*   **Data Complexity**: Requires access to high-quality historical analyst forecast data and precise announcement timestamps.

## Related
- [[earnings_momentum_post-earnings_drift_trading]] — This document expands upon the fundamental concepts of the Post-Earnings Announcement Drift (PEAD) anomaly.
- [[momentum_trading_strategies_for_small_accounts]] — This strategy is often strongest in small-cap stocks, a common focus in momentum strategies for smaller accounts, and incorporates momentum as a factor overlay.
- [[quantitative_risk_management_position_sizing]] — This document outlines a methodology for calculating and managing position sizes, which is explicitly referenced for portfolio construction within the PEAD strategy.
- [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] — Provides a specific mathematical framework for optimal bet sizing that can be applied to the position sizing aspect of this strategy, especially for small accounts.
- [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]] — This resource offers advanced techniques and principles that can be applied to refine the analysis of earnings surprise and predict drift using machine learning models.
- [[sector_rotation_strategy_using_relative_strength]] — This strategy employs relative strength, a form of momentum, which can be utilized as a factor overlay in enhancing PEAD strategies.
- [[mean_reversion_strategies_equities]] — Understanding strategies that contrast with momentum-based approaches like PEAD, such as mean reversion, is crucial for a comprehensive strategic perspective in equities trading.
- [[risk_of_ruin_calculations_for_aggressive_small_accounts]] — This document provides critical insights into managing the risk associated with aggressive position sizing strategies, particularly relevant when implementing PEAD in smaller accounts.
- [[volatility_breakout_strategies]] — Insights from volatility strategies can inform the understanding of how PEAD performs in different market volatility regimes.
- [[highest_sharpe_ratio_strategies_for_accounts_under_1000_doll]] — This document explores strategies optimized for small accounts, providing context for the universe selection and performance considerations of PEAD in similar contexts.
- [[combining_trend_following_with_volatility_filters_for_max_re]] — This document discusses combining trend following (momentum) with volatility filters, which is relevant to the "Factor Overlay" section of the PEAD strategy.
- [[earnings_momentum_post-earnings_drift_trading_3]] — This document is likely a continuation or a deeper dive into specific aspects of the earnings momentum and post-earnings drift trading strategy.
# edited by gemini

## Sources
- Frazzini, Andrea, and Ari P. Vov "Post-earnings-announcement drift and the role of professional and non-professional investors." (2008).
- Brandt, Michael W., et al. "The post-earnings announcement drift: A multi-factor story." (2020).

## Next Steps
- Explore using [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]] to apply [[NLP]] on 10-K/10-Q filings to create a "change in language" factor to supplement [[SUE]].
- Test the [[PEAD]] strategy's performance during different market [[volatility]] regimes, potentially referencing insights from [[volatility_breakout_strategies]].
- Build a [[machine learning]] model using gradient boosting to predict the magnitude of the drift based on [[SUE]], [[CAR]], [[volatility]], [[size]], and other factors, drawing inspiration from [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]].
- Investigate the "term structure" of [[PEAD]] - does the optimal holding period change over time?
- Analyze the interaction of [[PEAD]] with short-interest data, potentially linking to concepts in [[order_flow_analysis_tape_reading_for_short_term_trades]] if short interest is considered an order flow signal.
- Consider how the principles discussed in `[[highest_sharpe_ratio_strategies_for_accounts_under_1000_doll]]` and `[[risk_of_ruin_calculations_for_aggressive_small_accounts]]` could further refine the PEAD strategy for small accounts.
# edited by gemini
```