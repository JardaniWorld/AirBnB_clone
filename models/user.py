#!/usr/bin/python3
<<<<<<< MAIN
=======
# Encoding: utf-8
"""This script defines User Module
This Module inherits from BaseModel class.
It also contains the user information.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines User Class
    Attributes:
        email (str): The User email
        password (str): The User password
        first_name (str): The first name of the User
        last_name (str): The last name of the User
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
>>>>>>> features/console
