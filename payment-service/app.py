from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/payment")
def process_payment():
    
    return jsonify({
        "payment_id": 101,
        "amount": "50.00",
        "currency": "USD",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
