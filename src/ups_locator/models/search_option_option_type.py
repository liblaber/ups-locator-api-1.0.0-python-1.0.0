# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"code": "Code"})
class SearchOptionOptionType(BaseModel):
    """OptionType is a container that indicates the type of search for locations. There are 5 types of search. They are search by: Location, Retail Location, Additional Services, Program Type, and a Service Level Option.
    If search criteria by Location or Retail Location is not provided the default search of The UPS Store, UPS Center, UPS Drop Box, and Authorized Shipping Outlet location types will be performed.

    :param code: Code for Option type valid values are: - 01-Location - 02-Retail Location - 03-Additional Services - 04-Program Type - 05-Service Level Option. - 06-End Point Service Offering
    :type code: str
    """

    def __init__(self, code: str):
        self.code = code
