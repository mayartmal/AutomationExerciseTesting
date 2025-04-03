from dataclasses import dataclass
from http.client import responses
from typing import Any

import requests

from utils.data_generator import generate_current_datetime_string
from constants.urls.endpoints import Endpoints
from utils.factories import User, UniversalResponseData


class UserService:

    def create_user(self):
        user = User.generate()
        response = requests.post(url=Endpoints.BASE_URL + Endpoints.USER_CREATE_ACCOUNT, data=user.__dict__)
        response_data = UniversalResponseData.build(user, response)
        return response_data

    def delete_user(self, user):
        response = requests.delete(url=Endpoints.BASE_URL + Endpoints.USER_DELETE, data=user.credentials())
        response_data = UniversalResponseData.build(user, response)
        return response_data

    def verify_user(self, user):
        response = requests.get(url=Endpoints.BASE_URL + Endpoints.USER_GET_DETAILS, params=user.mail())
        response_data = UniversalResponseData.build(user, response)
        return response_data

    def get_user_details(self, user):
        response = requests.get(url=Endpoints.BASE_URL + Endpoints.USER_GET_DETAILS, params=user.mail())
        response_data = UniversalResponseData.build(user, response)
        return response_data

    def update_user_details(self, user, field_to_update, field_new_value):
        credentials = user.credentials()
        credentials[field_to_update] = field_new_value
        data = credentials
        response = requests.put(url=Endpoints.BASE_URL + Endpoints.USER_UPDATE_DETAILS, data=data)
        response_data = UniversalResponseData.build(user, response)
        return response_data