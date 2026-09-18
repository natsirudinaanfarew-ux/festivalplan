# === Stage 34: Add support for multiple local user profiles ===
# Project: FestivalPlan
import json
from pathlib import Path

class UserProfiles:
    def __init__(self, profiles_path="festival_profiles.json"):
        self.profiles_path = Path(profiles_path)
        self.profiles = {}
        if self.profiles_path.exists():
            with open(self.profiles_path) as f:
                self.profiles = json.load(f)

    def add_profile(self, name, email, role="attendee"):
        if name in self.profiles:
            raise ValueError(f"Profile '{name}' already exists")
        self.profiles[name] = {"email": email, "role": role}
        self.save()
        return self.profiles[name]

    def get_profile(self, name):
        return self.profiles.get(name)

    def list_profiles(self):
        return list(self.profiles.keys())

    def save(self):
        with open(self.profiles_path, "w") as f:
            json.dump(self.profiles, f, indent=2)

    def remove_profile(self, name):
        if name in self.profiles:
            del self.profiles[name]
            self.save()
            return True
        return False
