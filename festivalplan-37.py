# === Stage 37: Add recommendations for the next useful action ===
# Project: FestivalPlan
def generate_vendor_report(vendors):
    """Generate a simple text report of vendor performance."""
    report_lines = ["Festival Vendor Report", "=" * 40]
    for vendor in vendors:
        report_lines.append(f"{vendor['name']}: {vendor['status']}")
    return "\n".join(report_lines)
