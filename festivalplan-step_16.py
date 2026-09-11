# === Stage 16: Add argparse support for the most common commands ===
# Project: FestivalPlan
import argparse

def main():
    parser = argparse.ArgumentParser(description="FestivalPlan - Festival Planning Toolkit")
    subparsers = parser.add_subparsers(dest="command")

    vendors = subparsers.add_parser("vendors", help="Manage vendors")
    vendors.add_argument("action", choices=["list", "add", "remove"], help="Vendor action")
    vendors.add_argument("--name", help="Vendor name (for add)")
    vendors.add_argument("--email", help="Vendor email (for add)")

    schedule = subparsers.add_parser("schedule", help="Manage schedules")
    schedule.add_argument("action", choices=["list", "add", "remove"], help="Schedule action")
    schedule.add_argument("--event", help="Event name (for add)")
    schedule.add_argument("--time", help="Event time (for add)")

    tickets = subparsers.add_parser("tickets", help="Manage tickets")
    tickets.add_argument("action", choices=["list", "create", "refund"], help="Ticket action")
    tickets.add_argument("--ticket-id", help="Ticket ID (for create/refund)")
    tickets.add_argument("--attendee", help="Attendee name (for create)")

    volunteers = subparsers.add_parser("volunteers", help="Manage volunteer shifts")
    volunteers.add_argument("action", choices=["list", "assign", "complete"], help="Volunteer action")
    volunteers.add_argument("--shift", help="Shift ID (for assign/complete)")
    volunteers.add_argument("--volunteer", help="Volunteer name (for assign)")

    args = parser.parse_args()
    print(f"FestivalPlan: command='{args.command}'")

if __name__ == "__main__":
    main()
