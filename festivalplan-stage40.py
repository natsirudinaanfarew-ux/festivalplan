# === Stage 40: Add plain text report export ===
# Project: FestivalPlan
def export_report(data, filename="festival_report.txt"):
    """Export festival plan data as a plain text report."""
    lines = []
    lines.append("=" * 50)
    lines.append("FESTIVAL PLAN REPORT")
    lines.append("=" * 50)
    lines.append("")
    if "vendors" in data:
        lines.append("VENDORS:")
        for name, info in data["vendors"].items():
            lines.append(f"  - {name}: {info.get('category', 'N/A')}")
        lines.append("")
    if "schedule" in data:
        lines.append("SCHEDULE:")
        for day, events in data["schedule"].items():
            lines.append(f"  Day: {day}")
            for event in events:
                lines.append(f"    {event.get('time', 'N/A')} - {event.get('event_name', 'N/A')}")
            lines.append("")
    if "tickets" in data:
        lines.append("TICKETS:")
        for ticket in data["tickets"]:
            lines.append(f"  - {ticket.get('holder', 'Unknown')}: {ticket.get('ticket_type', 'N/A')}")
        lines.append("")
    if "volunteers" in data:
        lines.append("VOLUNTEERS:")
        for name, info in data["volunteers"].items():
            lines.append(f"  - {name}: {info.get('role', 'N/A')}")
        lines.append("")
    lines.append("=" * 50)
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    return filename
