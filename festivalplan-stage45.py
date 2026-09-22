# === Stage 45: Add restore from backup with validation ===
# Project: FestivalPlan
def restore_from_backup(self, backup_path, validate=True):
        """Restore festival data from a JSON backup file.
        
        Args:
            backup_path: Path to the backup JSON file.
            validate: If True, validate the backup structure before restoring.
            
        Returns:
            True if restoration was successful, False otherwise.
            
        Raises:
            FileNotFoundError: If backup file does not exist.
            ValueError: If validation fails or data is corrupted.
        """
        import json
        import os
        
        if not os.path.exists(backup_path):
            raise FileNotFoundError(f"Backup file not found: {backup_path}")
        
        with open(backup_path, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                raise ValueError("Backup file contains invalid JSON")
        
        if validate:
            required_keys = ['vendors', 'schedule', 'tickets', 'volunteers']
            for key in required_keys:
                if key not in data:
                    raise ValueError(f"Missing required key in backup: {key}")
        
        self.vendors.clear()
        self.vendors.update(data['vendors'])
        
        self.schedule.clear()
        self.schedule.update(data['schedule'])
        
        self.tickets.clear()
        self.tickets.update(data['tickets'])
        
        self.volunteers.clear()
        self.volunteers.update(data['volunteers'])
        
        return True
