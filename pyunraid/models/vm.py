from .model import Model


class VM(Model):
    """The VM class represents a VM on the Unraid server.

    :ivar uuid: The UUID of the VM
    :ivar name: The friendly name of the VM
    :ivar description: The description of the VM
    :ivar cpu_count: Assigned CPU count
    :ivar memory: Allocated memory size
    :ivar vdisks: An array of vdisks
    :ivar vnc_port: The VNC port, if any
    :ivar autostart: Whether autostart is enabled
    :ivar state: The state of the VM (e.g. started, stopped)
    """
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
        self.__unraid = None

    def action(self, action):
        """Send action to Unraid for specific VM.

        :param action: Action to send (e.g. start, stop)
        .. warning:: Please check you're sending a supported action, 'start' is
        not correct, 'domain-start' is.
        """
        return self._domain(action)

    def disable_autostart(self):
        """Disable autostart of the VM."""
        return self._domain_autostart('false')

    def enable_autostart(self):
        """Enabled autostart of the VM."""
        return self._domain_autostart('true')

    def start(self):
        """Start the VM."""
        return self._domain('domain-start')

    def stop(self):
        """Stop the VM."""
        return self._domain('domain-stop')

    def force_stop(self):
        """Force stop the VM."""
        return self._domain('domain-destroy')

    def restart(self):
        """Restart the VM."""
        return self._domain('domain-restart')

    def hibernate(self):
        """Hibernate the VM."""
        return self._domain('domain-pmsuspend')

    def remove(self):
        """Remove the VM, but leave the vdisks."""
        return self._domain('domain-undefine')

    def destroy(self):
        """Remove the VM and delete the vidsks."""
        return self._domain('domain-delete')

    # Internal functions
    def _set_unraid(self, unraid):
        self.__unraid = unraid

    def _domain(self, action, payload={}):
        unraid = self.__unraid

        payload = {**{
            'action': action,
            'uuid': self.uuid,
            'response': 'json'
        }, **payload}

        response_code = unraid.post(
            '/plugins/dynamix.vm.manager/include/VMajax.php',
            payload
        ).status_code

        if response_code == 200:
            return 'OK'

        else:
            return 'ERROR'

    def _domain_autostart(self, value):
        return self._domain('domain-autostart', {'autostart': value})
