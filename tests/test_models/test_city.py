#!/usr/bin/python3
"""
Unit tests for the city.py module.
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_init(self):
        """Test initialization of City."""
        city = City()
        self.assertTrue(isinstance(city, City))

    def test_city_attributes(self):
        """Test City class attributes."""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

if __name__ == '__main__':
    unittest.main()
