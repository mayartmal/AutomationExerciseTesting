import json
import os
from dataclasses import asdict

from constants.test import TEST_MAIL_DOMAIN, TEST_USER_BASE_NAME
from models.common import User, Credentials, Email, CredentialsWithUpdates
from utils.data_generator import generate_user_name_with_time_postfix


class UserFactory:
    users_db_path = "../test_db/users.json"

    @staticmethod
    def generate_create_user_payload() -> User:
       user_name = generate_user_name_with_time_postfix(TEST_USER_BASE_NAME)
       email = f"{user_name}{TEST_MAIL_DOMAIN}"
       user = User(name=user_name, email=email)
       UserFactory.save_user_to_db(user=user)
       return user

    @staticmethod
    def get_latest_user_credentials_payload() -> Credentials:
        return Credentials(email=UserFactory.get_latest_user_from_db().email,
                           password=UserFactory.get_latest_user_from_db().password)

    @staticmethod
    def get_latest_user_email_payload() -> Email:
        return Email(email=UserFactory.get_latest_user_from_db().email)

    @staticmethod
    def get_latest_user_credentials_with_updated_fields_payload(field_to_update: str, field_new_value: str) -> CredentialsWithUpdates:
        user = UserFactory.get_latest_user_from_db()
        setattr(user, field_to_update, field_new_value)
        UserFactory.save_user_to_db(user)
        return CredentialsWithUpdates(
            email=user.email,
            password=user.password,
            dynamic_field=(field_to_update, field_new_value)
        )

    @staticmethod
    def get_latest_user_from_db() -> User:
        with open(UserFactory.users_db_path, "r") as file:
            return User(**json.load(file)[-1])

    @staticmethod
    def save_user_to_db(user: User):
        with open(UserFactory.users_db_path, "r") as file:
            users = json.load(file)
        users.append(asdict(user))
        with open(UserFactory.users_db_path, "w") as file:
            json.dump((users), file, indent=4)




