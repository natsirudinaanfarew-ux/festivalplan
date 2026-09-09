# === Stage 13: Add file save support using a configurable path ===
# Project: FestivalPlan
import json
import os
from pathlib import Path

class Config:
    def __init__(self, save_path: str = "festival_config.json"):
        self.save_path = Path(save_path)
        self.data = {}

    def save(self, data):
        self.data = data
        self.save_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.save_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    def load(self):
        if self.save_path.exists():
            with open(self.save_path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        return self.data

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value

    def show(self):
        print(f"Config saved at: {self.save_path}")
        print(f"Current data: {self.data}")
