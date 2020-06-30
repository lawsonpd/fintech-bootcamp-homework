# Predicting stocks with LSTM (long short-term memory) neural networks

## Overview

In this experiment, we compare two RNNs (recursive neural networks) trained to predict BTC (Bitcoin) closing prices. The target values, namely the closing prices, are identical for both RNNs, but the training sets are different: [FNG][1] ("Fear and greed") values for one, and prior closing prices for the other. The train/test sets and the parameters for both models are the same so that we can evaluate the models under the same conditions.

For each training set, we choose a window size that determines how many prior data points we use to predict a given target point; my analysis is based on a window of 10 days. The training sets are 70% of the total data and all of the data is scaled with a min-max scaler.

## Results

### Loss metrics

The models performed nearly the same in terms of loss (mean squared error) evaluation. The loss values were:

- RNN trained on FNG: **0.1548**
- RNN trained on closing prices: **0.1823**

I find these results somewhat surprising, since I would expect any machine learning model to perform better when trained on incontrovertible financial data than when trained on numerical data based on human sentiment. It is known, however, that there are myriad feedback loops involving the psychology of traders, the chatter of media outlets and the rest of the financial ecosystem that can coax the price of securities to and fro.

### Plot interpretation

From a more intuitive reading we might notice a more significant difference between the models. At the bottom of each notebook we have a plot showing the real and predicted values of the test sets.

The FNG plot of predicted values has an odd shape. Although it's overall loss is lower than the closing price model, there doesn't seem to be a reliable pattern to the predictions, and in fact they appear (visually) to be *anticorrelated* with the real values.

In the plot of the closing price model, on the other hand, the predicted values do seem to track the real values, albeit missing the actual mark by quite a lot (at least upon visual inspection). The predicted values trend upward as the actual values do (excepting the sharp drop at the end).

Neither model, in my opinion, is suitable for real-world use, but if I were to choose a model to continue to develop—experimenting with different parameters, training sets, etc.—I would select the one based on closing prices. I think a fundamental principle of the methodology of machine learning is that these models are tools to be used *by humans* to augment our own ability to reason and make decisions. With that in mind, I see (though I may be wrong) that somehow the price-trained model is attuned to something that the other has missed. I would feel more confident using, and I think I'd extract more value from, a model that comports with my own intuition.

[1]: https://alternative.me/crypto/fear-and-greed-index/