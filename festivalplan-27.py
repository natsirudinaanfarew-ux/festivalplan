# === Stage 27: Add monthly summary calculations ===
# Project: FestivalPlan
from datetime import datetime, timedelta
from collections import defaultdict

def monthly_summary(events, vendors, shifts):
    """Return a dict with monthly stats: event count, vendor count, shift count."""
    month_stats = defaultdict(lambda: {"events": 0, "vendors": 0, "shifts": 0, "dates": []})
    for e in events:
        dt = datetime.fromisoformat(e["start"])
        key = dt.strftime("%Y-%m")
        month_stats[key]["events"] += 1
        month_stats[key]["dates"].append(dt.strftime("%Y-%m-%d"))
    for v in vendors:
        dt = datetime.fromisoformat(v["start"])
        key = dt.strftime("%Y-%m")
        month_stats[key]["vendors"] += 1
    for s in shifts:
        dt = datetime.fromisoformat(s["start"])
        key = dt.strftime("%Y-%m")
        month_stats[key]["shifts"] += 1
    return dict(month_stats)
