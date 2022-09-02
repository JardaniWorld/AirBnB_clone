#!/usr/bin/python3
# Encoding: utf-8
"""This defines the Base Model Module

This module establishes a reference `base_model`
from which other classes of the Airbnb clone project
inherit from. With this, it is possible to extract information
such as: A Universal Unique Identifier (UUID), the date and
time in which a class was created and updated, a standard format
to print the class content, a way to save the data created from
the instances and finally the representation of all the keys
and values of an instance.

"""

from datetime import datetime
import models
import uuid


class BaseModel:
    """Defines the Base Model Class

    This is the Base Model that take care of the
    initialization, serialization and deserialization
    of the future instances.

    Attributes:
        id (str): This is a UUID for a created instance
        created_at (datetime): The current date and time an
            instance is created.
        updated_at (datetime): The current date and time that
            an instance is created and will be updated every
            time the object changes.

    """

    def __init__(self, *args, **kwargs):
        """Base Model __init__ Method

        Here, the default values of a Base Model
        instance are initialized.

        """
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                if arg != '__class__':
                    setattr(self, arg, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Representation of the class for the User

        Example:
            $ bm = BaseModel()
            $ print(bm)

            This method prints the content of the Base Model
            class with this format
            
            $ [<class name>] (<self.id>) <self.__dict__>

        """
        return '[{0}] ({1}) {2}'.format(
                self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """This method updates a Base Model instance

        Updates the public instance attribute `update_at`
        with the current datetime and dumps the class data
        into a file

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """This method converts the class data into
        human-readable format.

        Returns a new dictionary containing all keys/values
        of __dict__ of the instance.
        """
        class_info = self.__dict__.copy()
        class_info['__class__'] = self.__class__.__name__
        class_info['created_at'] = self.created_at.isoformat()
        class_info['updated_at'] = self.updated_at.isoformat()

        return class_info
