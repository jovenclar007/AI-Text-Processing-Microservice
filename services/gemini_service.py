from google import genai

from config import GEMINI_API_KEY, GEMINI_MODEL


def translate_text(text, target_language):
    """Translate text using the configured Google Gemini model."""
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = (
        f"Translate the following text into {target_language}. "
        "Return only the translated text.\n\n"
        f"Text: {text}"
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    translated = (response.text or "").strip()
    if not translated:
        raise RuntimeError("The AI service returned an empty response.")

    return translated
