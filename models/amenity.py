#!/usr/bin/python3
# Encoding: utf-8
"""This script defines Amenity Module, it inherits from the Base Model class.
It also contains the attributes to be assigned 
to different amenities the destinations would have."""

from models.base_model import BaseModel

class Amenity(BaseModel):
    
    """Defines Amenity class
    Attributes:
        name (str): The amenity name
    """
    
    name = ""
