# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: FestivalPlan
def load_activity_log(path="activity_log.json"):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return json.load(f)


def format_timestamp(ts):
    return datetime.fromisoformat(ts).strftime("%Y-%m-%d %H:%M")


def build_changelog(activity_log):
    entries = []
    for record in activity_log:
        date = record.get("timestamp", "")
        label = record.get("type", "entry")
        message = record.get("message", "")
        author = record.get("author", "unknown")
        entries.append(f"- [{format_timestamp(date)}] ({label}) {author}: {message}")
    return entries


def write_changelog(activity_log, path="CHANGELOG.md"):
    entries = build_changelog(activity_log)
    with open(path, "w") as f:
        f.write("# FestivalPlan Changelog\n\n")
        f.write("## Recent Activity\n\n")
        if not entries:
            f.write("_No activity recorded yet._\n")
        else:
            f.write("\n".join(entries) + "\n")
    return path


if __name__ == "__main__":
    import os

    write_changelog(load_activity_log(), "CHANGELOG.md")
    print("Changelog written.")
