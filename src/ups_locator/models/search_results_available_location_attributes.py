# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .available_location_attributes_option_type import (
    AvailableLocationAttributesOptionType,
)
from .available_location_attributes_option_code import (
    AvailableLocationAttributesOptionCode,
)


@JsonMap({"option_type": "OptionType", "option_code": "OptionCode"})
class SearchResultsAvailableLocationAttributes(BaseModel):
    """SearchResultsAvailableLocationAttributes

    :param option_type: OptionType is a container that indicates the type of the location attribute that are available. For example if the Option Type is RetailLocation the list of all available retail locations will be returned in 1 or many corresponding OptionCodes.
    :type option_type: AvailableLocationAttributesOptionType
    :param option_code: Option code is a container that contains the information of a particular retail location type or additional service or program type that is available currently. One or more of this container will be returned to give all the available codes for Retail Type or Additional Services or Program Type.
    :type option_code: AvailableLocationAttributesOptionCode
    """

    def __init__(
        self,
        option_type: AvailableLocationAttributesOptionType,
        option_code: AvailableLocationAttributesOptionCode,
    ):
        self.option_type = self._define_object(
            option_type, AvailableLocationAttributesOptionType
        )
        self.option_code = self._define_object(
            option_code, AvailableLocationAttributesOptionCode
        )
