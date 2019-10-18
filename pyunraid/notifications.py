import json

import requests

from pyunraid.helpers import *
from pyunraid.constants import *
from pyunraid.models.notification import Notification


def _notifications(unraid):
    notifications = []

    for n in unraid.post('/webGui/include/Notify.php', {'cmd':'get'}).json():
        notification = Notification()

        n = json.loads(n)

        notification.timestamp = n['timestamp']
        notification.event = n['event']
        notification.subject = n['subject']
        notification.description = n['description']
        notification.importance = n['importance']
        notification.file = n['file']

        notification.unraid = unraid

        notifications.append(notification)

    return notifications
