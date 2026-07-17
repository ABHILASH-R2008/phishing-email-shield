# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from urllib.parse import urlparse
import re
import pickle
import pandas as pd

# 1. Initialize Flask and allow Cross-Origin browser requests
app = Flask(__name__)
CORS(app)

# 2. Load our trained AI brain ('phishing_model.pkl') into memory
with open('phishing_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

print("AI Model loaded successfully! Server is ready.")


# 3. Home Route: Serves the visual frontend web interface dashboard
@app.route('/')
def home_page():
    return render_template('index.html')


# 4. Helper Function: Translates a raw URL text string into structural metrics
def extract_features_from_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
        
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    # Extract structural metrics
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    has_ip = 1 if re.match(ip_pattern, domain) else 0
    has_at_symbol = 1 if '@' in url else 0
    url_length = len(url)
    
    # CRITICAL MATCH: Order must align precisely with your dataset configuration
    # Return array format: [url_length, has_ip, has_at_symbol]
    return [url_length, has_ip, has_at_symbol]


# 5. API Core Endpoint: Receives incoming URL string queries for inference
@app.route('/api/predict', methods=['POST'])
def predict_phishing():
    data = request.get_json()
    
    if not data or 'url' not in data:
        return jsonify({"error": "No URL provided"}), 400
        
    raw_url = data['url']
    
    # Step A: Convert raw string into index lists
    numerical_features = extract_features_from_url(raw_url)
    
    # Step B: CONVERSION FIX - Wrap numbers into a structured Pandas DataFrame
    # Using the exact structural header keys defined during training phase
    feature_df = pd.DataFrame([numerical_features], columns=['url_length', 'has_ip', 'has_at_symbol'])
    
    # Step C: Feed structured DataFrame into the classifier logic block
    prediction = model.predict(feature_df)
    result = int(prediction[0])
    verdict = "Phishing" if result == 1 else "Safe"
    
    # Step D: Package response objects and hand back clean JSON payloads
    return jsonify({
        "status": "success",
        "scanned_url": raw_url,
        "extracted_features": {
            "url_length": numerical_features[0],
            "has_ip": numerical_features[1],
            "has_at_symbol": numerical_features[2]
        },
        "verdict": verdict
    })


if __name__ == '__main__':
    # host='0.0.0.0' tells Flask to open up to your entire local network
    app.run(debug=True, host='0.0.0.0', port=5000)