# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: FestivalPlan
import json
from dataclasses import dataclass, field
from datetime import date

@dataclass
class Vendor:
    name: str
    booth: str
    category: str
    schedule: list[str] = field(default_factory=list)

@dataclass
class Ticket:
    ticket_id: str
    holder_name: str
    section: str
    date: str

@dataclass
class VolunteerShift:
    name: str
    shift_date: str
    role: str
    time_slot: str

class FestivalPlan:
    def __init__(self):
        self.vendors: dict[str, Vendor] = {}
        self.tickets: dict[str, Ticket] = {}
        self.shifts: dict[str, VolunteerShift] = {}

    def add_vendor(self, name, booth, category):
        v = Vendor(name, booth, category)
        self.vendors[booth] = v
        return v

    def sell_ticket(self, ticket_id, holder_name, section, date):
        t = Ticket(ticket_id, holder_name, section, date)
        self.tickets[ticket_id] = t
        return t

    def assign_shift(self, name, shift_date, role, time_slot):
        s = VolunteerShift(name, shift_date, role, time_slot)
        self.shifts[shift_date + "_" + time_slot] = s
        return s

    def to_dict(self):
        return {"vendors": self.vendors, "tickets": self.tickets, "shifts": self.shifts}

    @classmethod
    def from_dict(cls, data):
        p = cls()
        for booth, v in data["vendors"].items():
            p.vendors[booth] = Vendor(**v)
        for tid, t in data["tickets"].items():
            p.tickets[tid] = Ticket(**t)
        for key, s in data["shifts"].items():
            p.shifts[key] = VolunteerShift(**s)
        return p

demo = FestivalPlan()
demo.add_vendor("SoundWave", "A1", "Audio")
demo.add_vendor("FreshBites", "B3", "Food")
demo.sell_ticket("T001", "Alice", "VIP", "2026-07-15")
demo.sell_ticket("T002", "Bob", "General", "2026-07-15")
demo.assign_shift("Carol", "2026-07-15", "Stage Crew", "10-14")
demo.assign_shift("Dan", "2026-07-16", "Gate", "08-12")

with open("festival_plan.json", "w") as f:
    json.dump(demo.to_dict(), f, indent=2)

print(f"Loaded {len(demo.vendors)} vendors, {len(demo.tickets)} tickets, {len(demo.shifts)} shifts")
