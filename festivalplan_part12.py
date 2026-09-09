# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: FestivalPlan
import json

def load_json_file(filepath):
    """Load a JSON file with friendly error handling."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Malformed JSON in '{filepath}': {e}")
        return None
    except Exception as e:
        print(f"Unexpected error reading '{filepath}': {e}")
        return None
