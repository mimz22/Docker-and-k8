from flask import Flask, jsonify
import requests

app = Flask(__name__)

USER_SERVICE_URL = "http://user-service"
PAYMENT_SERVICE_URL = "http://payment-service"

@app.route("/")
def home():
    try:
        user = requests.get(f"{USER_SERVICE_URL}/user").json()
    except:
        user = {"error": "User service unavailable"}

    try:
        payment = requests.get(f"{PAYMENT_SERVICE_URL}/payment").json()
    except:
        payment = {"error": "Payment service unavailable"}

    return jsonify({
        "frontend": "hello from frontend-service",
        "user": user,
        "payment": payment
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
