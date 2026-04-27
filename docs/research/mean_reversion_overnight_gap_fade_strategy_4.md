# Market Microstructure and Regime-Dependence in Gap Fading

## Key Insight
The [[mean_reversion_overnight_gap_fade_strategy]] is not merely a statistical pattern but a direct consequence of [[market microstructure]], specifically the accumulation of [[order imbalance]] during off-market hours. The profitability and reliability of this strategy are highly dependent on the prevailing [[market regime]], particularly [[volatility]]. By modeling these factors, we can create a more robust strategy that filters for high-probability setups and avoids environments where fading is likely to fail.

## The Math
We can quantify the pre-open pressure and the market's volatility context to refine the strategy.

1.  **Pre-Market Order Imbalance ($OI$):** This metric captures the net buying or selling pressure before the market opens, which is a primary driver of the initial gap.
    $OI_t = \frac{V_{buy, t-1 \to t} - V_{sell, t-1 \to t}}{V_{buy, t-1 \to t} + V_{sell, t-1 \to t}}$
    Where $V_{buy}$ and $V_{sell}$ are the volumes of buy and sell orders in the pre-market session. A large positive $OI$ suggests a gap up driven by excess buy orders, and vice-versa.

2.  **Volatility Regime Estimation (GARCH):** A [[GARCH]](1,1) model can be used to forecast daily [[volatility]] ($\sigma_t^2$) and classify the market regime.
    $\sigma_t^2 = \omega + \alpha u_{t-1}^2 + \beta \sigma_{t-1}^2$
    - $u_t^2$ is the squared return at $t$.
    - $\omega, \alpha, \beta$ are parameters.
    - A high forecasted $\sigma_t$ can indicate a "trending" or "panic" regime, while a moderate level suggests a "mean-reverting" regime. Alternatively, the [[VIX]] can be used as a simpler proxy.

## Strategy Logic
1.  **Regime Classification:** Before the market open, determine the current [[market regime]].
    - **High Volatility / Trending Regime** (e.g., [[VIX]] > 30 or high GARCH forecast): Disable the fade strategy. Gaps in these regimes are often news-driven and likely to continue ([[Gap and Go]]).
    - **Low Volatility / Complacent Regime** (e.g., [[VIX]] < 15): Exercise caution. Low volatility can lead to breakouts, not reversions.
    - **Mean-Reverting Regime** (e.g., 15 < [[VIX]] < 30): The strategy is active.
2.  **Quantify Imbalance:** Identify a significant [[overnight gap]]. Measure the pre-market [[order imbalance]] ($OI$).
3.  **Entry Signal:** If in a [[Mean-Reverting Regime]], and the gap direction is consistent with the $OI$, initiate a fade tr
