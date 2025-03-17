import unittest
import sys
import os

# Ensure `src` is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.calculate_sip import calculate_sip  # Ensure correct import

class TestSIPCalculator(unittest.TestCase):
    def test_sip_calculation(self):
        expected_value = 12809.33  # Updated expected value based on correct formula
        calculated_value = calculate_sip(1000, 1, 12)  # 1000 per month, 1 year, 12% annual rate
        self.assertAlmostEqual(calculated_value, expected_value, places=1)

if __name__ == "__main__":
    unittest.main()
