#!/usr/bin/env python3
import uuid 
from datetime import datetime 
class BaseModel:
    def __init__(self,name='unknown',field=None,id=None,**kwargs):
        if not id: 
            self.id = uuid.uuid4().hex
            self.name = name 
            self.field= field
        else:
            self.id = id 
            self.created_at =str(datetime.now().isoformat())
            self.updated_at =self.created_at
            
            
        for key, value in kwargs.items():
            self.__dict__[key] = value
        
    def __str__(self):
        return f"The Id of this object is {self.id},{self.name} {self.field}"
    def save(self):
        self.updated_at =str(datetime.now().isoformat())
    def to_dict(self):
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__ 
        dict_rep['relationship'] = True
        dict_rep['Marital Status'] = 'Married'
        return dict_rep

# serialization 
# changing one object to another one representation of something
# object -> dictionary ->  dump in to json file 
base_1 = BaseModel('Meareg Teame','software Engineer',4343433434)
print(base_1.to_dict())

if '__name__' == '__main__':
    person_dict = {'name':'Meareg','field':'Software Engineer'}
    base_1 = BaseModel(**person_dict)
    base_2 = BaseModel('423423423423')
    base_3 = BaseModel(name='Abebe',field='SE')


