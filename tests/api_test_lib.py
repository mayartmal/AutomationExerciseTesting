from http.client import responses
from constants.test import MAIL

import pytest
import requests

@pytest.mark.api
def test_api_works():
    url = "https://automationexercise.com/api/productsList"
    response = requests.get(url)
    assert response.status_code == 200


@pytest.mark.api
def test_get_user_account_detail_by_email():
    url = "https://automationexercise.com/api/getUserDetailByEmail"
    params = {"email": MAIL}
    response = requests.get(url=url, params=params)
    print(response.status_code)
    print(response.json())
