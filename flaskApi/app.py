import os
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the models
random_forest_model = joblib.load('Model/credit_scoring_random_forest_model.pkl')
gradientBoosting_model = joblib.load('Model/credit_scoring_gradientBoosting_model.pkl')

@app.route('/')
def home():
    return "Welcome to the Credit Scoring Model API!"

# Endpoint to make predictions with Random Forest
@app.route('/predict/rf', methods=['POST'])
def predict_rf():
    try:
        # Get data from the POST request
        data = request.get_json()

        # Assume data is a list of feature values (e.g., [feature1, feature2, ..., featureN])
        features = np.array(data['features']).reshape(1, -1)  # Reshape for a single prediction

        # Make prediction using the Random Forest model
        prediction = random_forest_model.predict(features)

        # Return the prediction result as JSON
        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to make predictions with Gradient Boosting
@app.route('/predict/gb', methods=['POST'])
def predict_gb():
    try:
        # Get data from the POST request
        data = request.get_json()

        # Assume data is a list of feature values (e.g., [feature1, feature2, ..., featureN])
        features = np.array(data['features']).reshape(1, -1)  # Reshape for a single prediction

        # Make prediction using the Gradient Boosting model
        prediction = gradientBoosting_model.predict(features)

        # Return the prediction result as JSON
        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
