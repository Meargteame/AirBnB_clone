#!/usr/bin/python3
"""
This module contains the State class which inherits from BaseModel.
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    State class that inherits from BaseModel.
    Attributes:
        name (str): The name of the state.
    """
    name = ""
