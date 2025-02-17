# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .request_transaction_reference import RequestTransactionReference


@JsonMap(
    {
        "transaction_reference": "TransactionReference",
        "request_action": "RequestAction",
        "request_option": "RequestOption",
    }
)
class LocatorRequestRequest(BaseModel):
    """N/A

    :param transaction_reference: TransactionReference identifies transactions between client and server., defaults to None
    :type transaction_reference: RequestTransactionReference, optional
    :param request_action: Indicates the action to be taken by the XML service.  The only valid value is 'Locator'.
    :type request_action: str
    :param request_option: Indicates the type of request. Valid values: 1-Locations (Drop Locations and Will call locations) 8-All available Additional Services 16-All available Program Types 24-All available Additional Services and Program types 32-All available Retail Locations 40-All available Retail Locations and Additional Services  48-All available Retail Locations and Program Types  56-All available Retail Locations, Additional Services and Program Types  64-Search for UPS Access Point Locations.
    :type request_option: str
    """

    def __init__(
        self,
        request_action: str,
        request_option: str,
        transaction_reference: RequestTransactionReference = None,
    ):
        if transaction_reference is not None:
            self.transaction_reference = self._define_object(
                transaction_reference, RequestTransactionReference
            )
        self.request_action = request_action
        self.request_option = request_option
