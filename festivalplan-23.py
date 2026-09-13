# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: FestivalPlan
def add_tag(festival, tag):
    """Attach a tag to a festival if not already present."""
    tags = festival.tags
    if tag not in tags:
        tags.add(tag)
    return festival

def remove_tag(festival, tag):
    """Remove a tag from a festival if present."""
    tags = festival.tags
    if tag in tags:
        tags.remove(tag)
    return festival

def summary_by_tag(festival, tag):
    """Return a one-line summary of the festival filtered by tag."""
    if tag in festival.tags:
        return f"FestivalPlan [{tag}]: {festival.name} on {festival.date}"
    return ""
