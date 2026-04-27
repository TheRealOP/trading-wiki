---
topic: "risk management rules"
date: 2026-04-27
model: codex
tags: [quant/fundamentals, risk/management]
---

# Risk Management Rules

## Daily Loss Limit
Stop trading for the day if down more than 3% of account.
```python
day_start_equity = get_equity_at_open()
current_equity = get_current_equity()
daily_loss_pct = (current_equity - day_start_equity) / day_start_equity

if daily_loss_pct < -0.03:
    pause_all_trading()
    notify("Daily loss limit hit — trading paused")
```

## Max Drawdown from Peak
Kill a strategy if it falls 10% from its peak balance.
```python
drawdown = (peak_balance - current_balance) / peak_balance
if drawdown > 0.10:
    kill_strategy("10% drawdown from peak")
```

## Consecutive Loss Rule
After 3 consecutive losses, stop and reassess.
```python
if consecutive_losses >= 3:
    kill_strategy("3 consecutive losses")
```
- Prevents revenge trading and over-trading in bad conditions
- Reset count on first winning trade

## Portfolio Heat (Correlated Risk)
Never have more than 6% total account at risk simultaneously.
```python
# Don't hold TQQQ + QQQ + SPY at same time — all correlated
# Don't hold BTC + ETH as two full positions — highly correlated

correlated_groups = {
    "us_equity": ["SPY", "QQQ", "TQQQ", "SOXL"],
    "crypto": ["BTCUSD", "ETHUSD"],
}
# Max 1 position per correlated group at a time
```

## News/Earnings Blackout
Avoid entering new positions 30 min before and after:
- Fed announcements (FOMC)
- Earnings releases
- Major economic data (CPI, NFP, GDP)
```python
# These events cause unpredictable gaps that invalidate stops
```

## Time of Day Filters
- **First 15 min (9:30–9:45)**: avoid — spreads wide, price discovery chaotic
- **Lunch (12:00–13:00)**: low volume, choppy — reduce size or skip
- **Last 15 min (3:45–4:00)**: closing auctions, can be erratic

## VIX Regime Filter
Scale down position size when VIX is elevated:
```python
import yfinance as yf
vix = float(yf.Ticker("^VIX").fast_info["last_price"])

if vix > 30:
    risk_pct = 0.01   # half size in high volatility
elif vix > 20:
    risk_pct = 0.015  # reduced size
else:
    risk_pct = 0.02   # normal size
```

## Hard Rules (Never Break)
1. Never risk more than 2% per trade
2. Never hold through earnings without explicit earnings strategy
3. Never add to a losing position ("averaging down")
4. Always have a stop before entering
5. Never move a stop loss further away once set
