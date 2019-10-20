import re

import requests

from pyunraid.exceptions import InvalidCredentials


def get_csfr_token(url, username, password):
    unraid_page = requests.get(url + '/Main', auth=(username, password))

    if unraid_page.status_code == 401:
        raise InvalidCredentials('Incorrect credentials for Unraid provided')

    if unraid_page.status_code != 200:
        raise ConnectionError

    search = re.search('([csfr_token=]{11})([A-Z,0-9]{16})', unraid_page.text)
    csfr_token = search.group(2)

    return csfr_token


def get(u, url):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    request = requests.get(url,
                           headers=headers,
                           auth=(u['username'], u['password'])
                           )

    return request


def post(u, url, payload={}):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload['csrf_token'] = u['csfr_token']
    request = requests.post(url,
                            data=payload,
                            headers=headers,
                            auth=(u['username'], u['password'])
                            )

    return request


def parse_size(size):
    units = {
        "B": 1, "KB": 10 ** 3, "MB": 10 ** 6, "GB": 10 ** 9,
        "TB": 10 ** 12, "K": 10 ** 3, "M": 10 ** 6, "G": 10 ** 9,
        "T": 10 ** 12
    }

    if size == 'unknown':
        return 0

    if size == '<DIR>':
        return 0

    number, unit = [string.strip() for string in size.split()]
    return int(float(number)*units[unit])


def parse_speed(size):
    units = {"B/s": 1, "KB/s": 125, "MB/s": 125000}

    number, unit = [string.strip() for string in size.split()]
    return int(float(number)*units[unit])
