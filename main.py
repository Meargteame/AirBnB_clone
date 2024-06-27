#!/usr/bin/env python3
# main.py

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

def main():
    model = BaseModel()
    storage = FileStorage()
    storage.new(model)
    storage.reload()
    storage.save()
    print("File storage initialized and data reloaded.")

if __name__ == "__main__":
    main()
