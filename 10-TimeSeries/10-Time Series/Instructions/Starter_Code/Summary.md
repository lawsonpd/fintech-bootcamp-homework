### Pt. 1 conclusions

Prompt: _Based on your time series analysis, would you buy the yen now? Is the risk of the yen expected to increase or decrease? Based on the model evaluation, would you feel confident in using these models for trading?_

Our ARMA and ARIMA models both forecast the Yen futures dropping in the very near term (5 days). Neither of the models, however, have strong statistical confidence (i.e. low p-value), so I don't think they serve as a good basis for an investment decision. Our GARCH model did have good statistical significance, and since it predicts the volatility of the Yen futures increasing in the near term, I would choose not to buy now. If the GARCH model showed the volatility dropping, and the ARMA and ARIMA models had more statistical significance, then I may consider buying in 4 or 5 days (but of course at that point we'd have more data and could run the models again).



### Pt. 2 conclusions

Prompt: _Does this model perform better or worse on out-of-sample data compared to in-sample data?_

The LR model performed moderately well on the test set of our Yen futures data. It did not, however, do as well making predictions on the training data. Although certainly more analysis could be done, this leads me to think that in general a model that performs well on the test data will not perform as well on the training data. If the model was overfit it might perform better on the training set.
