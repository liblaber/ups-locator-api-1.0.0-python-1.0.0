# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"code": "Code", "description": "Description"})
class DcrAvailabilityUnavailableReason(BaseModel):
    """Container to hold shipping unavailable reason.

    :param code: Code for DCR/DCO unavailability. Valid values:  01-Temporarily Unavailable  02-Location Full 03-Unavailable 04-Weather
    :type code: str
    :param description: Description for DCR/ DCO unavailability.
    :type description: str
    """

    def __init__(self, code: str, description: str):
        self.code = code
        self.description = description
