#!/usr/bin/env python

from .transaction import Transaction


class DailyActivityTransaction(Transaction):

    def list_activities(self):
        """Get a list of activity resource urls in the transaction"""
        return self._get(endpoint=None, url=self.transaction_url,
                         access_token=self.access_token)

    def get_activity_summary(self, url):
        """Get user's activity summary from the transaction

        :param url: url of the activity entity
        """
        return self._get(endpoint=None, url=url,
                         access_token=self.access_token)

    def get_step_samples(self, url):
        """Get activity step samples

        :param url: url of the activity entity
        """
        return self._get(endpoint=None, url=url+"/step-samples",
                         access_token=self.access_token)

    def get_zone_samples(self, url):
        """Get activity zone samples

        :param url: url of the activity entity
        """
        return self._get(endpoint=None, url=url+"/zone-samples",
                         access_token=self.access_token)
