from flask import Blueprint, jsonify, request

from services.gemini_service import translate_text

translate_bp = Blueprint("translate", __name__)


@translate_bp.post("/translate")
def translate():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON body is required."}), 400

    text = data.get("text")
    target_language = data.get("target_language")

    if not isinstance(text, str) or not text.strip():
        return jsonify({"error": "'text' must be a non-empty string."}), 400

    if not isinstance(target_language, str) or not target_language.strip():
        return jsonify({"error": "'target_language' must be a non-empty string."}), 400

    try:
        translated = translate_text(text, target_language)
        return jsonify({
            "original_text": text,
            "translated_text": translated,
            "target_language": target_language
        }), 200
    except Exception:
        return jsonify({
            "error": "Translation failed.",
            "message": "The external AI service could not process the request."
        }), 502
