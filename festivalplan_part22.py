# === Stage 22: Add favorite records and quick favorite listing ===
# Project: FestivalPlan
from datetime import date, timedelta

class Favorite:
    def __init__(self, name, description="", due_date=None):
        self.name = name
        self.description = description
        self.due_date = due_date or date.today()

    def __repr__(self):
        return f"<Favorite {self.name} due {self.due_date}>"

    def is_overdue(self):
        return self.due_date < date.today()

    def priority(self):
        return 0 if self.is_overdue() else (1 if self.due_date < (date.today() + timedelta(days=7)) else 2)


favorites = []


def add_favorite(name, description="", due_date=None):
    f = Favorite(name, description, due_date)
    favorites.append(f)
    return f


def list_favorites():
    return [f for f in favorites if not f.is_overdue()]


def list_overdue():
    return [f for f in favorites if f.is_overdue()]


def quick_list():
    return sorted(favorites, key=lambda f: f.priority())
