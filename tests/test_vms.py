import requests
import pytest
from pyunraid import Unraid



def test_server_connection(requests_mock):
    requests_mock.get("http://192.168.1.4/Main", text=open('tests/responses/main.html', 'r').read())
    requests_mock.get("http://192.168.1.4/plugins/dynamix.docker.manager/include/DockerContainers.php", text=open('tests/responses/docker.html', 'r').read())

    unraid = Unraid('http://192.168.1.4', '', '')
    containers = unraid.containers()

    assert len(containers) > 0
