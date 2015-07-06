#!/usr/bin/env python

from __future__ import division, absolute_import, print_function
from future.builtins import super

from iris_sdk.models.available_numbers import AvailableNumbers
from iris_sdk.models.base_resource import BaseResource
from iris_sdk.models.in_service_numbers import InServiceNumbers
from iris_sdk.models.sites import Sites

from iris_sdk.models.data.account import AccountData

#from iris_sdk.models.resource.orders import Orders

XPATH_ACCOUNT = "/accounts/{}"

class Account(BaseResource, AccountData):

    """Iris account"""

    _xpath = XPATH_ACCOUNT

    @property
    def available_numbers(self):
        return self._available_numbers

    @property
    def in_service_numbers(self):
        return self._in_service_numbers

    @property
    def sites(self):
        return self._sites

    def __init__(self, parent=None, client=None):
        if (client is not None):
            self.id = client.config.account_id
            self.account_id = self.id
        super().__init__(parent, client)
        AccountData.__init__(self)
        self._available_numbers = AvailableNumbers(self, client)
        self._in_service_numbers = InServiceNumbers(self, client)
        self._sites = Sites(self, client)

    def get(self):
        return self.get_data(self.id)