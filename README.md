# Dynamic Pricing & Sentiment Analysis System

A real-time dynamic pricing system that adjusts product prices based on sentiment analysis of customer feedback, market conditions, and demand patterns.

## 🚀 Project Overview

This system combines machine learning-powered sentiment analysis with dynamic pricing algorithms to optimize product pricing in real-time. It analyzes customer feedback, social media mentions, and market data to determine optimal pricing strategies.

### Key Features

- **Real-time Sentiment Analysis**: Processes customer reviews, social media mentions, and feedback
- **Dynamic Pricing Engine**: Adjusts prices based on sentiment scores and market conditions
- **RESTful API**: Easy integration with existing e-commerce platforms
- **Machine Learning Models**: Uses advanced NLP and pricing algorithms
- **Real-time Monitoring**: Dashboard for tracking price changes and sentiment trends

## 📋 System Requirements

- Python 3.8 or higher
- pip (Python package installer)
- 4GB+ RAM recommended
- Internet connection for sentiment analysis APIs

### Dependencies

- Flask/FastAPI for web framework
- scikit-learn for machine learning
- NLTK/spaCy for natural language processing
- pandas for data manipulation
- numpy for numerical operations
- requests for API calls

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mathewslathish/dynamic-pricing-sentiment-system.git
cd dynamic-pricing-sentiment-system
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory:

```env
# API Configuration
FLASK_ENV=development
FLASK_DEBUG=True
API_PORT=5000

# Sentiment Analysis API Keys (if using external services)
SENTIMENT_API_KEY=your_api_key_here

# Database Configuration (if using database)
DATABASE_URL=sqlite:///pricing_system.db

# Pricing Configuration
MIN_PRICE_ADJUSTMENT=-0.20  # Maximum 20% decrease
MAX_PRICE_ADJUSTMENT=0.30   # Maximum 30% increase
BASE_PRICE_MULTIPLIER=1.0
```

## 🚀 Quick Start

### Start the System

```bash
# Start the API server
python api_server.py
```

The system will be available at `http://localhost:5000`

### Basic Usage

```python
import requests

# Analyze sentiment and get price recommendation
response = requests.post('http://localhost:5000/analyze-price', json={
    'product_id': 'PROD123',
    'base_price': 99.99,
    'reviews': [
        'Great product, love it!',
        'Excellent quality and fast shipping',
        'Not worth the money'
    ]
})

result = response.json()
print(f"Recommended price: ${result['recommended_price']}")
print(f"Sentiment score: {result['sentiment_score']}")
```

## 📚 API Documentation

### Endpoints

#### 1. Analyze Price
**POST** `/analyze-price`

Analyzes sentiment and returns price recommendation.

**Request Body:**
```json
{
  "product_id": "string",
  "base_price": "number",
  "reviews": ["string"],
  "market_data": {
    "demand_level": "number (0-1)",
    "competitor_price": "number",
    "inventory_level": "number"
  }
}
```

**Response:**
```json
{
  "product_id": "PROD123",
  "recommended_price": 104.99,
  "sentiment_score": 0.75,
  "price_adjustment": 0.05,
  "confidence": 0.89,
  "reasoning": "Positive sentiment detected, slight price increase recommended"
}
```

#### 2. Get Sentiment Analysis
**POST** `/sentiment-analysis`

Returns detailed sentiment analysis for text.

**Request Body:**
```json
{
  "text": "string or array of strings"
}
```

**Response:**
```json
{
  "overall_sentiment": "positive",
  "sentiment_score": 0.75,
  "individual_scores": [0.8, 0.7, -0.2],
  "keywords": ["great", "excellent", "expensive"]
}
```

#### 3. Update Pricing Model
**POST** `/update-model`

Updates the pricing model with new training data.

#### 4. Health Check
**GET** `/health`

Returns system status and health information.

## 🐳 Docker Deployment

### Option 1: Using Docker

1. **Build Docker Image:**
```bash
docker build -t dynamic-pricing-system .
```

2. **Run Container:**
```bash
docker run -p 5000:5000 -e FLASK_ENV=production dynamic-pricing-system
```

### Option 2: Using Docker Compose

1. **Create docker-compose.yml:**
```yaml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - API_PORT=5000
    volumes:
      - ./data:/app/data
```

2. **Deploy:**
```bash
docker-compose up -d
```

## 🚀 Production Deployment

### Cloud Deployment Options

#### AWS Deployment
```bash
# Using AWS Elastic Beanstalk
eb init dynamic-pricing-system
eb create production
eb deploy
```

#### Heroku Deployment
```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Deploy
git push heroku main
```

#### Google Cloud Platform
```bash
# Deploy to Google Cloud Run
gcloud run deploy dynamic-pricing-system --source .
```

### Environment Variables for Production

```env
FLASK_ENV=production
FLASK_DEBUG=False
API_PORT=8080
DATABASE_URL=postgresql://user:pass@host:port/db
REDIS_URL=redis://host:port/0
SENTIMENT_API_KEY=your_production_api_key
SECRET_KEY=your_secret_key_here
```

## 🧪 Testing

### Run Tests
```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_sentiment_analysis.py
```

### Test Examples
```python
# Test sentiment analysis
python -m pytest tests/test_sentiment.py -v

# Test pricing engine
python -m pytest tests/test_pricing.py -v

# Test API endpoints
python -m pytest tests/test_api.py -v
```

## 📊 Monitoring & Logging

### Application Metrics
- Response times
- Sentiment analysis accuracy
- Price adjustment frequency
- API error rates

### Logging Configuration
Logs are stored in `logs/` directory with rotation:
- `app.log` - Application logs
- `sentiment.log` - Sentiment analysis logs
- `pricing.log` - Pricing engine logs
- `api.log` - API request logs

## 🔧 Configuration

### Pricing Model Configuration
```python
# In config.py
PRICING_CONFIG = {
    'sentiment_weight': 0.4,
    'demand_weight': 0.3,
    'competitor_weight': 0.2,
    'inventory_weight': 0.1,
    'max_adjustment': 0.3,
    'min_adjustment': -0.2
}
```

### Sentiment Analysis Configuration
```python
SENTIMENT_CONFIG = {
    'model_type': 'vader',  # or 'textblob', 'custom'
    'confidence_threshold': 0.7,
    'batch_size': 100,
    'preprocessing': True
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Write unit tests for new features
- Update documentation for API changes
- Use meaningful commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **Documentation**: [Wiki](https://github.com/mathewslathish/dynamic-pricing-sentiment-system/wiki)
- **Issues**: [GitHub Issues](https://github.com/mathewslathish/dynamic-pricing-sentiment-system/issues)
- **Discussions**: [GitHub Discussions](https://github.com/mathewslathish/dynamic-pricing-sentiment-system/discussions)

## 🔄 Changelog

### v1.0.0 (Initial Release)
- Basic sentiment analysis functionality
- Dynamic pricing engine
- RESTful API
- Docker support
- Basic documentation

---

**Built with ❤️ by [mathewslathish](https://github.com/mathewslathish)**
