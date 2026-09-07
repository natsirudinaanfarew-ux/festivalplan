# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: FestivalPlan
def format_vendor(v):
    return f"[{v.id}] {v.name} | {v.category} | {v.status} | {v.contact}"

def format_schedule(s):
    return f"{s.date} | {s.time} | {s.event} | {s.location}"

def format_ticket(t):
    return f"[{t.id}] {t.holder} | {t.event} | {t.category} | {t.price}"

def format_shift(s):
    return f"[{s.id}] {s.volunteer} | {s.role} | {s.start}-{s.end} | {s.location}"

def print_vendor_list(vendors):
    if not vendors:
        print("No vendors registered.")
        return
    for v in vendors:
        print(format_vendor(v))

def print_schedule_list(schedules):
    if not schedules:
        print("No events scheduled.")
        return
    for s in schedules:
        print(format_schedule(s))

def print_ticket_list(tickets):
    if not tickets:
        print("No tickets sold.")
        return
    for t in tickets:
        print(format_ticket(t))

def print_shift_list(shifts):
    if not shifts:
        print("No volunteer shifts assigned.")
        return
    for s in shifts:
        print(format_shift(s))
