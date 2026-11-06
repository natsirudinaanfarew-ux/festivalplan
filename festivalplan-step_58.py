# === Stage 58: Add bulk update behavior for selected records ===
# Project: FestivalPlan
def bulk_update_records(collection, criteria, updates):
    """Apply a single field update to every record matching criteria."""
    for record in collection:
        if all(record.get(key) == value for key, value in criteria.items()):
            record.update(updates)
    return len(collection)

def bulk_update_by_field(collection, field, value, updates):
    """Apply updates to all records sharing the same field value."""
    for record in collection:
        if record.get(field) == value:
            record.update(updates)
    return len(collection)

def bulk_set_status(collection, status_field, status, updates=None):
    """Set a status value across all records and optionally apply updates."""
    for record in collection:
        record[status_field] = status
        if updates:
            record.update(updates)
    return len(collection)

def bulk_increment(collection, field, amount):
    """Increment a numeric field by a fixed amount for all records."""
    for record in collection:
        record[field] += amount
    return len(collection)

def bulk_delete_matching(collection, criteria):
    """Remove records that match the given criteria and return count."""
    removed = [record for record in collection if all(
        record.get(key) == value for key, value in criteria.items()
    )]
    for record in removed:
        collection.remove(record)
    return len(removed)
