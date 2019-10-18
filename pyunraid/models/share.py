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


    def size(self):
        """Compute the size in bytes of the share.

        :returns: size
        :rtype: int
        """
        pass


    def path(self, path = '/'):
        """List the directory in the share

        :returns: directory
        :rtype: list
        """
        pass


    def rename():
        pass

    def comment():
        pass

    def allocation_method():
        pass

    def minimum_free_space():
        pass

    def split_level():
        pass

    def included_disks():
        pass

    def excluded_disks():
        pass

    def use_cache_disk():
        pass

    def export(protocol):
        pass

    def security(protocol, security):
        pass
