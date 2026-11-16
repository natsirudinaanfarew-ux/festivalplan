# === Stage 72: Add Markdown report export ===
# Project: FestivalPlan
def export_markdown_report(festival):
    lines = []
    lines.append("# FestivalPlan Report")
    lines.append("")
    lines.append(f"Name: {festival['name']}")
    lines.append(f"Date: {festival['date']}")
    lines.append("")
    lines.append("## Vendors")
    for vendor in festival.get("vendors", []):
        lines.append(f"- {vendor['name']} ({vendor['category']})")
    lines.append("")
    lines.append("## Schedule")
    for time_slot, events in festival.get("schedule", {}).items():
        lines.append(f"### {time_slot}")
        for event in events:
            lines.append(f"- {event['name']} at {event['stage']}")
        lines.append("")
    lines.append("## Tickets")
    for ticket in festival.get("tickets", []):
        lines.append(f"- {ticket['name']}: {ticket['price']}")
    lines.append("")
    lines.append("## Volunteer Shifts")
    for shift in festival.get("volunteer_shifts", []):
        lines.append(f"- {shift['name']} at {shift['stage']} ({shift['hours']})")
    lines.append("")
    return "\n".join(lines)
