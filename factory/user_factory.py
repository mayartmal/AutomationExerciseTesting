from constants.test import UserRelated
from models.common import User, Credentials, Email, CredentialsWithUpdates, UserData
from utils.data_generator import generate_user_name_with_time_postfix


class UserFactory:

    @staticmethod
    def generate_create_user_payload() -> User:
        user_name = generate_user_name_with_time_postfix(UserRelated.TEST_USER_BASE_NAME)
        email = f"{user_name}{UserRelated.TEST_MAIL_DOMAIN}"
        user = User(name=user_name, email=email)
        return user

    @staticmethod
    def extract_user_credentials_payload(user: User, overridden_password: str = None):
        if overridden_password:
            return Credentials(email=user.email, password=overridden_password)
        else:
            return Credentials(email=user.email, password=user.password)

    @staticmethod
    def extract_user_email_payload(user: User):
        return Email(email=user.email)

    @staticmethod
    def extract_public_data_set_from_user_object(user: User) -> set[str]:
        user.__dict__.pop("password")
        user.__dict__.pop("mobile_number")
        return set(user.__dict__.values())

    @staticmethod
    def extract_public_data_set_from_user_data_object(user_data: UserData):
        user_data.__dict__.pop("id")
        return set(user_data.__dict__.values())

    @staticmethod
    def update_user_payload(user: User,
                            field_to_update: str,
                            field_new_value: str) -> CredentialsWithUpdates:
        setattr(user, field_to_update, field_new_value)
        return CredentialsWithUpdates(
            email=user.email,
            password=user.password,
            dynamic_field=(field_to_update, field_new_value)
        )

