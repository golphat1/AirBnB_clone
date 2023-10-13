#!/usr/bin/python3


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