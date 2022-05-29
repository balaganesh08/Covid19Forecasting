import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/dd')  
def dd():
    return render_template('Disease Description.html')

@app.route('/maps')
def maps():
    return render_template('Maps.html')

@app.route('/prediction')
def prediction():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    

    return render_template('index.html')

@app.route('/visual')
def visual():
    return render_template('visualize.html')

"""@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)"""

if __name__ == "__main__":
    app.run(debug=True)