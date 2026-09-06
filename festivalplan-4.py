# === Stage 4: Implement create operations for the primary records ===
# Project: FestivalPlan
# Step 4: Create operations for primary records in FestivalPlan

def create_vendor(vendor_data):
    """Create a new vendor record."""
    vendor_id = f"VND-{len(vendors)+1:04d}"
    vendors.append({
        "id": vendor_id,
        "name": vendor_data["name"],
        "category": vendor_data.get("category", "General"),
        "contact": vendor_data.get("contact", ""),
        "booth_number": vendor_data.get("booth_number", ""),
        "created_at": datetime.now().isoformat()
    })
    return vendor_id

def create_event(event_data):
    """Create a new event/act record."""
    event_id = f"EVT-{len(events)+1:04d}"
    events.append({
        "id": event_id,
        "name": event_data["name"],
        "genre": event_data.get("genre", "Music"),
        "scheduled_time": event_data.get("scheduled_time", ""),
        "duration_minutes": event_data.get("duration_minutes", 60),
        "stage": event_data.get("stage", "Main Stage"),
        "created_at": datetime.now().isoformat()
    })
    return event_id

def create_ticket(ticket_data):
    """Create a new ticket record."""
    ticket_id = f"TKT-{len(tickets)+1:04d}"
    tickets.append({
        "id": ticket_id,
        "event_id": ticket_data["event_id"],
        "holder_name": ticket_data["holder_name"],
        "seat_number": ticket_data.get("seat_number", ""),
        "ticket_type": ticket_data.get("ticket_type", "General"),
        "price": ticket_data.get("price", 0.0),
        "status": ticket_data.get("status", "active"),
        "created_at": datetime.now().isoformat()
    })
    return ticket_id

def create_volunteer_shift(shift_data):
    """Create a new volunteer shift record."""
    shift_id = f"SHF-{len(shifts)+1:04d}"
    shifts.append({
        "id": shift_id,
        "volunteer_name": shift_data["volunteer_name"],
        "event_id": shift_data["event_id"],
        "start_time": shift_data["start_time"],
        "end_time": shift_data["end_time"],
        "role": shift_data.get("role", "General"),
        "status": shift_data.get("status", "pending"),
        "created_at": datetime.now().isoformat()
    })
    return shift_id
