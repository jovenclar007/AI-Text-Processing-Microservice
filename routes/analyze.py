from flask import Blueprint, jsonify, request

from services.text_analysis_service import analyze_text

analyze_bp = Blueprint("analyze", __name__)


@analyze_bp.post("/analyze-text")
def analyze():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON body is required."}), 400

    text = data.get("text")

    if not isinstance(text, str) or not text.strip():
        return jsonify({"error": "'text' must be a non-empty string."}), 400

    return jsonify(analyze_text(text)), 200
