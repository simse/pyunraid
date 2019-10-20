import re

from bs4 import BeautifulSoup

from pyunraid.helpers import get, post, get_csfr_token
from pyunraid.constants import ARRAY_STATUS
from pyunraid.disks import _disks
from pyunraid.containers import _containers
from pyunraid.vms import _vms
from pyunraid.shares import _shares
from pyunraid.users import _users
from pyunraid.plugins import _plugins
from pyunraid.notifications import _notifications


class Unraid:
    """The Unraid class represents an Unraid server and stores information
    about the server, and methods to interact with it.
    """

    #: Unraid server versions supported by this minor version. For each Unraid
    #: version that requires an update in pyunraid, there will be a minor
    #: version bump. For each major Unraid release, there will be a major
    #: version bump.
    SUPPORTED_VERSIONS = ['6.7.2']

    def __init__(self, url, username='root', password=''):
        # Check schema is supplied, fall back to HTTP if not
        if 'http://' not in url:
            url = 'http://' + url

        self.url = url
        self.username = username
        self.password = password
        self.csfr_token = get_csfr_token(url, username, password)
        self.version = ''
        self.uptime = 0
        self.name = ''
        self.description = ''
        self.license = ''
        self.array_status = ''

        self.u = {
            'url': self.url,
            'username': username,
            'password': password,
            'csfr_token': self.csfr_token
        }

        self._get_server_information()

        if self.version not in self.SUPPORTED_VERSIONS:
            # TODO: Raise exception
            print('This server version is NOT supported!!')

    def reboot(self):
        """Reboots the unraid server."""
        return self.post('/webGui/include/Boot.php', {'cmd': 'reboot'})

    def get(self, url):
        """Sends a GET request to the server with correct headers and
        authentication.

        :param url: Path to send request to, it's automatically appended to
        the server URL.
        :returns: Requests object
        """
        return get(self.u, self.u['url'] + url)

    def post(self, url, payload={}):
        """Sends a POST request to the server with correct headers and
        authentication.

        :param url: Path to send request to, it's automatically appended to
        the server URL.
        :param payload: Payload to send.
        :returns: Requests object
        """
        return post(self.u, self.u['url'] + url, payload)

    def _get_server_information(self):
        server_page = BeautifulSoup(self.get('/Main').text, 'lxml')

        # Find server version
        self.version = re.findall(
            r'Version: ([0-9]{1,2}.[0-9]{1,2}.[0-9]{1,2})',
            server_page.find(class_='logo').text
        )[0]

        # Find server name
        self.name = server_page.select('span.text-right')[0].text \
            .split(' &bullet;')[0]

        # Find server license
        self.license = server_page.find(id="licensetype").text

        # Find server description
        self.description = str(server_page.select('span.text-right')[0]) \
            .split('<br/>')[1]

        # Find array status
        self.array_status = ARRAY_STATUS[
            server_page.find(id="statusbar").text.strip()
        ]

    def get_disk(self, identification):
        """Get a single Disk object given identification.

        :param identification: The identification of the disk
        (e.g. WDC_WD80EMAZ-00WJTA0_7HKRY8MJ)
        """
        disks = self.disks()

        for disk in disks:
            if disk.identification == identification:
                return disk

        return None

    def get_container(self, id):
        """Get a single Container object given image ID.

        :param id: The ID of the container image (e.g. 0d70980cf126)
        """
        containers = self.containers()

        for container in containers:
            if container.id == id:
                return container

        return None

    def get_vm(self, name):
        """Get a single VM object given name.

        :param name: The name of the VM (e.g. Windows 10 Gaming Machine)
        """
        vms = self.vms()

        for vm in vms:
            if vm.name == name:
                return vm

        return None

    def get_share(self, name):
        """Get a single Share object given name.

        :param name: The name of the Share (e.g. appdata)
        """
        shares = self.shares()

        for share in shares:
            if share.name == name:
                return share

        return None

    def get_user(self, name):
        """Get a single User object given name.

        :param name: The name of the User (e.g. simon)
        """
        users = self.users()

        for user in users:
            if user.name == name:
                return user

        return None

    def get_plugin(self, name):
        """Get a single Plugin object given name.

        :param name: The name of the PLugin (e.g. Fix Common Problems)
        """
        plugins = self.plugins()

        for plugin in plugins:
            if plugin.name == name:
                return plugin

        return None

    def disks(self):
        """Get a list of :class:`disks <pyunraid.models.disk>` connected to
        the server.
        """
        if self.array_status in ['STOPPING', 'STOPPED']:
            return []

        return _disks(self)

    def containers(self):
        """Get a list of :class:`containers <pyunraid.models.container>`
        running on the server.
        """
        if self.array_status in ['STOPPING', 'STOPPED']:
            return []

        return _containers(self)

    def vms(self):
        """Get a list of :class:`VMs <pyunraid.models.vm>` running on the
        server.
        """
        if self.array_status in ['STOPPING', 'STOPPED']:
            return []

        return _vms(self)

    def shares(self):
        """Get a list of :class:`shares <pyunraid.models.share>` on the
        server.
        """
        if self.array_status in ['STOPPING', 'STOPPED']:
            return []

        return _shares(self)

    def users(self):
        """Get a list of :class:`users <pyunraid.models.user>` on the
        server.
        """
        if self.array_status in ['STOPPING', 'STOPPED']:
            return []

        return _users(self)

    def plugins(self):
        """Get a list of :class:`plugins <pyunraid.models.plugin>` on the
        server.
        """
        if self.array_status in ['STOPPING', 'STOPPED']:
            return []

        return _plugins(self)

    def notifications(self):
        """Get a list of :class:`notifications <pyunraid.models.notification>`
        on the server.
        """
        if self.array_status in ['STOPPING', 'STOPPED']:
            return []

        return _notifications(self)
