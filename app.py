import pandas as pd
import pickle
import re
from flask import Flask, render_template,request,flash,jsonify
import statsmodels.api as sm
import datetime
import json

app=Flask(__name__)
app.secret_key='DPS-2021'

@app.route("/", methods=['GET', 'POST'])
def home():
	model=pickle.load(open("models/ARIMA.sav","rb"))
	if request.method == "POST":
		json_data = request.json
		year=json_data['year']
		month=json_data['month']
		pred=str(year)+"-"+str(month)+"-"+"01"
		return {'prediction':int(model.get_prediction(pred).predicted_mean.values.tolist()[0])}
	return "unsuccessful"

if __name__ == '__main__':
	app.run()    