---
topic: "backtesting methodology"
date: 2026-04-27
model: codex
tags: [quant/fundamentals, quant/backtesting]
---

> [!tip] Key Insight
> Backtesting is how a trading idea earns the right to risk live capital. If the test leaks future data or ignores costs, the strategy may look profitable on paper and fail immediately in execution, especially around stops and fast moves.

# Backtesting Methodology

## Key Metrics to Evaluate

```python
import numpy as np

def sharpe_ratio(returns, risk_free=0.05):
    excess = returns - risk_free / 252
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

```text
Total data: 4 years
In-sample: first 3 years, optimize parameters
Out-of-sample: last 1 year, validate without touching
```
- Never optimize on the test set; that is data leakage
- If OOS performance is much worse than IS, the strategy is likely overfit

## Walk-Forward Testing

```text
Window 1: train on Y1-Y2, test on Y3
Window 2: train on Y2-Y3, test on Y4
Window 3: train on Y3-Y4, test on Y5
Final: average OOS performance across all windows
```
- More realistic simulation of live trading
- Parameters should be stable across windows

## Avoiding Overfitting

```python
n_params = 5
min_trades_needed = n_params * 100
```
- Need enough trades per parameter being optimized
- Prefer simpler strategies
- If Sharpe improves only slightly from another parameter, do not add it

## Transaction Costs & Slippage

Always include realistic costs:
```python
commission = 0.0
slippage_pct = 0.001

effective_buy_price = price * (1 + slippage_pct)
effective_sell_price = price * (1 - slippage_pct)
```

## Look-Ahead Bias

```python
# WRONG: uses today's close to make today's decision.
signal = df["Close"].iloc[-1] > df["Close"].rolling(20).mean().iloc[-1]

# CORRECT: use previous bar's completed data.
signal = df["Close"].iloc[-2] > df["Close"].rolling(20).mean().iloc[-2]
df["signal"] = (df["Close"] > df["Close"].rolling(20).mean()).shift(1)
```

## Honest Backtest Checklist

- [ ] No look-ahead bias
- [ ] Transaction costs included
- [ ] Slippage and gap risk modeled
- [ ] Out-of-sample validation done
- [ ] At least 100 trades in test period
- [ ] Parameters stable across walk-forward windows
- [ ] Tested on bull, bear, sideways, and crisis regimes
- [ ] Max drawdown is tolerable in live trading
- [ ] Live execution rules match the backtest rules

## Working vs Failing

A backtest is working when its assumptions match live execution and the strategy still performs outside the optimization sample. The live trade log should resemble the simulated distribution of wins, losses, drawdowns, holding times, and slippage.

It is failing when the equity curve is too smooth, performance collapses out of sample, or trades depend on prices that were not known at decision time. It also fails when live order behavior, bracket stops, crypto manual exits, or cash constraints are absent from the simulation.

## Common Mistakes

- Using same-bar close for both signal and fill.
- Ignoring survivorship bias, delisted symbols, and unavailable historical constituents.
- Excluding slippage because commissions are zero.
- Optimizing indicator periods with too few trades.
- Forgetting that stop-loss behavior requires intraday data or conservative gap assumptions.

## Interactions With Other Concepts

Backtests validate whether [[technical_indicators_guide]] signals have edge after realistic execution. They must include [[entry_exit_techniques]], [[stop_loss_strategies]], and [[position_sizing]] exactly as they will run live.

[[risk_management_rules]] should be simulated, including kills, daily stops, and portfolio heat. [[market_conditions_filter]] must be tested across multiple regimes to prove it improves robustness instead of simply reducing trade count.

## In Our System

- `backtest_spy_qqq_mean_reversion.py` exists as a local backtest script, while live execution is handled by `trader.py`.
- `trader.py` logs fills through `append_trade_log()` and `db.log_trade()`, and computes live Sharpe with `db.compute_live_sharpe()` after sells.
- Current live assumptions: equities use limit buys at `price * 1.005`, bracket stop loss, 2R take-profit target, `MAX_RISK_PCT = 0.02`, `MAX_DRAWDOWN_PCT = 0.10`, and `CASH_BUFFER = 100.0`.
- Strategy parameters to mirror in backtests include RSI/MACD/Bollinger confluence, VWAP profile breakout settings, crypto EMA9/EMA21 with 5% stop, leveraged ETF 40-day momentum with 20-day volatility, and LLM sentiment's SMA/RSI/news inputs.
- Improvement: build a common backtest harness that imports the same strategy classes, models Alpaca order behavior, simulates bracket/manual crypto exits, and writes comparable metrics to the wiki.

## See Also

- [[technical_indicators_guide]]
- [[entry_exit_techniques]]
- [[stop_loss_strategies]]
- [[position_sizing]]
- [[risk_management_rules]]
- [[market_conditions_filter]]
