---
topic: "technical indicators guide"
date: 2026-04-27
model: codex
tags: [quant/fundamentals, quant/indicators]
---

# Technical Indicators Guide

## RSI (Relative Strength Index)
```python
delta = df["Close"].diff()
gain = delta.clip(lower=0).rolling(14).mean()
loss = (-delta.clip(upper=0)).rolling(14).mean()
rs = gain / loss
rsi = 100 - (100 / (1 + rs))
```
- **< 30**: oversold — potential buy
- **> 70**: overbought — potential sell
- **Divergence**: price makes new high but RSI doesn't → bearish warning
- Best for mean reversion. Less reliable in strong trends.

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
- **Price touches lower band**: potential buy (mean reversion)
- **Price touches upper band**: potential sell
- **Squeeze** (bands narrow): low volatility → expect breakout
- **Band walk**: price rides upper band → strong trend, don't fade it

## VWAP (Volume-Weighted Average Price)
```python
df["VWAP"] = (df["Close"] * df["Volume"]).cumsum() / df["Volume"].cumsum()
```
- Reset each trading day
- Price above VWAP = bullish intraday bias
- Institutions use VWAP as benchmark — they buy dips to VWAP
- **Anchored VWAP**: start from a significant date (earnings, IPO)

## ATR (Average True Range)
```python
high_low = df["High"] - df["Low"]
high_close = (df["High"] - df["Close"].shift()).abs()
low_close = (df["Low"] - df["Close"].shift()).abs()
tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
atr = tr.rolling(14).mean()
```
- Measures volatility in price terms (not %)
- Use for stop placement and position sizing
- High ATR = wider stops needed

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
    rsi < 50          # not overbought
    and price > vwap  # above VWAP
    and macd > signal # momentum positive
    and vol_ratio > 1.2  # volume confirming
)
```
