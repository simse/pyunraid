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
