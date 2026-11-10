# === Stage 61: Add performance timing for core list and search operations ===
# Project: FestivalPlan
import timeit
from festivalplanner import FestivalPlan


def _build_sample_plan(n=50):
    plan = FestivalPlan()
    for i in range(n):
        plan.add_vendor(id=f"V{i}", name=f"Vendor {i}", type="food")
        plan.add_schedule_slot(id=f"S{i}", title=f"Event {i}", start=600 + i, end=630 + i)
        plan.add_ticket(id=f"T{i}", event_id=f"S{i}", price=10.0, quantity=100)
        plan.add_shift(id=f"SH{i}", event_id=f"S{i}", volunteer_id=f"V{i}", start=600 + i, end=630 + i)
    return plan


def _measure_list_operations(plan):
    setup = "plan=_build_sample_plan()"
    vendor_add = timeit.timeit("plan.add_vendor(id='V', name='X', type='food')", setup=setup, number=1000)
    schedule_add = timeit.timeit("plan.add_schedule_slot(id='S', title='E', start=1, end=2)", setup=setup, number=1000)
    ticket_add = timeit.timeit("plan.add_ticket(id='T', event_id='S', price=1.0, quantity=10)", setup=setup, number=1000)
    shift_add = timeit.timeit("plan.add_shift(id='SH', event_id='S', volunteer_id='V', start=1, end=2)", setup=setup, number=1000)
    return vendor_add, schedule_add, ticket_add, shift_add


def _measure_search_operations(plan):
    setup = "plan=_build_sample_plan()"
    vendor_search = timeit.timeit("plan.search_vendors('Vendor')", setup=setup, number=1000)
    schedule_search = timeit.timeit("plan.search_schedule('Event')", setup=setup, number=1000)
    ticket_search = timeit.timeit("plan.search_tickets('S')", setup=setup, number=1000)
    shift_search = timeit.timeit("plan.search_shifts('S')", setup=setup, number=1000)
    return vendor_search, schedule_search, ticket_search, shift_search


if __name__ == "__main__":
    print("=== FestivalPlan Performance Timing ===\n")

    print("List Operations (seconds per operation):")
    va, sa, ta, sha = _measure_list_operations()
    print(f"  add_vendor:     {va:.6f}")
    print(f"  add_schedule:   {sa:.6f}")
    print(f"  add_ticket:     {ta:.6f}")
    print(f"  add_shift:      {sha:.6f}")

    print("\nSearch Operations (seconds per operation):")
    vss, sss, tss, shss = _measure_search_operations()
    print(f"  search_vendors:     {vss:.6f}")
    print(f"  search_schedule:    {sss:.6f}")
    print(f"  search_tickets:     {tss:.6f}")
    print(f"  search_shifts:      {shss:.6f}")
