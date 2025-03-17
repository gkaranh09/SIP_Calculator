import unittest
import sys
import os

# Ensure the `src` directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculate_sip import calculate_sip

class TestSIPCalculator(unittest.TestCase):
    def test_sip_calculation(self):
        
        expected_value = 12065.2  # Corrected expected value
        self.assertAlmostEqual(calculate_sip(1000, 12, 1), expected_value, places=1)

if __name__ == "__main__":
    unittest.main()
