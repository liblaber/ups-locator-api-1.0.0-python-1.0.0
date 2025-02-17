# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .pick_up_pick_up_details import PickUpPickUpDetails


@JsonMap({"day_of_week": "DayOfWeek", "pick_up_details": "PickUpDetails"})
class TransportationPickUpSchedulePickUp(BaseModel):
    """TransportationPickUpSchedulePickUp

    :param day_of_week: Day of week. - 1 - Sunday - 2 - Monday - 3 - Tuesday - 4 - Wednesday - 5 - Thursday - 6 - Friday - 7 - Saturday.
    :type day_of_week: str
    :param pick_up_details: PickUpDetails container contains either pickup time or NoPickupIndicator. Either PickUpTime or NoPickupIndicator
    :type pick_up_details: PickUpPickUpDetails
    """

    def __init__(self, day_of_week: str, pick_up_details: PickUpPickUpDetails):
        self.day_of_week = day_of_week
        self.pick_up_details = self._define_object(pick_up_details, PickUpPickUpDetails)
