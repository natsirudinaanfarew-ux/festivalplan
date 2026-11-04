# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: FestivalPlan
def find_vendor_by_id(vendor_ids, vendor_list):
    """Return the vendor whose id appears in the given set, or None."""
    for vendor in vendor_list:
        if vendor["id"] in vendor_ids:
            return vendor
    return None


def find_ticket_by_id(ticket_ids, ticket_list):
    """Return the ticket whose id appears in the given set, or None."""
    for ticket in ticket_list:
        if ticket["id"] in ticket_ids:
            return ticket
    return None


def find_shift_by_id(shift_ids, shift_list):
    """Return the volunteer shift whose id appears in the given set, or None."""
    for shift in shift_list:
        if shift["id"] in shift_ids:
            return shift
    return None


def find_schedule_by_id(schedule_ids, schedule_list):
    """Return the schedule entry whose id appears in the given set, or None."""
    for schedule in schedule_list:
        if schedule["id"] in schedule_ids:
            return schedule
    return None


def filter_vendors_by_category(categories, vendor_list):
    """Return vendors whose category is contained in the given set."""
    return [vendor for vendor in vendor_list if vendor["category"] in categories]


def filter_tickets_by_type(ticket_types, ticket_list):
    """Return tickets whose type is contained in the given set."""
    return [ticket for ticket in ticket_list if ticket["type"] in ticket_types]


def filter_shifts_by_role(roles, shift_list):
    """Return shifts whose role is contained in the given set."""
    return [shift for shift in shift_list if shift["role"] in roles]


def filter_schedules_by_date_range(start_date, end_date, schedule_list):
    """Return schedules scheduled within the inclusive start and end dates."""
    return [
        schedule
        for schedule in schedule_list
        if start_date <= schedule["date"] <= end_date
    ]


def count_tickets_by_type(ticket_list):
    """Return a dictionary mapping each ticket type to its occurrence count."""
    counts = {}
    for ticket in ticket_list:
        counts[ticket["type"]] = counts.get(ticket["type"], 0) + 1
    return counts


def format_schedule_entry(schedule):
    """Return a human-readable one-line description of a schedule entry."""
    return (
        f"Schedule {schedule['id']}: {schedule['event']} "
        f"at {schedule['stage']} on {schedule['date']} from {schedule['start_time']} to {schedule['end_time']}"
    )
