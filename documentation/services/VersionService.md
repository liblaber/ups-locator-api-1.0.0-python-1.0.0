# VersionService

A list of all methods in the `VersionService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [locator](#locator) | The Locator API allows you to find UPS locations - such as drop-off points, retail locations, and UPS access points (third-party retail locations that offer UPS package drop-off, or delivery services). The API provides capabilities to search by location, services offered, program types, and related criteria. You can also retrieve hours of operation, location details, and additional UPS services offered at specific locations. |

## locator

The Locator API allows you to find UPS locations - such as drop-off points, retail locations, and UPS access points (third-party retail locations that offer UPS package drop-off, or delivery services). The API provides capabilities to search by location, services offered, program types, and related criteria. You can also retrieve hours of operation, location details, and additional UPS services offered at specific locations.

- HTTP Method: `POST`
- Endpoint: `/locations/{version}/search/availabilities/{reqOption}`

**Parameters**

| Name            | Type                                                        | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :-------------- | :---------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body    | [LocatorRequestWrapper](../models/LocatorRequestWrapper.md) | ✅       | The request body.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| version         | str                                                         | ✅       | Version of API Valid values: - v2                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| req_option      | str                                                         | ✅       | Indicates the type of request. Valid values: 1-Locations (Drop Locations and Will call locations) 8-All available Additional Services 16-All available Program Types 24-All available Additional Services and Program types 32-All available Retail Locations 40-All available Retail Locations and Additional Services 48-All available Retail Locations and Program Types 56-All available Retail Locations, Additional Services and Program Types 64-Search for UPS Access Point Locations. |
| locale          | str                                                         | ❌       | Locale of request                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| trans_id        | str                                                         | ❌       | An identifier unique to the request. Length 32                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| transaction_src | str                                                         | ❌       | An identifier of the client/source application that is making the request.Length 512                                                                                                                                                                                                                                                                                                                                                                                                           |

**Return Type**

`LocatorResponseWrapper`

**Example Usage Code Snippet**

```python
from ups_locator import UpsLocator, Environment
from ups_locator.models import LocatorRequestWrapper

sdk = UpsLocator(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

request_body = LocatorRequestWrapper(
    locator_request={
        "request": {
            "transaction_reference": {
                "customer_context": "CustomerContext"
            },
            "request_action": "qui veniamcom",
            "request_option": "ipsu"
        },
        "origin_address": {
            "geocode": {
                "latitude": "dolor laborum m",
                "longitude": "aute enim adnis"
            },
            "address_key_format": {
                "consignee_name": "proident dolor deserunt",
                "address_line": "velit",
                "address_line2": "volup",
                "address_line3": "est",
                "political_division3": "elit ut eiusmod consectetur",
                "political_division2": "irure ut sunt conse",
                "political_division1": "officia incididunt et ea ve",
                "postcode_primary_low": "cu",
                "postcode_extended_low": "e",
                "country_code": "vo",
                "single_line_address": "SingleLineAddress"
            },
            "maximum_list_size": "U"
        },
        "translate": {
            "locale": "nostr"
        },
        "unit_of_measurement": {
            "code": "Code"
        },
        "location_id": [
            "LocationID"
        ],
        "location_search_criteria": {
            "search_option": [
                {
                    "option_type": {
                        "code": "mo"
                    },
                    "option_code": [
                        {
                            "code": "paria"
                        }
                    ],
                    "relation": {
                        "code": "no"
                    }
                }
            ],
            "maximum_list_size": "cu",
            "search_radius": "do",
            "service_search": {
                "time": "aliq",
                "service_code": [
                    {
                        "code": "ex"
                    }
                ],
                "service_option_code": [
                    {
                        "code": "al"
                    }
                ]
            },
            "freight_will_call_search": {
                "freight_will_call_request_type": "c",
                "facility_address": [
                    {
                        "slic": "irure",
                        "address_line": [
                            "AddressLine"
                        ],
                        "city": "quis ex est",
                        "postal_code_primary_low": "est",
                        "postal_code_extended_low": "exercit",
                        "state": "ipsum esse veniam Lorem dolor",
                        "country_code": "ad"
                    }
                ],
                "origin_or_destination": "cu",
                "format_postal_code": "qu",
                "day_of_week_code": "u"
            },
            "access_point_search": {
                "public_access_point_id": "s",
                "access_point_status": "ex",
                "account_number": "ipsum L",
                "include_criteria": {
                    "merchant_account_number_list": {
                        "merchant_account_number": [
                            "ullamco"
                        ]
                    },
                    "search_filter": {
                        "dcr_indicator": "DCRIndicator",
                        "shipping_availability_indicator": "ShippingAvailabilityIndicator",
                        "shipper_preparation_delay": "c",
                        "click_and_collect_sort_with_distance": "sin"
                    },
                    "service_offering_list": {
                        "service_offering": [
                            {
                                "code": "ips",
                                "description": "i"
                            }
                        ]
                    }
                },
                "exclude_from_result": {
                    "business_classification_code": [
                        "in "
                    ],
                    "business_name": "a",
                    "radius": "d",
                    "postal_code_list": {
                        "postal_code": [
                            {
                                "primary_postal_code": "Duis",
                                "secondary_postal_code": "d"
                            }
                        ]
                    }
                },
                "exact_match_indicator": "ExactMatchIndicator",
                "exist_indicator": "ExistIndicator"
            },
            "open_time_criteria": {
                "day_of_week_code": "a",
                "from_time": "ulla",
                "to_time": "in p"
            },
            "brexit_filter": "cupida"
        },
        "sort_criteria": {
            "sort_type": "cu"
        },
        "allow_all_confidence_levels": "AllowAllConfidenceLevels",
        "search_option_code": "de",
        "service_geo_unit": {
            "service_code": "sed",
            "geo_political_unit": "euc"
        },
        "freight_indicator": "FreightIndicator"
    }
)

result = sdk.version.locator(
    request_body=request_body,
    version="v2",
    req_option="labo",
    locale="en_US",
    trans_id="transId",
    transaction_src="testing"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
