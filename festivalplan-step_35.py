# === Stage 35: Add active user switching and user-specific records ===
# Project: FestivalPlan
class ActiveUser:
    """Manages the currently logged-in user and their festival records."""
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.vendor_list = []
        self.schedule = []
        self.ticket_list = []
        self.volunteer_shifts = []
        self.active = True

    def add_vendor(self, name: str, email: str, phone: str):
        self.vendor_list.append(Vendor(name, email, phone))

    def add_event(self, name: str, date: str, time: str, venue: str):
        self.schedule.append(Event(name, date, time, venue))

    def add_ticket(self, name: str, price: float):
        self.ticket_list.append(Ticket(name, price))

    def add_shift(self, name: str, date: str, time: str, hours: int):
        self.volunteer_shifts.append(Shift(name, date, time, hours))

    def deactivate(self):
        self.active = False
        self.vendor_list.clear()
        self.schedule.clear()
        self.ticket_list.clear()
        self.volunteer_shifts.clear()
