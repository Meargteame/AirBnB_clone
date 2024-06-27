#!/usr/bin/env python3
import json
from  models.base_model import BaseModel

class FileStorage:
    
    CLASSES = {'BaseModel': BaseModel}  # Map class names to their corresponding classes
    __file_path = 'data.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        help_obj = {}
        for key, value in self.__objects.items():
            help_obj[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(help_obj, file, indent=4)
            

    def reload(self):
        
            with open(self.__file_path, 'r') as file:
                loaded_data = json.load(file)

                for key, value in loaded_data.items():
                    class_name = value['__class__']

                    if class_name in self.CLASSES:
                        instance = self.CLASSES[class_name](**value)
                        self.__objects[key] = instance
                    

