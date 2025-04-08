from api_services.base_service import BaseService
from constants.urls.endpoints import Endpoints
from factory.user_factory import UserFactory
from models.common import GeneralResponse, UserDataResponse


class UserService(BaseService):

    def __init__(self):
        super().__init__()
        self.factory = UserFactory()

    def create_user(self):
        payload = self.factory.generate_create_user_payload()

        response = self.build_request(endpoint=Endpoints.USER_CREATE_ACCOUNT,
                                    payload=payload,
                                    expected_code=self.http_status.OK,
                                    decode_to=GeneralResponse).post().response_json

        return response, payload


    def verify_user(self):
        return self.build_request(endpoint=Endpoints.USER_VERIFY,
                                  payload=self.factory.get_latest_user_credentials_payload(),
                                  expected_code=self.http_status.OK,
                                  decode_to=GeneralResponse).post().response_json

    def delete_user(self):
        return self.build_request(endpoint=Endpoints.USER_DELETE,
                                  payload=self.factory.get_latest_user_credentials_payload(),
                                  expected_code=self.http_status.OK,
                                  decode_to=GeneralResponse).delete().response_json

    def get_user_details(self):



        result =  self.build_request(endpoint=Endpoints.USER_GET_DETAILS,
                                  payload=self.factory.get_latest_user_email_payload(),
                                  expected_code=self.http_status.OK,
                                  decode_to=UserDataResponse).get().response_decoded

        return result

    def update_user_details(self, field_to_update, field_new_value):
        return self.build_request(endpoint=Endpoints.USER_UPDATE_DETAILS,
                                  payload=self.factory.get_latest_user_credentials_with_updated_fields_payload(
                                      field_to_update=field_to_update,
                                      field_new_value=field_new_value),
                                  expected_code=self.http_status.OK,
                                  decode_to=GeneralResponse).put().response_json

        # credentials = user.credentials()
        # credentials[field_to_update] = field_new_value
        # data = credentials
        # response = requests.put(url=Endpoints.BASE_URL + Endpoints.USER_UPDATE_DETAILS, data=data)
        # response_data = UniversalResponseData.build(user, response)

