#!/usr/bin/python3
"""
This module contains the Place class which inherits from BaseModel.
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place class that inherits from BaseModel.
    Attributes:
        city_id (str): The id of the city where the place is located.
        user_id (str): The id of the user who owns the place.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests allowed at the place.
        price_by_night (int): The price per night to stay at the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of Amenity.id for the amenities available in the place.
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
