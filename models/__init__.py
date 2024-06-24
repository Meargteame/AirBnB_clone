#!/usr/bin/env python3
"""
Initialization module for models package.
"""
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()

# Call reload() method to load existing data from file
storage.reload()
