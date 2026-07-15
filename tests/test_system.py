import unittest
from unittest.mock import patch, MagicMock
from services.system_info import (
    get_cpu_status,
    get_ram_status,
    get_disk_status
)
class TestSystemInfo(unittest.TestCase):

    @patch("services.system_info.psutil.cpu_percent")
    def test_cpu_status(self, mock_cpu):

        mock_cpu.return_value = 14.5

        result = get_cpu_status()

        self.assertEqual(result, "14.5%")
        mock_cpu.assert_called_once_with(interval=1)

    @patch("services.system_info.psutil.virtual_memory")
    def test_ram_status(self, mock_ram):

        mock_memory = MagicMock()
        mock_memory.percent = 25.0
        mock_memory.used = 4 * (1024 ** 3)
        mock_memory.total = 16 * (1024 ** 3)

        mock_ram.return_value = mock_memory

        result = get_ram_status()

        self.assertEqual(result, "25.0% (4.00 GB / 16.00 GB)")

    @patch("services.system_info.psutil.disk_usage")
    @patch("services.system_info.psutil.disk_partitions")
    def test_disk_status(self, mock_partitions, mock_usage):

        part_c = MagicMock()
        part_c.device = "C:\\\\"

        part_d = MagicMock()
        part_d.device = "D:\\\\"

        mock_partitions.return_value = [part_c,part_d]

        usage_c = MagicMock()
        usage_c.total = 100 * (1024 ** 3)
        usage_c.free = 50 * (1024 ** 3)
        usage_c.percent = 50.0

        usage_d = MagicMock()
        usage_d.total = 500 * (1024 ** 3)
        usage_d.free = 400 * (1024 ** 3)
        usage_d.percent = 20.0

        mock_usage.side_effect = [usage_c, usage_d]

        result = get_disk_status()

        # testing C
        self.assertEqual(result[0]["name"], "C:")
        self.assertEqual(result[0]["percent"], 50.0)
        self.assertEqual(result[0]["free"], 50.0)
        self.assertEqual(result[0]["total"], 100.0)

        #testing D
        self.assertEqual(result[1]["name"], "D:")
        self.assertEqual(result[1]["percent"], 20.0)
        self.assertEqual(result[1]["free"], 400.0)
        self.assertEqual(result[1]["total"], 500.0)

if __name__ == "__main__":
    unittest.main()