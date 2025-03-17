# tests/test_sip.py
import unittest
import sys
import os

# Ensure the `src` directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculate_sip import calculate_sip  # Correct import path

class TestSIPCalculator(unittest.TestCase):
    def test_sip_calculation(self):
        """
        Test the SIP calculation with known inputs.
        """
        expected_value = 12809.33  # Update expected value if necessary
        self.assertAlmostEqual(calculate_sip(1000, 12, 12), expected_value, places=1)

if __name__ == "__main__":
    unittest.main()
