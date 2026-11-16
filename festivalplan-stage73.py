# === Stage 73: Add a lightweight HTML report export ===
# Project: FestivalPlan
def export_html_report(festival, vendors, schedule, tickets, volunteers, filename="festival_report.html"):
    lines = [
        "<!DOCTYPE html>",
        "<html lang='en'><head><meta charset='utf-8'>",
        "<title>FestivalPlan Report</title>",
        "<style>body{font-family:sans-serif;margin:2rem}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ccc;padding:6px;text-align:left}th{background:#f0f0f0}</style>",
        "</head><body>"
    ]
    lines.append(f"<h1>Festival Plan Report</h1>")
    lines.append(f"<p>{festival.get('name','Festival')} &middot; {festival.get('date','')}</p>")
    lines.append("<h2>Vendors</h2><table><tr><th>Name</th><th>Booth</th><th>Category</th></tr>")
    for v in vendors:
        lines.append(f"<tr><td>{v.get('name','')}</td><td>{v.get('booth','')}</td><td>{v.get('category','')}</td></tr>")
    lines.append("</table>")
    lines.append("<h2>Schedule</h2><table><tr><th>Time</th><th>Event</th><th>Stage</th></tr>")
    for s in schedule:
        lines.append(f"<tr><td>{s.get('time','')}</td><td>{s.get('event','')}</td><td>{s.get('stage','')}</td></tr>")
    lines.append("</table>")
    lines.append("<h2>Tickets</h2><table><tr><th>Event</th><th>Price</th><th>Sold</th><th>Available</th></tr>")
    for t in tickets:
        lines.append(f"<tr><td>{t.get('event','')}</td><td>{t.get('price','')}</td><td>{t.get('sold','')}</td><td>{t.get('capacity','') - t.get('sold','')}</td></tr>")
    lines.append("</table>")
    lines.append("<h2>Volunteer Shifts</h2><table><tr><th>Name</th><th>Shift</th><th>Role</th></tr>")
    for vol in volunteers:
        lines.append(f"<tr><td>{vol.get('name','')}</td><td>{vol.get('shift','')}</td><td>{vol.get('role','')}</td></tr>")
    lines.append("</table>")
    lines.append("</body></html>")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
