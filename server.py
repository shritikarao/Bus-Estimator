from flask import Flask, request, jsonify
from flask_cors import CORS
from predictor_lib import predict_eta

app = Flask(__name__)
# Enable CORS for requests from the React dev server
CORS(app, resources={r"/predict": {"origins": "http://localhost:3000"}})

@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        return '', 200
        
    data = request.json
    try:
        eta = predict_eta(
            line=data['line'],
            stop_name=data['stop'],
            time_str=data['time'],
            weather=data['weather'],
            bus_load=data['bus_load']
        )
        return jsonify({'eta': eta}), 200
    except Exception as e:
        print(f"Error in prediction: {str(e)}")  # Add logging
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Run on port 8080 to avoid conflicts with AirPlay
    app.run(port=8080, debug=True)  # Enable debug mode

