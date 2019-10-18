class Notification():

    def __init__(self):
        self.timestamp = ''
        self.event = ''
        self.subject = ''
        self.description = ''
        self.importance = ''
        self.file = ''
        self.unraid = None


    def dismiss(self):
        self.unraid.post('/webGui/include/Notify.php', {'cmd':'archive', 'file':self.file})
