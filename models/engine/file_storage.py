import json 
print('file started')

class FileStorage():
    __file_path = 'data.json'
    __objects= {}
    
    
    # all(self): returns the dictionary __objects
    def all(self):
        return self.__objects 
    # new(self, obj): sets in __objects the obj with key <obj class name>.id
    def new(self,obj):
        self.__objects['obj'] = self.__class____.__name__.self.id 
    # save(self): serializes __objects to the JSON file (path: __file_path)
    def save(self):
        data = self.__objects
        with open('data.json', 'w') as file:
            json.dump(data, file.json, indent=4)
    # reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
    # otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
    def reload(self):
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)

print('file ended')
