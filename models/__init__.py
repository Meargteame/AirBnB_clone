"""
models package initialization module.
"""

from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for your application
storage = FileStorage()
storage.reload()
