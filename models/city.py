#!/usr/bin/python3
# city.py
# defines a class city

from models.base_model import BaseModel


class City(BaseModel):
    """Empty city

    Attributes:
        state_id (_str_): _The state id_
        name (_str_): _The name of city_
    """

    state_id = ""
    name = ""
