#!/usr/bin/python3

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Repreents place class

    Attributes:
        city_id (str): The city ID.
        user_ide (str): The user ID.
        name (str): The name of place.
        description (str): The description of place.
        number_rooms (int): The number of rooms.
        number_bathrooms (int): The number of bathrooms
        max_guest (int): The maximum number of guests.
        price_by_night (int): The price by night.
        latitude (f): The latitude of place.
        longitude (f): The longitude of the place.
        amenity_ids (str): The list of amenity
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
