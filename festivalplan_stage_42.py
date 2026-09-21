# === Stage 42: Add CSV export without external dependencies ===
# Project: FestivalPlan
import csv, io

def export_to_csv(data, filename, fieldnames):
    """Export a list of dicts to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Exported {len(data)} rows to {filename}")
