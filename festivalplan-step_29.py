# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: FestivalPlan
def upcoming_items(self, item_type, days_ahead=7):
        """Return items of given type scheduled within `days_ahead` days."""
        today = datetime.date.today()
        end = today + timedelta(days=days_ahead)
        results = []
        if item_type == "vendor":
            for v in self.vendors:
                if v["start_date"] and v["start_date"] <= end:
                    results.append(v)
        elif item_type == "event":
            for e in self.events:
                if e["date"] and e["date"] <= end:
                    results.append(e)
        elif item_type == "volunteer_shift":
            for s in self.volunteer_shifts:
                if s["shift_date"] and s["shift_date"] <= end:
                    results.append(s)
        return results
