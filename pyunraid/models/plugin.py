class Plugin():

    def __init__(self):
        self.name = ''
        self.description = ''
        self.author = ''
        self.image = ''
        self.support_thread = ''
        self.update_status = ''
        self.version = ''
        self.unraid = None


    def uninstall(self):
        pass


    def release_notes(self):
        pass
        #return self.unraid.get("/plugins/dynamix.plugin.manager/include/ShowChanges.php?file=%2Ftmp%2Fplugins%2F{}.txt".format(self.name)).text
