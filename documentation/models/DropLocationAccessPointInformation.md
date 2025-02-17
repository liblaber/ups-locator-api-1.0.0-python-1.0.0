# DropLocationAccessPointInformation

Container for UPS Access Point specific parameters.

**Properties**

| Name                         | Type                                             | Required | Description                                                                                           |
| :--------------------------- | :----------------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------- |
| public_access_point_id       | str                                              | ❌       | The Public Access Point ID associated with UPS access point.                                          |
| image_url                    | str                                              | ❌       | Image URL associated with UPS access point.                                                           |
| business_classification_list | AccessPointInformationBusinessClassificationList | ❌       | Container to hold list for business classification.                                                   |
| access_point_status          | AccessPointInformationAccessPointStatus          | ❌       | Container for UPS AccessPoint status.                                                                 |
| facility_slic                | str                                              | ❌       | Holds the value of facility SLIC of Access Point Location. Not implemented currently. For future use. |
| private_network_list         | AccessPointInformationPrivateNetworkList         | ❌       | Container to hold the list of private networks.                                                       |
| availability                 | AccessPointInformationAvailability               | ❌       | Container to hold the status of shipping or DRC/DCO availability of a UPS Access Point.               |

<!-- This file was generated by liblab | https://liblab.com/ -->
