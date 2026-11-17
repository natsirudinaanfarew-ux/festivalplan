# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: FestivalPlan
def snapshot_diff(before, after):
    """Return a compact before/after comparison of two equal-shaped snapshots."""
    changes = []
    for key in sorted(set(before) | set(after)):
        old = before.get(key)
        new = after.get(key)
        if old != new:
            changes.append({"key": key, "before": old, "after": new})
    return changes


def summarize_changes(changes):
    """Summarize changes as added, removed, or updated fields."""
    summary = {"added": [], "removed": [], "updated": []}
    for change in changes:
        key = change["key"]
        old = change["before"]
        new = change["after"]
        if old is None:
            summary["added"].append(key)
        elif new is None:
            summary["removed"].append(key)
        else:
            summary["updated"].append((key, old, new))
    return summary


def render_snapshot_report(before, after):
    """Render a readable before/after report string."""
    changes = snapshot_diff(before, after)
    lines = []
    lines.append("Snapshot Comparison")
    lines.append("=" * 30)
    if not changes:
        lines.append("No changes detected.")
    for change in changes:
        lines.append(f"key: {change['key']}")
        lines.append(f"  before: {change['before']}")
        lines.append(f"  after:  {change['after']}")
    return "\n".join(lines)
