#!/usr/bin/python3
"""
This module contains the Review class which inherits from BaseModel.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    
    Attributes:
        place_id (str): The ID of the place being reviewed. (default: empty string)
        user_id (str): The ID of the user who wrote the review. (default: empty string)
        text (str): The text of the review. (default: empty string)
    """
    place_id = ""
    user_id = ""
    text = ""
