#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents reveiew class
    Attributes:
        place_id (str): The place ID.
        user_id (str): The user ID.
        text (str): The text message.
    """

    place_id = ""
    user_id = ""
    text = ""
