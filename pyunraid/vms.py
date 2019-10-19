import re

import requests
from bs4 import BeautifulSoup

from pyunraid.helpers import *
from pyunraid.constants import *
from pyunraid.models.vm import VM


def _vms(u):
    # Parse containers page
    soup = BeautifulSoup(u.get('/plugins/dynamix.vm.manager/include/VMMachines.php').text, 'lxml')
    vms = []

    # Loop through each VM
    for vm_row in soup.find_all(class_="sortable"):
        vm = VM()

        # Find VM uuid
        vm.uuid = vm_row.find_all('td')[6].find_all("input")[0]['uuid']

        # Find VM name
        vm.name = vm_row.select(".vm-name a")[0].text

        # Find VM description
        vm.description = vm_row.find_all('td')[1].text

        # Find VM state
        vm.state = vm_row.select("span.state")[0].text

        # Find CPU count
        vm.cpu_count = int(vm_row.find_all('td')[2].text)

        # Find memory amount
        vm.memory = parse_size(vm_row.find_all('td')[3].text.replace('M', ' M'))

        # Find vdisks
        vm.vdisks = _find_vdisks(soup, vm_row['parent-id'])

        # Find VNC port
        vm.vnc_port = vm_row.find_all('td')[5].text.replace('VNC:', '')

        # Find autostart status
        vm.autostart = vm_row.find_all('td')[6].find_all("input")[0].has_attr('checked')

        vm.unraid = u

        vms.append(vm)

    return vms


def _find_vdisks(soup, index):
    vdisks = []

    row = soup.find(id="name-" + index)
    vdisk_rows = row.select('#domdisk_list tr')

    for row in vdisk_rows:
        vdisks.append(
            {
                'path': row.find_all('td')[0].text,
                'bus': row.find_all('td')[1].text,
                'capacity': parse_size(_add_space(row.find_all('td')[2].text.strip())),
                'allocation': parse_size(_add_space(row.find_all('td')[3].text.strip()))
            }
        )

    return vdisks


def _add_space(input):
    return input.replace('B', ' B') \
                .replace('M', ' M') \
                .replace('K', ' K') \
                .replace('G', ' G') \
                .replace('T', ' T')
