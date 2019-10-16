from pyunraid.helpers import *
from pyunraid.exceptions import *
from pyunraid.disks import disks
from pyunraid.containers import containers
from pyunraid.vms import vms
from pyunraid.shares import shares
from pyunraid.users import users


class Unraid:
    SUPPORTED_VERSIONS = ['6.7.2']

    def __init__(self, url, username='root', password=''):
        self.url = url
        self.username = username,
        self.password = password
        self.csfr_token = get_csfr_token(url, username, password)

        self.u = {
            'url': url,
            'username': username,
            'password': password,
            'csfr_token': self.csfr_token
        }


    def get(self, url):
        return get(self.u, self.u['url'] + url)


    def post(self, url, payload):
        return post(self.u, self.u['url'] + url, payload)


    def disks(self):
        return disks(self)


    def containers(self):
        return containers(self)


    def vms(self):
        return vms(self)


    def shares(self):
        return shares(self)


    def users(self):
        return users(self)
