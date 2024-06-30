#!/usr/bin/python3
"""
Unit tests for the state.py module.
"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_init(self):
        """Test initialization of State."""
        state = State()
        self.assertTrue(isinstance(state, State))

    def test_state_attributes(self):
        """Test State class attributes."""
        state = State()
        self.assertTrue(hasattr(state, 'name'))

if __name__ == '__main__':
    unittest.main()
