---
topic: "entry and exit techniques"
date: 2026-04-27
model: codex
tags: [quant/fundamentals, quant/entries]
---

> [!tip] Key Insight
> Entries and exits define the trade's actual edge, not just its story. A strong idea with a late entry and vague exit can still lose money; chasing a breakout after the volume spike is the common version.

# Entry & Exit Techniques

## Entry Types

### Breakout Entry

Enter when price clears a key level with volume confirmation.
```python
breakout_buy = (
    price > resistance_level
    and volume > avg_volume * 1.5
    and candle_body > atr * 0.5
)
```
- Best in trending markets
- Fails often in ranging markets, so use a volume and regime filter

### Pullback Entry (Preferred)

Wait for price to pull back to a support level before entering.
```python
pullback_buy = (
    price > vwap
    and price <= sma20
    and rsi < 50
    and volume < avg_volume
)
```
- Better risk/reward than chasing breakouts
- Entry closer to stop means smaller loss if wrong

### Momentum Entry

Enter in direction of strong move, expecting continuation.
```python
momentum_buy = (
    price > ema9 > ema21
    and macd > signal
    and rsi > 50 and rsi < 65
    and volume > avg_volume * 1.2
)
```
- Best for trending stocks, crypto, and rotation systems
- Use trailing stops or signal exits to ride the move

## Exit Types

### Fixed R-Multiple Target

Take profit at 2x or 3x the initial risk.
```python
risk = entry_price - stop_price
target_2r = entry_price + 2 * risk
target_3r = entry_price + 3 * risk
```
- Simple and consistent
- Positive expectancy is possible even with below-50% win rate
- At 2R target with 40% win rate: `(0.4 * 2) - (0.6 * 1) = +0.2R`

### Trailing Stop Exit

```python
trailing_stop = max(trailing_stop, price - atr * 2)
if price <= trailing_stop:
    exit_trade()
```
- Lets winners run
- Best for momentum and trend trades

### Partial Exit (Scale Out)

Sell half at 1R target, trail the rest.
```python
if price >= target_1r and not partial_taken:
    sell_half_position()
    move_stop_to_breakeven()
    partial_taken = True
```
- Locks in profit and reduces pressure
- Gives remaining position room to run

### Signal Reversal Exit

Exit when the entry signal reverses.
```python
if entry_signal == "vwap_breakout" and price < vwap:
    exit_trade("signal reversed - price below VWAP")
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

## Working vs Failing

Entry and exit rules are working when trades have a repeatable reason, clear invalidation, and a planned target before the order is sent. A clean trade log should make it obvious whether the system entered on breakout, pullback, momentum, sentiment, or rotation.

They are failing when entries are mostly late, exits are emotional, or sell decisions happen only after profits disappear. Another failure pattern is mixing entry styles, such as buying a breakout but using a mean-reversion exit.

## Common Mistakes

- Entering before confirmation and calling it "early."
- Entering after confirmation is exhausted and calling it "safe."
- Taking trades with no objective target.
- Exiting winners too early while letting losers reach full stop.
- Changing the exit logic after seeing unrealized P&L.

## Interactions With Other Concepts

Entries determine where [[stop_loss_strategies]] belong and whether [[position_sizing]] produces a reasonable share count. Exits are the practical expression of [[risk_management_rules]], especially stops, targets, and forced sells.

[[technical_indicators_guide]] supplies confirmation signals such as RSI, MACD, VWAP, Bollinger Bands, moving averages, and volume. [[market_conditions_filter]] decides which entry family is appropriate. [[backtesting_methodology]] measures whether the entry/exit pair has positive expectancy after costs.

## In Our System

- `trader.py` accepts each strategy's `signal`, `price`, `stop`, and `reason`, then executes buys and sells through `place_buy()` and `place_sell()`.
- Equity entries use limit buys at `price * 1.005`, bracket stop loss at the supplied stop, and take profit at 2R.
- Crypto entries use notional market buys; stops and 2R targets are checked manually each signal cycle.
- `strategies/rsi_macd_bb_strategy.py` enters on RSI/MACD/Bollinger confluence and exits on overbought/reversal conditions.
- `strategies/vwap_strategy.py` enters on VWAP/AVWAP/volume-profile breakout with OFI, volume, trend efficiency, and Z-score confirmation; exits on VWAP, AVWAP, or OFI failure. It is currently benched in `trader.py`.
- `strategies/crypto_momentum_strategy.py` enters when EMA9 crosses above EMA21 with RSI between 40 and 65, and exits on EMA cross down or RSI above 75.
- `strategies/leveraged_etf_momentum_strategy.py` rebalances on Fridays into the better 40-day momentum leader if momentum is positive; otherwise it rotates out.
- `strategies/llm_sentiment_strategy.py` enters or exits from Codex-generated JSON using price, simple technicals, and recent news.
- Improvement: add explicit order-type policy per strategy, partial exits, trailing exits, and structured trade reasons that separate entry type from exit type.

## See Also

- [[technical_indicators_guide]]
- [[stop_loss_strategies]]
- [[position_sizing]]
- [[risk_management_rules]]
- [[market_conditions_filter]]
- [[backtesting_methodology]]
