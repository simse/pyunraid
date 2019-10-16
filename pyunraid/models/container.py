from pyunraid.helpers import *


class Container():

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
        self.cpu_usage = 0
        self.memory_usage = 0
        self.startup_delay = 0
        self.uptime = 0
        self.age = 0
        self.unraid = None


    def start(self):
        return self._action('start')


    def stop(self):
        return self._action('stop')


    def restart(self):
        return self._action('restart')


    def disable_autostart(self):
        return self._action('')


    def remove(self, remove_image=False):
        if remove_image:
            self._action('remove_container')
            return self._action('remove_image')

        else:
            return self._action('remove_container')


    # TODO: Read logs from /plugins/dynamix.docker.manager/include/Events.php?action=log&container=??????????
    def logs(self):
        pass

    # Internal functions
    def _action(self, action, payload = {}):
        unraid = self.unraid

        payload = {**{
            'action': action,
            'container': self.id,
            'name': self.name,
            'response': 'json'
        }, **payload}

        response_code = unraid.post('/plugins/dynamix.docker.manager/include/Events.php', payload).status_code

        if response_code == 200:
            return 'OK'

        else:
            return 'ERROR'
