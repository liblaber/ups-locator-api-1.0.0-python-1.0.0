# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .location_attribute_option_type import LocationAttributeOptionType
from .location_attribute_option_code import LocationAttributeOptionCode


@JsonMap({"option_type": "OptionType", "option_code": "OptionCode"})
class DropLocationLocationAttribute(BaseModel):
    """LocationAttribute is a container that contains the information about the location's Location Type, Retail Location Type, Additional Services, or Program Type.

    :param option_type: option_type
    :type option_type: LocationAttributeOptionType
    :param option_code: Option code is a container that contains the information of a particular type of Location or retail location or additional service or program type that the drop location contains. If the OptionType is Location or Retail Location Type there will be one code since each location has only one location type or retail location type. If the Option type is additional services or program types there can be one or more option codes. **NOTE:** For versions >= v2, this element will always be returned as an array. For requests using version = v1, this element will be returned as an array if there is more than one object and a single object if there is only 1.
    :type option_code: List[LocationAttributeOptionCode]
    """

    def __init__(
        self,
        option_type: LocationAttributeOptionType,
        option_code: List[LocationAttributeOptionCode],
    ):
        self.option_type = self._define_object(option_type, LocationAttributeOptionType)
        self.option_code = self._define_list(option_code, LocationAttributeOptionCode)
