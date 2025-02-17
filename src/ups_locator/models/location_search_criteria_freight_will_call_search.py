# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .freight_will_call_search_facility_address import (
    FreightWillCallSearchFacilityAddress,
)


@JsonMap(
    {
        "freight_will_call_request_type": "FreightWillCallRequestType",
        "facility_address": "FacilityAddress",
        "origin_or_destination": "OriginOrDestination",
        "format_postal_code": "FormatPostalCode",
        "day_of_week_code": "DayOfWeekCode",
    }
)
class LocationSearchCriteriaFreightWillCallSearch(BaseModel):
    """Freight Will Call Search Container. Required if SearchOption is '05-Freight Will Call Search'

    :param freight_will_call_request_type: Valid values are:  1 - Postal Code 2 - Delivery SLIC 3 - Delivery City/State. 1: Freight Will Call Search based on Postal Code, this search is valid for Postal code countries. 2: Freight Will Call Search based on SLIC. 3: Freight Will Call Search based on City and/or State. This Search is valid for non-postal code Countries
    :type freight_will_call_request_type: str
    :param facility_address: facility_address
    :type facility_address: List[FreightWillCallSearchFacilityAddress]
    :param origin_or_destination: OriginOrDestination is required for FreightWillCallRequestType 1 and type 3 . Valid values: 01-Origin facilities 02-Destination facilities.
    :type origin_or_destination: str
    :param format_postal_code: FormatPostalCode would be required in the request when FreightWillCallRequestType is 1. Valid values are: NFR-No format requested FR-format requested FS-format and search NVR-No validation requested.
    :type format_postal_code: str
    :param day_of_week_code: Day Of week Code. Valid Values are 1 to 7.  1-Sunday 2-Monday  3-Tuesday  4-Wednesday 5-Thursday 6-Friday 7-Saturday., defaults to None
    :type day_of_week_code: str, optional
    """

    def __init__(
        self,
        freight_will_call_request_type: str,
        facility_address: List[FreightWillCallSearchFacilityAddress],
        origin_or_destination: str,
        format_postal_code: str,
        day_of_week_code: str = None,
    ):
        self.freight_will_call_request_type = freight_will_call_request_type
        self.facility_address = self._define_list(
            facility_address, FreightWillCallSearchFacilityAddress
        )
        self.origin_or_destination = origin_or_destination
        self.format_postal_code = format_postal_code
        if day_of_week_code is not None:
            self.day_of_week_code = day_of_week_code
