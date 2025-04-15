from api_services.base_service import BaseService
from constants.urls.endpoints import Endpoints
from factory.user_factory import UserFactory
from models.common import GeneralResponse, UserDataResponse, User


class UserService(BaseService):

    def __init__(self):
        super().__init__()
        self.factory = UserFactory()

    def create_user(self):
        payload = self.factory.generate_create_user_payload()
        response = self.build_request(endpoint=Endpoints.USER_CREATE_ACCOUNT,
                                      payload=payload,
                                      expected_code=self.http_status.OK,
                                      decode_to=GeneralResponse).post().response_decoded
        return response, payload

    def verify_user(self, user: User, overridden_password: str = None, delete_password=False, method: str = "post"):
        if delete_password:
            payload = self.factory.extract_user_email_payload(user=user)
        else:
            payload=self.factory.extract_user_credentials_payload(user=user, overridden_password=overridden_password)

        request = self.build_request(endpoint=Endpoints.USER_VERIFY,
                                      payload=payload,
                                      expected_code=self.http_status.OK,
                                      decode_to=GeneralResponse)
        response = getattr(request, method)()
        return response.response_decoded

        # return self.build_request(endpoint=Endpoints.USER_VERIFY,
        #                           payload=payload,
        #                           expected_code=self.http_status.OK,
        #                           decode_to=GeneralResponse).post().response_decoded

    def delete_user(self, user: User):
        return self.build_request(endpoint=Endpoints.USER_DELETE,
                                  payload=self.factory.extract_user_credentials_payload(user=user),
                                  expected_code=self.http_status.OK,
                                  decode_to=GeneralResponse,
                                  deserialize=False).delete().response_decoded

    def get_user_details(self, user: User):
        return self.build_request(endpoint=Endpoints.USER_GET_DETAILS,
                                  payload=self.factory.extract_user_email_payload(user=user),
                                  expected_code=self.http_status.OK,
                                  decode_to=UserDataResponse).get().response_decoded

    def update_user_details(self, user: User, field_to_update: str, field_new_value: str):
        return self.build_request(endpoint=Endpoints.USER_UPDATE_DETAILS,
                                  payload=self.factory.update_user_payload(
                                      user=user,
                                      field_to_update=field_to_update,
                                      field_new_value=field_new_value),
                                  expected_code=self.http_status.OK,
                                  decode_to=GeneralResponse).put().response_decoded
