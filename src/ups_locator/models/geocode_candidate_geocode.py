# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"latitude": "Latitude", "longitude": "Longitude"})
class GeocodeCandidateGeocode(BaseModel):
    """Geocode is the latitude and longitude of the origin candidate.

    :param latitude: The latitude of the origin address, center point of the exchange, center point of the postal code, or center point of the city.
    :type latitude: str
    :param longitude: The longitude of the origin address, center point of the exchange, center point of the postal code, or center point of the city.
    :type longitude: str
    """

    def __init__(self, latitude: str, longitude: str):
        self.latitude = latitude
        self.longitude = longitude
