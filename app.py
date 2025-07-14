from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_json():
    # Static JSON data
    data = {
        "message": "Hello, World!",
        "status": "success",
        "data": {
            "id": 1,
            "name": "Sample User",
            "email": "user@example.com"
        }
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)