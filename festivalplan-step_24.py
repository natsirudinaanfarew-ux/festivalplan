# === Stage 24: Add grouped summaries by category or status ===
# Project: FestivalPlan
def grouped_summary(items, key_fn, value_fn):
    """Summarize a list of items by a key into a dict of lists."""
    groups = {}
    for item in items:
        key = key_fn(item)
        groups.setdefault(key, []).append(value_fn(item))
    return groups
