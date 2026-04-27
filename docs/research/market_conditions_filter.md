---
topic: "market conditions filter"
date: 2026-04-27
model: codex
tags: [quant/fundamentals, quant/filters]
---

> [!tip] Key Insight
> Market filters answer whether the strategy should be trading this environment at all. Ignoring regime is how a mean-reversion setup keeps buying dips during a crash or a breakout system gets chopped up in a quiet range.

# Market Conditions Filter

## VIX Regime

VIX is implied volatility of SPY options and a proxy for market fear.
```python
import yfinance as yf
vix = float(yf.Ticker("^VIX").fast_info["last_price"])

# < 15: calm, normal sizing
# 15-20: normal
# 20-30: elevated, reduce size 25-50%
# > 30: crisis, reduce size 50-75% or stop equities
```

## Trending vs Ranging (ADX Filter)

ADX measures trend strength and helps choose strategy type.
```python
import pandas_ta as ta
adx = ta.adx(df["High"], df["Low"], df["Close"], length=14)
adx_value = adx["ADX_14"].iloc[-1]

if adx_value > 25:
    mode = "trending"
else:
    mode = "ranging"
```
- ADX > 25: strong trend, momentum entries work
- ADX < 20: choppy/ranging, mean reversion works better
- ADX 20-25: transitional, be cautious

## SPY/QQQ Market Regime

Do not fight the broad market direction.
```python
spy = yf.download("SPY", period="5d", interval="1d", auto_adjust=True)
spy_trend = "bullish" if spy["Close"].iloc[-1] > spy["Close"].iloc[-5] else "bearish"
```

## Pre-Market Gap Rules

```python
prev_close = get_previous_close(symbol)
open_price = get_premarket_price(symbol)
gap_pct = (open_price - prev_close) / prev_close

if gap_pct > 0.03:
    skip_breakout_entries = True
if gap_pct < -0.03:
    wait_for_first_15_min = True
```

## Earnings Blackout

```python
import yfinance as yf
calendar = yf.Ticker(symbol).calendar
next_earnings = calendar.get("Earnings Date", [None])[0]

days_to_earnings = (next_earnings - date.today()).days if next_earnings else 999
if days_to_earnings <= 2:
    skip_entry(f"{symbol}: earnings in {days_to_earnings} days")
```

## Time of Day Filter

```python
from datetime import time
now = datetime.now(timezone("US/Eastern")).time()

avoid_entry = (
    now < time(9, 45)
    or time(12, 0) <= now <= time(13, 0)
    or now > time(15, 45)
)
```

## Combined Filter Function

```python
def market_ok_to_trade(symbol, is_crypto=False):
    if is_crypto:
        return True

    vix = get_vix()
    if vix > 35:
        return False

    if avoid_entry_time():
        return False

    if near_earnings(symbol, days=2):
        return False

    return True
```

## Working vs Failing

A market filter is working when the system takes fewer trades in hostile regimes and the skipped trades would have had poor expectancy. It should reduce churn during chop, reduce size during volatility spikes, and keep strategies aligned with their intended environment.

It is failing when it blocks almost every good trade, reacts too late, or is so broad that it hides strategy problems. A filter can also overfit if it only protects the exact historical drawdowns used to design it.

## Common Mistakes

- Using VIX to filter crypto as if it were a direct volatility measure.
- Treating ADX trend strength as trend direction.
- Adding too many filters until the backtest has too few trades.
- Ignoring earnings, Fed, and CPI gap risk.
- Forgetting that leveraged ETFs amplify broad-market regime changes.

## Interactions With Other Concepts

Market filters decide when [[entry_exit_techniques]] are allowed and which entry type is favored. High-volatility regimes require wider [[stop_loss_strategies]] or smaller [[position_sizing]].

[[technical_indicators_guide]] provides regime inputs such as ADX, moving averages, VWAP, volume, and volatility. [[risk_management_rules]] are the hard backstop when filters miss. [[backtesting_methodology]] must test filters across bull, bear, sideways, and crisis periods.

## In Our System

- `trader.py` currently has mechanical gates for `KILLSWITCH`, `PAUSE_FILE`, per-strategy killed flags, cash buffer, drawdown, consecutive losses, and day-start balance.
- It does not yet implement VIX, time-of-day, earnings, pre-market gap, or broad-market regime filters as shared executor rules.
- `strategies/leveraged_etf_momentum_strategy.py` embeds a regime filter by moving risk-off when 40-day momentum for TQQQ/SOXL is not positive.
- `strategies/vwap_strategy.py` requires trend efficiency above `0.3`, positive OFI, volume above `1.1x` average, and Z-score between `0.2` and `2.5`.
- `strategies/crypto_momentum_strategy.py` uses EMA cross and RSI range as a simple trend/momentum filter.
- `strategies/llm_sentiment_strategy.py` includes recent news headlines and simple price context, but it does not enforce a formal market-wide blackout.
- Improvement: add a shared `market_ok_to_trade()` layer before `place_buy()` and log each skipped trade with the exact filter reason.

## See Also

- [[risk_management_rules]]
- [[technical_indicators_guide]]
- [[entry_exit_techniques]]
- [[stop_loss_strategies]]
- [[position_sizing]]
- [[backtesting_methodology]]
