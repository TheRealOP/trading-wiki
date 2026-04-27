---
topic: "position sizing"
date: 2026-04-27
model: codex
tags: [quant/fundamentals, risk/position-sizing]
---

> [!tip] Key Insight
> Position sizing decides whether a correct strategy survives its losing streaks. If size is based on excitement instead of defined risk, even good entries can bankrupt the system; a 5% stop on an oversized crypto position is not a small loss.

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
- At 2%: need many consecutive full-risk losses to destroy the account

## Kelly Criterion

Mathematically optimal bet size given edge.
```python
def kelly_fraction(win_rate, avg_win, avg_loss):
    b = avg_win / avg_loss
    p = win_rate
    q = 1 - win_rate
    k = (b * p - q) / b
    return max(k, 0)

bet_fraction = kelly_fraction(...) * 0.5  # half Kelly
```
- Full Kelly is theoretically optimal but too volatile in practice
- Half Kelly gives much of the return with lower drawdown
- Requires accurate win rate and average win/loss estimates

## ATR-Based Sizing

Size position so 1 ATR move equals a fixed account risk.
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

Always apply caps regardless of formula:
```python
max_position_value = account_balance * 0.20
max_shares = int(max_position_value / entry_price)
shares = min(calculated_shares, max_shares)
```

## Combined Formula

```python
def calc_shares(strategy_balance, price, stop, max_risk_pct=0.02):
    risk_dollars = strategy_balance * max_risk_pct
    stop_distance = max(price - stop, price * 0.01)
    shares = math.floor(risk_dollars / stop_distance)
    shares = min(shares, math.floor(strategy_balance / price))
    return shares
```

## Portfolio Heat

Total percent of account at risk across all open trades.
```python
total_risk = sum(
    (entry - stop) * qty / account_balance
    for entry, stop, qty in open_trades
)
# Keep total_risk < 6% (3 trades x 2% each)
```

## Working vs Failing

Sizing is working when a stopped-out trade loses the intended amount and no single trade dominates the equity curve. Losing streaks should hurt but not force emotional decisions or disable the whole account.

It is failing when high-volatility symbols receive the same share count as low-volatility symbols, when leveraged ETFs consume most of the risk budget, or when several correlated positions create hidden concentration. Another failure sign is a strategy with decent win rate but drawdowns too large to keep trading.

## Common Mistakes

- Sizing from available cash instead of stop distance.
- Forgetting that wider stops require smaller size.
- Treating all symbols as equally volatile.
- Ignoring correlated exposure across SPY, QQQ, TQQQ, SOXL, BTC, and ETH.
- Using Kelly estimates from too few trades.

## Interactions With Other Concepts

[[stop_loss_strategies]] give the denominator for share calculation: wider stop, smaller position. [[risk_management_rules]] cap per-trade risk, drawdown, and portfolio heat.

[[technical_indicators_guide]] provides ATR and volatility estimates for adaptive sizing. [[entry_exit_techniques]] affect stop distance and reward/risk, which determine whether the size is worth taking. [[market_conditions_filter]] should reduce size in high volatility or poor regimes. [[backtesting_methodology]] must evaluate whether sizing rules improve returns without unacceptable drawdown.

## In Our System

- `trader.py` implements share sizing in `calc_shares(balance, price, stop)`.
- Current parameters: `MAX_RISK_PCT = 0.02`, minimum stop distance is `price * 0.01`, and final shares are capped by `floor(strategy_balance / price)`.
- Every active strategy starts with `STRATEGY_START_BALANCE = 100.0`, and the account keeps `CASH_BUFFER = 100.0` unallocated.
- Equity buys use the calculated share count and bracket orders.
- Crypto buys in `place_buy()` use a fixed notional equal to 10% of the strategy balance instead of `calc_shares()`.
- `strategies/leveraged_etf_momentum_strategy.py` computes target weights using 20-day annualized volatility, `_TARGET_VOL = 0.25`, and `_MAX_RISK_PER_TRADE = 0.02`, but the executor still converts final orders through strategy balance constraints.
- Improvement: unify crypto sizing with stop-distance risk, add portfolio heat checks across correlated symbols, and record intended risk dollars per order.

## See Also

- [[stop_loss_strategies]]
- [[risk_management_rules]]
- [[technical_indicators_guide]]
- [[entry_exit_techniques]]
- [[market_conditions_filter]]
- [[backtesting_methodology]]
