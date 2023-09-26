from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data - you can replace this with your own data or database
data = []

@app.route('/api/gpsData', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        return jsonify(data)
    elif request.method == 'POST':
        new_item = request.json  # Assumes JSON data in the request body
        data.append(new_item)
        return jsonify({"message": "Item added successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
