from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the SARIMA model
sarima_model = joblib.load('sarima_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data
    steps = int(request.form['steps'])
    
    # Make prediction
    forecast = sarima_model.forecast(steps=steps)
    
    return render_template('result.html', forecast=forecast)

if __name__ == '__main__':
    app.run(debug=True)
