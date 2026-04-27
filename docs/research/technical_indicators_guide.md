---
topic: "technical indicators guide"
date: 2026-04-27
model: codex
tags: [quant/fundamentals, quant/indicators]
---

> [!tip] Key Insight
> Indicators turn raw price and volume into repeatable context, but they are not predictions by themselves. Ignoring them leaves entries subjective; worshiping them creates false confidence, like buying every RSI 30 print during a strong downtrend.

# Technical Indicators Guide

## RSI (Relative Strength Index)
```python
delta = df["Close"].diff()
gain = delta.clip(lower=0).rolling(14).mean()
loss = (-delta.clip(upper=0)).rolling(14).mean()
rs = gain / loss
rsi = 100 - (100 / (1 + rs))
```
- **< 30**: oversold, potential buy
- **> 70**: overbought, potential sell
- **Divergence**: price makes a new high but RSI does not, a bearish warning
- Best for mean reversion; less reliable in strong trends

## MACD (Moving Average Convergence Divergence)
```python
ema12 = df["Close"].ewm(span=12).mean()
ema26 = df["Close"].ewm(span=26).mean()
macd = ema12 - ema26
signal = macd.ewm(span=9).mean()
histogram = macd - signal
```
- **MACD crosses above signal**: bullish
- **MACD crosses below signal**: bearish
- **Histogram growing**: momentum increasing
- Best for trend-following entries

## Bollinger Bands
```python
sma = df["Close"].rolling(20).mean()
std = df["Close"].rolling(20).std()
upper = sma + 2 * std
lower = sma - 2 * std
```
- **Price touches lower band**: potential buy for mean reversion
- **Price touches upper band**: potential sell
- **Squeeze**: low volatility, possible breakout setup
- **Band walk**: price rides upper band, strong trend, do not blindly fade it

## VWAP (Volume-Weighted Average Price)
```python
df["VWAP"] = (df["Close"] * df["Volume"]).cumsum() / df["Volume"].cumsum()
```
- Reset each trading day for intraday VWAP
- Price above VWAP = bullish intraday bias
- Institutions use VWAP as a benchmark; they often buy dips to VWAP
- **Anchored VWAP** starts from a significant date such as earnings, IPO, or a major low

## ATR (Average True Range)
```python
high_low = df["High"] - df["Low"]
high_close = (df["High"] - df["Close"].shift()).abs()
low_close = (df["Low"] - df["Close"].shift()).abs()
tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
atr = tr.rolling(14).mean()
```
- Measures volatility in price terms, not percent
- Use for stop placement and position sizing
- High ATR means wider stops or smaller position size

## EMA vs SMA

| | EMA | SMA |
|-|-----|-----|
| Reacts to price | Faster | Slower |
| Lag | Less | More |
| Best for | Trend following | Support/resistance |
| Common periods | 9, 21, 50, 200 | 20, 50, 200 |

```python
ema = df["Close"].ewm(span=period).mean()
sma = df["Close"].rolling(period).mean()
```

## Volume

- **Above avg volume on breakout**: confirms move, high conviction
- **Below avg volume on breakout**: weak, likely to fail
- **High volume on reversal candle**: exhaustion, trend may be ending
```python
avg_volume = df["Volume"].rolling(20).mean()
vol_ratio = df["Volume"].iloc[-1] / avg_volume.iloc[-1]
# vol_ratio > 1.5 = significant volume
```

## Combining Indicators (Signal Stacking)

Strong signals require 3+ indicators agreeing:
```python
buy_signal = (
    rsi < 50
    and price > vwap
    and macd > signal
    and vol_ratio > 1.2
)
```

## Working vs Failing

Indicators are working when they filter the trade universe into fewer, cleaner setups and the reason for each trade can be explained before entry. A good confluence signal should reduce impulsive trades and should remain understandable after the trade closes.

They are failing when every indicator says something different, when parameters are constantly adjusted to justify a desired trade, or when lagging signals enter after most of the move is already gone. Failure also shows up when an indicator optimized on one regime collapses in another.

## Common Mistakes

- Treating overbought as an automatic short signal in a strong uptrend.
- Combining several versions of the same idea and thinking it is diversification.
- Optimizing periods until the backtest looks perfect.
- Ignoring volume confirmation on breakouts.
- Forgetting that daily, hourly, and intraday indicators answer different questions.

## Interactions With Other Concepts

Indicators help define [[entry_exit_techniques]] and [[stop_loss_strategies]], but they must be converted into executable rules. ATR affects [[position_sizing]] because volatile instruments need fewer shares for the same dollar risk.

Indicator quality depends on [[market_conditions_filter]] because RSI, MACD, VWAP, and Bollinger Bands behave differently in trend, range, and crisis regimes. [[risk_management_rules]] cap the damage when indicators fail. [[backtesting_methodology]] checks whether indicator parameters survive out-of-sample data instead of just fitting the past.

## In Our System

- `strategies/rsi_macd_bb_strategy.py` implements RSI, MACD, and Bollinger Bands with `rsi_period = 14`, overbought/oversold at `70/30`, MACD `12/26/9`, Bollinger period `20`, standard deviation `2`, and a `confluence_window = 5`.
- `strategies/vwap_strategy.py` implements rolling VWAP, anchored VWAP, ATR, order-flow imbalance, trend efficiency, and volume profile levels. Current parameters include `VWAP_LOOKBACK = 20`, `AVWAP_LOOKBACK = 60`, `ATR_LOOKBACK = 14`, `PROFILE_LOOKBACK = 20`, `PROFILE_BINS = 24`, and `VOLUME_MULTIPLIER = 1.1`.
- `strategies/crypto_momentum_strategy.py` uses `EMA_FAST = 9`, `EMA_SLOW = 21`, `RSI_PERIOD = 14`, buy RSI range `40-65`, and sell RSI threshold `75`.
- `strategies/leveraged_etf_momentum_strategy.py` uses 40-day momentum and 20-day volatility for TQQQ/SOXL rotation.
- `strategies/llm_sentiment_strategy.py` calculates 5-day change, RSI(14), SMA5, SMA20, and volume versus 10-day average before asking Codex for a JSON signal.
- `trader.py` does not compute indicators itself; it executes signals produced by these strategy modules and applies shared risk controls.
- Improvement: store each indicator snapshot with the trade log so later backtests can compare entry context against realized P&L.

## See Also

- [[entry_exit_techniques]]
- [[stop_loss_strategies]]
- [[position_sizing]]
- [[market_conditions_filter]]
- [[risk_management_rules]]
- [[backtesting_methodology]]
