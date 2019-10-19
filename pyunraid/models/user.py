import base64
import ntpath
import codecs
from os import path

class User():
    """The User class represents a user on the Unraid server

    :ivar name: The name of the user
    :ivar description: The description of the user
    :ivar image: The image of the user
    """
    def __init__(self):

        self.name = ''
        self.description = ''
        self.image = ''
        self._unraid = None


    def set_description(self, description):
        """Set the description of the user.

        :param description: The new description.
        """
        self.description = description

        return self._unraid.post('/update.htm',
            {
                'userName': self.name,
                'userDesc': description,
                'cmdUserEdit': 'Apply'
            }
        ).status_code


    def set_image(self, image):
        """Set the profile picture of the user."""
        if not path.exists(image):
            return False

        encoded = base64.b64encode(open(image, 'rb').read())
        filename = ntpath.basename(image)

        # Upload the image
        self._unraid.post('/webGui/include/FileUpload.php',
            {
                'filename': filename,
                'filedata': encoded
            }
        )

        # Assign image
        self._unraid.post('/webGui/include/FileUpload.php',
            {
                'cmd': 'save',
                'path': '/boot/config/plugins/dynamix/users',
                'filename': filename,
                'output': self.name + '.png'
            }
        )

        # Apply changes
        return self._unraid.post('/update.htm',
            {
                'userName': self.name,
                'userDesc': self.description,
                'cmdUserEdit': 'Apply'
            }
        ).status_code


    def delete(self):
        """Delete the user."""
        if self.name == 'root':
            return 403

        return self._unraid.post('/update.htm',
            {
                'userName': self.name,
                'userDesc': self.description,
                'confirmDelete': 'on',
                'cmdUserEdit': 'Delete'
            }
        ).status_code


    def set_password(self, password):
        """Set a new password

        :param password: The new password to be set
        """
        if self.name == 'root':
            return 403

        return self._unraid.post('/update.htm',
            {
                'userName': self.name,
                'userPassword': password,
                'userPasswordConf': password,
                'confirmDelete': 'on',
                'cmdUserEdit': 'Change'
            }
        ).status_code
