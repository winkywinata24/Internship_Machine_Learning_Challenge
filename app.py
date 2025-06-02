from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load model (dilatih sebelumnya)
model = joblib.load("models/random_forest_model.pkl")

# ========== Endpoint: Health Check ==========
@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "API is running."}), 200

# ========== Endpoint: Prediction ==========
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Ambil dan susun fitur
        features = [
            data["Pclass"],
            data["Sex"],
            data["Age"],
            data["Fare"],
            data["Embarked"],
            data["FamilySize"]
        ]

        # Ubah jadi array dan prediksi
        prediction = model.predict([features])
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ========== Endpoint: Train Model ==========
@app.route("/train", methods=["POST"])
def train_model():
    try:
        # Format data baru (harus JSON array of objects)
        data = request.get_json()
        df = pd.DataFrame(data, index=[0]) if isinstance(data, dict) else pd.DataFrame(data)

        # Fitur dan target
        features = ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'FamilySize']
        X = df[features]
        y = df['Survived']

        # Latih model baru
        new_model = RandomForestClassifier()
        new_model.fit(X, y)

        # Simpan model baru
        joblib.dump(new_model, "models/random_forest_model.pkl")
        return jsonify({"status": "Model retrained and saved."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
