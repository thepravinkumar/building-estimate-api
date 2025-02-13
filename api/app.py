from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app, origins="*")  # Allow all origins

CPWD_RATE_PER_CUBIC_METER = 25000

@app.route('/estimate', methods=['POST'])
def estimate():
    data = request.get_json()
    base_area = data.get('baseArea')
    floor_height = data.get('floorHeight')
    total_floors = data.get('totalFloors')

    if not base_area or not floor_height or not total_floors:
        return jsonify({'error': 'Missing required parameters'}), 400

    total_volume = base_area * floor_height * total_floors
    estimated_cost = total_volume * CPWD_RATE_PER_CUBIC_METER

    return jsonify({'estimatedCost': estimated_cost})

if __name__ == '__main__':
    app.run(debug=True)
