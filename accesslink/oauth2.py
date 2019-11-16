#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

class OAuth2Client(object):
    """Wrapper class for OAuth2 requests"""

    def __init__(self, url, authorization_url, access_token_url, redirect_url,
                 client_id, client_secret):
        self.url = url
        self.authorization_url = authorization_url
        self.access_token_url = access_token_url
        self.redirect_url = redirect_url
        self.client_id = client_id
        self.client_secret = client_secret

    def get_auth_headers(self, access_token):
        """Get authorization headers for user level api resources"""

        return {
            "Authorization": "Bearer {}".format(access_token),
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get_authorization_url(self, response_type="code"):
        """Build authorization url for the client"""

        params = {
            "client_id": self.client_id,
            "response_type": response_type,
        }

        if self.redirect_url:
            params["redirect_uri"] = self.redirect_url

        return "{url}?{params}".format(url=self.authorization_url,
                                       params=urlencode(params))

    def get_access_token(self, authorization_code):
        """Exchange authorization code for an access token"""

        headers = {
            "Content-Type" : "application/x-www-form-urlencoded",
            "Accept" : "application/json;charset=UTF-8"
        }

        data = {
            "grant_type" : "authorization_code",
            "redirect_uri" : self.redirect_url,
            "code" : authorization_code
        }

        return self.post(endpoint=None,
                         url=self.access_token_url,
                         data=data,
                         headers=headers)

    def __build_endpoint_kwargs(self, **kwargs):
        """Create endpoint url for requests

        If `endpoint` argument is given, it is appended to the api url
        and used as the request url. Otherwise `url` argument is used.
        """

        if "endpoint" in kwargs:
            if kwargs["endpoint"] is not None:
                kwargs["url"] = self.url + kwargs["endpoint"]
            del kwargs["endpoint"]

        return kwargs

    def __build_auth_kwargs(self, **kwargs):
        """Setup authentication for requests

        If `access_token` is given, it is used in Authentication header.
        Otherwise basic auth is used with the client credentials.
        """

        if "access_token" in kwargs:
            headers = self.get_auth_headers(kwargs["access_token"])

            if "headers" in kwargs:
                headers.update(kwargs["headers"])

            kwargs["headers"] = headers
            del kwargs["access_token"]
        elif "auth" not in kwargs:
            kwargs["auth"] = HTTPBasicAuth(self.client_id, self.client_secret)

        return kwargs

    def __build_request_kwargs(self, **kwargs):
        kwargs = self.__build_endpoint_kwargs(**kwargs)
        kwargs = self.__build_auth_kwargs(**kwargs)
        return kwargs

    def __parse_response(self, response):
        if response.status_code >= 400:
            message = "{code} {reason}: {body}".format(code=response.status_code,
                                                       reason=response.reason,
                                                       body=response.text)
            raise HTTPError(message, response=response)

        if response.status_code is 204:
            return {}

        try:
            return response.json()
        except ValueError:
            return response.text

    def __request(self, method, **kwargs):
        kwargs = self.__build_request_kwargs(**kwargs)
        response = requests.request(method, **kwargs)
        return self.__parse_response(response)

    def get(self, endpoint, **kwargs):
        return self.__request("get", endpoint=endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.__request("post", endpoint=endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.__request("put", endpoint=endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.__request("delete", endpoint=endpoint, **kwargs)
