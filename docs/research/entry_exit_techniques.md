---
topic: "entry and exit techniques"
date: 2026-04-27
model: codex
tags: [quant/fundamentals, quant/entries]
---

# Entry & Exit Techniques

## Entry Types

### Breakout Entry
Enter when price clears a key level with volume confirmation.
```python
breakout_buy = (
    price > resistance_level
    and volume > avg_volume * 1.5   # must have volume
    and candle_body > atr * 0.5     # strong candle, not a wick
)
```
- Best in trending markets
- Fails often in ranging markets — use volume filter

### Pullback Entry (Preferred)
Wait for price to pull back to a support level before entering.
```python
pullback_buy = (
    price > vwap             # above VWAP (uptrend)
    and price <= sma20       # pulled back to SMA20
    and rsi < 50             # not overbought
    and volume < avg_volume  # low-volume pullback is healthy
)
```
- Better risk/reward than chasing breakouts
- Entry closer to stop = smaller loss if wrong

### Momentum Entry
Enter in direction of strong move, expecting continuation.
```python
momentum_buy = (
    price > ema9 > ema21     # stacked EMAs
    and macd > signal        # momentum positive
    and rsi > 50 and rsi < 65  # strong but not overbought
    and volume > avg_volume * 1.2
)
```
- Best for trending stocks/crypto
- Use trailing stop to ride the move

## Exit Types

### Fixed R-Multiple Target
Take profit at 2x or 3x the initial risk (R).
```python
risk = entry_price - stop_price      # 1R
target_2r = entry_price + 2 * risk
target_3r = entry_price + 3 * risk
```
- Simple and consistent
- Ensures positive expectancy even with <50% win rate
- At 2R target with 40% win rate: (0.4 * 2) - (0.6 * 1) = +0.2R per trade

### Trailing Stop Exit
```python
# Update each bar — never move backwards
trailing_stop = max(trailing_stop, price - atr * 2)
if price <= trailing_stop:
    exit_trade()
```
- Lets winners run
- Best for momentum/trend trades

### Partial Exit (Scale Out)
Sell half at 1R target, trail the rest.
```python
if price >= target_1r and not partial_taken:
    sell_half_position()
    move_stop_to_breakeven()
    partial_taken = True
```
- Locks in profit, removes pressure
- Gives remaining position room to run

### Signal Reversal Exit
Exit when the entry signal reverses.
```python
# VWAP strategy: exit when price crosses back below VWAP
if entry_signal == "vwap_breakout" and price < vwap:
    exit_trade("signal reversed — price below VWAP")
```

## Risk/Reward Minimums
Never take a trade with less than 2:1 reward/risk:
```python
reward = target - entry
risk = entry - stop
rr_ratio = reward / risk
if rr_ratio < 2.0:
    skip_trade("R/R below 2:1")
```
