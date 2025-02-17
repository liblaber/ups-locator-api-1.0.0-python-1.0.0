# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"code": "Code", "description": "Description"})
class BusinessClassificationListBusinessClassification(BaseModel):
    """BusinessClassificationListBusinessClassification

    :param code: Business Classification code of UPS Access Point. Please refer to appendix D for a list of business classification.
    :type code: str
    :param description: Description of business classification.
    :type description: str
    """

    def __init__(self, code: str, description: str):
        self.code = code
        self.description = description
