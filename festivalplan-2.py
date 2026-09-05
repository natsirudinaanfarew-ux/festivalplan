# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: FestivalPlan
from dataclasses import dataclass
from datetime import date, time
from enum import Enum


class TicketType(Enum):
    STANDARD = "standard"
    VIP = "vip"
    BACKSTAGE = "backstage"


class VendorCategory(Enum):
    FOOD = "food"
    MERCH = "merch"
    ART = "art"
    SERVICES = "services"


@dataclass
class Ticket:
    ticket_id: int
    type: TicketType
    price: float
    holder_name: str
    purchased_at: date
    is_used: bool

    def __str__(self) -> str:
        return (
            f"[Ticket #{self.ticket_id}] "
            f"type={self.type.value} "
            f"price=${self.price:.2f} "
            f"holder={self.holder_name} "
            f"used={self.is_used}"
        )


@dataclass
class Vendor:
    vendor_id: int
    name: str
    category: VendorCategory
    location: str
    schedule: list[tuple[date, time, date, time]]
    contact_email: str
    is_active: bool

    def __str__(self) -> str:
        return (
            f"[Vendor #{self.vendor_id}] "
            f"{self.name} "
            f"({self.category.value}) "
            f"at {self.location} "
            f"email={self.contact_email} "
            f"active={self.is_active}"
        )


@dataclass
class VolunteerShift:
    shift_id: int
    name: str
    role: str
    date: date
    start_time: time
    end_time: time
    assigned_volunteer: str | None

    def __str__(self) -> str:
        return (
            f"[Shift #{self.shift_id}] "
            f"{self.name} "
            f"role={self.role} "
            f"{self.date} {self.start_time}-{self.end_time} "
            f"volunteer={self.assigned_volunteer}"
        )


@dataclass
class Schedule:
    event_id: int
    name: str
    stage: str
    date: date
    start_time: time
    end_time: time
    description: str

    def __str__(self) -> str:
        return (
            f"[Event #{self.event_id}] "
            f"{self.name} "
            f"on {self.date} "
            f"{self.start_time}-{self.end_time} "
            f"at {self.stage} "
            f"desc={self.description}"
        )
