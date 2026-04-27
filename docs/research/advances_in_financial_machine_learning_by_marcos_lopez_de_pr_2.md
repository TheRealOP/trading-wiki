---
topic: ""Advances in Financial Machine Learning" by Marcos Lopez de Prado"
date: 2026-04-09
model: Pro
tags: [agent/research]
---

# Triple-Barrier Method & Meta-Labeling

## Key Insight
The Triple-Barrier Method, a cornerstone of [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]], defines trade outcomes by setting three barriers: a [[take-profit]] limit (upper), a [[stop-loss]] (lower), and a maximum holding period (vertical). This structure captures path-dependency and [[volatility]], creating higher-quality labels for [[machine learning]] models compared to fixed-horizon methods. [[Meta-Labeling]] then uses a second model to determine the likelihood of the primary model's success, enabling sophisticated [[bet sizing]] and risk control.

## The Math
Given a starting price $p_t$, we define dynamic barriers based on [[volatility]] $\sigma_t$:
- Upper Barrier (Take Profit): $u_t = p_t (1 + \alpha_u \sigma_t)$, for $\alpha_u > 0$
- Lower Barrier (Stop Loss): $l_t = p_t (1 - \alpha_l \sigma_t)$, for $\alpha_l > 0$

The label $y \in \{-1, 1, 0\}$ is assigned based on the first barrier the price path $\{p_{t+\Delta t}\}$ touches within a maximum holding period $T$:
$$
y = \begin{cases}
1 & \text{if } p_{t+\Delta t} \ge u_t \text{ first} \\
-1 & \text{if } p_{t+\Delta t} \le l_t \text{ first} \\
0 & \text{if time expires at } t+T
\end{cases}
$$
For [[Meta-Labeling]], a primary model predicts the side $ \hat{y} \in \{-1, 1\}$. The meta-model is trained on a binary label $m$:
$$
m = \begin{cases}
1 & \text{if } \hat{y} \cdot y > 0 \text{ (primary model was right)} \\
0 & \text{if } \hat{y} \cdot y \le 0 \text{ (primary model was wrong or didn't profit)}
\end{cases}
$$
The output of this second model, $P(m=1)$, is the confidence for [[bet sizing]].

## Strategy Logic
1.  For each data point, calculate a measure of recent [[volatility]], e.g., the standard deviation of returns over a 20-day window.
2.  Set the triple barriers based on this [[volatility]] and predefined multiples ($\alpha_u, \alpha_l$).
3.  Label the data by observing which of the three barriers is hit first.
4.  Train a primary [[machine learning]] model (e.g., RandomForest) on relevant features to predict the side of the trade ($y \in \{-1, 1\}$).
5.  Train a secondary "meta" model on the binary labels ($m \in \{0, 1\}$) to predict the *probability* of the primary model being correct.
6.  Use the primary model for direction and the meta-model's probability output to size the position, referencing [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]].

## Parameters
-   `vol_window`: Lookback period for calculating [[volatility]].
-   `take_profit_mult`: Multiplier ($\alpha_u$) for setting the upper barrier.
-   `stop_loss_mult`: Multiplier ($\alpha_l$) for setting the lower barrier.
-   `max_hold_bars`: The vertical barrier; maximum time to hold a position.

## Risks
-   [[Overfitting]]: High risk due to the complexity of two models. Requires robust backtesting like Purged K-Fold [[cross-validation]].
-   [[Feature Engineering]]: Performance is highly sensitive to the quality of input features, which must be stationary.
-   [[Look-ahead bias]]: Volatility and barriers must be calculated strictly using information available at the time of the decision.

## Related
-   [[advances_in_financial_machine_learning_by_marcos_lopez_de_pr]]
-   [[quantitative_risk_management_position_sizing]]
-   [[volatility_breakout_strategies]]
-   [[backtest_statistical_edge_in_short_term_mean_reversion]]
-   [[kelly_criterion_optimal_bet_sizing_for_small_portfolios]]

## Sources
-   "Advances in Financial Machine Learning" by Marcos Lopez de Prado

## Next Steps
- [ ] Implement Triple-Barrier labeling on [[QQQ]] tick data.
- [ ] Test the predictive power of features like [[order flow imbalance]] with the primary model.
- [ ] Evaluate the performance improvement of using a [[Meta-Labeling]] model for [[bet sizing]] vs. a fixed size.
- [ ] Research and implement Purged K-Fold [[cross-validation]] for a time-series backtest.