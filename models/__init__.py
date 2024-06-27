'''
Update `models/__init__.py`: to create a unique `FileStorage` instance for your application

- import `file_storage.py`
- create the variable `storage`, an instance of `FileStorage`
- call `reload()` method on this variable
'''
import file_storage 

storage = file_storage.FileStorage()
storage.reload()