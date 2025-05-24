from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains (good for local dev)

# Load your trained model (make sure model.pkl is in the same folder or adjust path)
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Input validation
    try:
        area = float(data['area'])
        bedrooms = int(data['bedrooms'])
        bathrooms = int(data['bathrooms'])
    except (KeyError, ValueError, TypeError):
        return jsonify({'error': 'Invalid input data. Please send area (float), bedrooms (int), bathrooms (int).'}), 400

    # Prepare feature array for prediction (make sure order matches model training)
    features = np.array([[area, bedrooms, bathrooms]])

    # Predict price using the loaded model
    predicted_price = model.predict(features)[0]

    # Return the predicted price rounded to 2 decimals
    return jsonify({'predicted_price': round(predicted_price, 2)})

if __name__ == '__main__':
    app.run(debug=True)
