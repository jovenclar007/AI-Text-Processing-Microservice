from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health():
    return jsonify({
        "service": "AI Text Processing Microservice",
        "status": "healthy",
        "version": "1.0.0"
    })
