# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: FestivalPlan
def bulk_delete(kind, ids, confirm_flag):
    """Delete multiple records of a kind only when the confirmation flag is set.

    Args:
        kind: The type of record to delete (e.g. 'vendor', 'ticket', 'shift').
        ids: A list of ids to remove.
        confirm_flag: A boolean that must be True to perform the deletion.

    Returns:
        A tuple (deleted_count, remaining_ids) describing the outcome.
    """
    if not confirm_flag:
        return 0, list(ids)

    deleted = []
    remaining = []
    for record in _store.get(kind):
        if record['id'] in ids:
            _store.delete(kind, record['id'])
            deleted.append(record['id'])
        else:
            remaining.append(record['id'])

    return len(deleted), remaining


def confirm_bulk_delete():
    """Prompt the user for confirmation and return True if they agree."""
    answer = input("Type 'yes' to confirm bulk deletion: ")
    return answer.strip().lower() == 'yes'


def request_bulk_delete(kind, ids):
    """Ask for confirmation and delete the records if the user agrees."""
    if confirm_bulk_delete():
        deleted, remaining = bulk_delete(kind, ids, True)
        print(f"Deleted {deleted} record(s). {len(remaining)} remaining.")
    else:
        print("Deletion cancelled.")
