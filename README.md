# 2021-DPS-AI
### This repository contains Data Processing, Exploratory Data Analysis and creating a time series predicting model for the dataset “Monatszahlen Verkehrsunfälle”.
### The dataset includes:
* 'Alkoholunfälle' i.e. Alcohol accidents
* 'Fluchtunfälle' i.e. Escape accidents
* 'Verkehrsunfälle' i.e. Traffic Accidents
### For forecasting, The models tried are as follows:
* SARIMAX (statistical)
* Holt-Winters-Exponential-Smoothing (statistical)
* Nbeats (deep learning)
* Prophet by fb (statistical)
### After comparing results, SARIMAX model is selected for forecasting and a flask API is deployed on heroku at https://dps-2021-ai.herokuapp.com/ that accepts a POST request containing date of prediction in the form of:
![input format](https://github.com/SiddharthSadhwani/2021-DPS-AI/blob/master/utils/input.png?raw=true)
### Output:
![output format](https://github.com/SiddharthSadhwani/2021-DPS-AI/blob/master/utils/output.png?raw=true)
### The jupyter notebook [a link](https://github.com/SiddharthSadhwani/2021-DPS-AI/blob/master/utils/input.png) covers the entire processing of generating historic visualisations, performing EDA and testing mulitple models.
