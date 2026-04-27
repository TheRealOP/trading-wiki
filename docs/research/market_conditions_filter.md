---
topic: "market conditions filter"
date: 2026-04-27
model: codex
tags: [quant/fundamentals, quant/filters]
---

# Market Conditions Filter

## VIX Regime
VIX = implied volatility of SPY options. Measures market fear.
```python
import yfinance as yf
vix = float(yf.Ticker("^VIX").fast_info["last_price"])

# Regimes:
# < 15: calm, low vol — normal sizing, trend strategies work well
# 15–20: normal — standard operation
# 20–30: elevated — reduce size 25–50%, avoid breakouts
# > 30: crisis — reduce size 50–75% or stop trading equities
#        (crypto less affected by VIX)
```

## Trending vs Ranging (ADX Filter)
ADX measures trend strength. Tells you which strategy type to use.
```python
import pandas_ta as ta
adx = ta.adx(df["High"], df["Low"], df["Close"], length=14)
adx_value = adx["ADX_14"].iloc[-1]

if adx_value > 25:
    mode = "trending"    # use momentum/breakout strategies
else:
    mode = "ranging"     # use mean reversion strategies
```
- ADX > 25: strong trend → momentum entries work
- ADX < 20: choppy/ranging → VWAP mean reversion works
- ADX 20–25: transitional — be cautious

## SPY/QQQ Market Regime
Don't fight the broad market direction.
```python
spy = yf.download("SPY", period="5d", interval="1d", auto_adjust=True)
spy_trend = "bullish" if spy["Close"].iloc[-1] > spy["Close"].iloc[-5] else "bearish"

# If bearish market: only take short setups or sit in cash for equities
# Crypto is less correlated but still affected in panic selloffs
```

## Pre-Market Gap Rules
```python
prev_close = get_previous_close(symbol)
open_price = get_premarket_price(symbol)
gap_pct = (open_price - prev_close) / prev_close

if gap_pct > 0.03:    # gapped up > 3%
    # Don't chase — wait for pullback to VWAP or gap fill
    skip_breakout_entries = True
if gap_pct < -0.03:   # gapped down > 3%
    # Potential bounce trade — wait for first 15 min to settle
    pass
```

## Earnings Blackout
```python
import yfinance as yf
calendar = yf.Ticker(symbol).calendar
next_earnings = calendar.get("Earnings Date", [None])[0]

days_to_earnings = (next_earnings - date.today()).days if next_earnings else 999
if days_to_earnings <= 2:
    skip_entry(f"{symbol}: earnings in {days_to_earnings} days — blackout")
```

## Time of Day Filter
```python
from datetime import time
now = datetime.now(timezone("US/Eastern")).time()

avoid_entry = (
    now < time(9, 45)    # first 15 min — chaotic
    or time(12, 0) <= now <= time(13, 0)  # lunch lull
    or now > time(15, 45)  # last 15 min — closing auctions
)
```

## Combined Filter Function
```python
def market_ok_to_trade(symbol, is_crypto=False):
    if is_crypto:
        return True  # crypto trades 24/7, no time filters

    vix = get_vix()
    if vix > 35:
        return False  # extreme fear

    if avoid_entry_time():
        return False

    if near_earnings(symbol, days=2):
        return False

    return True
```
