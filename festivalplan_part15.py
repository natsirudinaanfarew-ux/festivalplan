# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: FestivalPlan
def dispatch_command(text):
    """Parse a space-separated command and return the handler function."""
    parts = text.strip().split(maxsplit=1)
    cmd = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ""

    commands = {
        "add_vendor": lambda a: add_vendor(a),
        "add_schedule": lambda a: add_schedule(a),
        "add_ticket": lambda a: add_ticket(a),
        "add_volunteer": lambda a: add_volunteer(a),
        "list_vendors": lambda a: list_vendors(),
        "list_schedules": lambda a: list_schedules(),
        "list_tickets": lambda a: list_tickets(),
        "list_volunteers": lambda a: list_volunteers(),
        "show_vendor": lambda a: show_vendor(a),
        "show_schedule": lambda a: show_schedule(a),
        "show_ticket": lambda a: show_ticket(a),
        "show_volunteer": lambda a: show_volunteer(a),
        "delete_vendor": lambda a: delete_vendor(a),
        "delete_schedule": lambda a: delete_schedule(a),
        "delete_ticket": lambda a: delete_ticket(a),
        "delete_volunteer": lambda a: delete_volunteer(a),
        "help": lambda a: help_menu(),
        "quit": lambda a: quit_app(),
        "clear": lambda a: clear_screen(),
    }

    handler = commands.get(cmd)
    if handler is None:
        return print(f"Unknown command: {cmd}. Type 'help' for available commands.")
    return handler(args)
