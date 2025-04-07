import requests


def test_api_works():
    url = "https://automationexercise.com/api/productsList"
    response = requests.get(url)
    assert response.status_code == 200

#  create and delete user in fixture (with yield)

def test_create_verify_and_delete_user(user_service):
    response, user = user_service.create_user()
    user_service.verify_user()
    user_service.delete_user()
    user_service.verify_user()
    # user_service.not_found().verify_user()


def test_create_details_update_and_delete_user(user_service):
    user_service.create_user()
    user_service.verify_user()
    user_service.get_user_details()
    user_service.update_user_details(field_to_update="firstname",
                                     field_new_value="Simon")
    user_service.get_user_details()
    user_service.delete_user()
