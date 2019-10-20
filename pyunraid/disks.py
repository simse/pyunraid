import re

from bs4 import BeautifulSoup

from pyunraid.helpers import parse_size, parse_speed
from pyunraid.constants import DISK_STATUS
from pyunraid.models.disk import Disk


def _disks(u):
    return _parse_devices(u, 'array') + \
           _parse_devices(u, 'cache') + \
           _parse_devices(u, 'flash')


def _parse_devices(unraid, device):
    payload = {
        'path': 'Main',
        'device': device
    }

    parsed_page = BeautifulSoup(
        unraid.post('/webGui/include/DeviceList.php', payload).text,
        features="lxml"
    )
    rows = parsed_page.find_all('tr')
    disks = []

    for row in rows:
        parsed_row = parse_disk_row(row)

        if parsed_row:
            disks.append(parsed_row)

    return disks


def parse_disk_row(row):
    # Create disk object
    disk = Disk()
    disk.disk_type = "hdd"

    # Remove empty rows
    if row.get_text() == '':
        return None

    # Remove last status row
    try:
        if 'tr_last' in row.attrs['class']:
            return None
    except KeyError:
        pass

    # Find disk status
    status_span = row.find_all('span')[0].get_text()

    try:
        disk.status = DISK_STATUS[status_span]
    except KeyError:
        disk.status = None

    # Find disk name
    name_a = row.find_all('a')[1]
    disk.name = name_a.get_text()

    # Find storage type
    if disk.name == 'Parity':
        disk.type = 'parity'
    elif disk.name == 'Cache':
        disk.type = 'cache'
    elif disk.name == 'Flash':
        disk.type = 'boot'
    else:
        disk.type = 'storage'

    # Find disk identification, size and mount
    id_td = row.find_all('td')[1]
    info = id_td.get_text()
    disk.identification = info.split(' - ')[0]

    disk.mount = re.search('[(]([a-z]{3})[)]', info).group(0).strip('()')

    size = re.search('([0-9]+) (PB|TB|GB|MB)', info)
    disk.size = parse_size(size.group(0))

    # Find disk temperature
    temp_td = row.find_all('td')[2].get_text()
    if temp_td == '*':
        disk.temperature = None
    else:
        disk.temperature = int(temp_td.strip(' C'))

    # Find disk read statistics
    read_td = row.find_all('td')[3]
    disk.current_read_speed = parse_speed(
        read_td.find_all('span')[0].get_text()
    )
    disk.current_read_count = int(
        read_td.find_all('span')[1].get_text().replace(',', '')
    )

    # Find disk write statistics
    read_td = row.find_all('td')[4]
    disk.current_write_speed = parse_speed(
        read_td.find_all('span')[0].get_text()
    )
    disk.current_write_count = int(
        read_td.find_all('span')[1].get_text().replace(',', '')
    )

    # Find disk errors
    error_td = row.find_all('td')[5]
    disk.errors = int(error_td.get_text())

    # Find filesystem
    if disk.type == 'parity':
        disk.filesystem = None
    else:
        fs_td = row.find_all('td')[6]
        disk.filesystem = fs_td.get_text()

    # Find space used and available
    if disk.type == 'parity':
        disk.space_used = None
        disk.space_available = None
    else:
        disk.space_used = parse_size(row.find_all('td')[8].get_text())
        disk.space_available = parse_size(row.find_all('td')[9].get_text())

    # Add disk object to disks list
    return disk
