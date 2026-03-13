import os, logging
from flask import Blueprint, jsonify, request


log = logging.getLogger(__name__)
reports_bp = Blueprint("reports", __name__)

@reports_bp.route("/reports/campagne/<id>", methods=["GET"])
def reports_campagne_id_get():
    """Rapport détaillé d'une campagne (performance, accords, prospects)"""
    try:
        return jsonify({"message": "OK"}), 200
    except Exception as e:
        log.error(f"reports_campagne_id_get error: {e}")
        return jsonify({"error": str(e)}), 500

