# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .additional_comments_comment_type import AdditionalCommentsCommentType


@JsonMap({"comment_type": "CommentType"})
class DropLocationAdditionalComments(BaseModel):
    """Container for Additional Comments about Location.Text will be displayed in the Locale requested.

    :param comment_type: Container for CommentType Code and Text. **NOTE:** For versions >= v2, this element will always be returned as an array. For requests using version = v1, this element will be returned as an array if there is more than one object and a single object if there is only 1.
    :type comment_type: List[AdditionalCommentsCommentType]
    """

    def __init__(self, comment_type: List[AdditionalCommentsCommentType]):
        self.comment_type = self._define_list(
            comment_type, AdditionalCommentsCommentType
        )
