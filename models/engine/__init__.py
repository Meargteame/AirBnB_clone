print("before filestorage")
from models.engine.file_storage import FileStorage
print("Just after this,  the filestorage import")
storage = FileStorage()
storage.reload()


