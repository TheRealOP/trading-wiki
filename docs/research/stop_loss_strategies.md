---
topic: "stop loss strategies"
date: 2026-04-27
model: codex
tags: [quant/fundamentals, risk/stops]
---

# Stop Loss Strategies

## 1. Fixed Percentage Stop
```python
stop = entry_price * (1 - stop_pct)  # e.g. stop_pct = 0.02 for 2%
```
- Simple, consistent
- Ignores volatility — too tight in choppy markets, too wide in calm ones

## 2. ATR-Based Stop (Volatility-Adjusted)
```python
import pandas_ta as ta
atr = df["Close"].ta.atr(length=14).iloc[-1]
stop = entry_price - (atr_multiplier * atr)  # e.g. atr_multiplier = 1.5
```
- Adapts to current market volatility
- Best practice for most strategies — use 1.5–2x ATR
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
- Use 2–3% trail for trending stocks, 5–8% for crypto

## 4. Support/VWAP Stop
```python
stop = max(vwap, recent_swing_low, value_area_low) * 0.995
```
- Stop placed just below a key level
- Natural — matches where the trade thesis is invalidated
- Best for VWAP and volume profile strategies

## 5. Time-Based Stop
```python
if (current_time - entry_time).seconds > 3600 and pnl < 0:
    exit()  # exit if down after 1 hour
```
- Kills stagnant trades that aren't working
- Combine with price stop (whichever hits first)

## When to Use Which

| Situation | Best Stop |
|-----------|-----------|
| Trending momentum | ATR trailing |
| Mean reversion | Fixed % (tight, 1–1.5%) |
| Breakout trade | Just below breakout level |
| Crypto (high vol) | ATR x2.5 or notional trail |
| LLM/sentiment trade | ATR x1.5 + time stop (1 day) |

## Rule of Thumb
Always size position so that hitting the stop = max 2% account loss:
```python
risk_dollars = account_balance * 0.02
shares = risk_dollars / (entry_price - stop_price)
```
