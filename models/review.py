#!/usr/bin/python3
"""
class Review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Summary: Definning the Review class that inherits from BaseModel
        Public class attributes:
            text string - empty string
            place_id - empty string (it will be the Place.id)
            user_id - empty string (it will be the User.id)
    """
    text = ""
    place_id = ""
    user_id = ""
