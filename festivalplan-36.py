# === Stage 36: Add templates for quickly creating common records ===
# Project: FestivalPlan
# Templates for quickly creating common records
def make_vendor(name, booth, category="food", price=0):
    return {"id": name, "name": name, "booth": booth, "category": category, "price": price}

def make_schedule(date, time, vendor, stage="main", duration=30):
    return {"id": f"{date}-{time}", "date": date, "time": time, "vendor": vendor, "stage": stage, "duration": duration}

def make_ticket(holder, event, seats=1, price=0):
    return {"id": holder, "holder": holder, "event": event, "seats": seats, "price": price}

def make_shift(volunteer, day, time_start, time_end, task="setup"):
    return {"id": f"{volunteer}-{day}", "volunteer": volunteer, "day": day, "time_start": time_start, "time_end": time_end, "task": task}
