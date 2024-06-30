#!/usr/bin/python3
"""
Unit tests for the console.py module.
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class."""

    def setUp(self):
        """Reset the console before each test."""
        self.console = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        """Test the 'help' command."""
        self.console.onecmd('help')
        output = mock_stdout.getvalue()
        self.assertIn('Documented commands', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Test the 'create' command."""
        self.console.onecmd('create User')
        output = mock_stdout.getvalue()
        self.assertTrue(output.strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Test the 'show' command."""
        self.console.onecmd('show User some_id')
        output = mock_stdout.getvalue()
        self.assertIn('** no instance found **', output)

    def test_do_quit(self):
        """Test the 'quit' command."""
        self.assertTrue(self.console.do_quit(None))

    def test_do_EOF(self):
        """Test the 'EOF' command."""
        self.assertTrue(self.console.do_EOF(None))

    # Add more tests for other commands like `destroy`, `all`, `update`, etc.

if __name__ == '__main__':
    unittest.main()
