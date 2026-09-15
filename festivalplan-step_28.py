# === Stage 28: Add overdue item detection based on due dates ===
# Project: FestivalPlan
def find_overdue_items(items, reference_date=None):
    """Return a list of items whose due_date is strictly before the reference date."""
    if reference_date is None:
        reference_date = datetime.datetime.now()
    overdue = []
    for item in items:
        if hasattr(item, 'due_date') and item.due_date < reference_date:
            overdue.append(item)
    return overdue
