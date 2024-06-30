#!/usr/bin/python3
"""
Unit tests for the base_model.py module.
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_init(self):
        """Test initialization of BaseModel."""
        obj = BaseModel()
        self.assertTrue(isinstance(obj, BaseModel))

    def test_save(self):
        """Test the save method."""
        obj = BaseModel()
        obj.save()
        self.assertTrue(obj.updated_at > obj.created_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
