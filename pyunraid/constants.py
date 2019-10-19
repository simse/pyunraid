"""The constants module stores constants to ensure consistency for certain status properties across versions.

"""

DISK_STATUS = {
    'Normal operation, device is active': 'ACTIVE',
    'Device is in standby mode (spun-down)': 'INACTIVE',
    'Device contents emulated': 'EMULATED',
    'Device is disabled, contents emulated': 'DISABLED',
    'New device': 'NEW',
    'No device present, position is empty': 'EMPTY'
}

ARRAY_STATUS = {
    'Array Started': 'STARTED',
    'Array Stopped': 'STOPPED',
    'Array Stopping&bullet;Stopping services...': 'STOPPING'
}
