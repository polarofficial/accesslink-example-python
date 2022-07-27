#!/usr/bin/env python

from datetime import datetime
from requests import HTTPError
from .resource import Resource


class Sleep(Resource):
    """This resource allows partners to access their sleep information.

    https://www.polar.com/accesslink-api/#sleep
    """

    def list_sleeps(self, access_token):
        """List sleep data of user for the last 28 days.

        :param access_token: access token of the user
        """
        return self._get(endpoint="/users/sleep",
                              access_token=access_token)

    def list_sleeps_available(self, access_token):
        """Get the dates with sleep start and end times, where user has sleep data available in the last 28 days.

        :param access_token: access token of the user
        """
        return self._get(endpoint="/users/sleep/available",
                              access_token=access_token)

    def get_sleep_by_date(self, access_token, date=datetime.today()):
        """Get Users sleep data for given date.

        :param access_token: access token of the user
        :param date: datetime instance
        """
        try:
            return self._get(endpoint=f"/users/sleep/{date.strftime('%Y-%m-%d')}",
                                access_token=access_token)
        except HTTPError:
            return None
