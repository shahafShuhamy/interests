import urllib.request as client
from urllib.parse import urlparse, urlencode

"""
simple get Request with params option
"""
def Get(baseUrl, params):
    if(params):
        url = client.urlopen(baseUrl + '?' + urlencode(params))
    else:
        url = client.urlopen(baseUrl)
    result = url.read().decode("utf-8")
    return result
