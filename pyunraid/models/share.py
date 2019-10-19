from bs4 import BeautifulSoup

from pyunraid.helpers import *

class Share():
    """The Share class represents a share on the Unraid server.

    :ivar type: User share or disk share
    :ivar status: The parity status of the share
    :ivar name: The name of the share
    :ivar comment: The comment attached to the share
    :ivar smb_security: Public, hidden or private SMB security. None if no security set.
    :ivar nfs_security: Public, hidden or private NFS security. None if no security set.
    :ivar afp_security: None, AFP security will be removed in Unraid 6.9 and thus not supported
    :ivar free_size: Free size of share in bytes
    """
    def __init__(self):
        self.type = ''
        self.status = ''
        self.name = ''
        self.comment = ''
        self.smb_security = ''
        self.nfs_security = ''
        self.afp_security = None
        self.free_size = 0
        self._unraid = None


    def _compute_size(self):
        """Compute the size in bytes of the share.

        .. warning:: This function is just a prototype and does not do anything.

        :returns: size
        :rtype: int
        """
        #print(self._unraid.get('/webGui/include/ShareList.php?compute=no&path=Shares&scale=-1&number=.%2C&fill=ssz').text)
        pass


    def path(self, path = '/'):
        """List the directory in the share

        :returns: directory
        :rtype: list
        """
        directory = '/mnt/user/' + self.name + path
        table = BeautifulSoup(self._unraid.get('/webGui/include/Browse.php?dir=' + directory).text, 'lxml')

        return self._parse_directory(table)


    def _parse_directory(self, table):
        """Internal function to parse path directory table."""
        path = []

        for row in table.select('tbody tr'):
            p = {
                'type': '',
                'name': '',
                'size': 0,
                'last_modified': '',
                'location': ''
            }

            # Find path type
            if row.select('tr div.icon-file'):
                p['type'] = 'FILE'


            if row.select('tr div.icon-dir'):
                p['type'] = 'FOLDER'


            # Find path name
            p['name'] = row.find_all('td')[1].text.strip()

            # Find path size
            p['size'] = parse_size(row.find_all('td')[2].text.strip())

            # Find last modified date
            p['last_modified'] = row.find_all('td')[3].text.strip()

            # Find location
            p['location'] = row.find_all('td')[4].text.strip()


            path.append(p)

        return path
