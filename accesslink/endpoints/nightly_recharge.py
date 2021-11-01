#!/usr/bin/env python

from datetime import datetime
from requests import HTTPError
from .resource import Resource


class NightlyRecharge(Resource):
    """This resource allows partners to access their nightly recharges information.

    https://www.polar.com/accesslink-api/#nightly-recharge
    """

    def list_nightly_recharges(self, access_token):
        """List Nightly Recharge data of user for the last 28 days.

        :param access_token: access token of the user
        """
        return self._get(endpoint="/users/nightly-recharge",
                              access_token=access_token)

    def get_nightly_recharge_by_date(self, access_token, date=datetime.today()):
        """Get Users Nightly Recharge data for given date.

        :param access_token: access token of the user
        :param date: datetime instance
        """
        try:
            return self._get(endpoint=f"/users/nightly-recharge/{date.strftime('%Y-%m-%d')}",
                                access_token=access_token)
        except HTTPError:
            return None
