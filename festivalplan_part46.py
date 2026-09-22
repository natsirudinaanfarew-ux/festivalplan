# === Stage 46: Add a schema version field and migration helper ===
# Project: FestivalPlan
def migrate_database(db_path, schema_version):
    """Migrate the database to the specified schema version."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    current_version = cursor.execute("SELECT schema_version FROM metadata").fetchone()
    if current_version[0] < schema_version:
        cursor.execute("ALTER TABLE metadata ADD COLUMN schema_version INTEGER")
        cursor.execute("UPDATE metadata SET schema_version = ?", (schema_version,))
    conn.commit()
    conn.close()
