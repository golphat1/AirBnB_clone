#!/usr/bin/python3
# review.py

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents Revie

    Attributes:
        place_ide (str): The place id
        user_id (str): The user id
        text (str): The text
    """

    place_id = ""
    user_id = ""
    text = ""
