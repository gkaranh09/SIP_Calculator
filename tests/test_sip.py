import unittest
import sys
import os

# Ensure `src` is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.calculate_sip import calculate_sip  # FIXED: Explicit src reference

class TestSIPCalculator(unittest.TestCase):
    def test_sip_calculation(self):
        expected_value = 12682.4  # Corrected expected value
        self.assertAlmostEqual(calculate_sip(1000, 1, 12), expected_value, places=1)

if __name__ == "__main__":
    unittest.main()
