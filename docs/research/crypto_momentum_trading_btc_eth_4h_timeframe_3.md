```markdown
---
topic: "crypto momentum trading BTC ETH 4h timeframe"
date: 2026-04-07
model: Flash
tags: [agent/research, quant/momentum, instrument/crypto]
---

# Crypto Momentum: Liquidity-Weighted 4H BTC/ETH Strategy

## Key Insight
Leveraging [[liquidity]] and [[intermarket analysis]] (e.g., [[correlation]] between [[BTC]] and [[ETH]]) can significantly enhance [[momentum signals]] on the 4-hour timeframe. Incorporating [[Volume Weighted Average Price (VWAP)]] as a dynamic [[support and resistance]] level and trend confirmation, alongside a [[correlation]] filter, aims to improve [[signal quality]] and mitigate [[whipsaw]] risks inherent in price-only approaches.

## The Math
### Volume Weighted Average Price (VWAP)
The [[Volume Weighted Average Price (VWAP)]] at time $t$ is calculated as:
$VWAP_t = \frac{\sum_{i=1}^{t} (P_i \cdot V_i)}{\sum_{i=1}^{t} V_i}$
where $P_i$ is the typical price (e.g., $(H_i + L_i + C_i)/3$) and $V_i$ is the [[volume]] for period $i$. This serves as a [[liquidity]]-aware [[mean]] value.

### Pearson Correlation Coefficient ($\rho$)
The [[Pearson Correlation Coefficient]] between [[BTC]] returns ($R_{BTC}$) and [[ETH]] returns ($R_{ETH}$) over $N$ periods is:
$\rho = \frac{\sum_{i=1}^{N} (R_{BTC,i} - \bar{R}_{BTC})(R_{ETH,i} - \bar{R}_{ETH})}{\sqrt{\sum_{i=1}^{N} (R_{BTC,i} - \bar{R}_{BTC})^2 \sum_{i=1}^{N} (R_{ETH,i} - \bar{R}_{ETH})^2}}$
High positive [[correlation]] ($\rho \approx 1$) confirms a synchronized [[market trend]].

## Strategy Logic
1.  **Core Momentum Signal**: Identify a [[momentum]] shift (e.g., [[Rate of Change (ROC)]]$ (14) > 0$ and [[VAMA]] crossover (Fast 9, Slow 21, ATR-adjusted) as described in [[crypto_momentum_trading_btc_eth_4h_timeframe_2]]).
2.  **[[Liquidity]] Confirmation**: Only enter long if the current price closes above $VWAP(20)$ AND the $VWAP(20)$ is sloping upwards, indicating strong buying [[pressure]] with [[volume]].
3.  **[[Intermarket Correlation]] Filter**: The 20-period [[correlation]] ($\rho$) between [[BTC]] and [[ETH]] 4-hour returns must be above a threshold (e.g., $\rho > 0.7$). This filters out divergent movements or asset-specific news.
4.  **Entry & Exits**:
    *   **Entry**: On 4H candle close when all conditions (momentum, liquidity, correlation) are met.
    *   **Stop Loss**: Initial [[stop-loss]] at $2 \times ATR(14)$ below entry.
    *   **Take Profit**: Target $3 \times ATR(14)$ or a trailing stop based on $1.5 \times ATR(14)$ from highest price since entry.
    *   **Alternative Exit**: Exit if price closes below $VWAP(20)$ or if [[correlation]] breaks down ($\rho < 0.5$).
5.  **[[Position Sizing]]**: Maintain 1-2% [[risk]] per [[trade]] of capital, guided by [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]].

## Parameters
*   **Assets**: [[BTC]]/USD, [[ETH]]/USD
*   **Timeframe**: 4-hour candles
*   **Momentum Indicators**: $ROC(14)$, [[VAMA]] (Fast 9, Slow 21 - ATR adjusted)
*   **VWAP Period**: 20 periods
*   **Correlation Period**: 20 periods
*   **Correlation Threshold**: $\rho > 0.7$ (entry), $\rho < 0.5$ (exit filter)
*   **ATR Period**: 14 periods for [[stop-loss]]/[[take-profit]]

## Risks
*   **Over-optimization**: Too many filters can lead to [[curve-fitting]] and poor out-of-sample performance.
*   **Lag**: Adding [[VWAP]] and [[correlation]] introduces more [[lag]] to signals, potentially delaying entries/exits.
*   **Dynamic Correlation**: [[Correlation]] can shift rapidly in [[crypto markets]], making a static threshold problematic.
*   **Data Quality**: Accurate [[volume]] data across various exchanges is critical for reliable [[VWAP]] calculations.

## Related
- [[crypto_momentum_trading_btc_eth_4h_timeframe]]: This file provides the foundational context for the crypto momentum strategy.
- [[crypto_momentum_trading_btc_eth_4h_timeframe_2]]: The core momentum signal for this strategy is detailed in this preceding file.
- [[momentum_trading_strategies_for_small_accounts]]: This strategy is a specific application of general principles discussed in broader momentum trading contexts for small accounts.
- [[algorithmic_trading_with_moving_averages]]: The VAMA indicator used in this strategy is a type of moving average, connecting to broader algorithmic trading concepts using such indicators.
- [[combining_trend_following_with_volatility_filters_for_max_re]]: This strategy incorporates elements of trend following (VAMA, VWAP) and volatility filters (ATR), similar to the approach outlined in this file.
- [[quantitative_risk_management_position_sizing]]: This file covers the core principles of position sizing that are applied in this strategy's risk management.
- [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]]: This file is directly referenced as guidance for the optimal bet sizing component of the strategy's risk management.
- [[risk_of_ruin_calculations_for_aggressive_small_accounts]]: Understanding the risk of ruin is crucial for aggressive position sizing strategies, and this file provides relevant calculations.
- [[volatility_breakout_strategies]]: While not a direct breakout strategy, the use of ATR for stop-loss and take-profit calculation is a common element shared with volatility-based strategies.
- [[high_probability_setups_combining_multiple_indicators_rsi_ma]]: This strategy combines multiple indicators (momentum, VWAP, correlation) to form a high-probability setup, similar to the approach discussed in this file.

## Sources
*   P. Kaufman, *Trading Systems and Methods*
*   J. Ehlers, *Cybernetic Analysis for Stocks and Futures*
*   Academic papers on [[correlation]] and [[statistical arbitrage]] in financial markets.

## Next Steps
- [ ] Develop [[VWAP]] implementation and rigorously backtest its effectiveness as a [[liquidity]] and trend filter, drawing insights from `[[vwap_and_volume_profile_day_trading_edge]]` and `[[vwap_anchored_to_earnings_events_strategy]]`.
- [ ] Analyze historical [[BTC]]/[[ETH]] [[correlation]] dynamics to identify stable vs. unstable regimes and optimal thresholds, considering methodologies from `[[pairs_trading_statistical_arbitrage_methods]]`.
- [ ] Explore dynamic [[correlation]] thresholds, perhaps using [[adaptive moving averages]] on the [[correlation]] series itself.
- [ ] Integrate realistic [[slippage]] and [[transaction costs]] into [[backtesting]] results to assess true profitability, as is crucial when considering `[[risk_of_ruin_calculations_for_aggressive_small_accounts]]`.
- [ ] Investigate alternative [[liquidity]] metrics and their impact on [[signal quality]] for [[crypto markets]].
# edited by gemini
```