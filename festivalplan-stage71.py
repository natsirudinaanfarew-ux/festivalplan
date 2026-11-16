# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: FestivalPlan
def seed_demo_data(db, count=5):
    vendors = []
    for i in range(count):
        vendors.append({
            'id': f'V{i+1:03d}',
            'name': f'VENDOR {i+1}',
            'category': ['Food', 'Music', 'Crafts'][i % 3],
            'booth': f'Booth {chr(65 + i)}',
            'contact': f'vendor{i+1}@demo.festival',
            'phone': f'555000{100+i}',
            'status': 'confirmed' if i % 2 == 0 else 'pending',
            'commission': 10.0,
        })
    db['vendors'] = vendors

    schedules = []
    for i in range(count):
        schedules.append({
            'id': f'S{i+1:03d}',
            'event': f'Workshop {i+1}',
            'vendor_id': vendors[i % count]['id'],
            'day': 1 + (i % 3),
            'start_time': f'09:00',
            'end_time': f'11:00',
            'location': f'Tent {chr(65 + i % 3)}',
        })
    db['schedules'] = schedules

    tickets = []
    for i in range(count):
        tickets.append({
            'id': f'T{i+1:04d}',
            'ticket_type': ['General', 'VIP', 'Student'][i % 3],
            'attendee': f'Attendee {i+1}',
            'email': f'attendee{i+1}@demo.festival',
            'quantity': 1 + (i % 4),
            'price': 25.0 * (1 + (i % 3)),
            'status': 'active',
            'purchased_at': '2024-01-15',
        })
    db['tickets'] = tickets

    shifts = []
    for i in range(count):
        shifts.append({
            'id': f'SH{i+1:04d}',
            'volunteer': f'Volunteer {i+1}',
            'email': f'volunteer{i+1}@demo.festival',
            'event_id': f'S{i % count + 1:03d}',
            'day': 1 + (i % 3),
            'start_time': f'08:00',
            'end_time': f'16:00',
            'role': ['Setup', 'Ushering', 'Cleanup'][i % 3],
            'status': 'assigned',
        })
    db['shifts'] = shifts
