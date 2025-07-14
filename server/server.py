from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/api/get_location_names')
def get_location_names():
    return jsonify({
        'locations': util.get_locations()
    })

@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()  # <-- Accept JSON from frontend
    total_sqft = float(data['total_sqft'])
    location = data['location']
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    return jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })

if __name__ == "__main__":
    print("Starting the Python Flask Server for Home Price Prediction")
    util.load_artifcats()
    app.run()
