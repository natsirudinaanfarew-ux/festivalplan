# === Stage 11: Add JSON export for the current application state ===
# Project: FestivalPlan
def export_state():
    """Export the current FestivalPlan state to a JSON file."""
    import json
    state = {
        "vendors": vendors,
        "schedule": schedule,
        "tickets": tickets,
        "volunteers": volunteers,
        "settings": settings,
    }
    with open("festival_plan_state.json", "w") as f:
        json.dump(state, f, indent=2)
    print("FestivalPlan state exported to festival_plan_state.json")
