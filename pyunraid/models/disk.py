class Disk():
    """The Disk class represents a harddrive, SSD or flash drive connected to the Unraid server

    :ivar disk_type: Whether disk is HDD, SSD or USB
    :ivar status: The status of the disk (active, inactive, emulated, disabled, new, empty)
    :ivar name: The name of the disk
    :ivar type: The array the disk is in (array, cache or boot)
    :ivar identification: The identification string for the disk, usually includes the serial number
    :ivar mount: The UNIX mount (e.g. /dev/sdc)
    :ivar size: The size in bytes
    :ivar temperature: The temperature in Celsius
    :ivar current_read_speed: The current read speed in bytes per second
    :ivar current_read_count: The current read count
    :ivar current_write_speed: The current write speed in bytes per second
    :ivar current_write_count: The current write count
    :ivar errors: Read/write errors
    :ivar filesystem: The filesystem used (e.g. xfs, btrfs)
    :ivar space_used: Space used in bytes
    :ivar space_available: Space available in bytes
    """
    def __init__(self):
        self.disk_type = ''
        self.status = ''
        self.name = ''
        self.type = ''
        self.identification = ''
        self.mount = ''
        self.size = 0
        self.temperature = 0
        self.current_read_speed = 0
        self.current_read_count = 0
        self.current_write_speed = 0
        self.current_write_count = 0
        self.errors = 0
        self.filesystem = ''
        self.space_used = 0
        self.space_available = 0


    def _smart():
        pass
