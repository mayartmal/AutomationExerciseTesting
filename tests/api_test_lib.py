from http.client import responses
from constants.test import MAIL

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


def test_create_verify_and_delete_user(user_service):
    create_user_response = user_service.create_user()
    assert create_user_response.code == 201
    verify_user_response = user_service.verify_user(user=create_user_response.user)
    assert verify_user_response.code == 200
    delete_user_response = user_service.delete_user(user=verify_user_response.user)
    assert delete_user_response.code == 200
    verify_user_response = user_service.verify_user(user=delete_user_response.user)
    assert verify_user_response.code == 404

def test_create_details_update_and_delete_user(user_service):
    create_user_response = user_service.create_user()
    assert create_user_response.code == 201
    verify_user_response = user_service.verify_user(user=create_user_response.user)
    assert verify_user_response.code == 200
    user_details_response = user_service.get_user_details(user=verify_user_response.user)
    actual_result = user_details_response.raw_response.get("user").get("first_name")
    assert user_details_response.code == 200
    assert actual_result == "John"
    update_user_response = user_service.update_user_details(user_details_response.user,
                                                            field_to_update="firstname",
                                                            field_new_value="Simon")
    user_details_response = user_service.get_user_details(user=update_user_response.user)
    actual_result = user_details_response.raw_response.get("user").get("first_name")
    assert user_details_response.code == 200
    assert actual_result == "Simon"
    delete_user_response = user_service.delete_user(user_details_response.user)
    assert delete_user_response.code == 200
    verify_user_response = user_service.verify_user(user=delete_user_response.user)
    assert verify_user_response.code == 404





# def test_new():
#     session = requests.session()
#     response =  session.get()
#     session.cookies = response.cookies



