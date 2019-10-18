import requests
import pytest
from pyunraid import Unraid



def test_server_connection(requests_mock):
    requests_mock.get("http://192.168.0.4/Main", text=open('tests/responses/main.html', 'r').read())

    unraid = Unraid('http://192.168.0.4', 'root', 'hotfla123As')

    assert unraid.version == "6.7.2"
