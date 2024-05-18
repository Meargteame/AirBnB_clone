#!/usr/bin/python3

import uuid 
from datetime import datetime 


class BaseModel:
    """Base class for other models."""

    
    def __init__(self,*args, **kwargs):
        """Initialize instance attributes."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.now()
            self.updated_at =datetime.now()

    def __str__(self):
        """Return string representation of the instance."""

        class_name =self.__class__.__name__
        return f"[{class_name}] ({self.id}) ({self.__dict__})"
    
    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()


    def to_dict(self):
        """Return dictionary representation of the instance."""
        to_json =self.__dict__
        to_json['__class__'] = self.__class__.__name__
        to_json['created_at'] =self.created_at.isoformat()
        to_json['updated_at'] =self.updated_at.isoformat()

        return to_json

