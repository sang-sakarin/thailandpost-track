"""
A libraly that provides a python interface to Thailand Post API
"""
import requests
import warnings

from requests.packages.urllib3.exceptions import InsecureRequestWarning


def basic_request(method, url, headers={}, payload={}):
    # Ignore warning message after turn-off verify
    warnings.simplefilter('ignore', InsecureRequestWarning)

    return requests.request(method, url, headers=headers, data=payload, verify=False).json()
