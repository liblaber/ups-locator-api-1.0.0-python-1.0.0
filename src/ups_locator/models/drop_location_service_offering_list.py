# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .service_offering_list_service_offering import ServiceOfferingListServiceOffering


@JsonMap({"service_offering": "ServiceOffering"})
class DropLocationServiceOfferingList(BaseModel):
    """Container to hold the list of service offerings at the end point.

    :param service_offering: Container for Service offering code. **NOTE:** For versions >= v2, this element will always be returned as an array. For requests using version = v1, this element will be returned as an array if there is more than one object and a single object if there is only 1.
    :type service_offering: List[ServiceOfferingListServiceOffering]
    """

    def __init__(self, service_offering: List[ServiceOfferingListServiceOffering]):
        self.service_offering = self._define_list(
            service_offering, ServiceOfferingListServiceOffering
        )
