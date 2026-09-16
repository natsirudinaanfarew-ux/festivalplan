# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: FestivalPlan
import re
from datetime import date, timedelta

_DATE_RE = re.compile(
    r"^(?:(?P<y>\d{4})[-/\.](?P<m>\d{1,2})[-/\.](?P<d>\d{1,2})|"
    r"(?P<m>\d{1,2})[-/\.](?P<d>\d{1,2})[-/\.]?(?P<y>\d{4}))$",
)

def parse_date(text: str) -> date:
    """Parse a date string into a datetime.date object.

    Accepted formats: YYYY-MM-DD, YYYY/MM/DD, MM/DD/YYYY, MM-DD-YYYY,
    DD-MM-YYYY, DD/MM/YYYY.  When year is omitted it defaults to 2025.
    Raises ValueError with a clear message on failure.
    """
    text = text.strip()
    if not text:
        raise ValueError("parse_date: empty string")

    m = _DATE_RE.match(text)
    if not m:
        raise ValueError(
            f"parse_date: '{text}' is not a recognised date format."
        )

    parts = {
        "y": m.group("y") or "2025",
        "m": m.group("m"),
        "d": m.group("d"),
    }
    try:
        year, month, day = int(parts["y"]), int(parts["m"]), int(parts["d"])
    except ValueError:
        raise ValueError(
            f"parse_date: numeric values expected, got '{text}'."
        )
    try:
        return date(year, month, day)
    except ValueError as exc:
        raise ValueError(
            f"parse_date: invalid calendar date '{text}' ({exc})."
        )
