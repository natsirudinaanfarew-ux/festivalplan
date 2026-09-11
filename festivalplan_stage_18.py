# === Stage 18: Add an activity log with timestamps and action names ===
# Project: FestivalPlan
import time

class ActivityLog:
    def __init__(self):
        self.entries = []
    
    def log(self, action, timestamp=None):
        ts = time.strftime('%Y-%m-%d %H:%M:%S') if timestamp is None else timestamp
        self.entries.append({'timestamp': ts, 'action': action})
    
    def get_log(self):
        return self.entries
