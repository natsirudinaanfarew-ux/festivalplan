# === Stage 19: Add undo support for the last simple mutation ===
# Project: FestivalPlan
import json
from datetime import datetime
from pathlib import Path
from collections import OrderedDict

class FestivalUndoManager:
    def __init__(self):
        self.history = OrderedDict()

    def record(self, action, state, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now()
        self.history[timestamp] = (action, state)

    def undo(self):
        if not self.history:
            return None
        latest = max(self.history.keys())
        _, state = self.history.pop(latest)
        return state

    def get_history(self):
        return self.history
