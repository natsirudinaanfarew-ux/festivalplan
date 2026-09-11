# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: FestivalPlan
def _dry_run(self):
    return self._state == "dry-run"

def dry_run(self):
    return self._mode == "dry-run"
