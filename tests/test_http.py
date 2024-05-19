import requests
import pytest


@pytest.mark.http
def test_first_request():
    url = 'https://api.github.com/zen'
    response = requests.get(url=url)

    print("The message is: {}".format(response.text))


@pytest.mark.http
def test_second_request():
    url = 'https://api.github.com/users/defunkt'
    response = requests.get(url=url)
    headers = response.headers.get('Server')
    name = response.json()['name']

    expected_name = 'Chris Wanstrath'
    expected_server_name = 'GitHub.com'

    assert response.status_code == 200 and name == expected_name and headers == expected_server_name


@pytest.mark.http
def test_status_code_request():
    url = 'https://api.github.com/users/sergii_butenko'
    response = requests.get(url=url)

    assert response.status_code == 404
