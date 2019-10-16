import re

from bs4 import BeautifulSoup

from pyunraid.helpers import *
from pyunraid.exceptions import *
from pyunraid.disks import disks
from pyunraid.containers import containers
from pyunraid.vms import vms
from pyunraid.shares import shares
from pyunraid.users import users
from pyunraid.plugins import plugins


class Unraid:
    SUPPORTED_VERSIONS = ['6.7.2']
    ARRAY_STATUS = {
        'Array Started': 'STARTED',
        'Array Stopped': 'STOPPED',
        'Array Stopping&bullet;Stopping services...': 'STOPPING'
    }

    def __init__(self, url, username='root', password=''):
        self.url = url
        self.username = username
        self.password = password
        self.csfr_token = get_csfr_token(url, username, password)
        self.version = ''
        self.uptime = 0
        self.name = ''
        self.description = ''
        self.license = ''
        self.array_status = ''

        self.u = {
            'url': url,
            'username': username,
            'password': password,
            'csfr_token': self.csfr_token
        }

        self._get_server_information()

        if not self.version in self.SUPPORTED_VERSIONS:
            print('This server version is NOT supported!!')


    def get(self, url):
        return get(self.u, self.u['url'] + url)


    def post(self, url, payload):
        return post(self.u, self.u['url'] + url, payload)


    def _get_server_information(self):
        server_page = BeautifulSoup(self.get('/Main').text, 'lxml')

        # Find server version
        self.version = re.findall(r'Version: ([0-9]{1,2}.[0-9]{1,2}.[0-9]{1,2})', server_page.find(class_='logo').text)[0]


        # Find server name
        self.name = server_page.select('span.text-right')[0].text.split(' &bullet;')[0]

        # Find server license
        self.license = server_page.find(id="licensetype").text

        # Find server description
        self.description = str(server_page.select('span.text-right')[0]).split('<br/>')[1]

        # Find array status
        self.array_status = self.ARRAY_STATUS[server_page.find(id="statusbar").text.strip()]


    def disks(self):
        if self.array_status in ['STOPPING', 'STOPPED']:
            return []

        return disks(self)


    def containers(self):
        if self.array_status in ['STOPPING', 'STOPPED']:
            return []

        return containers(self)


    def vms(self):
        if self.array_status in ['STOPPING', 'STOPPED']:
            return []

        return vms(self)


    def shares(self):
        if self.array_status in ['STOPPING', 'STOPPED']:
            return []

        return shares(self)


    def users(self):
        if self.array_status in ['STOPPING', 'STOPPED']:
            return []

        return users(self)


    def plugins(self):
        if self.array_status in ['STOPPING', 'STOPPED']:
            return []
            
        return plugins(self)
