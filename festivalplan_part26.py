# === Stage 26: Add weekly summary calculations ===
# Project: FestivalPlan
def weekly_summary(festival):
    """Compute per-week summary of revenue, vendor count, and volunteer hours."""
    weeks = {}
    for day in festival.get_days():
        week = day["date"].isocalendar()[1]
        if week not in weeks:
            weeks[week] = {"revenue": 0, "vendors": 0, "volunteer_hours": 0, "days": 0}
        weeks[week]["revenue"] += day.get("revenue", 0)
        weeks[week]["vendors"] += len(day.get("vendors", []))
        weeks[week]["volunteer_hours"] += sum(s["hours"] for s in day.get("volunteers", []))
        weeks[week]["days"] += 1
    return weeks
