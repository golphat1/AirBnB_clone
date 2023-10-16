#!/usr/bin/python3
# place.py

from models.base_model import BaseModel


class Place(BaseModel):
    """Empty place

    Attributes:
        city_id(_str_): _The city id_
        user_id (_str_): _The usr id_
        name (_str_): _The name of place_
        description (_str_): _The description of the place_
        number_rooms (_int_): _The number of rooms_
        number_bathrooms (_int_): _The number of bathrooms_
        max_guest (_int_): _The maximum number of guests_
        price_by_night (_int_): _The price by night_
        latitude (f): _The latitude of place_
        longitude (_f_): _The longitude of place_
        amenity_ids (_str_): __The list of Amenity.id
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
