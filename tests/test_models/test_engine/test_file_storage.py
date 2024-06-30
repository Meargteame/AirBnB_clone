#!/usr/bin/python3
"""
Unit tests for the file_storage.py module.
"""
import unittest
from models.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Reset the storage before each test."""
        self.storage = FileStorage()
        self.storage.reload()

    def test_all(self):
        """Test the all method."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test the new method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f'BaseModel.{obj.id}', self.storage.all())

    def test_save(self):
        """Test the save method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(len(self.storage.all()) > 0)

    def test_reload(self):
        """Test the reload method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        self.assertIn(f'BaseModel.{obj.id}', self.storage.all())

if __name__ == '__main__':
    unittest.main()
