```markdown
---
topic: "highest sharpe ratio strategies for accounts under 1000 dollars"
date: 2026-04-07
model: Pro
tags: [agent/research, quant/momentum]
---

# High Sharpe Ratio Pairs Trading
## Key Insight
This strategy exploits [[mean reversion]] in the price relationship between two [[cointegration|cointegrated]] assets. By identifying a pair of securities whose prices historically move together, we can trade the temporary [[spread]] divergences, betting on their eventual convergence. This approach offers a [[market neutral]] exposure, focusing on relative value rather than market direction.

## The Math
The core of this strategy is modeling the spread between two assets, A and B.

1.  **Price Series**: Let $P_A(t)$ and $P_B(t)$ be the prices of asset A and asset B at time $t$.
2.  **Hedge Ratio**: We find a [[hedge ratio]] $\beta$ by regressing $P_A$ on $P_B$: $P_A(t) = \alpha + \beta P_B(t) + \epsilon(t)$. The residual, $\epsilon(t)$, is the [[spread]].
3.  **Spread Calculation**: The [[spread]] $S(t)$ is calculated as:
    $S(t) = P_A(t) - \beta P_B(t)$
4.  **Stationarity Test**: We must ensure the spread is [[stationarity|stationary]] (i.e., mean-reverting) using a statistical test like the [[Augmented Dickey-Fuller test]]. A p-value < 0.05 is typically required.
5.  **Z-Score**: The trading signal is generated from the z-score of the spread, which standardizes it. For a given lookback window:
    $Z(t) = \frac{S(t) - \mu_{S(t)}}{\sigma_{S(t)}}$
    Where $\mu_{S(t)}$ and $\sigma_{S(t)}$ are the rolling mean and standard deviation of the spread.

## Strategy Logic
1.  Identify a pair of historically [[cointegration|cointegrated]] assets (e.g., [[GLD]] and [[GDX]], or [[SPY]] and [[IVV]]).
2.  Over a defined lookback period (e.g., 90 days), calculate the [[hedge ratio]] $\beta$.
3.  Calculate the current [[spread]] $S(t)$ and its corresponding [[Z-Score]] $Z(t)$.
4.  **Entry Signal**:
    - If $Z(t) > Z_{entry}$, short the spread (Short 1 share of Asset A, Buy $\beta$ shares of Asset B).
    - If $Z(t) < -Z_{entry}$, long the spread (Buy 1 share of Asset A, Short $\beta$ shares of Asset B).
5.  **Exit Signal**:
    - Exit the position when the [[Z-Score]] $Z(t)$ crosses back to 0.

## Parameters
- **Asset Pair**: e.g., [[GLD]]/[[GDX]], [[PEP]]/[[KO]]
- **Lookback Window**: 60-120 days for rolling mean/std. dev.
- **Entry Z-Score ($Z_{entry}$)**: Typically between 1.5 and 2.0.
- **Stop-Loss Z-Score**: A value (e.g., 3.0) at which the trade is closed to prevent large losses if the [[spread]] continues to diverge.

## Risks
- **[[Cointegration Breakdown]]**: The historical relationship between the assets may break down, leading to a non-reverting [[spread]].
- **[[Execution Risk]]**: [[Slippage]] and transaction costs can erode profits, especially for a [[small account]].
- **[[Beta]] Instability**: The [[hedge ratio]] is not static and may change over time, requiring periodic recalculation.

## Related # edited by gemini
- [[pairs_trading_statistical_arbitrage_methods]] — This document elaborates on the broader concept of [[statistical arbitrage]], of which pairs trading is a specific application. # edited by gemini
- [[mean_reversion_strategies_equities]] — Pairs trading is a classic example of a [[mean reversion]] strategy, applying the principle to the spread between two assets rather than a single asset's price. # edited by gemini
- [[statistical_edge_in_short_term_mean_reversion_spy_qqq]] — This explores specific examples of [[statistical edge]] within [[mean reversion]], which provides context for the underlying statistical assumptions of pairs trading. # edited by gemini
- [[quantitative_risk_management_position_sizing]] — Provides the foundational principles for determining appropriate [[position sizing]] and managing [[risk]] in rule-based strategies like pairs trading. # edited by gemini
- [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] — Offers a specific method for calculating optimal [[bet sizing]] to maximize [[portfolio growth]] for [[small accounts]], which is crucial for managing capital in pairs trading strategies. # edited by gemini
- [[risk_of_ruin_calculations_for_aggressive_small_accounts]] — This document is critical for understanding and quantifying the potential for [[capital loss]] and [[drawdown]] when employing aggressive strategies in [[small accounts]]. # edited by gemini
- [[algorithmic_trading_with_moving_averages]] — While different in approach, this document covers another rule-based [[algorithmic trading]] strategy that can share common implementation considerations. # edited by gemini
- [[alpaca_api_algorithmic_order_types_bracket_orders_trailing_s]] — This is relevant for understanding how to execute the simultaneous long/short orders required for pairs trading using a broker API. # edited by gemini

## Sources
- "Pairs Trading: Performance of a Relative Value Arbitrage Rule" by Gatev, Goetzmann, and Rouwenhorst.
- "The Econometrics of Financial Markets" by Campbell, Lo, and MacKinlay.

## Next Steps # edited by gemini
- [ ] Backtest potential pairs like [[EWA]]/[[EWC]] for [[cointegration]] and historical [[spread]] behavior. # edited by gemini
- [ ] Analyze the impact of different [[lookback window]] lengths on the strategy's [[Sharpe Ratio]], referencing concepts in [[algorithmic_trading_with_moving_averages]] for backtesting methodology. # edited by gemini
- [ ] Implement a dynamic [[stop-loss]] mechanism based on maximum [[Z-Score]] or [[volatility]], incorporating principles from [[quantitative_risk_management_position_sizing]]. # edited by gemini
- [ ] Apply the [[bet sizing]] rules from [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]] to a backtest of this pairs strategy to optimize [[capital allocation]]. # edited by gemini
- [ ] Based on backtest results, perform [[risk_of_ruin_calculations_for_aggressive_small_accounts]] to assess the robustness for [[small accounts]]. # edited by gemini
- [ ] Model the simultaneous order execution needed for this strategy, leveraging knowledge of order types discussed in [[alpaca_api_algorithmic_order_types_bracket_orders_trailing_s]]. # edited by gemini
- [ ] Explore using advanced statistical techniques like the [[Kalman Filter]] to estimate a dynamic [[hedge ratio]] and address [[beta]] instability, potentially drawing from resources on advanced [[quantitative]] methods. # edited by gemini
- [ ] Research the impact of [[execution risk]] and [[slippage]] on profitability for [[small accounts]], potentially informing more robust [[entry]] and [[exit signals]]. # edited by gemini
```