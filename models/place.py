#!/usr/bin/python3
"""
class Place that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        Summary: Definning the Place class that inherits from BaseModel
        Public class attributes:
            city_id string - empty string (it will be the City.id)
            user_id string - empty string (it will be the User.id)
            name: string - empty string
            description string - empty string
            number_rooms[int] - 0
            number_bathrooms[int] - 0
            max_guest[int] - 0
            price_by_night[int] - 0
            latitude[float] - 0.0
            longitude[float] - 0.0
            amenity_ids[list] - empty list (it will be the list of Amenity.id)
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
    amenity_ids = [""]
