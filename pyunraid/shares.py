import re

import requests
from bs4 import BeautifulSoup

from pyunraid.helpers import *
from pyunraid.constants import *
from pyunraid.models.share import Share


SHARE_STATUS = {
    'Some or all files unprotected': 'UNPROTECTED'
}

SHARE_SECURITY = {
    'Public': 'PUBLIC',
    'Hidden': 'HIDDEN',
    'Private': 'PRIVATE',
    '-': None
}


def _shares(unraid):
    # Parse shares page
    soup = BeautifulSoup(unraid.get('/webGui/include/ShareList.php?compute=no&path=Shares&scale=-1&number=.%2C').text, 'lxml')
    shares = []

    for share in soup.find_all('tr'):
        s = Share()

        # Find share status
        s.status = SHARE_STATUS[share.find_all('a')[0].text]

        # Find share name
        s.name = share.find_all('a')[1].text

        # Find share comment
        s.comment = share.find_all('td')[1].text

        # Find SMB security
        s.smb_security = SHARE_SECURITY[share.find_all('td')[2].text]

        # Find SMB security
        s.nfs_security = SHARE_SECURITY[share.find_all('td')[3].text]

        # Find free space
        s.free_size = parse_size(share.find_all('td')[6].text)

        s._unraid = unraid

        shares.append(s)

    return shares
