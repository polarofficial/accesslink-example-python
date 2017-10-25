#!/usr/bin/env python

import uuid

from .resource import Resource


class Users(Resource):
    """This resource provides all the necessary functions to manage users.

    https://www.polar.com/accesslink-api/?http#users
    """

    def register(self, access_token, member_id=uuid.uuid4().hex):
        """Registration

        Once partner has been authorized by user, partner must register user before being able to access her data.

        :param access_token: access token of the user
        :param member_id: unique client-specific identifier for the user
        """
        return self._post(endpoint="/users",
                          access_token=access_token,
                          json={"member-id": member_id})

    def delete(self, user_id, access_token):
        """De-registration

        When partner wishes no longer to receive user data, user can be de-registered.
        This will revoke the access token authorized by user.

        :param user_id: id of the user
        :param access_token: access token of the user
        """
        return self._delete(endpoint="/users/{user_id}".format(user_id=user_id),
                            access_token=access_token)

    def get_information(self, user_id, access_token):
        """List user's basic information.

        :param user_id: id of the user
        :param access_token: access token of the user
        """
        return self._get(endpoint="/users/{user_id}".format(user_id=user_id),
                         access_token=access_token)
