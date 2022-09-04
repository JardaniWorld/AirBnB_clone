#!/usr/bin/python3
# Encoding: utf-8
"""This script defines the City Module, it inherits from the Base Model class.
It also contains the attributes to be assigned to the cities.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """Defines the City Class

    Attributes:
        state_id (str): The UUID of the state, the city belongs to
        name (str): The City name
    """
    
    state_id = ""
    name = ""
