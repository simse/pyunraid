import requests
import pytest
from pyunraid import Unraid

def test_server_connection(mock_unraid):


    unraid = Unraid('http://192.168.0.4', 'root', 'hotfla123As')

    assert unraid.version == "6.7.2"
