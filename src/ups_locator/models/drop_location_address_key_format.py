# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "consignee_name": "ConsigneeName",
        "address_line": "AddressLine",
        "political_division3": "PoliticalDivision3",
        "political_division2": "PoliticalDivision2",
        "political_division1": "PoliticalDivision1",
        "postcode_primary_low": "PostcodePrimaryLow",
        "postcode_extended_low": "PostcodeExtendedLow",
        "country_code": "CountryCode",
    }
)
class DropLocationAddressKeyFormat(BaseModel):
    """Contains all of the basic information about a location, Consignee Name, Building Name, Address Lines, City, State/Province, Postal Code and Country or Terriotry Code.

    :param consignee_name: Name. (Also includes the building name)Return if available., defaults to None
    :type consignee_name: str, optional
    :param address_line: Address Line Information of the UPS location The address level or Intersection information. Only two address lines will be returned. The second line may contain such information as the building name, the suite, and room.
    :type address_line: str
    :param political_division3: Subdivision within a City. e.g., a Barrio., defaults to None
    :type political_division3: str, optional
    :param political_division2: City.
    :type political_division2: str
    :param political_division1: State/Province.
    :type political_division1: str
    :param postcode_primary_low: Postal Code.
    :type postcode_primary_low: str
    :param postcode_extended_low: 4 Digit postal code extension. Valid for US only., defaults to None
    :type postcode_extended_low: str, optional
    :param country_code: A country or territory code. Valid values to be returned are: US-United States (meaning US 50).
    :type country_code: str
    """

    def __init__(
        self,
        address_line: str,
        political_division2: str,
        political_division1: str,
        postcode_primary_low: str,
        country_code: str,
        consignee_name: str = None,
        political_division3: str = None,
        postcode_extended_low: str = None,
    ):
        if consignee_name is not None:
            self.consignee_name = consignee_name
        self.address_line = address_line
        if political_division3 is not None:
            self.political_division3 = political_division3
        self.political_division2 = political_division2
        self.political_division1 = political_division1
        self.postcode_primary_low = postcode_primary_low
        if postcode_extended_low is not None:
            self.postcode_extended_low = postcode_extended_low
        self.country_code = country_code
