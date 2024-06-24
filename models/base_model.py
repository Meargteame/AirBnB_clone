#!/usr/bin/env python3
"""
BaseModel module for defining the base class for all models.
"""

import uuid
from datetime import datetime

class BaseModel:
    """Base class for all models."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance.
        
        Args:
            *args: Variable length argument list. Not used in this implementation.
            **kwargs: Arbitrary keyword arguments. Used for deserialization.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            # Convert created_at and updated_at strings to datetime objects
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Return a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance.
        
        Returns:
            dict: Dictionary representation of the instance.
        """
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr

    @classmethod
    def from_dict(cls, dict_obj):
        """Create an instance from a dictionary representation.
        
        Args:
            dict_obj (dict): Dictionary containing object attributes.
        
        Returns:
            instance: Instance of the class created from dictionary.
        """
        return cls(**dict_obj)

# Example usage
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel.from_dict(my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
