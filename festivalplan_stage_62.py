# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: FestivalPlan
def recommend_priorities(vendors, schedule, volunteers, capacity=1):
    """Score each task and return the most urgent ones first."""
    scores = {}
    for vendor in vendors:
        if not vendor.get("booked", False):
            scores[vendor["id"]] = 100 + vendor.get("deadline", 30) * 5
    for slot in schedule:
        if not slot.get("confirmed", False):
            scores[slot["id"]] = 50 + slot.get("day", 7) * 10
    for shift in volunteers:
        if not shift.get("assigned", False):
            scores[shift["id"]] = 30 + shift.get("hours", 4) * 2
    ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
    return ranked[:capacity]
