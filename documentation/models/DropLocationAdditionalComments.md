# DropLocationAdditionalComments

Container for Additional Comments about Location.Text will be displayed in the Locale requested.

**Properties**

| Name         | Type                                | Required | Description                                                                                                                                                                                                                                                                  |
| :----------- | :---------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| comment_type | List[AdditionalCommentsCommentType] | ✅       | Container for CommentType Code and Text. **NOTE:** For versions >= v2, this element will always be returned as an array. For requests using version = v1, this element will be returned as an array if there is more than one object and a single object if there is only 1. |

<!-- This file was generated by liblab | https://liblab.com/ -->
