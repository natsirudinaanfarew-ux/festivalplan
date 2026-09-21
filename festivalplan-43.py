# === Stage 43: Add CSV import for the primary record type ===
# Project: FestivalPlan
import csv

def import_csv(file_path, record_type):
    records = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            record = {col: row[col].strip() for col in row}
            records.append(record)
    return records
