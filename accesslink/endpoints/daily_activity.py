#!/usr/bin/env python

from .resource import Resource
from .daily_activity_transaction import DailyActivityTransaction


class DailyActivity(Resource):
    """This resource allows partners to access their users' daily activity data.

    https://www.polar.com/accesslink-api/?http#daily-activity
    """
    def create_transaction(self, user_id, access_token):
        """Initiate daily activity transaction

        Check for new daily activity and create a new transaction if data is available.

        :param user_id: id of the user
        :param access_token: access token of the user
        """
        response = self._post(endpoint="/users/{}/activity-transactions".format(user_id),
                              access_token=access_token)
        if not response:
            return None

        return DailyActivityTransaction(oauth=self.oauth,
                                        transaction_url=response["resource-uri"],
                                        user_id=user_id,
                                        access_token=access_token)