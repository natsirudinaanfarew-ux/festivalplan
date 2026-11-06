# === Stage 57: Add structured result objects for command handlers ===
# Project: FestivalPlan
class VendorResult:
    def __init__(self, vendor_id, name, category, booth, status):
        self.vendor_id = vendor_id
        self.name = name
        self.category = category
        self.booth = booth
        self.status = status

    def to_dict(self):
        return {
            "vendor_id": self.vendor_id,
            "name": self.name,
            "category": self.category,
            "booth": self.booth,
            "status": self.status,
        }


class ScheduleResult:
    def __init__(self, event_id, title, stage, start_time, end_time, performer):
        self.event_id = event_id
        self.title = title
        self.stage = stage
        self.start_time = start_time
        self.end_time = end_time
        self.performer = performer

    def to_dict(self):
        return {
            "event_id": self.event_id,
            "title": self.title,
            "stage": self.stage,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "performer": self.performer,
        }


class TicketResult:
    def __init__(self, ticket_id, holder_name, ticket_type, quantity, price, seat):
        self.ticket_id = ticket_id
        self.holder_name = holder_name
        self.ticket_type = ticket_type
        self.quantity = quantity
        self.price = price
        self.seat = seat

    def to_dict(self):
        return {
            "ticket_id": self.ticket_id,
            "holder_name": self.holder_name,
            "ticket_type": self.ticket_type,
            "quantity": self.quantity,
            "price": self.price,
            "seat": self.seat,
        }


class VolunteerShiftResult:
    def __init__(self, shift_id, volunteer_name, role, stage, start_time, end_time):
        self.shift_id = shift_id
        self.volunteer_name = volunteer_name
        self.role = role
        self.stage = stage
        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self):
        return {
            "shift_id": self.shift_id,
            "volunteer_name": self.volunteer_name,
            "role": self.role,
            "stage": self.stage,
            "start_time": self.start_time,
            "end_time": self.end_time,
        }
