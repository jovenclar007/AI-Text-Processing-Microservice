from concurrent.futures import ThreadPoolExecutor

from flask import Blueprint, jsonify, request

from services.text_analysis_service import analyze_text

batch_bp = Blueprint("batch", __name__)


@batch_bp.post("/batch-analyze")
def batch_analyze():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON body is required."}), 400

    texts = data.get("texts")

    if not isinstance(texts, list) or not texts:
        return jsonify({"error": "'texts' must be a non-empty list."}), 400

    if len(texts) > 20:
        return jsonify({"error": "A maximum of 20 texts is allowed."}), 400

    if not all(isinstance(text, str) and text.strip() for text in texts):
        return jsonify({"error": "Each item in 'texts' must be a non-empty string."}), 400

    # Concurrency: analyze independent texts at the same time.
    with ThreadPoolExecutor(max_workers=min(5, len(texts))) as executor:
        results = list(executor.map(analyze_text, texts))

    return jsonify({"count": len(results), "results": results}), 200
