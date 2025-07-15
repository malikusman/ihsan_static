from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/payments', methods=['POST'])
def process_payment():
    # Get JSON data from the request
    data = request.get_json()
    
    # Extract parameters
    recipient_email = data.get('recipientEmail')
    amount = data.get('amount')
    currency = data.get('currency')
    
    # Create response mirroring the input
    response = {
        "recipientEmail": recipient_email,
        "amount": amount,
        "currency": currency
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)