#!/usr/bin/env python3
import uuid 
from datetime import datetime 
class BaseModel:
    def __init__(self,**kwargs):
        if not id: 
            self.id = uuid.uuid4().hex
            self.created_at =str(datetime.now().isoformat())
            self.updated_at =self.created_at
        
        else:
            self.id = id 
            self.created_at =str(datetime.now().isoformat())
            self.updated_at =self.created_at
            
            
        for key, value in kwargs.items():
            self.__dict__[key] = value
        
    def __str__(self):
        return f"{self.id},{self.created_at},{self.updated_at}"
    def save(self):
        self.updated_at =str(datetime.now().isoformat())
    def to_dict(self):
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__ 
        return dict_rep

# serialization 
# changing one object to another one representation of something
# object -> dictionary ->  dump in to json file 


# if '__name__' == '__main__':
#     person_dict = {'name':'Meareg','field':'Software Engineer'}
#     base_1 = BaseModel(**person_dict)
#     base_2 = BaseModel('423423423423')
#     base_3 = BaseModel(name='Abebe',field='SE')


