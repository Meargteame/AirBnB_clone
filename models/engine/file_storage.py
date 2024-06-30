#!/usr/bin/env python3
"""
FileStorage module for managing the storage of BaseModel instances in JSON format.
"""

from models.base_model import BaseModel
from models.user import User  # Import User class
from models.place import Place  # Import Place class
from models.state import State  # Import State class
from models.city import City  # Import City class
from models.amenity import Amenity  # Import Amenity class
from models.review import Review  # Import Review class
import json

class FileStorage:
    """
    FileStorage class that serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        CLASSES (dict): A dictionary mapping class names to class objects.
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store all objects by <class name>.id.
    """
    
    CLASSES = {
        'BaseModel': BaseModel, 
        'User': User,
        'Place': Place,  # Added Place class
        'State': State,  # Added State class
        'City': City,    # Added City class
        'Amenity': Amenity,  # Added Amenity class
        'Review': Review  # Added Review class
    }
    __file_path = 'data.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects or objects of a specific class.
        
        Args:
            cls (type, optional): The class to filter objects by. If None, returns all objects.

        Returns:
            dict: The dictionary containing all stored objects or objects of the specified class.
        """
        if cls is None:
            return self.__objects
        cls_name = cls.__name__
        return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (BaseModel): The object to store.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        help_obj = {}
        for key, value in self.__objects.items():
            help_obj[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(help_obj, file, indent=4)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists).
        """
        try:
            with open(self.__file_path, 'r') as file:
                loaded_data = json.load(file)
                for key, value in loaded_data.items():
                    class_name = value['__class__']
                    if class_name in self.CLASSES:
                        instance = self.CLASSES[class_name](**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            pass

# Create an instance of FileStorage
storage = FileStorage()
storage.reload()
