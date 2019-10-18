import requests
import pytest
from pyunraid import Unraid



def test_vms(requests_mock):
    requests_mock.get("http://192.168.1.4/Main", text=open('tests/responses/main.html', 'r').read())
    requests_mock.get("http://192.168.1.4/plugins/dynamix.vm.manager/include/VMMachines.php", text=open('tests/responses/vm.html', 'r').read())

    unraid = Unraid('http://192.168.1.4', '', '')
    vms = unraid.vms()

    assert len(vms) > 0
    assert vms[0].name == "CapRover"
    assert vms[0].memory == 2048000000
    assert vms[0].cpu_count == 4
    assert vms[0].description == "A CapRover VM"
    assert vms[0].autostart == True
    assert vms[0].state == "started"
    assert vms[0].vnc_port == '5900'
    assert vms[0].vdisks == [{'allocation': 49000000000, 'bus': 'VirtIO', 'capacity': 50000000000, 'path': '/mnt/user/domains/CapRover/vdisk1.img'}]
