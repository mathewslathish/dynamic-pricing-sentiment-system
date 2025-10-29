from flask import Flask, request, jsonify
from dynamic_pricing_model import DynamicPricingModel
from sentiment_analysis import SentimentAnalyzer
import pandas as pd

app = Flask(__name__)

pricing_model = DynamicPricingModel()
sentiment_analyzer = SentimentAnalyzer()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/predict_price', methods=['POST'])
def predict_price():
    data = request.get_json()
    features = pd.DataFrame([data['features']])
    price = pricing_model.predict(features)
    return jsonify({'predicted_price': float(price[0])})

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data['text']
    result = sentiment_analyzer.analyze(text)
    label = sentiment_analyzer.get_sentiment_label(result['compound'])
    return jsonify({'text': text, 'scores': result, 'label': label})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)