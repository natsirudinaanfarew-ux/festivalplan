# === Stage 20: Add duplicate detection for newly created records ===
# Project: FestivalPlan
from datetime import datetime


def is_duplicate_record(record, existing_records):
    """Check whether a new record is a duplicate of any existing one.

    Comparison is done by the record's primary key fields. If the record
    already exists in the collection we return True so the caller can skip
    inserting it again.
    """
    if record is None:
        return False

    key_fields = _extract_key(record)
    for existing in existing_records:
        if _extract_key(existing) == key_fields:
            return True
    return False


def _extract_key(record):
    """Pull the natural primary key out of a record dict.

    We look for common festival keys in this order:
    - name (for vendors)
    - stage + start_time (for schedule entries)
    - ticket_id (for tickets)
    - volunteer_id (for shifts)
    """
    if "name" in record:
        return ("name", record["name"])
    if "stage" in record and "start_time" in record:
        return ("stage", record["stage"], record["start_time"])
    if "ticket_id" in record:
        return ("ticket_id", record["ticket_id"])
    if "volunteer_id" in record:
        return ("volunteer_id", record["volunteer_id"])
    if "id" in record:
        return ("id", record["id"])
    return ()
