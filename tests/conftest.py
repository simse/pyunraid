import pytest

@pytest.fixture
def mock_unraid():
    import requests_mock

    with requests_mock.Mocker() as m:
        m.get(
            "http://192.168.0.4/Main",
            status_code=200,
            reason='OK',
            headers={},
            text=open('tests/responses/main.html', 'r').read()
        )

        return True
