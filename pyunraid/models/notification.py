class Notification():
    """The Notification class represents a notification on the Unraid server

    :ivar timestamp: The timestamp of the notification (e.g. 19-10-2019 00:26)
    :ivar event: The event
    :ivar subject: The subject
    :ivar description: The description
    :ivar importance: Importance of the notification
    :ivar file: File that emitted the notification
    """

    def __init__(self):
        self.timestamp = ''
        self.event = ''
        self.subject = ''
        self.description = ''
        self.importance = ''
        self.file = ''
        self.unraid = None


    def dismiss(self):
        """Dismiss the notification.

        :returns: void
        """
        self.unraid.post('/webGui/include/Notify.php', {'cmd':'archive', 'file':self.file})
