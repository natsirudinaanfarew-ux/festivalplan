# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: FestivalPlan
class ArchiveMixin:
    """Mixin adding archive/restore behavior to record models."""
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._is_archived = False
        cls._archive_date = None

    @property
    def is_archived(self):
        return self._is_archived

    @property
    def archived_on(self):
        return self._archive_date

    def archive(self, date=None):
        self._is_archived = True
        self._archive_date = date
        self.save()

    def restore(self):
        self._is_archived = False
        self._archive_date = None
        self.save()

    def __repr__(self):
        status = "archived" if self._is_archived else "active"
        return f"{self.__class__.__name__}({status})"
