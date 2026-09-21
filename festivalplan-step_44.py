# === Stage 44: Add backup creation for the data file ===
# Project: FestivalPlan
import os
import shutil

def create_backup(source_path, backup_dir=None):
    if backup_dir is None:
        backup_dir = os.path.join(os.path.dirname(source_path), "backups")
    os.makedirs(backup_dir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(source_path))[0]
    suffix = os.path.splitext(os.path.basename(source_path))[1]
    # Rotate: remove oldest backup if more than 5 exist
    backups = sorted(
        os.listdir(backup_dir),
        key=lambda f: f,
        reverse=True
    )
    if len(backups) > 5:
        os.remove(os.path.join(backup_dir, backups[0]))
    target = os.path.join(backup_dir, f"{stem}_backup_{suffix}")
    shutil.copy2(source_path, target)
    print(f"Backup created: {target}")
