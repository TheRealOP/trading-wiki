---
topic: "stop loss strategies"
date: 2026-04-27
model: codex
tags: [quant/fundamentals, risk/stops]
---

> [!tip] Key Insight
> A stop loss defines the price where the trade thesis is wrong, not where the pain becomes annoying. Without one, a single position can turn from a planned 2% account risk into a portfolio-level drawdown; the classic example is holding a leveraged ETF through a sharp gap because "it should bounce."

# Stop Loss Strategies

## 1. Fixed Percentage Stop
```python
stop = entry_price * (1 - stop_pct)  # e.g. stop_pct = 0.02 for 2%
```
- Simple, consistent
- Ignores volatility; too tight in choppy markets, too wide in calm ones
- Useful when the strategy horizon and instrument volatility are stable

## 2. ATR-Based Stop (Volatility-Adjusted)
```python
import pandas_ta as ta
atr = df["Close"].ta.atr(length=14).iloc[-1]
stop = entry_price - (atr_multiplier * atr)  # e.g. atr_multiplier = 1.5
```
- Adapts to current market volatility
- Best practice for most strategies; use 1.5-2x ATR for equities, wider for crypto
- Wider in volatile conditions, tighter in calm ones

## 3. Trailing Stop
```python
# Update each bar:
trailing_stop = max(trailing_stop, current_price * (1 - trail_pct))
if current_price <= trailing_stop:
    exit()
```
- Locks in profits as price rises
- Never moves down, only up
- Use 2-3% trail for trending stocks, 5-8% for crypto

## 4. Support/VWAP Stop
```python
stop = max(vwap, recent_swing_low, value_area_low) * 0.995
```
- Stop placed just below a key level
- Natural because it matches where the trade thesis is invalidated
- Best for VWAP and volume profile strategies

## 5. Time-Based Stop
```python
if (current_time - entry_time).seconds > 3600 and pnl < 0:
    exit()  # exit if down after 1 hour
```
- Kills stagnant trades that are not working
- Combine with price stop, whichever hits first

## When to Use Which

| Situation | Best Stop |
|-----------|-----------|
| Trending momentum | ATR trailing |
| Mean reversion | Fixed % or nearby structure |
| Breakout trade | Just below breakout level |
| Crypto (high vol) | ATR x2.5 or 5-8% notional trail |
| LLM/sentiment trade | 1.5% to 1.5x ATR + time stop |

## Working vs Failing

A stop process is working when losses are small, boring, and close to the pre-trade risk estimate. You should see losing trades exit quickly when price invalidates the setup, while winning trades have enough room to reach the planned target or trail.

It is failing when stops cluster right before reversals, when losses are far larger than expected, or when the trader keeps widening stops after entry. Another warning sign is strategy performance depending on "it came back eventually" instead of disciplined exits.

## Common Mistakes

- Placing stops at round numbers where everyone else is likely to cluster orders.
- Using the same 2% price stop on SPY, TQQQ, BTC, and a low-float stock.
- Moving a stop farther away after entry.
- Sizing by dollars invested instead of dollars at risk to the stop.
- Backtesting stops on closing prices only, then discovering live intraday stops behave differently.

## Interactions With Other Concepts

Stop distance directly controls [[position_sizing]] because shares should be calculated from account risk divided by price risk. Stops are part of [[risk_management_rules]] because they prevent single-trade damage from becoming portfolio damage.

The stop should match the [[entry_exit_techniques]] logic: breakout stops belong below the breakout area, mean-reversion stops belong beyond the failed reversion level, and momentum stops often trail. [[technical_indicators_guide]] provides ATR, VWAP, Bollinger Bands, and swing levels that can define objective stops. [[market_conditions_filter]] changes how wide stops must be, because high volatility needs more room or smaller size. [[backtesting_methodology]] must model stop execution, slippage, gaps, and whether the stop is evaluated intraday or only at bar close.

## Rule of Thumb

Always size position so that hitting the stop equals max 2% account loss:
```python
risk_dollars = account_balance * 0.02
shares = risk_dollars / (entry_price - stop_price)
```

## In Our System

- `trader.py` implements the portfolio stop discipline in `calc_shares()`, `place_buy()`, `place_sell()`, `run_signals()`, and `check_strategy_kill()`.
- Current parameters: `MAX_RISK_PCT = 0.02`, `MAX_DRAWDOWN_PCT = 0.10`, `CONSECUTIVE_LOSSES = 3`, and `CASH_BUFFER = 100.0`.
- Equity buys use Alpaca bracket orders with `stop_loss={"stop_price": stop}` and a take-profit target at `entry + 2 * (entry - stop)`.
- Crypto positions cannot use Alpaca bracket orders in this executor, so `run_signals()` manually sells when price hits the stored stop or the same 2R target.
- `strategies/vwap_strategy.py` sets stops from VWAP, POC, VAL, or `close - ATR`, with `ATR_LOOKBACK = 14`.
- `strategies/rsi_macd_bb_strategy.py` uses the lower Bollinger Band or 10-day swing low, falling back to a 3% stop.
- `strategies/crypto_momentum_strategy.py` uses `STOP_PCT = 0.05`.
- `strategies/leveraged_etf_momentum_strategy.py` uses `_STOP_PCT = 0.08`.
- `strategies/llm_sentiment_strategy.py` asks Codex for a stop and falls back to roughly 1.5% below current price.
- Improvement: add true trailing-stop updates for momentum trades, add gap/slippage modeling to exits, and centralize stop validation so every strategy reports whether the stop is structure-based, volatility-based, or fixed-percent.

## See Also

- [[position_sizing]]
- [[risk_management_rules]]
- [[entry_exit_techniques]]
- [[technical_indicators_guide]]
- [[market_conditions_filter]]
- [[backtesting_methodology]]
