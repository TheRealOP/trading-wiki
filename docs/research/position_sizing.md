---
topic: "position sizing"
date: 2026-04-27
model: codex
tags: [quant/fundamentals, risk/position-sizing]
---

# Position Sizing

## Fixed Fractional (2% Rule)
Risk exactly 2% of account on every trade, regardless of conviction.
```python
def size_fixed_fractional(account_balance, entry, stop, risk_pct=0.02):
    risk_dollars = account_balance * risk_pct
    stop_distance = entry - stop
    shares = int(risk_dollars / stop_distance)
    return shares
```
- Simple, consistent, protects against ruin
- 2% is standard; aggressive traders use up to 5%
- At 2%: need 50 consecutive losses to wipe account

## Kelly Criterion
Mathematically optimal bet size given edge.
```python
def kelly_fraction(win_rate, avg_win, avg_loss):
    # win_rate: fraction of trades that win (0.0-1.0)
    # avg_win / avg_loss: in dollars
    b = avg_win / avg_loss   # reward/risk ratio
    p = win_rate
    q = 1 - win_rate
    k = (b * p - q) / b
    return max(k, 0)

# Always use Half-Kelly for safety:
bet_fraction = kelly_fraction(...) * 0.5
```
- Full Kelly is theoretically optimal but too volatile in practice
- Half-Kelly gives ~75% of returns with much lower drawdown
- Requires accurate win rate and avg win/loss estimates

## ATR-Based Sizing
Size position so 1 ATR move = 1% account risk.
```python
def size_atr(account_balance, atr, risk_pct=0.01):
    risk_dollars = account_balance * risk_pct
    shares = int(risk_dollars / atr)
    return shares
```
- Naturally adapts to volatility
- In high-vol markets: fewer shares. In calm markets: more shares.
- Best for strategies using ATR stops

## Max Position Size Caps
Always apply these caps regardless of formula:
```python
max_position_value = account_balance * 0.20  # never > 20% in one stock
max_shares = int(max_position_value / entry_price)
shares = min(calculated_shares, max_shares)
```

## Combined Formula (Used in This System)
```python
def calc_shares(strategy_balance, price, stop, max_risk_pct=0.02):
    risk_dollars = strategy_balance * max_risk_pct
    stop_distance = max(price - stop, price * 0.01)  # min 1% distance
    shares = math.floor(risk_dollars / stop_distance)
    # Cap at what the strategy balance can afford
    shares = min(shares, math.floor(strategy_balance / price))
    return shares
```

## Portfolio Heat
Total % of account at risk across all open trades.
```python
total_risk = sum(
    (entry - stop) * qty / account_balance
    for entry, stop, qty in open_trades
)
# Keep total_risk < 6% (3 trades x 2% each)
```
