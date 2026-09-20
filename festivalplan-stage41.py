# === Stage 41: Add plain text import for a simple line-based format ===
# Project: FestivalPlan
def read_lines(path):
    with open(path) as f:
        return f.read().splitlines()
