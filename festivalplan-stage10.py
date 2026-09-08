# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: FestivalPlan
class CaseInsensitiveMixin:
    """Mixin adding case-insensitive search across common fields."""
    SEARCH_FIELDS = ("name", "type", "genre", "email", "phone", "date", "time", "role", "status")

    def search(self, query: str) -> list:
        query = query.strip().lower()
        return [item for item in self._items if
                any(query in str(getattr(item, f, "")).lower() for f in self.SEARCH_FIELDS)]
