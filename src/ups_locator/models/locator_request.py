# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .locator_request_request import LocatorRequestRequest
from .locator_request_origin_address import LocatorRequestOriginAddress
from .locator_request_translate import LocatorRequestTranslate
from .locator_request_unit_of_measurement import LocatorRequestUnitOfMeasurement
from .locator_request_location_search_criteria import (
    LocatorRequestLocationSearchCriteria,
)
from .locator_request_sort_criteria import LocatorRequestSortCriteria
from .locator_request_service_geo_unit import LocatorRequestServiceGeoUnit


@JsonMap(
    {
        "request": "Request",
        "origin_address": "OriginAddress",
        "translate": "Translate",
        "unit_of_measurement": "UnitOfMeasurement",
        "location_id": "LocationID",
        "location_search_criteria": "LocationSearchCriteria",
        "sort_criteria": "SortCriteria",
        "allow_all_confidence_levels": "AllowAllConfidenceLevels",
        "search_option_code": "SearchOptionCode",
        "service_geo_unit": "ServiceGeoUnit",
        "freight_indicator": "FreightIndicator",
    }
)
class LocatorRequest(BaseModel):
    """N/A

    :param request: N/A
    :type request: LocatorRequestRequest
    :param origin_address: Container for origin address information.
    :type origin_address: LocatorRequestOriginAddress
    :param translate: Contains the locale information for the request.
    :type translate: LocatorRequestTranslate
    :param unit_of_measurement: Distance unit of measurement. This is required for location requests (request option 1)., defaults to None
    :type unit_of_measurement: LocatorRequestUnitOfMeasurement, optional
    :param location_id: Location ID is the identification number of the UPS affiliated location., defaults to None
    :type location_id: List[str], optional
    :param location_search_criteria: The Location search criteria container allows the user to further define the basis to which they wish to receive the UPS locations.  Only relevant when the user requests a Location search (request option 1)., defaults to None
    :type location_search_criteria: LocatorRequestLocationSearchCriteria, optional
    :param sort_criteria: Container for Sort Criteria, defaults to None
    :type sort_criteria: LocatorRequestSortCriteria, optional
    :param allow_all_confidence_levels: Indicator to allow confidence level in search., defaults to None
    :type allow_all_confidence_levels: str, optional
    :param search_option_code: Valid values:  01-Proximity Search Details 02-Address Search Details 03-Proximity Search Summary 04-Address Search Summary 05-Freight Will Call Search.  Either OptionType 03 or 04 is required., defaults to None
    :type search_option_code: str, optional
    :param service_geo_unit: ServiceGeoUnit Container. Required to search for the freight facility information, defaults to None
    :type service_geo_unit: LocatorRequestServiceGeoUnit, optional
    :param freight_indicator: FreightIndicator. Required for Freight Location Search., defaults to None
    :type freight_indicator: str, optional
    """

    def __init__(
        self,
        request: LocatorRequestRequest,
        origin_address: LocatorRequestOriginAddress,
        translate: LocatorRequestTranslate,
        unit_of_measurement: LocatorRequestUnitOfMeasurement = None,
        location_id: List[str] = None,
        location_search_criteria: LocatorRequestLocationSearchCriteria = None,
        sort_criteria: LocatorRequestSortCriteria = None,
        allow_all_confidence_levels: str = None,
        search_option_code: str = None,
        service_geo_unit: LocatorRequestServiceGeoUnit = None,
        freight_indicator: str = None,
    ):
        self.request = self._define_object(request, LocatorRequestRequest)
        self.origin_address = self._define_object(
            origin_address, LocatorRequestOriginAddress
        )
        self.translate = self._define_object(translate, LocatorRequestTranslate)
        if unit_of_measurement is not None:
            self.unit_of_measurement = self._define_object(
                unit_of_measurement, LocatorRequestUnitOfMeasurement
            )
        if location_id is not None:
            self.location_id = location_id
        if location_search_criteria is not None:
            self.location_search_criteria = self._define_object(
                location_search_criteria, LocatorRequestLocationSearchCriteria
            )
        if sort_criteria is not None:
            self.sort_criteria = self._define_object(
                sort_criteria, LocatorRequestSortCriteria
            )
        if allow_all_confidence_levels is not None:
            self.allow_all_confidence_levels = allow_all_confidence_levels
        if search_option_code is not None:
            self.search_option_code = search_option_code
        if service_geo_unit is not None:
            self.service_geo_unit = self._define_object(
                service_geo_unit, LocatorRequestServiceGeoUnit
            )
        if freight_indicator is not None:
            self.freight_indicator = freight_indicator
