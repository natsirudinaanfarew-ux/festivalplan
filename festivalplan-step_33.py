# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: FestivalPlan
SETTINGS = {
    "festival_name": "Summer Vibes 2025",
    "venue": "Riverfront Park",
    "date": "2025-08-15",
    "timezone": "UTC",
    "currency": "USD",
    "max_vendors": 30,
    "max_volunteers": 100,
    "min_ticket_price": 10.0,
    "max_ticket_price": 50.0,
    "working_hours_start": 10,
    "working_hours_end": 22,
    "emergency_contact": "+1-555-0199",
    "website": "https://festivalplan.example.com",
}

def get_setting(key):
    """Retrieve a single setting value; raise KeyError if missing."""
    return SETTINGS[key]

def update_settings(**kwargs):
    """Update one or more settings in place and return a copy of the full dict."""
    SETTINGS.update(kwargs)
    return dict(SETTINGS)
