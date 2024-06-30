#!/usr/bin/python3
"""
This module contains the City class which inherits from BaseModel.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City class that inherits from BaseModel.
    Attributes:
        state_id (str): The id of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
