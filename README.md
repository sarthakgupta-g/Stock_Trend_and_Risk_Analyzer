# Stock_Trend_and_Risk_Analyzer

## Overview

This project analyzes a stock's price movement, trading volume, volatility, drawdowns, and moving-average signals using Python.

The goal is to practice using **Pandas, NumPy, and Matplotlib** to perform quantitative financial analysis and evaluate whether a simple moving-average strategy provides evidence of stronger subsequent returns.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* CSV data

## Dataset

The dataset contains 60 days of simulated stock data with the following variables:

* `Date` — Trading date
* `Price` — Daily closing price
* `Volume` — Daily trading volume
* `Daily_return` — Daily percentage return
* `Abs_return` — Absolute daily return
* `Rolling_volatility` — Rolling measure of return volatility

The stock increased from approximately **$100 to $150** over the 60-day period.

## Analysis Performed

### 1. Moving Averages

Two moving averages were calculated:

* **MA5** — 5-day moving average
* **MA20** — 20-day moving average

These were used to smooth short-term price fluctuations and identify the stock's underlying trend.

The MA5 remained above the MA20 once enough data was available, indicating a consistently bullish trend throughout the dataset.

### 2. Rolling Volatility

Rolling volatility was analyzed to determine how the magnitude of daily price movements changed over time.

The stock experienced periods of increased short-term movement while maintaining its overall upward trend.

### 3. Drawdown Analysis

A running peak price was calculated using the cumulative maximum:

```python
data["Peak"] = data["Price"].cummax()
```

Drawdown was then calculated as:

```python
data["Drawdown"] = (data["Price"] - data["Peak"]) / data["Peak"]
```

The largest drawdown was approximately **−2.6%**.

Compared with the stock's approximately 50% overall increase, the drawdowns were relatively shallow.

### 4. Volume Analysis

Trading volume generally increased as the stock price increased.

However, the observed price dips did not appear to coincide with unusually large volume spikes. The size of the pullbacks also remained relatively small throughout the dataset.

### 5. Moving-Average Trading Signal

A simple trading signal was created using the relationship between MA5 and MA20:

* `1` → MA5 > MA20 → bullish signal
* `0` → MA5 ≤ MA20 → non-bullish signal

The signal was created using NumPy:

```python
data["Signal"] = np.where(
    data["MA20"].isna(),
    np.nan,
    np.where(data["MA5"] > data["MA20"], 1, 0)
)
```

Once MA20 became available, all 41 usable observations produced a bullish signal.

### 6. Subsequent Return Analysis

To determine whether the bullish signal corresponded with stronger future returns, the following day's return was calculated:

```python
data["Next_day_return"] = data["Daily_return"].shift(-1)
```

The results were:

| Metric                         | Average Return |
| ------------------------------ | -------------: |
| Bullish-signal next-day return |         0.674% |
| Overall next-day return        |         0.690% |

The bullish-signal return was therefore slightly **below** the overall average return.

## Key Findings

The analysis suggests that:

* The stock experienced a strong and relatively consistent upward trend.
* MA5 remained above MA20, indicating a persistent bullish regime.
* Volatility fluctuated but did not prevent the overall upward movement.
* Drawdowns were relatively shallow, with a maximum drawdown of approximately −2.6%.
* Trading volume generally increased alongside the stock price.
* The moving-average signal did **not** demonstrate stronger subsequent returns than the stock's overall average in this dataset.
* Because the stock never entered a bearish MA5/MA20 regime, the dataset does not provide a meaningful comparison between bullish and bearish signals.

## Conclusion

This project demonstrates how basic quantitative indicators can be combined to evaluate market behavior.

Although the moving-average relationship consistently indicated a bullish trend, the signal did not provide evidence of superior next-day returns. The bullish-signal average return of **0.674%** was slightly lower than the overall average of **0.690%**.

This highlights an important principle in quantitative finance: **a signal that describes an existing trend does not necessarily predict future returns.**

## Skills Practiced

* Reading CSV data with Pandas
* DataFrame inspection
* Rolling-window calculations
* Moving averages
* Boolean conditions
* NumPy `where`
* Handling missing values
* Cumulative maximums
* Drawdown calculations
* Return analysis
* Basic strategy evaluation
* Data visualization with Matplotlib
* Financial interpretation of quantitative results

## Future Improvements

Potential extensions include:

* Test the strategy on a dataset containing both bullish and bearish periods.
* Calculate cumulative strategy returns.
* Compare the strategy against a buy-and-hold strategy.
* Add transaction costs.
* Analyze Sharpe ratio and other risk-adjusted metrics.
* Test different moving-average periods.
* Analyze whether high-volume days predict larger subsequent returns.
* Use real historical market data instead of simulated data.

