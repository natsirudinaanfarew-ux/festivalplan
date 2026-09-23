# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: FestivalPlan
import sys
sys.path.insert(0, '..')

from festivalplan import Vendor, Schedule, Ticket, VolunteerShift

# --- Demo scenario ---

# 1. Create vendors
vendors = [
    Vendor(name="DJ Thunder", stage="Main Stage", price=50.0, capacity=2000),
    Vendor(name="Street Artists", stage="Art Plaza", price=15.0, capacity=500),
    Vendor(name="Food Truck", stage="Food Court", price=10.0, capacity=300),
]

# 2. Create schedule
schedule = Schedule(
    name="Summer Vibes 2025",
    day="Saturday",
    hour=10,
    artists=vendors,
    duration=4,
)

# 3. Create tickets
ticket = Ticket(
    name="VIP Pass",
    price=150.0,
    capacity=500,
    events=[schedule],
)

# 4. Create volunteer shifts
volunteers = [
    VolunteerShift(name="Alice", role="Stage Crew", shift_start="08:00", shift_end="16:00"),
    VolunteerShift(name="Bob", role="Security", shift_start="12:00", shift_end="20:00"),
]

# 5. Print summary
print(f"Festival: {ticket.name}")
print(f"Day: {schedule.day}, Hour: {schedule.hour}")
print(f"Vendors: {len(vendors)}")
print(f"Tickets sold: {ticket.capacity}")
print(f"Volunteers: {len(volunteers)}")

for v in vendors:
    print(f"  - {v.name} @ {v.stage} (${v.price})")

for vol in volunteers:
    print(f"  - {vol.name}: {vol.role} ({vol.shift_start}-{vol.shift_end})")
