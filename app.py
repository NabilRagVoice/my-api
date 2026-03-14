import os, logging
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

API_KEY = os.getenv("API_KEY", "f61a7e35-2c46-4f46-8fad-1608c0245758")

def create_app():
    app = Flask(__name__)

    @app.before_request
    def _check_api_key():
        if request.path in ("/api/health", "/health"):
            return
        key = request.headers.get("X-API-Key", "")
        if key != API_KEY:
            return jsonify({"error": "Invalid API key"}), 401

    from routes.clients_routes import clients_bp
    from routes.contacts_routes import contacts_bp
    from routes.adresses_routes import adresses_bp
    app.register_blueprint(clients_bp, url_prefix="/api/clients")
    app.register_blueprint(contacts_bp, url_prefix="/api/contacts")
    app.register_blueprint(adresses_bp, url_prefix="/api/adresses")

    @app.route("/api/health")
    def health():
        return jsonify({"status": "ok"})

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
