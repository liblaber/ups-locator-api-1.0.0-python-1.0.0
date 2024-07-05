# This file was generated by liblab | https://liblab.com/

from .services.version import VersionService
from .services.deprecated_version import DeprecatedVersionService
from .net.environment import Environment


class UpsLocator:
    def __init__(
        self,
        username: str = None,
        password: str = None,
        base_url: str = Environment.DEFAULT.value,
    ):
        """
        Initializes UpsLocator the SDK class.
        """
        self.version = VersionService(base_url=base_url)
        self.deprecated_version = DeprecatedVersionService(base_url=base_url)
        self.set_basic_auth(username=username, password=password)

    def set_base_url(self, base_url):
        """
        Sets the base URL for the entire SDK.
        """
        self.version.set_base_url(base_url)
        self.deprecated_version.set_base_url(base_url)

        return self

    def set_basic_auth(self, username: str, password: str):
        """
        Sets the username and password for the entire SDK.
        """
        self.version.set_basic_auth(username=username, password=password)
        self.deprecated_version.set_basic_auth(username=username, password=password)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
