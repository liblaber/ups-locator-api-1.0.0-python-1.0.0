# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .location_search_criteria_search_option import LocationSearchCriteriaSearchOption
from .location_search_criteria_service_search import LocationSearchCriteriaServiceSearch
from .location_search_criteria_freight_will_call_search import (
    LocationSearchCriteriaFreightWillCallSearch,
)
from .location_search_criteria_access_point_search import (
    LocationSearchCriteriaAccessPointSearch,
)
from .location_search_criteria_open_time_criteria import (
    LocationSearchCriteriaOpenTimeCriteria,
)


@JsonMap(
    {
        "search_option": "SearchOption",
        "maximum_list_size": "MaximumListSize",
        "search_radius": "SearchRadius",
        "service_search": "ServiceSearch",
        "freight_will_call_search": "FreightWillCallSearch",
        "access_point_search": "AccessPointSearch",
        "open_time_criteria": "OpenTimeCriteria",
        "brexit_filter": "BrexitFilter",
    }
)
class LocatorRequestLocationSearchCriteria(BaseModel):
    """The Location search criteria container allows the user to further define the basis to which they wish to receive the UPS locations.
    Only relevant when the user requests a Location search (request option 1).

    :param search_option: search_option, defaults to None
    :type search_option: List[LocationSearchCriteriaSearchOption], optional
    :param maximum_list_size: If present, indicates the maximum number of locations the client wishes to receive in response; ranges from 1 to 50 with a default value of 5., defaults to None
    :type maximum_list_size: str, optional
    :param search_radius: Defines the maximum radius the user wishes to search for a UPS location. If the user does not specify, the default value is 100 miles. Whole numbers only.  Valid values are: 5-100 for UnitOfMeasure MI 5-150 for UnitOfMesaure KM, defaults to None
    :type search_radius: str, optional
    :param service_search: Allows for users to further define the search criteria. Refer to the rules specified in Service Search section., defaults to None
    :type service_search: LocationSearchCriteriaServiceSearch, optional
    :param freight_will_call_search: Freight Will Call Search Container. Required if SearchOption is '05-Freight Will Call Search', defaults to None
    :type freight_will_call_search: LocationSearchCriteriaFreightWillCallSearch, optional
    :param access_point_search: Applicable for request option 64 only. This contains inclusion and exclusion criteria for address search. It also contains Account Number and Access Point Public ID search elements., defaults to None
    :type access_point_search: LocationSearchCriteriaAccessPointSearch, optional
    :param open_time_criteria: Container to hold open times of the Location., defaults to None
    :type open_time_criteria: LocationSearchCriteriaOpenTimeCriteria, optional
    :param brexit_filter: Brexit Filter. Applicable for country code GB; Pass the PostalCode for the address in the location search if Brexit functionality is desired. UAPs with postal code starts with BT returned when brexit filter starts with BT, else UAPs returned with non BT postal code. Applicable for UAP and Proximal building search., defaults to None
    :type brexit_filter: str, optional
    """

    def __init__(
        self,
        search_option: List[LocationSearchCriteriaSearchOption] = None,
        maximum_list_size: str = None,
        search_radius: str = None,
        service_search: LocationSearchCriteriaServiceSearch = None,
        freight_will_call_search: LocationSearchCriteriaFreightWillCallSearch = None,
        access_point_search: LocationSearchCriteriaAccessPointSearch = None,
        open_time_criteria: LocationSearchCriteriaOpenTimeCriteria = None,
        brexit_filter: str = None,
    ):
        if search_option is not None:
            self.search_option = self._define_list(
                search_option, LocationSearchCriteriaSearchOption
            )
        if maximum_list_size is not None:
            self.maximum_list_size = maximum_list_size
        if search_radius is not None:
            self.search_radius = search_radius
        if service_search is not None:
            self.service_search = self._define_object(
                service_search, LocationSearchCriteriaServiceSearch
            )
        if freight_will_call_search is not None:
            self.freight_will_call_search = self._define_object(
                freight_will_call_search, LocationSearchCriteriaFreightWillCallSearch
            )
        if access_point_search is not None:
            self.access_point_search = self._define_object(
                access_point_search, LocationSearchCriteriaAccessPointSearch
            )
        if open_time_criteria is not None:
            self.open_time_criteria = self._define_object(
                open_time_criteria, LocationSearchCriteriaOpenTimeCriteria
            )
        if brexit_filter is not None:
            self.brexit_filter = brexit_filter
