#!/usr/bin/python3
# Encoding: utf-8
"""This script defines State Module
This Module inherits from BaseModel class.
Itt also contains the attributes to be assigned
to the States.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """Defines State Class
    Attributes:
        name (str): The State name
    """
    name = ""
