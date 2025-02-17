# LocatorResponseResponse

Container for Response.

**Properties**

| Name                        | Type                         | Required | Description                                                                                                                                                    |
| :-------------------------- | :--------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| response_status_code        | str                          | ✅       | Identifies the success or failure of the interchange. 1-Success 0-Failure                                                                                      |
| transaction_reference       | ResponseTransactionReference | ❌       | Container for customer provided data and the XPCI Version.                                                                                                     |
| response_status_description | str                          | ❌       | Describes the Response Status Code.                                                                                                                            |
| error                       | ResponseError                | ❌       | If an error is encountered during the interchange, the Response contains an error. If the error is present, then the ErrorSeverity and ErrorCode are required. |

<!-- This file was generated by liblab | https://liblab.com/ -->
