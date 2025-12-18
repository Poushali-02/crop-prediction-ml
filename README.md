# 🌾 Crop Prediction ML

A machine learning-based crop recommendation system that helps farmers make data-driven decisions about crop selection based on soil properties and environmental conditions.
Web application live at https://whattogrow.onrender.com/

## 📋 Overview

This project implements an intelligent crop prediction system using machine learning algorithms to recommend the most suitable crops for cultivation based on various soil and climatic parameters. By analyzing factors such as NPK values (Nitrogen, Phosphorus, Potassium), pH levels, temperature, humidity, and rainfall, the system provides personalized crop recommendations to maximize agricultural productivity and profitability [web:22][web:30].

## 🎯 Project Objectives

- Assist farmers in selecting optimal crops based on soil and environmental conditions
- Maximize crop yield and profitability through data-driven recommendations
- Reduce agricultural risks by matching crops to suitable growing conditions
- Promote sustainable farming practices through informed decision-making
- Provide an easy-to-use interface for real-time crop recommendations

## ✨ Key Features

- **Multi-parameter Analysis**: Considers soil nutrients (N, P, K), pH, temperature, humidity, and rainfall
- **Multiple ML Algorithms**: Implementation and comparison of various classification models
- **High Accuracy**: Achieves prediction accuracy of 95%+ using optimized algorithms
- **User-Friendly Interface**: Simple input system for farmers to get instant recommendations
- **Scalable Architecture**: Easily adaptable to different regions and crop varieties

## 🔧 Technologies Used

### Programming & Libraries
- **Python 3.x** - Core programming language
- **NumPy** - Numerical computations
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning algorithms
- **Matplotlib/Seaborn** - Data visualization

### Machine Learning Algorithms
- Random Forest Classifier
- Decision Tree
- Logistic Regression

## 📊 Dataset Features

Dataset available at [here](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset).
- Kaggle notebook [here](https://www.kaggle.com/code/poushal02/crop-recommendation)
  
The system analyzes the following parameters:

| Parameter | Description | Unit |
|-----------|-------------|------|
| Nitrogen (N) | Nitrogen content in soil | kg/ha |
| Phosphorus (P) | Phosphorus content in soil | kg/ha |
| Potassium (K) | Potassium content in soil | kg/ha |
| pH | Soil pH level | 0-14 scale |
| Temperature | Average temperature | °C |
| Humidity | Relative humidity | % |
| Rainfall | Annual rainfall | mm |

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Poushali-02/crop-prediction-ml.git
cd crop-prediction-ml

```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # on Mac/Linux
```

3. **Install required dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```
## 💻 Usage

### Basic Usage Example

```python
# Import necessary libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

Load the trained model
model = load_model('crop_prediction_model.pkl')

Input parameters
soil_data = {
'N': 90,
'P': 42,
'K': 43,
'temperature': 20.5,
'humidity': 82,
'ph': 6.5,
'rainfall': 202.9
}

Get crop recommendation
predicted_crop = model.predict([list(soil_data.values())])
print(f"Recommended Crop: {predicted_crop}")

```
text

### Web Interface Usage

1. Launch the application
2. Enter soil parameters (N, P, K, pH)
3. Input environmental conditions (temperature, humidity, rainfall)
4. Click "Predict" to get crop recommendation
5. View detailed analysis and alternative crop suggestions

## 🌱 Supported Crops

The system can recommend from a variety of crops including:

- rice
- maize
- chickpea
- kidneybeans
- pigeonpeas
- mothbeans
- mungbean
- blackgram
- lentil
- pomegranate
- banana
- mango
- grapes
- watermelon
- muskmelon
- apple
- orange
- papaya
- coconut
- cotton
- jute
- coffee

## 📁 Project Structure

crop-prediction-ml/
- ├── templates/
- │ └── index.html # Web interface
- ├── static/
- │ ├── css/ # Stylesheets
- │ └── js/ # JavaScript files
- ├── app.py # Flask application
- ├── requirements.txt # Dependencies
- └── README.md # Documentation

## 🎓 Key Learnings

- Implementation of supervised learning for classification tasks
- Comparison of multiple ML algorithms for agricultural applications
- Feature importance analysis in crop recommendation
- Model optimization and hyperparameter tuning
- Deployment of ML models in production environments

## 📧 Contact

For questions, suggestions, or collaborations:
- Open an issue in the repository
- Connect via GitHub

---

⭐ **Star this repository if you find it helpful!**

*Empowering farmers with data-driven crop recommendations for sustainable agriculture* 🌾
