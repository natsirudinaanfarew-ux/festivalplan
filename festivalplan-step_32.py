# === Stage 32: Add pagination helpers for long console output ===
# Project: FestivalPlan
def paginate(text, chunk_size=80):
    """Split a long string into fixed-width lines for console display."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
