"""Translation wrapper using deep-translator."""
try:
    from deep_translator import GoogleTranslator
except Exception:
    GoogleTranslator = None

def translate_text(text, source="auto", target="es"):
    text = str(text).strip()
    if not text:
        return ""
    if GoogleTranslator is None:
        return f"[Translation unavailable] {text}"
    try:
        return GoogleTranslator(source=source, target=target).translate(text[:4500])
    except Exception as error:
        return f"[Translation unavailable: {type(error).__name__}] {text}"
