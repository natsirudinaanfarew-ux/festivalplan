# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: FestivalPlan
import re

def delete_line(line: str, confirm: bool = False) -> str:
    """Remove a line if it matches 'DELETE' keyword, optionally after confirmation."""
    if not re.search(r'\bDELETE\b', line, re.IGNORECASE):
        return line
    if not confirm:
        print(f"⚠️  WARNING: DELETE detected but not confirmed. Skipping line:")
        print(f"   {line.strip()}")
        return line
    print(f"✅ DELETE confirmed. Removing:")
    print(f"   {line.strip()}")
    return ""
