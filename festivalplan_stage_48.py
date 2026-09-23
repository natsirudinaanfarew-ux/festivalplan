# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: FestivalPlan
import unittest
from datetime import date

def parse_date(s):
    if isinstance(s, date):
        return s
    parts = s.split('-')
    return date(int(parts[0]), int(parts[1]), int(parts[2]))

def is_valid_date(s):
    try:
        parse_date(s)
        return True
    except (ValueError, TypeError):
        return False

class DateHelperTests(unittest.TestCase):
    def test_parse_known(self):
        self.assertEqual(parse_date('2025-07-04'), date(2025, 7, 4))
    def test_parse_date_obj(self):
        d = date(2025, 1, 15)
        self.assertEqual(parse_date(d), d)
    def test_invalid_string(self):
        self.assertFalse(is_valid_date('nope'))
    def test_invalid_none(self):
        self.assertFalse(is_valid_date(None))
    def test_invalid_format(self):
        self.assertFalse(is_valid_date('2025/07/04'))

if __name__ == '__main__':
    unittest.main()
