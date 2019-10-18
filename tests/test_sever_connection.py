import requests
import pytest
from pyunraid import Unraid



def test_server_connection(requests_mock):
    requests_mock.get("http://192.168.1.4/Main", text=open('tests/responses/main.html', 'r').read())

    USERNAME = 'root'
    PASSWORD = 'password'

    unraid = Unraid('http://192.168.1.4', USERNAME, PASSWORD)

    assert unraid.version == "6.7.2"
    assert unraid.name == "Proton"
    assert unraid.url == "http://192.168.1.4"
    assert unraid.description == "Simse's server"
    assert unraid.license == "Plus"
