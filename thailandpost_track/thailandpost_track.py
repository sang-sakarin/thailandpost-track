"""
A libraly that provides a python interface to Thailand Post API
"""
import json

from .constants import ENDPOINTS
from .request import basic_request


class ThailandpostTrack:
    def __init__(self, token_key=None):
        self.token_key = token_key
        self.API_ROOT = ENDPOINTS["API_ROOT"]
        self.token_key = self._get_token()

    def _get_path(self, path_name):
        """
        Get full endpoint for a specific path.
        """
        return self.API_ROOT + ENDPOINTS[path_name]

    def _get_headers(self):
        headers = {
            "CONTENT-TYPE": "application/json",
            "AUTHORIZATION": "Token {0}".format(self.token_key)
        }

        return headers

    def _get_token(self):
        url = self._get_path("AUTHENTICATE_TOKEN_PATH")
        response = basic_request('POST', url, headers=self._get_headers())

        return response["token"]

    def track(self, barcode=[]):
        url = self._get_path("TRACK_PATH")

        payload = {
           "status": "all",
           "language": "TH",
           "barcode": barcode
        }

        payload = json.dumps(payload)
        response = basic_request('POST', url, headers=self._get_headers(), payload=payload)

        return response
