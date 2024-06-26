import json 

class FileStorage():
    __file_path = 'data.json'
    __objects= {}
    
    
    def all(self):
        return self.__objects 
    def new(self,obj):
        self.__objects['obj'] = self.__class____.__name__.self.id 
    def save(self):
        data = self.__objects
        with open('data.json', 'w') as file:
            json.dump(data, file.json, indent=4)
    def reload(self):
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)

