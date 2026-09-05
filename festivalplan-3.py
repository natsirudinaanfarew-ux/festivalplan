# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: FestivalPlan
def validate_required(value, field_name):
    """Raise ValueError if value is None or empty string."""
    if not value:
        raise ValueError(f"{field_name} is required")

def validate_positive_int(value, field_name):
    """Raise ValueError if value is not a positive integer."""
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{field_name} must be a positive integer")

def validate_short_text(value, field_name, max_length=50):
    """Raise ValueError if value exceeds max_length characters."""
    if not isinstance(value, str) or len(value) > max_length:
        raise ValueError(f"{field_name} must be a short text (max {max_length} chars)")

def validate_identifier(value, field_name):
    """Raise ValueError if value is not a non-empty string (identifier use case)."""
    validate_required(value, field_name)
    validate_short_text(value, field_name, max_length=20)

def validate_email(value, field_name):
    """Basic email validation: check for @ and domain."""
    validate_required(value, field_name)
    if "@" not in value or "." not in value.split("@")[1]:
        raise ValueError(f"{field_name} must be a valid email address")

def validate_date(date_str, field_name):
    """Validate date string in YYYY-MM-DD format."""
    import datetime
    validate_required(date_str, field_name)
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"{field_name} must be in YYYY-MM-DD format")

def validate_time(time_str, field_name):
    """Validate time string in HH:MM format."""
    import datetime
    validate_required(time_str, field_name)
    try:
        datetime.datetime.strptime(time_str, "%H:%M")
    except ValueError:
        raise ValueError(f"{field_name} must be in HH:MM format")

def validate_datetime(dt_str, field_name):
    """Validate datetime string in YYYY-MM-DD HH:MM format."""
    import datetime
    validate_required(dt_str, field_name)
    try:
        datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    except ValueError:
        raise ValueError(f"{field_name} must be in YYYY-MM-DD HH:MM format")

def validate_positive_float(value, field_name):
    """Raise ValueError if value is not a positive float."""
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValueError(f"{field_name} must be a positive number")
