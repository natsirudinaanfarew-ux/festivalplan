# === Stage 53: Add command help text and usage examples ===
# Project: FestivalPlan
def show_help():
    print("FestivalPlan - festival planning toolkit")
    print("Commands:")
    print("  add_vendor   Add a vendor with name, category, and booth")
    print("  list_vendors Show all registered vendors")
    print("  add_event    Add a scheduled event with date, time, and stage")
    print("  list_events  Show the full festival schedule")
    print("  add_ticket   Add a ticket type with price and capacity")
    print("  list_tickets Show available ticket types")
    print("  add_shift    Add a volunteer shift with role and hours")
    print("  list_shifts  Show all volunteer shifts")
    print("  help         Show this help message")
    print("  exit         Exit the program")

if __name__ == "__main__":
    show_help()
