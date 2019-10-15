from pyunraid.helpers import *
from pyunraid.exceptions import *
from pyunraid.disks import disks
from pyunraid.containers import containers
from pyunraid.vms import vms


class Unraid:
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


    def disks(self):
        return disks(self.u)


    def containers(self):
        return containers(self.u)


    def vms(self):
        return vms(self.u)
