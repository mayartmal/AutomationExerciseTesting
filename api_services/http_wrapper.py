from dataclasses import dataclass
from http import HTTPStatus
from typing import Any

import requests
from requests import Response

from models.common import RequestParameters


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
        """
        Sends an HTTP request using the specified method and current request parameters

        :param method: str - an HTTP method to use for request ('GET', 'POST'...)
        :return: HTTPWrapper - The instance of HTTPWrapper for method chaining.

        """
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
        return self.send_request(method="POST")

    def delete(self):
        return self.send_request(method="DELETE")

    def get(self):
        return self.send_request(method="GET")

    def put(self):
        return self.send_request(method="PUT")

    def assert_status_code(self, expected_status_code: HTTPStatus):
        assert self.response_not_decoded.status_code == expected_status_code

    def decoder(self, target_data_class: dataclass):
        self.response_decoded = target_data_class(**self.response_not_decoded.json())
