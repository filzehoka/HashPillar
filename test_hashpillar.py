# test_hashpillar.py
"""
Tests for HashPillar module.
"""

import unittest
from hashpillar import HashPillar

class TestHashPillar(unittest.TestCase):
    """Test cases for HashPillar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HashPillar()
        self.assertIsInstance(instance, HashPillar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HashPillar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
