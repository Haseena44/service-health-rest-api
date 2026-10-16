from flask import Flask, jsonify, request
from functools import wraps

app = Flask(__name__)

# Simple auth
def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get("Authorization")
        if auth!= "Bearer mysecret123":
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

services = {
    "dns": "up",
    "api": "up",
    "database": "down"
}

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "services": services}), 200

@app.route("/health/<name>", methods=["GET"])
@require_auth
def service_health(name):
    if name not in services:
        return jsonify({"error": "Not found"}), 404
    return jsonify({name: services[name]}), 200

@app.route("/check", methods=["POST"])
@require_auth
def check():
    data = request.get_json()
    if not data or "service" not in data:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"checked": data["service"], "result": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
