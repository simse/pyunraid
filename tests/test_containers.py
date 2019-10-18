import requests
import pytest
from pyunraid import Unraid



def test_containers(requests_mock):
    requests_mock.get("http://192.168.1.4/Main", text=open('tests/responses/main.html', 'r').read())
    requests_mock.get("http://192.168.1.4/plugins/dynamix.docker.manager/include/DockerContainers.php", text=open('tests/responses/docker.html', 'r').read())

    unraid = Unraid('http://192.168.1.4', '', '')
    containers = unraid.containers()
    c = containers[0]

    assert len(containers) > 0
    assert c.name == 'bazarr'
    assert c.state == 'started'
    assert c.id == '40f9eb1e719d'
    assert c.network == 'bridge'
    assert c.update_status == 'UP_TO_DATE'
    assert c.tag == 'latest'
    assert c.port_mappings == [[6767]]
    assert c.path_mappings == [['/config', '/mnt/user/appdata/bazarr'], ['/movies', '/mnt/user/Proton/Movies/'], ['/tv', '/mnt/user/Proton/TV Series/']]
    assert c.startup_delay == 0
    assert c.uptime == 72
    assert c.age == 72
