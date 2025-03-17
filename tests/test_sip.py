import unittest
import sys
import os

# Add src/ to the system path so Python can find sip_calculator.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sip_calculator import calculate_sip  # Import directly from sip_calculator.py

class TestSIPCalculator(unittest.TestCase):
    def test_sip_calculation(self):
        self.assertAlmostEqual(calculate_sip(1000, 12, 1), 12682.4, places=1)

if __name__ == "__main__":
    unittest.main()
