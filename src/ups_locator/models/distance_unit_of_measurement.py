# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"code": "Code", "description": "Description"})
class DistanceUnitOfMeasurement(BaseModel):
    """The unit of measurement the user will see for the distance is based on the user input provided in the search request.

    :param code: The distance unit of measurement code. The unit of measurement used in the search request is returned.  Valid values: MI-Miles or KM-Kilometers
    :type code: str
    :param description: May return the description of the unit of measure specified in the request., defaults to None
    :type description: str, optional
    """

    def __init__(self, code: str, description: str = None):
        self.code = code
        if description is not None:
            self.description = description
