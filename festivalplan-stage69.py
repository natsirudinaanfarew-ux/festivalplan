# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: FestivalPlan
def reset_demo_data(db):
    """Reset all tables to demo data for manual testing.

    Idempotent: clears and re-populates every collection so the
    festival toolkit always starts from a known, self-consistent
    demo state regardless of prior edits.
    """
    vendors = [
        {"id": 1, "name": "Acoustic Stage", "booth": "A1", "contact": "acoustic@demo.org"},
        {"id": 2, "name": "Craft Food Co", "booth": "B2", "contact": "food@demo.org"},
        {"id": 3, "name": "Live Sound", "booth": "C3", "contact": "sound@demo.org"},
    ]
    db["vendors"].replace(vendors)

    schedules = [
        {"id": 1, "date": "2025-08-15", "stage": "A1", "time": "10:00", "artist": "Sunset Trio"},
        {"id": 2, "date": "2025-08-15", "stage": "B2", "time": "12:00", "artist": "Food Truck Rally"},
        {"id": 3, "date": "2025-08-16", "stage": "A1", "time": "15:00", "artist": "Neon Lights"},
    ]
    db["schedules"].replace(schedules)

    tickets = [
        {"id": 1, "type": "General", "price": 25.0, "capacity": 500, "sold": 120},
        {"id": 2, "type": "VIP", "price": 75.0, "capacity": 100, "sold": 40},
        {"id": 3, "type": "Student", "price": 15.0, "capacity": 750, "sold": 300},
    ]
    db["tickets"].replace(tickets)

    shifts = [
        {"id": 1, "name": "Gate Team", "date": "2025-08-15", "hours": 8, "assigned": 10},
        {"id": 2, "name": "Stage Crew", "date": "2025-08-15", "hours": 6, "assigned": 8},
        {"id": 3, "name": "First Aid", "date": "2025-08-16", "hours": 10, "assigned": 6},
    ]
    db["shifts"].replace(shifts)

    print("FestivalPlan demo data reset complete.")
