# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"code": "Code", "description": "Description"})
class LocationAttributeOptionType(BaseModel):
    """LocationAttributeOptionType

    :param code: Code for Option type. Valid values: - 01 - Location - 02 - Retail Location - 03 - Additional Services - 04 - Program Type
    :type code: str
    :param description: Description for Option type such as Location, RetailLocation, AdditionalServices and ProgramType.
    :type description: str
    """

    def __init__(self, code: str, description: str):
        self.code = code
        self.description = description
