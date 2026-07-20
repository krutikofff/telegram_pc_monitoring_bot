from services.analytics import forecast_disk_full
import unittest

class TestAnalytics(unittest.TestCase):

    def test_forecast_disk_full_decreasing(self):
        snapshots = [
            ("2026-01-01T00:00:00", 100.0),
            ("2026-01-02T00:00:00", 90.0),
        ]
        result = forecast_disk_full(snapshots)
        self.assertIsNotNone(result)
        self.assertGreater(result, 0)

    def test_forecast_disk_full_stable(self):
        snapshots = [
            ("2026-01-01T00:00:00", 100.0),
            ("2026-01-02T00:00:00", 100.0),
        ]
        result = forecast_disk_full(snapshots)
        self.assertIsNone(result)

    def test_forecast_disk_full_not_enough_data(self):
        result = forecast_disk_full([("2026-01-01T00:00:00", 100.0)])
        self.assertIsNone(result)