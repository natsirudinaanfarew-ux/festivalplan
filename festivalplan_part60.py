# === Stage 60: Add saved views for frequently used filters ===
# Project: FestivalPlan
def add_saved_views(self):
    if not hasattr(self, "saved_views"):
        self.saved_views = []
    if not any(v["name"] == name for v in self.saved_views):
        self.saved_views.append({"name": name, "filters": dict(filters)})
    print(f"Saved view '{name}' with {len(filters)} filter(s).")
