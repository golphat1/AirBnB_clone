#!/usr/bin/python3
# user.py

from models.base_model import BaseModel
"""defines a class user"""


class User(BaseModel):
    """Empty user

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first_name of the user.
        last_name (str): The last_name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
