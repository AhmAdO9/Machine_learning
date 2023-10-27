from flask import Flask, render_template, request, jsonify
import requests
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression.pkl', 'rb'))
@app.route('/', methods = ['GET'])
def Home():
    return render_template('index_html')


standard_to = StandardScaler()
@app.route('/predict', methods= ['POST'])
def predict():
    Fuel_Type_Diesel = 0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Kms_Driven2 = np.log(Kms_Driven)
        Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']
        Owner = int(request.form['Owner'])
        