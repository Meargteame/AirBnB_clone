#!usr/bin/env python3 

"""

"""
import uuid
import datetime

class BaseModel:
    def __init__(self):
        """

        """ 
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at 
        
    def save(self):
        """
        
        """

        self.updated_at= datetime.datetime.now()

    
    def to_dict(self):
        """
        
        """

        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["create_at"] = self.created_at
        obj_dict["updated_at"] = self.updated_at 
        return obj_dict 

    def __str__(self):
        """
        
        """

        class_name = self.__class__.__name__

        return f"{class_name} {self.id} {self.__dict__}"
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

