import unittest
from src import calculate_sip

class TestSIPCalculator(unittest.TestCase):
    def test_sip_calculation(self):
        self.assertAlmostEqual(calculate_sip(1000, 12, 1), 12682.4, places=1)

if __name__ == "__main__":
    unittest.main()
