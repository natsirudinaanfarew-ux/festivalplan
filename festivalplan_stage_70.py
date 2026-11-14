# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: FestivalPlan
CONFIRM_DELETE = False


def _prompt(message):
    reply = input(message).strip().lower()
    return reply == "y" or reply == "yes"


def clear_state():
    if CONFIRM_DELETE:
        if not _prompt("This will remove all vendors, schedules, tickets, and shifts. Continue? "):
            print("Aborted. No data was changed.")
            return
        print("All festival data has been cleared.")
        vendors.clear()
        schedules.clear()
        tickets.clear()
        shifts.clear()
        print("Next steps:")
        print("  add_vendor  -> register a new vendor")
        print("  add_schedule -> plan a stage schedule")
        print("  add_ticket   -> sell a ticket")
        print("  add_shift    -> assign a volunteer shift")
    else:
        print("Refusing to clear data. Set CONFIRM_DELETE = True to enable this command.")
