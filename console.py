#!/usr/bin/python3
"""Defines the HBnB Console."""

import cmd
import re
from shlex import split
form models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

