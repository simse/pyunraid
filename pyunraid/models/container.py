from pyunraid.helpers import *


class Container():
    """
    Represents a Docker container on the Unraid server.

    :ivar name: Container name
    :ivar id: Container image ID
    :ivar image: Container image (e.g. simsemand/chronos)
    :ivar dockerhub_url: Dockerhub URL to image
    :ivar state: Container state (running, stopped)
    :ivar update_status: Whether container has any updates available
    :ivar tag: The image tag installed (e.g. latest)
    :ivar network: Container network (e.g. br0)
    :ivar port_mappings: Array of port mappings (e.g. [['5050', '5000'], ['80', '81']])
    :ivar path_mappings: Array of path mappings (e.g. [['/chronos', '/mnt/user/appdata/chronos']])
    :ivar startup_delay: Startup delay for the container
    :ivar uptime: Uptime in minutes
    :ivar age: Age in minutes
    """

    def __init__(self):
        self.name = ''
        self.id = ''
        self.image = ''
        self.dockerhub_url = ''
        self.state = ''
        self.update_status = ''
        self.tag = ''
        self.network = ''
        self.port_mappings = []
        self.path_mappings = []
        self.startup_delay = 0
        self.uptime = 0
        self.age = 0
        self.unraid = None


    def start(self):
        """Starts the Docker container."""
        return self._action('start')


    def stop(self):
        """Stops the Docker container."""
        return self._action('stop')


    def restart(self):
        """Restarts the Docker container."""
        return self._action('restart')


    def disable_autostart(self):
        """Disables autostart."""
        return self._action('autostart',
            {'auto':'false', 'container':self.name, 'wait':''},
            '/plugins/dynamix.docker.manager/include/UpdateConfig.php'
        )


    def enable_autostart(self):
        """Enables autostart."""
        return self._action('autostart',
            {'auto':'true', 'container':self.name, 'wait':''},
            '/plugins/dynamix.docker.manager/include/UpdateConfig.php'
        )


    def remove(self, remove_image=False):
        """Removes container from Unraid.

        :param remove_image: Whether to also remove Docker image or leave it orphaned.
        """
        if remove_image:
            self._action('remove_container')
            return self._action('remove_image')

        else:
            return self._action('remove_container')


    # TODO: Read logs from /plugins/dynamix.docker.manager/include/Events.php?action=log&container=??????????
    def _logs(self):
        """Loads container logs."""
        pass

    # Internal functions
    def _action(self, action, payload = {}, url = '/plugins/dynamix.docker.manager/include/Events.php'):
        unraid = self.unraid

        payload = {**{
            'action': action,
            'container': self.id,
            'name': self.name,
            'response': 'json'
        }, **payload}

        print(payload)

        response_code = unraid.post(url, payload).status_code

        if response_code == 200:
            return 'OK'

        else:
            return 'ERROR'
