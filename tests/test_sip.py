import unittest
import sys
import os

# Add src/ to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sip_calculator import calculate_sip  

class TestSIPCalculator(unittest.TestCase):
    def test_sip_calculation(self):
        expected_value = 12809.33  # Update this if needed
        self.assertAlmostEqual(calculate_sip(1000, 12, 1), expected_value, places=1)

if __name__ == "__main__":
    unittest.main()
