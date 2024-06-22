import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class for creating and managing instances.
    """
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, **kwargs):
        """Initialize a new instance of BaseModel.
            - **kwargs: a dictionary of key-values arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, self.TIME_FORMAT)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Return a string representation of the instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute and save the instance."""
        print("just inside basemodel save")
        import models
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save_obj()


    def to_dict(self) -> dict:
        """Return a dictionary of instance attributes."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        for k, v in obj_dict.items():
            if isinstance(v, datetime):
                obj_dict[k] = v.isoformat()

        return obj_dict
