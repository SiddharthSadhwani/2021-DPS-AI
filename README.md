# 2021-DPS-AI
## This repository contains Data Processing, Exploratory Data Analysis and creating a time series predicting model for the dataset " “Monatszahlen Verkehrsunfälle” that contains the record of accidents that occurred in Munich from 2020-2020.
## The dataset includes:
* 'Alkoholunfälle' i.e. Alcohol accidents
* 'Fluchtunfälle' i.e. Escape accidents
* 'Verkehrsunfälle' i.e. Traffic Accidents
## I preprocess the data, perform EDA by observing graphs and mathematical approaches.
## For forecasting, I try 4 different models that include statistical as well as deep learning models. The models tried are as follows:
* SARIMAX
* Holt-Winters-Exponential-Smoothing
* Nbeats
* Prophet by fb
## After comparing results, I decide to choose SARIMAX for forecasting and deploy a flask API on heroku at https://dps-2021-ai.herokuapp.com/
## The app accpets a POST request containing data of prediction in the form of:
![input format](https://github.com/SiddharthSadhwani/2021-DPS-AI/blob/master/utils/input.png?raw=true)
## Output:
![output format](https://github.com/SiddharthSadhwani/2021-DPS-AI/blob/master/utils/output.png?raw=true)
