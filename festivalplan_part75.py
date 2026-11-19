# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: FestivalPlan
def generate_validation_report(festival):
    warnings = []
    errors = []
    for vendor in festival["vendors"]:
        if vendor["end"] < vendor["start"]:
            errors.append(f"Vendor {vendor['id']} has end before start")
        if vendor["capacity"] <= 0:
            errors.append(f"Vendor {vendor['id']} has non-positive capacity")
        if vendor.get("payment_method") not in ("cash", "card", "none"):
            warnings.append(f"Vendor {vendor['id']} has unknown payment method")
    for shift in festival["volunteer_shifts"]:
        if shift["start"] < 0 or shift["end"] <= shift["start"]:
            errors.append(f"Volunteer shift {shift['id']} has invalid time window")
        if shift.get("required_skill") not in shift["allowed_skills"]:
            warnings.append(f"Volunteer shift {shift['id']} requires unlisted skill")
    for ticket in festival["tickets"]:
        if ticket["price"] < 0:
            errors.append(f"Ticket {ticket['id']} has negative price")
        if ticket["max_sales"] < 0:
            errors.append(f"Ticket {ticket['id']} has negative max sales")
    report = {"errors": errors, "warnings": warnings, "total_errors": len(errors), "total_warnings": len(warnings)}
    return report
