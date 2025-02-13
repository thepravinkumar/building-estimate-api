from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

CPWD_RATE_PER_CUBIC_METER = 25000

@app.route('/estimate', methods=['POST'])
def estimate():
    try:
        data = request.get_json()
        print("🔍 Received Data:", data)  # Debugging log

        base_area = data.get('baseArea')
        floor_height = data.get('floorHeight')
        total_floors = data.get('totalFloors')

        if not base_area or not floor_height or not total_floors:
            return jsonify({'error': 'Missing required parameters'}), 400

        total_volume = base_area * floor_height * total_floors
        estimated_cost = total_volume * CPWD_RATE_PER_CUBIC_METER

        print("✅ Estimated Cost:", estimated_cost)  # Debugging log
        return jsonify({'estimatedCost': estimated_cost})

    except Exception as e:
        print("❌ Server Error:", str(e))
        return jsonify({'error': 'Internal Server Error', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
