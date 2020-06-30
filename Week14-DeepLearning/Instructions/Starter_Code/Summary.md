# Predicting stocks with LSTM (long short-term memory) neural networks

## Overview

In this experiment, we compare two RNNs (recursive neural networks) trained to predict BTC (Bitcoin) closing prices. The target values, namely the closing prices, are identical for both RNNs, but the training sets are different: [FNG][1] ("Fear and greed") values for one, and prior closing prices for the other. The train/test sets and the parameters for both models are the same so that we can evaluate the models under the same conditions.

For each training set, we choose a window size that determines how many prior data points we use to predict a given target point; this is the training parameter we adjust in this experiment and compare results. The training sets are 70% of the total data and all of the data is scaled with a min-max scaler.

## Results

### Loss metrics

There was a significant gulf between the two models in terms of loss (mean squared error) evaluation. The loss values were:

- RNN trained on FNG with window size 3: **0.1166**
- RNN trained on closing prices with window size 3: **0.0283**

I don't find these results surprising, since I would expect any machine learning model to perform better when trained on incontrovertible financial data than when trained on numerical data based on human sentiment. It is known, however, that there are myriad feedback loops in the securities and trading ecosystem, so the influence of many factors is implicit in both data sets.

### Plot interpretation

From a more intuitive reading we might notice a more significant difference between the models. At the bottom of each notebook we have a plot showing the real and predicted values of the test sets.

The FNG plot of predicted values is quite unstable. There doesn't seem to be a reliable pattern to the predictions, and in fact they appear (visually) not to be strongly correlated with the actual values.

In the plot of the closing price model, on the other hand, the predicted values do seem to track the real values. The pair trend quite closely together, excepting some volatility in the actual price.

### Window size comparison

Window size is effectively the number of data points used to make a particular prediction. For example, a window size of 10 means that the price of day **n** is based on days **n-1, n-2,..., n-10**. 

I tested windows of 3, 5, 7 and 10, and it can be seen that the performance declines as window size grows:

- window 3
closing price: 0.0283
FNG: 0.1166
- window 5
closing price: 0.0487
FNG: 0.1391
- window 7
closing price: 0.0557
FNG: 0.1438
- window 10
closing price: 0.0754
FNG: 0.1744

This is somewhat surprising to me as even a 10 day window seems like a narrow prediction basis. A RNN can predict a price with fairly low loss using just 3 prior data points.

## Conclusion

These results suggest that closing price is a better indicator of future prices than fear and greed sentiments. In fact, a simple recursive neural network performs quite well at predicting prices even when trained on a relatively small data set and without much hyperparameter tuning. With more training and testing the loss could surely be reduced if only by a small margin. It's conceivable that one trained both on prior closing prices *and* FNG could achieve even higher accuracy.

[1]: https://alternative.me/crypto/fear-and-greed-index/