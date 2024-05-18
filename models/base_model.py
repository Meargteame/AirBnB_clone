#!/usr/bin/python3

import uuid 
from datetime import datetime 


class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        self.creatd_at = datetime.now()
        self.updated_at =datetime.now()

    def __str__(self):
        class_name =self.__class__.__name__
        return f"[{class_name}] ({self.id}) ({self.__dict__})"
    
    def save(self):
        self.updated_at = datetime.now()


    def to_dict(self):
        to_json =self.__dict__
        to_json['__class__'] = self.__class__.__name__
        to_json['creatd_at'] =to_json['creatd_at'].isoformat()
        to_json['updated_at'] =to_json['updated_at'].isoformat()
        return to_json

