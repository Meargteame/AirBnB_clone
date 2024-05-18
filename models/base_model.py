#!/usr/bin/python3
"""This is the BaseModel"""
# importing the modules needed
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """
        __init__ constructor method of the class
        """
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
                    continue
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """__str__ method that returns string representation of the instance
        Returns:
        [str]: instance of BaseModel string representation"""
        class_name = self.__class__.__name__
        return "[{:s}] ({:s}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        save method that saves instance information in JSON file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to_dict method that return dictionary representation of the instance

        Returns:
            [dict]: dictionary with information about the BaseModel instance
        """
        inst_dict = dict((self.__dict__).copy())
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict
