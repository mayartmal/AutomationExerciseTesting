from http.client import responses
from constants.test import MAIL
from datetime import datetime

import pytest
import requests


def test_api_works():
    url = "https://automationexercise.com/api/productsList"
    response = requests.get(url)
    assert response.status_code == 200


def test_get_user_account_detail_by_email():
    url = "https://automationexercise.com/api/getUserDetailByEmail"
    params = {"email": MAIL}
    response = requests.get(url=url, params=params)
    print(response.status_code)
    print(response.json())


def test_create_check_and_delete_user():
    # API11
    now = datetime.now()
    user = "user" + now.strftime("%d%m%Y%H%M%S")
    email = user + "@host.on"
    url = "https://automationexercise.com/api/createAccount"
    params = {
        "name": user,
        "email": email,
        "password": "12345678",
        "title": "Mr",
        "birth_date": "3",
        "birth_month": "2",
        "birth_year": "1990",
        "firstname": "John",
        "lastname": "Smitty",
        "company": "APEX",
        "address1": "owl st. 11",
        "address2": "far st. 27",
        "country": "India",
        "zipcode": "0111",
        "state": "ND",
        "city": "ND",
        "mobile_number":"555 111 333"
    }
    response = requests.post(url=url, data=params)
    print(response.cookies)
    print(response.json())
    assert response.json().get("responseCode") == 201
    # API7
    url = "https://automationexercise.com/api/verifyLogin"
    params = {
        "email": email,
        "password": "12345678"

    }
    response = requests.post(url=url, data=params)
    print(response.cookies)
    print(response.json())
    assert response.json().get("responseCode") == 200
    # API12
    url = "https://automationexercise.com/api/deleteAccount"
    params = {
        "email": email,
        "password": "12345678"

    }
    response = requests.delete(url=url, data=params)
    print(response.cookies)
    print(response.json())
    assert response.json().get("responseCode") == 200
    # API7
    url = "https://automationexercise.com/api/verifyLogin"
    params = {
        "email": email,
        "password": "12345678"

    }
    response = requests.post(url=url, data=params)
    print(response.cookies)
    print(response.json())
    assert response.json().get("responseCode") != 200

def test_create_details_update_and_delete_user():
    # API11
    now = datetime.now()
    user = "user" + now.strftime("%d%m%Y%H%M%S")
    email = user + "@host.on"
    url = "https://automationexercise.com/api/createAccount"
    user_params = {
        "name": user,
        "email": email,
        "password": "12345678",
        "title": "Mr",
        "birth_date": "3",
        "birth_month": "2",
        "birth_year": "1990",
        "firstname": "John",
        "lastname": "Smitty",
        "company": "APEX",
        "address1": "owl st. 11",
        "address2": "far st. 27",
        "country": "India",
        "zipcode": "0111",
        "state": "ND",
        "city": "ND",
        "mobile_number": "555 111 333"
    }
    response = requests.post(url=url, data=user_params)
    assert response.json().get("responseCode") == 201

    # API7
    url = "https://automationexercise.com/api/verifyLogin"
    params = {
        "email": email,
        "password": "12345678"

    }
    response = requests.post(url=url, data=params)
    assert response.json().get("responseCode") == 200

    # API 14
    url = "https://automationexercise.com/api/getUserDetailByEmail"
    params = {
        "email": email
    }
    response = requests.get(url=url, params=params)
    assert response.json().get("user").get("first_name") == user_params.get("firstname")
    assert response.json().get("responseCode") == 200

    # API 13
    url = "https://automationexercise.com/api/updateAccount"
    updated_params = {
        "email": email,
        "password": "12345678",
        "firstname": "Simon"
    }
    response = requests.put(url=url, data=updated_params)
    assert response.json().get("responseCode") == 200

    # API 14
    url = "https://automationexercise.com/api/getUserDetailByEmail"
    params = {
        "email": email
    }
    response = requests.get(url=url, params=params)
    assert response.json().get("user").get("first_name") == updated_params.get("firstname")
    assert response.json().get("responseCode") == 200

    # API12
    url = "https://automationexercise.com/api/deleteAccount"
    params = {
        "email": email,
        "password": "12345678"

    }
    response = requests.delete(url=url, data=params)
    print(response.cookies)
    print(response.json())
    assert response.json().get("responseCode") == 200
    # API7
    url = "https://automationexercise.com/api/verifyLogin"
    params = {
        "email": email,
        "password": "12345678"

    }
    response = requests.post(url=url, data=params)
    print(response.cookies)
    print(response.json())
    assert response.json().get("responseCode") != 200












































def test_new():
    session = requests.session()
    response =  session.get()
    session.cookies = response.cookies



