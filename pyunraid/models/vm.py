from pyunraid.helpers import *

class VM:
    def __init__(self):
        self.uuid = ''
        self.name = ''
        self.description = ''
        self.cpu_count = 0
        self.memory = 0
        self.vdisks = []
        self.vnc_port = 0
        self.autostart = False
        self.state = ''
        self.unraid = None


    def disable_autostart(self):
        return self._domain_autostart('false')


    def enable_autostart(self):
        return self._domain_autostart('true')


    def start(self):
        return self._domain('domain-start')


    def stop(self):
        return self._domain('domain-stop')


    def force_stop(self):
        return self._domain('domain-destroy')


    def restart(self):
        return self._domain('domain-restart')


    def hibernate(self):
        return self._domain('domain-pmsuspend')


    def remove(self):
        return self._domain('domain-undefine')


    def destroy(self):
        return self._domain('domain-delete')


    # Internal functions
    def _domain(self, action, payload = {}):
        unraid = self.unraid

        payload = {**{
            'action': action,
            'uuid': self.uuid,
            'response': 'json'
        }, **payload}

        response_code = unraid.post('/plugins/dynamix.vm.manager/include/VMajax.php', payload).status_code

        if response_code == 200:
            return 'OK'

        else:
            return 'ERROR'


    def _domain_autostart(self, value):
        return self._domain('domain-autostart', {'autostart': value})
