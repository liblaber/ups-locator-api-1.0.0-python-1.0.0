# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"code": "Code", "description": "Description"})
class AvailableLocationAttributesOptionType(BaseModel):
    """OptionType is a container that indicates the type of the location attribute that are available. For example if the Option Type is RetailLocation the list of all available retail locations will be returned in 1 or many corresponding OptionCodes.

    :param code: Code for Option type.
    :type code: str
    :param description: Description for Option type such as RetailLocation, AdditionalServices and ProgramType.
    :type description: str
    """

    def __init__(self, code: str, description: str):
        self.code = code
        self.description = description
