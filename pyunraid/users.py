import re

import requests
from bs4 import BeautifulSoup

from pyunraid.helpers import *
from pyunraid.constants import *
from pyunraid.models.user import User


def users(u):

    return parse_users(u)


def parse_users(u):
    # Parse containers page
    soup = BeautifulSoup(u.get('/Users').text, 'lxml')
    users = []

    for user in soup.select('div.user-list'):
        u = User()

        # Find user description
        u.description = user.find('span').text

        # Find username
        if not u.description:
            u.name = user.find('a').text

        else:
            u.name = user.find('a').text.replace(u.description, '')


        # Find image
        u.image = user.find('img')['src']

        users.append(u)

    return users
