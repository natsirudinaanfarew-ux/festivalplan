# === Stage 67: Add a function that returns key project metrics ===
# Project: FestivalPlan
def project_metrics(vendors, schedule, tickets, volunteers):
    """Return key project metrics for the festival."""
    total_vendors = len(vendors)
    total_days = len({day for day in schedule if day})
    total_events = len(schedule)
    total_tickets = sum(1 for t in tickets if t.get("sold", 0))
    total_capacity = sum(t.get("capacity", 0) for t in tickets)
    total_volunteers = len(volunteers)
    total_shifts = len(volunteers)
    sold_percentage = (total_tickets / total_capacity * 100) if total_capacity else 0
    return {
        "total_vendors": total_vendors,
        "total_days": total_days,
        "total_events": total_events,
        "total_tickets_sold": total_tickets,
        "total_capacity": total_capacity,
        "ticket_sales_percentage": round(sold_percentage, 1),
        "total_volunteers": total_volunteers,
        "total_shifts": total_shifts,
    }
