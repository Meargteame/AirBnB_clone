from uuid import uuid4 
from datetime import datetime 

class BaseModel:
           # the instance attributes and methods are in the below methods the so called the init method
            
           def __init__(self):
               self.id =str(uuid4())
               self.created_at = str(datetime.now())
               self.updated_at = str(self.created_at)
           def __str__(self):
           #__str__: should print: [<class name>] (<self.id>) <self.__dict__>
                return f"{self.__class__.__name__} {self.id} {self.__dict__}"
           def save(self):
                 self.updated_at = datetime.now()
    
           def to_dict(self):
           # the first step of the serilizaation process chaning the object to dictionary representation
           
                obj_dict = self.__dict__
                obj_dict[__class__ ] = self.__class__.__name__
                self.created_at = self.created_at.isofromat()
                self.created_at = self.updated_at.isoformat()
                
                return obj_dict
            
    
my_model = BaseModel()
print(my_model)
