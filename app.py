from flask import Flask, render_template, request, url_for
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

model = joblib.load('crop_recommendation.pkl')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        try:
            N = float(request.form.get('N'))
            P = float(request.form.get('P'))
            K = float(request.form.get('K'))
            temperature = float(request.form.get('temperature'))
            humidity = float(request.form.get('humidity'))
            ph = float(request.form.get('ph'))
            rainfall = float(request.form.get('rainfall'))
            
            input_values = [[N, P, K, temperature, humidity, ph, rainfall]]
            
            data = pd.DataFrame(input_values, columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
            
            prediction = model.predict(data)[0]
            crop_mapping = {
                        'Apple': 0,
                        'Banana': 1,
                        'Blackgram': 2,
                        'Chickpea': 3,
                        'Coconut': 4,
                        'Coffee': 5,
                        'Cotton': 6,
                        'Grapes': 7,
                        'Jute': 8,
                        'Kidneybeans': 9,
                        'Lentil': 10,
                        'Maize': 11,
                        'Mango': 12,
                        'Mothbeans': 13,
                        'Mungbean': 14,
                        'Muskmelon': 15,
                        'Orange': 16,
                        'Papaya': 17,
                        'Pigeonpeas': 18,
                        'Pomegranate': 19,
                        'Rice': 20,
                        'Watermelon': 21
                    }
            inverse_mapping = {v: k for k, v in crop_mapping.items()}
            
            text = f"You can grow {inverse_mapping[prediction]} in this conditions."
            colour = "success"
            return render_template('index.html', prediction_text=text, colour=colour)
        except Exception as e:
            text = f"Error {e}"
            colour = "danger"
            return render_template('index.html', error_text=text, colour=colour)

if __name__ == '__main__':
    app.run(debug=True)