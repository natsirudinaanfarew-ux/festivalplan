# === Stage 56: Add compact error classes for domain failures ===
# Project: FestivalPlan
class FestivalError(Exception):
    pass


class VendorError(FestivalError):
    pass


class ScheduleError(FestivalError):
    pass


class TicketError(FestivalError):
    pass


class VolunteerError(FestivalError):
    pass


class CapacityError(TicketError):
    pass


class ConflictError(ScheduleError):
    pass


class OverlapError(VolunteerError):
    pass


class DuplicateError(FestivalError):
    pass


class NotFoundError(FestivalError):
    pass
