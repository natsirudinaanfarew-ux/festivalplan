# === Stage 38: Add data integrity checks for broken references ===
# Project: FestivalPlan
def validate_references():
    """Ensure all cross-references in FestivalPlan are valid."""
    errors = []
    if 'vendors' in festival_data:
        vendor_ids = {v['id'] for v in festival_data['vendors']}
        for schedule in festival_data.get('schedules', []):
            for vendor in schedule.get('vendors', []):
                if vendor not in vendor_ids:
                    errors.append(f"Schedule {schedule['id']} references unknown vendor {vendor}")
    if 'tickets' in festival_data:
        ticket_types = {t['id'] for t in festival_data['tickets']}
        for ticket in festival_data.get('tickets', []):
            if ticket['type'] not in ticket_types:
                errors.append(f"Ticket {ticket['id']} references unknown type {ticket['type']}")
    if 'volunteers' in festival_data:
        volunteer_ids = {v['id'] for v in festival_data['volunteers']}
        for shift in festival_data.get('shifts', []):
            for volunteer in shift.get('volunteers', []):
                if volunteer not in volunteer_ids:
                    errors.append(f"Shift {shift['id']} references unknown volunteer {volunteer}")
    return errors
