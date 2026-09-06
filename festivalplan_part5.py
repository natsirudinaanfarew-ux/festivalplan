# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: FestivalPlan
def update_record(db_path, collection, record_id, updates):
    """Update a single record by ID; return the new dict or None if missing."""
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {collection} WHERE id = ?", (record_id,))
        row = cur.fetchone()
        if row is None:
            return None
        cols = [d[0] for d in cur.description]
        new_row = dict(zip(cols, row))
        new_row.update(updates)
        set_clause = ", ".join(f"{k} = ?" for k in updates)
        cur.execute(f"UPDATE {collection} SET {set_clause} WHERE id = ?",
                    list(updates.values()) + [record_id])
        conn.commit()
        return new_row
    finally:
        conn.close()
