---
topic: "risk management rules"
date: 2026-04-27
model: codex
tags: [quant/fundamentals, risk/management]
---

> [!tip] Key Insight
> Risk rules are the circuit breakers that keep a bad day from becoming a bad month. Without them, a strategy can keep firing after the market regime has changed, like taking repeated long signals during a volatility shock.

# Risk Management Rules

## Daily Loss Limit

Stop trading for the day if down more than 3% of account.
```python
day_start_equity = get_equity_at_open()
current_equity = get_current_equity()
daily_loss_pct = (current_equity - day_start_equity) / day_start_equity

if daily_loss_pct < -0.03:
    pause_all_trading()
    notify("Daily loss limit hit - trading paused")
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
correlated_groups = {
    "us_equity": ["SPY", "QQQ", "TQQQ", "SOXL"],
    "crypto": ["BTCUSD", "ETHUSD"],
}
# Max 1 position per correlated group at a time
```

## News/Earnings Blackout

Avoid entering new positions 30 minutes before and after:
- Fed announcements such as FOMC
- Earnings releases
- Major economic data such as CPI, NFP, GDP
```python
# These events cause unpredictable gaps that invalidate stops.
```

## Time of Day Filters

- **First 15 min (9:30-9:45)**: avoid; spreads wide, price discovery chaotic
- **Lunch (12:00-13:00)**: low volume, choppy; reduce size or skip
- **Last 15 min (3:45-4:00)**: closing auctions can be erratic

## VIX Regime Filter

Scale down position size when VIX is elevated:
```python
import yfinance as yf
vix = float(yf.Ticker("^VIX").fast_info["last_price"])

if vix > 30:
    risk_pct = 0.01
elif vix > 20:
    risk_pct = 0.015
else:
    risk_pct = 0.02
```

## Hard Rules (Never Break)

1. Never risk more than 2% per trade.
2. Never hold through earnings without an explicit earnings strategy.
3. Never add to a losing position.
4. Always have a stop before entering.
5. Never move a stop loss farther away once set.

## Working vs Failing

Risk management is working when the system stops itself before the trader needs to intervene. Drawdowns stay within expected bounds, a losing streak pauses the strategy, and cash remains available.

It is failing when the same loss pattern repeats across strategies, when correlated positions all lose together, or when a kill switch triggers only after account-level damage. Risk controls also fail when they exist in documentation but not in executable code.

## Common Mistakes

- Counting each strategy independently while ignoring shared market beta.
- Having stops but no rule for when a strategy is disabled.
- Restarting a killed strategy without reviewing the failure mode.
- Reducing risk only after the drawdown has already happened.
- Skipping event filters because the setup looks too good.

## Interactions With Other Concepts

[[position_sizing]] and [[stop_loss_strategies]] implement the per-trade risk budget. [[entry_exit_techniques]] must produce trades with enough reward/risk to justify that budget.

[[market_conditions_filter]] decides when the system should reduce size or avoid trading altogether. [[technical_indicators_guide]] can detect regime and volatility shifts, but risk rules decide what to do with that information. [[backtesting_methodology]] validates whether rules reduce tail risk without overfitting.

## In Our System

- `trader.py` implements shared risk controls in `run_signals()`, `check_strategy_kill()`, `place_buy()`, and `place_sell()`.
- Current parameters: `MAX_RISK_PCT = 0.02`, `MAX_DRAWDOWN_PCT = 0.10`, `CONSECUTIVE_LOSSES = 3`, and `CASH_BUFFER = 100.0`.
- The executor respects `KILLSWITCH` and `PAUSE_FILE` before processing signals.
- Per-strategy state tracks `balance`, `peak_balance`, `day_start_balance`, open trades, wins, losses, consecutive losses, killed flag, and kill reason.
- `check_strategy_kill()` kills a strategy when equity falls more than 10% from peak, when consecutive losses reach 3, or when strategy equity is below day-start balance.
- Equity positions get bracket stop and target orders; crypto stop/target enforcement is manual inside `run_signals()`.
- Improvement: add explicit account-level daily loss percentage, correlated group exposure checks, earnings/FOMC blackout integration, and VIX-based risk scaling.

## See Also

- [[position_sizing]]
- [[stop_loss_strategies]]
- [[market_conditions_filter]]
- [[entry_exit_techniques]]
- [[technical_indicators_guide]]
- [[backtesting_methodology]]
