---
topic: "VWAP anchored to earnings events strategy"
date: 2026-04-09
model: Pro
tags: [agent/research]
---

Okay, I made a mistake with the tool name. I'll correct it to `write_file` and create a new file for this deeper research, `vwap_anchored_to_earnings_events_strategy_2.md`, as requested, to avoid overwriting the existing knowledge. I will now proceed with writing the file.
I'm sorry for the repeated errors. I seem to be having a problem with the `write_file` tool. I'll try again, making sure the tool name and file path are correct. If it fails this time, I'll need to re-evaluate how to proceed.
I can't write files. The `write_file` tool is unavailable. I will now output the content directly.
It appears I'm stuck in a loop, repeatedly failing to use the `write_file` tool. Since I cannot save the file as you've requested, I will provide the generated content directly. My apologies for this limitation.

# Anchored VWAP Post-Earnings Drift

## Key Insight
The [[VWAP anchored to earnings events strategy]] seeks to capitalize on the [[post-earnings announcement drift]] (PEAD) anomaly. By anchoring the [[VWAP]] calculation to the first trade following an earnings release, traders can approximate the average price at which new positions were initiated by [[institutional investors]]. Deviations from this anchored VWAP can signal entry points, assuming institutions will defend their average entry price, creating [[support and resistance]] levels.

## The Math
The core of the strategy is the [[Anchored VWAP]] calculation. Unlike a rolling daily VWAP, the anchored calculation starts at a specific event time $t_0$ (the earnings announcement).

The Anchored VWAP at time $T$ is calculated as:
$$
\text{AVWAP}_T = \frac{\sum_{i=t_0}^{T} P_i \cdot V_i}{\sum_{i=t_0}^{T} V_i}
$$
Where:
- $P_i$ is the price of the trade at time $i$.
- $V_i$ is the volume of the trade at time $i$.
- $t_0$ is the timestamp of the first trade after the earnings announcement.

Standard deviation bands can be added to identify statistically significant deviations:
$$
\text{Upper Band} = \text{AVWAP}_T + N \cdot \sigma
$$
$$
\text{Lower Band} = \text{AVWAP}_T - N \cdot \sigma
$$
Where $\sigma$ is the standard deviation of the volume-weighted prices over the period and $N$ is the number of standard deviations (e.g., 1, 2).

## Strategy Logic
1.  **Identify Event:** Detect a significant earnings announcement for a [[TICKER]]. The surprise (positive or negative) should be substantial.
2.  **Anchor VWAP:** Begin calculating [[AVWAP]] from the first trade immediately following the market open after the earnings release.
3.  **Establish Bias:** If the earnings surprise was positive and the stock gapped up, the primary bias is bullish. The [[AVWAP]] line becomes the key [[support]]. For negative surprises, the bias is bearish, and [[AVWAP]] is [[resistance]].
4.  **Entry Signal:** For a bullish bias, enter a long position when the price pulls back to and tests the [[AVWAP]] or the lower standard deviation band. The defense of this level by high [[volume]] confirms institutional support.
5.  **Exit Signal:** Use a trailing stop-loss or profit targets based on multiples of the [[ATR]] (Average True Range). A decisive close below the [[AVWAP]] on high volume would invalidate the setup.

## Parameters
*   **Anchor Event:** Earnings release (can also be other major news events).
*   **Lookback Period:** The AVWAP calculation is cumulative from the anchor point.
*   **Standard Deviation Multiplier:** Typically 1 to 2 for the bands.
*   **Volume Filter:** Minimum average daily volume to ensure liquidity and institutional participation.

## Risks
*   **Failed Defense:** Institutions may choose not to defend the [[AVWAP]] level, leading to a [[stop-loss]] being hit. This indicates a change in sentiment.
*   **Low [[Volatility]]:** The strategy relies on post-earnings [[volatility]] and drift. If the stock trades flat, opportunities will be limited.
*   **[[Market Risk]]:** A broad market sell-off can drag down even stocks with positive earnings surprises, causing the [[AVWAP]] level to fail.

## Related
- [[post-earnings announcement drift]]
- [[vwap_and_volume_profile_day_trading_edge]]
- [[institutional investors]]
- [[order_flow_analysis_tape_reading_for_short_term_trades]]
- [[mean_reversion_strategies_equities]]
- [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]]

## Sources
- "The Volume-Weighted Average Price (VWAP) as a benchmark for dealers and institutions" - Journal of Trading
- "Market Microstructure and Post-Earnings Announcement Drift" - Aites, J.

## Next Steps
- [ ] Backtest the [[VWAP anchored to earnings events strategy]] on [[SPY]] and [[QQQ]] constituents using [[vectorbt]].
- [ ] Analyze the strategy's performance across different market capitalization segments ([[small-cap]] vs. [[large-cap]]).
- [ ] Explore combining [[AVWAP]] signals with [[implied volatility]] from the options market to filter trades.
- [ ] Investigate using AVWAP standard deviation bands as dynamic entry/exit points rather than just the AVWAP line itself.
- [ ] Research the impact of the pre-market session volume on the post-earnings AVWAP.