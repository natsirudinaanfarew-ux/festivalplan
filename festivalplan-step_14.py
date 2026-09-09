# === Stage 14: Add file load support with fallback demo data ===
# Project: FestivalPlan
def load_demo_data():
    """Provide fallback demo data when no file is loaded."""
    return {
        "vendors": [
            {"id": 1, "name": "Food Truck Co", "category": "food", "status": "active"},
            {"id": 2, "name": "Live Band A", "category": "entertainment", "status": "active"},
            {"id": 3, "name": "Merch Stand B", "category": "merchandise", "status": "pending"},
        ],
        "schedule": [
            {"time": "10:00", "event": "Opening Ceremony", "location": "Main Stage"},
            {"time": "12:00", "event": "Lunch Break", "location": "General"},
            {"time": "14:00", "event": "Live Band A", "location": "Main Stage"},
        ],
        "tickets": [
            {"id": 1, "type": "day_pass", "price": 50.00, "available": 200},
            {"id": 2, "type": "vip_pass", "price": 120.00, "available": 50},
        ],
        "volunteers": [
            {"id": 1, "name": "Alice", "shift": "security", "hours": 8},
            {"id": 2, "name": "Bob", "shift": "setup", "hours": 4},
        ],
    }
