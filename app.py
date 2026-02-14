from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('energy_model.pkl', 'rb'))

# Add this new route to your app.py
@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/calculator')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json() 
        feature_order = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8']
        input_data = [float(data[f]) for f in feature_order]
        
        prediction = model.predict(np.array([input_data]))
        
        return jsonify({
            "heating": round(float(prediction[0][0]), 2),
            "cooling": round(float(prediction[0][1]), 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)