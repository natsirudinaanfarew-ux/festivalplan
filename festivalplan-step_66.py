# === Stage 66: Add export of a short status dashboard ===
# Project: FestivalPlan
def print_dashboard():
    vendors = len(VENDORS)
    events = len(SCHEDULE)
    tickets = sum(len(t['sold']) for t in TICKETS.values())
    shifts = sum(len(s['shifts']) for s in VOLUNTEERS.values())
    print("=" * 40)
    print("FestivalPlan Status Dashboard")
    print("=" * 40)
    print(f"Vendors:      {vendors}")
    print(f"Events:       {events}")
    print(f"Tickets sold: {tickets}")
    print(f"Volunteer shifts: {shifts}")
    print("=" * 40)
