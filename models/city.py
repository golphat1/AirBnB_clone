#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represent city

    Attributes:
        state_id (str): The state id of the city
        name (str): The name of the city
    """

    state_id = ""
    name = ""
