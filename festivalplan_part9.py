# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: FestivalPlan
def sort_records(records, key, reverse=False):
    if key == 'title':
        return sorted(records, key=lambda r: r.get('title', ''), reverse=reverse)
    elif key == 'date':
        return sorted(records, key=lambda r: r.get('date', ''), reverse=reverse)
    elif key == 'priority':
        return sorted(records, key=lambda r: r.get('priority', 0), reverse=reverse)
    elif key == 'last_update':
        return sorted(records, key=lambda r: r.get('last_update', ''), reverse=reverse)
    else:
        return records

def get_sorted_records(records, key='date', reverse=False):
    return sort_records(records, key, reverse)
