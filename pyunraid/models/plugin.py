class Plugin():
    """The Plugin class represents a plugin on the Unraid server

    :ivar name: The name of the plugin
    :ivar description: Description of the plugin
    :ivar author: Plugin author
    :ivar image: The image/icon of the plugin
    :ivar support_thread: The support thread for the plugin
    :ivar update_status: Whether there is an update or not
    :ivar version: The installed version of the plugin
    """
    def __init__(self):
        self.name = ''
        self.description = ''
        self.author = ''
        self.image = ''
        self.support_thread = ''
        self.update_status = ''
        self.version = ''
        self.__unraid = None

    def _uninstall(self):
        pass

    def _release_notes(self):
        pass
        # return self.unraid.get("/plugins/dynamix.plugin.manager/include/
        # ShowChanges.php
        # ?file=%2Ftmp%2Fplugins%2F{}.txt".format(self.name)).text

    def _set_unraid(self, unraid):
        self.__unraid = unraid
