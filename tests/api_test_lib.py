import pytest

from constants.test import ExpectedCodes, ExpectedMessages
from factory.user_factory import UserFactory



def test_create_user(log_test_start_and_end, create_and_clean_up_user):
    # Given: a user does not exist yet

    # When: we create the user
    response, _ = create_and_clean_up_user

    # Then: the response message should indicate the user was successfully created
    assert response.message == ExpectedMessages.USER_CREATED


def test_verify_user(log_test_start_and_end, create_and_clean_up_user, user_service):
    # Given: a user has been successfully created
    _, user = create_and_clean_up_user

    # When: we verify the user via the user service
    response = user_service.verify_user(user=user)

    # Then: the response should indicate the user exists
    assert response.responseCode == ExpectedCodes.OK
    assert response.message == ExpectedMessages.USER_EXIST


def test_get_user_details(log_test_start_and_end, create_and_clean_up_user, user_service):
    # Given: a newly created user with known public details
    _, user = create_and_clean_up_user
    expected_user_details = UserFactory.extract_public_data_set_from_user_object(user)

    # When: requesting user details from the service
    response = user_service.get_user_details(user=user)
    actual_user_details = UserFactory.extract_public_data_set_from_user_data_object(user_data=response.user)

    # Then: the returned user details should match the expected ones
    assert expected_user_details == actual_user_details


@pytest.mark.parametrize("update_user_data", [["company", "new_work"]], indirect=True)
def test_update_user_data(log_test_start_and_end, update_user_data, user_service):
    # Given: a previously created user has been updated
    _, user = update_user_data

    # When: requesting user details from the service
    response = user_service.get_user_details(user=user)

    # Then: the returned user details should match the expected ones
    assert response.user.company == "new_work"
