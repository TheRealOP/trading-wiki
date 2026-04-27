```markdown
---
topic: "pairs trading statistical arbitrage methods"
date: 2026-04-07
tags: [agent/research, quant/pairs]
---

# Pairs Trading Statistical Arbitrage

## Key Insight
[[Pairs Trading]] is a [[market neutral]] [[statistical arbitrage]] strategy that profits from the [[mean reversion]] of the spread between two historically correlated assets. The core idea is that a long-term equilibrium relationship, often identified via [[cointegration]], will hold, and any short-term deviations present a trading opportunity. The goal is to isolate relative performance, hedging out broad [[market risk]].

## Strategy Logic
1.  **Pair Selection:** Identify pairs of securities (e.g., [[KO]] and [[PEP]]) with high [[correlation]] and, more importantly, a statistically significant [[cointegration]] relationship. This suggests a stable long-term economic link.
2.  **Spread Calculation:** Define the spread, often as the price ratio or the residual from a regression of one asset's price on the other. Normalize the spread using a [[Z-Score]] to identify deviations from the historical mean.
3.  **Signal Generation:** When the [[Z-Score]] crosses a predefined threshold (e.g., > +2.0), the spread is considered wide. Short the relatively overvalued asset and long the undervalued one.
4.  **Position Closing:** Exit the trade when the spread reverts to its mean (e.g., [[Z-Score]] crosses 0) for a profit, or if it diverges further to a [[stop-loss]] threshold (e.g., > +3.0) to limit [[drawdown]].

## Parameters
-   **Lookback Period:** For calculating historical [[mean]] and [[standard deviation]] of the spread.
-   **Entry/Exit Thresholds:** The [[Z-Score]] values that trigger opening and closing trades (e.g., +/- 2.0 for entry, 0 for exit).
-   **[[Cointegration]] Test:** Significance level (p-value) for the Engle-Granger or Johansen test.
-   **[[Stop-Loss]]:** A wider [[Z-Score]] threshold to prevent large losses if the relationship breaks down.

## Risks
-   **[[Cointegration Risk]]**: The stable relationship between pairs may break down due to fundamental changes.
-   **[[Execution Risk]]**: [[Slippage]] and transaction costs can erode profits, especially for high-frequency implementations.
-   **[[Drawdown]]**: Even with [[market neutral]] exposure, a series of losing trades can lead to significant capital reduction. Requires careful [[position sizing]].
-   **[[Overfitting]]**: Parameter optimization during [[backtesting]] may not translate to live performance.

## Related
-   [[Statistical Arbitrage]] — Pairs trading is a prominent example of a statistical arbitrage strategy, exploiting temporary price divergences. # edited by gemini
-   [[Mean Reversion]] — The fundamental principle behind pairs trading is the expectation that the spread between two assets will revert to its historical mean. # edited by gemini
-   [[Cointegration]] — A crucial statistical concept used in pairs trading to identify a stable, long-term equilibrium relationship between two non-stationary time series. # edited by gemini
-   [[Market Neutral Strategy]] — Pairs trading aims to be market-neutral by simultaneously longing and shorting assets, thereby hedging against broad market movements. # edited by gemini
-   [[ETFs]] — Exchange-Traded Funds can be used as components in pairs trading strategies, especially for broader sector or index pairs. # edited by gemini
-   [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]] — Machine learning techniques discussed here can be applied to enhance pair selection, spread forecasting, or dynamic parameter tuning in pairs trading. # edited by gemini
-   [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] — This criterion provides a mathematical framework for optimal position sizing, which is essential for managing risk and maximizing returns in pairs trading. # edited by gemini
-   [[mean_reversion_overnight_gap_fade_strategy]] — Offers another example of a mean reversion approach, illustrating how temporary market inefficiencies can be exploited, similar to pairs trading. # edited by gemini
-   [[mean_reversion_strategies_equities]] — Pairs trading falls under the broader umbrella of mean reversion strategies, particularly within equity markets. # edited by gemini
-   [[quantitative_risk_management_position_sizing]] — This document covers the critical aspects of managing trading capital and exposure, directly applicable to the robust implementation of any pairs trading strategy. # edited by gemini
-   [[risk_of_ruin_calculations_for_aggressive_small_accounts]] — Understanding and calculating the risk of ruin is vital for aggressive pairs trading strategies to prevent catastrophic capital loss. # edited by gemini
-   [[statistical_edge_in_short_term_mean_reversion_spy_qqq]] — Explores the concept of finding a statistical advantage through short-term mean reversion, which is the core mechanism pairs trading leverages. # edited by gemini

## Sources
-   Gatev, Goetzmann, & Rouwenhorst (2006), "Pairs Trading: Performance of a Relative-Value Arbitrage Rule"
-   Vidyamurthy (2004), "Pairs Trading: Quantitative Methods and Analysis"
-   Engle & Granger (1987), "Co-Integration and Error Correction: Representation, Estimation, and Testing"

## Next Steps
- [ ] Explore [[cointegration]] vs. distance-based methods in more depth for pair selection. # edited by gemini
- [ ] Test a basic [[Engle-Granger]] strategy on [[S&P 500]] components using [[Python]]. # edited by gemini
- [ ] Investigate optimal [[position sizing]] by applying concepts from [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] and [[quantitative_risk_management_position_sizing]] for pairs strategies. # edited by gemini
- [ ] Research [[machine learning]] approaches for dynamic pair selection, drawing insights from [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]]. # edited by gemini
- [ ] Analyze [[risk_of_ruin_calculations_for_aggressive_small_accounts]] in the context of pairs trading strategies to better understand potential capital depletion. # edited by gemini
```