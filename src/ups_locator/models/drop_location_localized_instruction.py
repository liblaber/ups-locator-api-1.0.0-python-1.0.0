# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"locale": "Locale", "last50ft_instruction": "Last50ftInstruction"})
class DropLocationLocalizedInstruction(BaseModel):
    """DropLocationLocalizedInstruction

    :param locale: Locale
    :type locale: str
    :param last50ft_instruction: Holds the additional instructions. Text will be displayed in English or the locale given in the request. The max length of the additional instruction text is 750 characters.
    :type last50ft_instruction: str
    """

    def __init__(self, locale: str, last50ft_instruction: str):
        self.locale = locale
        self.last50ft_instruction = last50ft_instruction
