import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

def test_file_storage():
    # Create an instance of FileStorage
    storage = FileStorage()

    # Create a few BaseModel instances
    obj1 = BaseModel()
    obj1.name = "Object 1"
    obj1.save()

    obj2 = BaseModel()
    obj2.name = "Object 2"
    obj2.save()

    # Add objects to FileStorage
    storage.new(obj1)
    storage.new(obj2)

    # Save objects to JSON file
    storage.save()

    # Clear objects from memory to simulate reload
    storage.__objects = {}

    # Reload objects from JSON file
    storage.reload()

    # Retrieve reloaded objects
    reloaded_objects = storage.all()

    # Print reloaded objects for verification
    print("-- Reloaded objects --")
    for obj_id, obj in reloaded_objects.items():
        print(obj)

    # Verify the objects were reloaded correctly
    assert len(reloaded_objects) == 2
    assert reloaded_objects[f"BaseModel.{obj1.id}"].name == obj1.name
    assert reloaded_objects[f"BaseModel.{obj2.id}"].name == obj2.name

    print("Tests passed successfully!")

if __name__ == "__main__":
    test_file_storage()
