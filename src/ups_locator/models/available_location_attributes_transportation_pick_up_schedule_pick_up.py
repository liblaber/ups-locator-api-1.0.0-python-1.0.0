# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .available_location_attributes_pick_up_pick_up_details import (
    AvailableLocationAttributesPickUpPickUpDetails,
)


@JsonMap({"day_of_week": "DayOfWeek", "pick_up_details": "PickUpDetails"})
class AvailableLocationAttributesTransportationPickUpSchedulePickUp(BaseModel):
    """AvailableLocationAttributesTransportationPickUpSchedulePickUp

    :param day_of_week: Day of the week for scheduled pickup. Valid values are: - 1 - Sunday - 2 - Monday - 3 - Tuesday - 4 - Wednesday - 5 - Thursday - 6 - Friday - 7 - Saturday.
    :type day_of_week: str
    :param pick_up_details: Container to hold information regarding pickup time and pickup availability indicator.
    :type pick_up_details: AvailableLocationAttributesPickUpPickUpDetails
    """

    def __init__(
        self,
        day_of_week: str,
        pick_up_details: AvailableLocationAttributesPickUpPickUpDetails,
    ):
        self.day_of_week = day_of_week
        self.pick_up_details = self._define_object(
            pick_up_details, AvailableLocationAttributesPickUpPickUpDetails
        )
