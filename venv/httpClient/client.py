import requests
"""
simple get Request with params option
"""
def Get(baseUrl, params):
    if(params):
        response = requests.get(baseUrl + '?', params)
    else:
        response = requests.get(baseUrl)
    result = response.content.decode("utf-8")
    return result
