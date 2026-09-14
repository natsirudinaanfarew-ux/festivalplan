# === Stage 25: Add daily summary calculations ===
# Project: FestivalPlan
def daily_summary(festival):
    """Compute a compact daily summary: revenue, attendance, and volunteer hours."""
    summary = {}
    for day in festival.schedule:
        day_summary = {
            'date': day['date'],
            'revenue': sum(v['sales'] for v in day.get('vendors', [])),
            'attendance': sum(t['attendees'] for t in day.get('tickets', [])),
            'volunteer_hours': sum(vs['hours'] for vs in day.get('volunteers', [])),
        }
        summary[day['date']] = day_summary
    return summary
