# === Stage 50: Add unit tests for import and export behavior ===
# Project: FestivalPlan
import os

# Verify the project directory exists
project_dir = os.path.dirname(os.path.abspath(__file__))
assert os.path.isdir(project_dir), "FestivalPlan directory not found"

# Test import and export functionality
from festival_plan import FestivalPlan

# Create a sample festival plan
festival = FestivalPlan("Test Festival 2024")

# Add vendors
festival.add_vendor("Food Truck", {"category": "food", "price_range": "moderate"})
festival.add_vendor("Live Band", {"category": "entertainment", "price_range": "premium"})

# Add schedule events
festival.add_event("Opening Ceremony", {"time": "12:00", "location": "Main Stage"})
festival.add_event("Food Truck", {"time": "13:00", "location": "Food Court"})

# Add tickets
festival.add_ticket("General Admission", {"price": 50, "capacity": 1000})
festival.add_ticket("VIP Pass", {"price": 150, "capacity": 100})

# Add volunteer shifts
festival.add_volunteer_shift("Stage Crew", {"hours": 8, "pay": 15})
festival.add_volunteer_shift("Security", {"hours": 10, "pay": 20})

# Test export functionality
festival.export_schedule()
festival.export_vendors()
festival.export_tickets()
festival.export_volunteer_shifts()

# Verify exports were created
exports = os.listdir(project_dir)
expected_exports = ["schedule.csv", "vendors.csv", "tickets.csv", "volunteer_shifts.csv"]

for export_file in expected_exports:
    assert os.path.isfile(os.path.join(project_dir, export_file)), f"{export_file} not created"

# Test import functionality
festival2 = FestivalPlan()
festival2.import_schedule()
festival2.import_vendors()
festival2.import_tickets()
festival2.import_volunteer_shifts()

# Verify imported data matches original
assert festival2.events == festival.events
assert festival2.vendors == festival.vendors
assert festival2.tickets == festival.tickets
assert festival2.shifts == festival.shifts

print("All import and export tests passed successfully!")
