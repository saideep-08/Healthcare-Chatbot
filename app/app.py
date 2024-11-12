import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict_intent

from flask import Flask, request, jsonify, render_template
from src.predict import predict_intent  # Import the prediction function

app = Flask(__name__)

# Route for chatbot interface
@app.route('/')
def index():
    return render_template('index.html')

# API route to handle messages
@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.json.get("query")
    intent = predict_intent(user_input)
    response = f"Detected intent: {intent}"  # Basic response for demonstration
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
