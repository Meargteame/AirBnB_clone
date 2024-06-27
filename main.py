#!/usr/bin/env python3
"""
Main module for initializing and using FileStorage and BaseModel.
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

def main():
    """
    Main function to demonstrate the use of FileStorage and BaseModel.
    """
    model = BaseModel()
    storage = FileStorage()
    storage.new(model)
    storage.save()
    storage.reload()
    print("File storage initialized and data reloaded.")

if __name__ == "__main__":
    main()
