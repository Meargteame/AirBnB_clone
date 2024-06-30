#!/usr/bin/python3
"""
This module contains the Place class which inherits from BaseModel.
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place class that inherits from BaseModel.
    
    Attributes:
        city_id (str): The city's id where the place is located. (default: empty string)
        user_id (str): The user's id who owns the place. (default: empty string)
        name (str): The name of the place. (default: empty string)
        description (str): A brief description of the place. (default: empty string)
        number_rooms (int): The number of rooms in the place. (default: 0)
        number_bathrooms (int): The number of bathrooms in the place. (default: 0)
        max_guest (int): The maximum number of guests allowed at the place. (default: 0)
        price_by_night (int): The price for one night at the place. (default: 0)
        latitude (float): The latitude coordinate of the place. (default: 0.0)
        longitude (float): The longitude coordinate of the place. (default: 0.0)
        amenity_ids (list): List of Amenity ids associated with the place. (default: empty list)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
