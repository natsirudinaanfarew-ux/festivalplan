# === Stage 64: Add validation for relationship references ===
# Project: FestivalPlan
def validate_references(data):
    if not isinstance(data, dict):
        return "Root must be a dict"
    errors = []
    vendors = data.get("vendors", [])
    if not isinstance(vendors, list):
        return "vendors must be a list"
    for vendor in vendors:
        if not isinstance(vendor, dict):
            continue
        if vendor.get("booth") and vendor["booth"] not in [v.get("id") for v in vendors]:
            errors.append(f"Vendor {vendor.get('id')} references unknown booth {vendor['booth']}")
        if vendor.get("manager_id") and vendor["manager_id"] not in [v.get("manager_id") for v in vendors if v.get("manager_id")]:
            errors.append(f"Vendor {vendor.get('id')} references unknown manager {vendor['manager_id']}")
    shifts = data.get("volunteer_shifts", [])
    if not isinstance(shifts, list):
        return "volunteer_shifts must be a list"
    for shift in shifts:
        if not isinstance(shift, dict):
            continue
        if shift.get("vendor_id") and shift["vendor_id"] not in [v.get("id") for v in vendors]:
            errors.append(f"Shift {shift.get('id')} references unknown vendor {shift['vendor_id']}")
        if shift.get("volunteer_id") and shift["volunteer_id"] not in [v.get("volunteer_id") for v in vendors]:
            errors.append(f"Shift {shift.get('id')} references unknown volunteer {shift['volunteer_id']}")
    return errors
