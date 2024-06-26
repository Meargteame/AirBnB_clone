#!/usr/bin/env python3
"""
BaseModel module for defining a common base class for other models.
"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Base model class that defines common attributes/methods for other classes.

    Attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): Timestamp when the instance was created.
        updated_at (datetime): Timestamp when the instance was last updated.
    """

    def __init__(self, **kwargs):
        """
        Initialize a new instance of BaseModel.

        Args:
            **kwargs: Key-value pairs of attributes to set on the instance. If empty, a new instance
                      with a unique ID and current timestamps for creation and update is created.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at'] and isinstance(value, str):
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from models import storage
            storage.new(self)

    def __str__(self):
        """
        Return a string representation of the instance.

        Returns:
            str: String representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the updated_at attribute with the current datetime and save the instance to storage.
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """
        Convert the instance attributes to a dictionary representation.

        Returns:
            dict: Dictionary containing the instance attributes and class name.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
