#!/usr/bin/env python

from .resource import Resource


class PullNotifications(Resource):
    """This resource allows partners to check if their users have available data for downloading

    https://www.polar.com/accesslink-api/?http#pull-notifications
    """

    def list(self):
        """List available data

        Get list of available exercises and activities for users
        """
        return self._get(endpoint="/notifications")
