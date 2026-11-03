# === Stage 51: Add unit tests for search and filter behavior ===
# Project: FestivalPlan
def test_search_by_name_contains():
    vendors = Vendor("Food Truck A", "Food", 100)
    vendors += Vendor("Bev Bar B", "Beverages", 150)
    assert len(vendors.search("food")) == 1
    assert len(vendors.search("bev")) == 1

def test_search_no_match_returns_empty():
    vendors = Vendor("Food Truck", "Food", 100)
    assert vendors.search("xyz") == []

def test_search_is_case_insensitive():
    vendors = Vendor("Sound System", "Gear", 200)
    assert len(vendors.search("sound")) == 1
    assert len(vendors.search("SOUND")) == 1

def test_filter_by_category():
    vendors = Vendor("Food Truck", "Food", 100)
    vendors += Vendor("Live Band", "Music", 300)
    assert len(vendors.filter("Music")) == 1

def test_filter_no_match_returns_empty():
    vendors = Vendor("Food Truck", "Food", 100)
    assert vendors.filter("Nonexistent") == []

def test_filter_by_price_range():
    vendors = Vendor("Cheap Booth", "Food", 50)
    vendors += Vendor("Expensive Booth", "Food", 500)
    assert len(vendors.filter(price_min=100, price_max=300)) == 1

def test_filter_by_capacity():
    vendors = Vendor("Small Stage", "Music", 100)
    vendors += Vendor("Big Stage", "Music", 500)
    assert len(vendors.filter(min_capacity=200)) == 1
    assert len(vendors.filter(min_capacity=50)) == 2

def test_filter_by_status():
    vendors = Vendor("Confirmed", "Food", 100, status="confirmed")
    vendors += Vendor("Pending", "Food", 100, status="pending")
    assert len(vendors.filter(status="confirmed")) == 1

def test_filter_multiple_categories():
    vendors = Vendor("Food Truck", "Food", 100)
    vendors += Vendor("Live Band", "Music", 300)
    vendors += Vendor("Art Booth", "Art", 150)
    assert len(vendors.filter(categories=["Art", "Food"])) == 2

def test_search_matches_multiple_vendors():
    vendors = Vendor("Food Truck A", "Food", 100)
    vendors += Vendor("Food Stand B", "Food", 120)
    assert len(vendors.search("food")) == 2
