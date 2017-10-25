#!/usr/bin/env python

from .resource import Resource
from .physical_info_transaction import PhysicalInfoTransaction


class PhysicalInfo(Resource):
    """This resource allows partners to access their users' physical information.

    https://www.polar.com/accesslink-api/?http#physical-info
    """

    def create_transaction(self, user_id, access_token):
        """Initiate physical info transaction

        Check for new physical info and create a new transaction if data is available.

        :param user_id: id of the user
        :param access_token: access token of the user
        """
        response = self._post(endpoint="/users/{}/physical-information-transactions".format(user_id),
                              access_token=access_token)
        if not response:
            return None

        return PhysicalInfoTransaction(oauth=self.oauth,
                                       transaction_url=response["resource-uri"],
                                       user_id=user_id,
                                       access_token=access_token)
