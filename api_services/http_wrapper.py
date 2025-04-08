import json
import pickle
from dataclasses import fields, dataclass
from http.client import responses
from typing import Any

import requests
from http import HTTPStatus
from models.common import RequestParameters, GeneralResponse
from requests import Response


class HTTPWrapper:
    """
    An HTTP client for sending and managing responses
    """

    http_status = HTTPStatus

    def __init__(self, base_url: str = None):
        self.BASE_URL = base_url
        self.session = requests.Session()
        self.request_parameters: RequestParameters = None
        self.response_not_decoded: Response = None
        self.response_decoded: Any = None
        self.response_json = None
        self.expected_status_code = None

    def send_request(self, method: str):
        url = f"{self.BASE_URL}{self.request_parameters.endpoint}"
        self.response_not_decoded = self.session.request(
                                        method=method,
                                        url=url,
                                        params=self.request_parameters.payload.__dict__ if method == "GET" else None,
                                        data=self.request_parameters.payload.__dict__ if method != "GET" else None)
        self.response_json = self.response_not_decoded.json()
        self.decoder(self.request_parameters.decode_to)
        self.assert_status_code(
            expected_status_code=self.expected_status_code if self.expected_status_code else self.request_parameters.expected_code)
        return self

    def post(self):
        return self.send_request(method = "POST")

    def delete(self):
        return self.send_request(method="DELETE")

    def get(self):
        return self.send_request(method="GET")

    def put(self):
        return self.send_request(method="PUT")

    def assert_status_code(self, expected_status_code):
        assert self.response_not_decoded.status_code == expected_status_code

    def decoder(self, target_data_class: dataclass):
        self.response_decoded = target_data_class(**self.response_not_decoded.json())

    # def decoder(self, target_data_class: dataclass):
    #     step1 = target_data_class(**self.response_not_decoded.json())
    #     step1.user(**step1.get("user"))
    #
    #     self.response_decoded = target_data_class(**self.response_not_decoded.json())
