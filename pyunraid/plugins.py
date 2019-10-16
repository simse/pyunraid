import re

import requests
from bs4 import BeautifulSoup

from pyunraid.helpers import *
from pyunraid.constants import *
from pyunraid.models.plugin import Plugin


def plugins(u):

    return parse_plugins(u)


def parse_plugins(u):
    # Parse containers page
    soup = BeautifulSoup(u.get('/plugins/dynamix.plugin.manager/include/ShowPlugins.php?check=0').text, 'lxml')
    plugins = []

    for plugin in soup.find_all('tr'):
        p = Plugin()

        # Find plugin name
        p.name = plugin.select('strong')[0].text


        plugins.append(p)

    return plugins
