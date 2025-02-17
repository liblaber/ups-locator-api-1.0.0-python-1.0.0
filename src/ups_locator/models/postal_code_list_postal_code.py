# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "primary_postal_code": "PrimaryPostalCode",
        "secondary_postal_code": "SecondaryPostalCode",
    }
)
class PostalCodeListPostalCode(BaseModel):
    """Container to hold the postal code .

    :param primary_postal_code: Primary postal code.
    :type primary_postal_code: str
    :param secondary_postal_code: Secondary postal code., defaults to None
    :type secondary_postal_code: str, optional
    """

    def __init__(self, primary_postal_code: str, secondary_postal_code: str = None):
        self.primary_postal_code = primary_postal_code
        if secondary_postal_code is not None:
            self.secondary_postal_code = secondary_postal_code
