---
topic: "backtesting methodology"
date: 2026-04-27
model: codex
tags: [quant/fundamentals, quant/backtesting]
---

# Backtesting Methodology

## Key Metrics to Evaluate

```python
import numpy as np

def sharpe_ratio(returns, risk_free=0.05):
    excess = returns - risk_free / 252  # daily risk-free rate
    return np.sqrt(252) * excess.mean() / excess.std()

def sortino_ratio(returns, risk_free=0.05):
    excess = returns - risk_free / 252
    downside = returns[returns < 0].std()
    return np.sqrt(252) * excess.mean() / downside

def max_drawdown(equity_curve):
    peak = equity_curve.cummax()
    drawdown = (equity_curve - peak) / peak
    return drawdown.min()

def profit_factor(trades):
    gross_profit = sum(t["pnl"] for t in trades if t["pnl"] > 0)
    gross_loss = abs(sum(t["pnl"] for t in trades if t["pnl"] < 0))
    return gross_profit / gross_loss if gross_loss > 0 else float("inf")
```

| Metric | Minimum | Good | Excellent |
|--------|---------|------|-----------|
| Sharpe | > 0.5 | > 1.0 | > 2.0 |
| Sortino | > 0.5 | > 1.5 | > 3.0 |
| Max Drawdown | < 30% | < 15% | < 10% |
| Profit Factor | > 1.0 | > 1.5 | > 2.0 |
| Win Rate | > 40% | > 50% | > 60% |

## In-Sample / Out-of-Sample Split
```
Total data: 4 years
├── In-sample (training): first 3 years  → optimize parameters
└── Out-of-sample (test): last 1 year   → validate (never touch during optimization)
```
- **Never optimize on the test set** — that's data leakage
- If OOS performance is much worse than IS: overfitted

## Walk-Forward Testing
More rigorous than single split. Rolls forward in time:
```
Window 1: train on Y1-Y2, test on Y3
Window 2: train on Y2-Y3, test on Y4
Window 3: train on Y3-Y4, test on Y5
Final: average OOS performance across all windows
```
- More realistic simulation of live trading
- Parameters should be stable across windows

## Avoiding Overfitting
```python
# Rule of thumb: need at least 100 trades per parameter being optimized
# If your strategy has 5 parameters: need >= 500 trades in backtest

n_params = 5
min_trades_needed = n_params * 100

# Prefer simpler strategies — fewer parameters = more robust
# If Sharpe only improves by 0.1 when adding a parameter: don't add it
```

## Transaction Costs & Slippage
Always include realistic costs:
```python
commission = 0.0  # Alpaca is commission-free
slippage_pct = 0.001  # 0.1% slippage on market orders (conservative)

# For limit orders (less slippage):
slippage_pct = 0.0005

effective_buy_price = price * (1 + slippage_pct)
effective_sell_price = price * (1 - slippage_pct)
```

## Look-Ahead Bias (Most Common Mistake)
```python
# WRONG — uses today's close to make today's decision:
signal = df["Close"].iloc[-1] > df["Close"].rolling(20).mean().iloc[-1]

# CORRECT — use previous bar's data:
signal = df["Close"].iloc[-2] > df["Close"].rolling(20).mean().iloc[-2]
# Or use shift(1):
df["signal"] = (df["Close"] > df["Close"].rolling(20).mean()).shift(1)
```

## Honest Backtest Checklist
- [ ] No look-ahead bias (using future data)
- [ ] Transaction costs included
- [ ] Out-of-sample validation done
- [ ] At least 100 trades in test period
- [ ] Parameters stable across walk-forward windows
- [ ] Tested on multiple market regimes (bull, bear, sideways)
- [ ] Max drawdown is tolerable in live trading
