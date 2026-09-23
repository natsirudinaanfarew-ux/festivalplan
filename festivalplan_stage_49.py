# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: FestivalPlan
import pytest
from festivalplan.models import Vendor, Schedule, Ticket, VolunteerShift
from festivalplan.database import Database


@pytest.fixture
def db():
    db_instance = Database()
    db_instance.connect()
    return db_instance


def test_update_vendor_nonexistent(db):
    vendor = db.update_vendor("nonexistent_vendor_id", {"name": "Updated Vendor"})
    assert vendor is None


def test_update_schedule_invalid_date(db):
    schedule = db.update_schedule(
        "schedule_id",
        {"start": "2024-12-31", "end": "2024-12-31"},
    )
    assert schedule is None


def test_update_ticket_invalid_quantity(db):
    ticket = db.update_ticket(
        "ticket_id",
        {"quantity": -1},
    )
    assert ticket is None


def test_update_volunteer_shift_invalid_hours(db):
    shift = db.update_volunteer_shift(
        "shift_id",
        {"hours": 0},
    )
    assert shift is None


def test_delete_vendor_nonexistent(db):
    result = db.delete_vendor("nonexistent_vendor_id")
    assert result is False


def test_delete_schedule_nonexistent(db):
    result = db.delete_schedule("nonexistent_schedule_id")
    assert result is False


def test_delete_ticket_nonexistent(db):
    result = db.delete_ticket("nonexistent_ticket_id")
    assert result is False


def test_delete_volunteer_shift_nonexistent(db):
    result = db.delete_volunteer_shift("nonexistent_shift_id")
    assert result is False
