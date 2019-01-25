from pyunraid.helpers import *
from pyunraid.exceptions import *
from pyunraid.disks import disks


class Unraid:
    def __init__(self, url, username='root', password=''):
        self.url = url
        self.username = username,
        self.password = password
        self.csfr_token = get_csfr_token(url, username, password)

        self.u = [username,
                  password,
                  self.csfr_token]

    def disks(self):
        return disks(self.url, self.u)
