from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle
import os

app = Flask(__name__)
CORS(app)

# Adjusted path: Go one directory up from backend, then into model/
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'crop_yield_model.pkl')

# Normalize the path (handles .. properly)
model_path = os.path.normpath(model_path)

# Load the model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [float(data['soil_ph']), float(data['rainfall']), float(data['temperature'])]
    prediction = model.predict([features])[0]
    return jsonify({'yield': round(prediction, 2)})

if __name__ == '__main__':
    app.run(debug=True)
