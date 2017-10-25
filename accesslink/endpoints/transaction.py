#!/usr/bin/env python

from .resource import Resource


class Transaction(Resource):

    def __init__(self, oauth, transaction_url, user_id, access_token):
        super(Transaction, self).__init__(oauth)
        self.transaction_url = transaction_url
        self.user_id = user_id
        self.access_token = access_token

    def commit(self):
        """Commit the transaction

        This should be done after retrieving data from the transaction.
        """
        return self._put(endpoint=None, url=self.transaction_url,
                         access_token=self.access_token)
