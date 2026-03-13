    import os, logging
    from flask import Flask, jsonify, request

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    API_KEY = os.getenv("API_KEY", "d7e5fe5d-0082-45b5-b60c-2bf4bb4df531")

    def create_app():
        app = Flask(__name__)

        @app.before_request
        def _check_api_key():
            if request.path in ("/api/health", "/health"):
                return
            key = request.headers.get("X-API-Key", "")
            if key != API_KEY:
                return jsonify({"error": "Invalid API key"}), 401

        from routes.prospects_routes import prospects_bp
from routes.campagnes_routes import campagnes_bp
from routes.offres_routes import offres_bp
from routes.accords_routes import accords_bp
from routes.dashboard_routes import dashboard_bp
from routes.reports_routes import reports_bp
        app.register_blueprint(prospects_bp, url_prefix="/api/prospects")
app.register_blueprint(campagnes_bp, url_prefix="/api/campagnes")
app.register_blueprint(offres_bp, url_prefix="/api/offres")
app.register_blueprint(accords_bp, url_prefix="/api/accords")
app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")
app.register_blueprint(reports_bp, url_prefix="/api/reports")

        @app.route("/api/health")
        def health():
            return jsonify({"status": "ok"})

        return app

    if __name__ == "__main__":
        create_app().run(host="0.0.0.0", port=5000)
