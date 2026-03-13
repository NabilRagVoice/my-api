import os, logging
from flask import Blueprint, jsonify, request


log = logging.getLogger(__name__)
dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard/kpis", methods=["GET"])
def dashboard_kpis_get():
    """KPIs globaux (nb prospects, campagnes actives, accords du mois, CA)"""
    try:
        return jsonify({"message": "OK"}), 200
    except Exception as e:
        log.error(f"dashboard_kpis_get error: {e}")
        return jsonify({"error": str(e)}), 500

@dashboard_bp.route("/dashboard/conversion-rate", methods=["GET"])
def dashboard_conversion-rate_get():
    """Taux de conversion global (accords/prospects contactés)"""
    try:
        return jsonify({"message": "OK"}), 200
    except Exception as e:
        log.error(f"dashboard_conversion-rate_get error: {e}")
        return jsonify({"error": str(e)}), 500

