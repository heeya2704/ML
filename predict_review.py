import os
import pickle
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)

MODEL_FILE = 'review_sentiment_model.pkl'

def load_model():
    if os.path.exists(MODEL_FILE):
        with open(MODEL_FILE, 'rb') as f:
            return pickle.load(f)
    return None

@app.route('/', methods=['GET'])
def index():
    """Serves the HTML frontend interface."""
    if os.path.exists('templates/review_predictor.html'):
        return render_template('review_predictor.html')
    elif os.path.exists('review_predictor.html'):
        return send_from_directory('.', 'review_predictor.html')
    return "Flipkart Review Sentiment Predictor API is running."

@app.route('/predict', methods=['POST'])
def predict_sentiment():
    """
    Task 2: Flask API endpoint accepting POST request with JSON payload:
    {"review": "sample review text..."}
    Returns 'Positive' or 'Negative' sentiment prediction.
    """
    try:
        data = request.get_json()
        if not data or 'review' not in data:
            return jsonify({
                "status": "error",
                "message": "Missing 'review' field in JSON request body."
            }), 400

        review_text = str(data['review']).strip()
        if not review_text:
            return jsonify({
                "status": "error",
                "message": "Review text cannot be empty."
            }), 400

        sentiment_pipeline = load_model()
        if sentiment_pipeline is None:
            return jsonify({
                "status": "error",
                "message": "Model file not found on server."
            }), 500

        # Predict using loaded model pipeline
        pred = sentiment_pipeline.predict([review_text])[0]
        sentiment_label = "Positive" if pred == 1 else "Negative"

        return jsonify({
            "status": "success",
            "review": review_text,
            "sentiment": sentiment_label
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    # Run locally on port 5002
    app.run(host='127.0.0.1', port=5002, debug=True)
