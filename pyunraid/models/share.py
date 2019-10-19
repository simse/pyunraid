from bs4 import BeautifulSoup

from pyunraid.helpers import parse_size


class Share():
    """The Share class represents a share on the Unraid server.

    :ivar type: User share or disk share
    :ivar status: The parity status of the share
    :ivar name: The name of the share
    :ivar comment: The comment attached to the share
    :ivar smb_security: Public, hidden or private SMB security. None if no
    security set.
    :ivar nfs_security: Public, hidden or private NFS security. None if no
    security set.
    :ivar afp_security: None, AFP security will be removed in Unraid 6.9 and
    thus not supported
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

        .. warning:: This function is just a prototype and does not do
        anything.

        :returns: size
        :rtype: int
        """
        pass

    def rename(self, name):
        """Rename the share.

        :param name: The new name.
        """
        old_name = self.name
        self.name = name

        return self._unraid.post('/update.htm',
            {
                'shareNameOrig': old_name,
                'shareName': name,
                'cmdEditShare': 'Apply'
            }
        ).status_code

    def set_comment(self, comment):
        """Set the comment for the share.

        :param comment: The new comment.
        """
        self.comment = comment

        return self._unraid.post('/update.htm',
            {
                'shareComment': comment,
                'cmdEditShare': 'Apply'
            }
        ).status_code

    def set_allocation_method(self, method):
        """Set the allocation method for the share.

        :param comment: The new comment.
        """

        return self._unraid.post('/update.htm',
            {
                'shareAllocator': method,
                'cmdEditShare': 'Apply'
            }
        ).status_code

    def set_minimum_free_space(self, floor=0):
        """Set minimum free space for the share.

        :param floor: Minimum free space in bytes
        """

        return self._unraid.post('/update.htm',
            {
                'shareFloor': floor,
                'cmdEditShare': 'Apply'
            }
        ).status_code

    def set_split_level(self, split=None):
        """Set split level for the share.

        :param split: The split level where None is automatic splitting, 1 is
        only split top level dir and 0 is no splitting.
        """

        return self._unraid.post('/update.htm',
            {
                'shareSplitLevel': split,
                'cmdEditShare': 'Apply'
            }
        ).status_code

    def _included_disks():
        pass

    def _excluded_disks():
        pass

    def set_cache_disk(self, use_cache='no'):
        """Set whether cache disk should be used for share.

        :param use_cache: 'yes' for yes and 'no' for no
        """

        return self._unraid.post('/update.htm',
            {
                'shareUseCache': use_cache,
                'cmdEditShare': 'Apply'
            }
        ).status_code

    def _export(protocol):
        pass

    def _security(protocol, security):
        pass

    def path(self, path='/'):
        """List the directory in the share

        :returns: directory
        :rtype: list
        """
        directory = '/mnt/user/' + self.name + path
        table_page = self._unraid.get(
            '/webGui/include/Browse.php?dir=' + directory
        ).text
        table = BeautifulSoup(table_page, 'lxml')

        return self._parse_directory(table)

    # Internal functions
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
