"""
A libraly that provides a python interface to Thailand Post API
"""
import json

from .constants import ENDPOINTS
from .language import Language
from .request import basic_request
from .status_code import StatusCode


class ThailandpostTrack:
    def __init__(self, token_key=None):
        self.token_key = token_key
        self.API_ROOT = ENDPOINTS["API_ROOT"]
        self.token = ''
        self._expire = None
        self.fetch_token()

    def _get_path(self, path_name):
        """
        Get full endpoint for a specific path.
        """
        return self.API_ROOT + ENDPOINTS[path_name]

    def _get_headers(self, token=''):
        headers = {
            "CONTENT-TYPE": "application/json",
            "AUTHORIZATION": "Token {0}".format(token)
        }

        return headers

    def fetch_token(self):
        print(self.token)
        url = self._get_path("AUTHENTICATE_TOKEN_PATH")
        response = basic_request('POST', url, headers=self._get_headers(token=self.token_key))

        self._expire = response["expire"]
        self.token = response["token"]

    def track(self, barcode=[], status=StatusCode.ALL, language=Language.EN):
        url = self._get_path("TRACK_PATH")

        payload = {}
        payload["barcode"] = barcode
        payload["status"] = status
        payload["language"] = language

        payload = json.dumps(payload)
        response = basic_request('POST', url, headers=self._get_headers(self.token), payload=payload)

        return response

    def expire(self):
        return self._expire
