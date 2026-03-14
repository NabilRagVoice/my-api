import os, logging
from flask import Blueprint, jsonify, request


log = logging.getLogger(__name__)
adresses_bp = Blueprint("adresses", __name__)

@adresses_bp.route("/clients/<client_id>/adresses", methods=["GET"])
def clients_client_id_adresses_get(client_id):
    """Lister toutes les adresses d'un client"""
    try:
        return jsonify({"message": "OK"}), 200
    except Exception as e:
        log.error(f"clients_client_id_adresses_get error: {e}")
        return jsonify({"error": str(e)}), 500

@adresses_bp.route("/clients/<client_id>/adresses/<id>", methods=["GET"])
def clients_client_id_adresses_id_get(client_id, id):
    """Récupérer une adresse spécifique d'un client"""
    try:
        return jsonify({"message": "OK"}), 200
    except Exception as e:
        log.error(f"clients_client_id_adresses_id_get error: {e}")
        return jsonify({"error": str(e)}), 500

@adresses_bp.route("/clients/<client_id>/adresses", methods=["POST"])
def clients_client_id_adresses_post(client_id):
    """Ajouter une adresse à un client"""
    try:
        data = request.get_json(force=True)
        return jsonify({"received": data}), 200
    except Exception as e:
        log.error(f"clients_client_id_adresses_post error: {e}")
        return jsonify({"error": str(e)}), 500

@adresses_bp.route("/clients/<client_id>/adresses/<id>", methods=["PUT"])
def clients_client_id_adresses_id_put(client_id, id):
    """Mettre à jour une adresse"""
    try:
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        log.error(f"clients_client_id_adresses_id_put error: {e}")
        return jsonify({"error": str(e)}), 500

@adresses_bp.route("/clients/<client_id>/adresses/<id>", methods=["PATCH"])
def clients_client_id_adresses_id_patch(client_id, id):
    """Modifier partiellement une adresse"""
    try:
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        log.error(f"clients_client_id_adresses_id_patch error: {e}")
        return jsonify({"error": str(e)}), 500

@adresses_bp.route("/clients/<client_id>/adresses/<id>", methods=["DELETE"])
def clients_client_id_adresses_id_delete(client_id, id):
    """Supprimer une adresse"""
    try:
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        log.error(f"clients_client_id_adresses_id_delete error: {e}")
        return jsonify({"error": str(e)}), 500

@adresses_bp.route("/clients/<client_id>/adresses/<id>/set-principale", methods=["POST"])
def clients_client_id_adresses_id_set_principale_post(client_id, id):
    """Définir une adresse comme principale"""
    try:
        data = request.get_json(force=True)
        return jsonify({"received": data}), 200
    except Exception as e:
        log.error(f"clients_client_id_adresses_id_set_principale_post error: {e}")
        return jsonify({"error": str(e)}), 500

