#!/usr/bin/ env python3 

from uuid import uuid4
from datetime import datetime
class BaseModel:
    """
    Base model class that defines common attributes/methods for other classes.

    Attributes:
        id (str): Unique identifier for the instance.
        created_at (str): Timestamp when the instance was created.
        updated_at (str): Timestamp when the instance was last updated.
    """

    def __init__(self):
        """
        Initialize a new instance of BaseModel.
        """
        self.id = str(uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = self.created_at

    def __str__(self):
        """
        Return a string representation of the instance.
        
        Returns:
            str: String representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """
        self.updated_at = str(datetime.now())

    def to_dict(self):
        """
        Convert the instance attributes to a dictionary representation.
        
        Returns:
            dict: Dictionary containing the instance attributes and class name.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at
        obj_dict['updated_at'] = self.updated_at
        return obj_dict
