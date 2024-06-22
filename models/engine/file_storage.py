import json 

from base_model import BaseModel
class FileStorage():
    def __init__(self):
        self.__fileName = 'JsonData.json'
        self.__objects = {}
    
    def save(self):
        data_to_write = {}
        
        # changing all data in to dict form when we want to save it in to json form and next we will change in to json 
        for key, values in self.__objects.items():
            data_to_write[key] = values.to_dict()
            
        with open('file.json','w') as file :
            json.dump(data_to_write,file)
    def new(self,data):
        key = f'{data.id} # {data.__class__.__name__}'
        self.__objects[key] =data 
        
    def reload():
        from  base_model import BaseModel
        
        pass 
    
    def load():
        pass 
    
    

model = BaseModel()
storage = FileStorage()
storage.save()
# storage.new()

print('Done')