from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form['location']
    time = int(request.form['time']) 
    day_of_week = request.form['day_of_week']

    location_mapping = {'A': 0, 'B': 1, 'C': 2}
    day_mapping = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

    X_input = np.array([[location_mapping.get(location, -1), time, day_mapping.get(day_of_week, -1)]])
    
    if X_input[0][0] == -1 or X_input[0][2] == -1:
        return render_template('index.html', prediction_text="Invalid location or day of the week")

    prediction = model.predict(X_input)

    return render_template('index.html', prediction_text=f'Parking availability: {prediction[0]}')

if __name__ == "__main__":
    app.run(debug=True)
