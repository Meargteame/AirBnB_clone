#!/usr/bin/python3
"""
Unit tests for the place.py module.
"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_init(self):
        """Test initialization of Place."""
        place = Place()
        self.assertTrue(isinstance(place, Place))

    def test_place_attributes(self):
        """Test Place class attributes."""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))

if __name__ == '__main__':
    unittest.main()
