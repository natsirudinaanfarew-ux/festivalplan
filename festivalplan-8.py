# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: FestivalPlan
def filter_entries(entries, **filters):
    """Filter entries by status, category, owner, or tag.
    
    Args:
        entries: List of dicts.
        **filters: Keyword arguments with filter values.
            - status: Filter by status.
            - category: Filter by category.
            - owner: Filter by owner.
            - tag: Filter by tag.
    
    Returns:
        List of entries matching all filters.
    """
    if not filters:
        return entries

    filtered = entries
    for key, value in filters.items():
        if value is not None:
            filtered = [entry for entry in filtered if entry.get(key) == value]

    return filtered
