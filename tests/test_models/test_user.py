#!/usr/bin/python3
"""
Unit tests for the user.py module.
"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_init(self):
        """Test initialization of User."""
        user = User()
        self.assertTrue(isinstance(user, User))

    def test_user_attributes(self):
        """Test User class attributes."""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

if __name__ == '__main__':
    unittest.main()
