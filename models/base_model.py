#!/usr/bin/python3
"""
Module: base_model.py
Defines the BaseModel class.
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class defines common attributes/methods for other classes.

    Attributes:
        id (str): Unique identifier generated using uuid.uuid4().
        created_at (datetime): Date and time of instance creation.
        updated_at (datetime): Date and time of instance update.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            kwargs (dict): Dictionary containing attributes and values to initialize the instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    
    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: Dictionary containing all keys/values of instance attributes.
                  Includes '__class__', 'created_at', and 'updated_at' formatted
                  as ISO 8601 strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
