# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: FestivalPlan
def repair_data(filepath):
    """Repair common data integrity issues in FestivalPlan data files."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return False

    if filepath.endswith('.json'):
        try:
            data = json.loads(content)
            if 'vendors' in data:
                for vendor in data['vendors']:
                    if 'id' not in vendor:
                        vendor['id'] = str(uuid.uuid4())[:8]
                    if 'name' not in vendor:
                        vendor['name'] = 'Unnamed Vendor'
            if 'tickets' in data:
                for ticket in data['tickets']:
                    if 'id' not in ticket:
                        ticket['id'] = str(uuid.uuid4())[:8]
                    if 'price' not in ticket:
                        ticket['price'] = 0.0
            if 'volunteers' in data:
                for vol in data['volunteers']:
                    if 'id' not in vol:
                        vol['id'] = str(uuid.uuid4())[:8]
                    if 'name' not in vol:
                        vol['name'] = 'Unnamed Volunteer'
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            print("JSON file repaired successfully.")
            return True
        except json.JSONDecodeError:
            print("Invalid JSON format. Cannot repair.")
            return False
    elif filepath.endswith('.csv'):
        try:
            import csv
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                rows = list(reader)
            if rows:
                headers = rows[0]
                required = ['name']
                for row in rows[1:]:
                    if row and not any(cell.strip() for cell in row):
                        row[0] = 'Unnamed'
                    if row and not any(cell.strip() for cell in row[:len(headers)]):
                        for h in required:
                            if h in headers:
                                idx = headers.index(h)
                                if not row[idx].strip():
                                    row[idx] = 'Default'
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(rows)
            print("CSV file repaired successfully.")
            return True
        except Exception as e:
            print(f"CSV repair failed: {e}")
            return False
    return False
