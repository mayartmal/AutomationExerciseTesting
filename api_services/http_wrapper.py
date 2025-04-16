import json
import logging
from dataclasses import dataclass
from http import HTTPStatus
from typing import Union, Optional

import requests
from requests import Response

from models.common import RequestParameters, GeneralResponse, UserDataResponse
from utils.logger_config import get_logger


logger = get_logger(__name__)

class HTTPWrapper:
    """
    An HTTP client for sending and managing responses
    """

    http_status = HTTPStatus

    def __init__(self, base_url: str = None):
        self.BASE_URL = base_url
        self.session = requests.Session()
        self.request_parameters: RequestParameters = None
        self.response_not_decoded: Optional[Response] = None
        self.response_decoded: Optional[Union[GeneralResponse, UserDataResponse]] = None
        self.expected_status_code = None
        self.deserialize: bool = True
        # self.password = None
        self.method: Optional[str] = None

    def send_request(self, method: str):
        """
        Sends an HTTP request using the specified method and current request parameters

        :param method: str - an HTTP method to use for request ('GET', 'POST'...)
        :return: HTTPWrapper - The instance of HTTPWrapper for method chaining.

        """
        url = f"{self.BASE_URL}{self.request_parameters.endpoint}"
        payload = self.request_parameters.payload
        # region request logging
        logger.debug(f"---- Sending {method.upper()} request to {url} ----")
        logger.debug(f"Payload dataclass is {type(payload)}")
        logger.debug(f"Payload\n{json.dumps(payload.__dict__, indent=2)}")
        # endregion
        self.response_not_decoded = self.session.request(
            method=self.method if self.method else method,
            # method=method,
            url=url,
            params=payload.__dict__ if method == "GET" else None,
            data=payload.__dict__ if method != "GET" else None)
        if self.request_parameters.deserialize and self.deserialize:
            self.deserialize_response(self.request_parameters.deserialize_to)
        else:
            self.response_decoded = self.response_not_decoded
        self.assert_status_code(
            expected_status_code=self.expected_status_code if self.expected_status_code else self.request_parameters.expected_code)
        # region response logging
        logger.debug(f"---- Receiving response ----")
        logger.debug(f"Raw response is: {self.response_not_decoded}")
        logger.debug(f"Response body is: \n{json.dumps(self.response_not_decoded.json(), indent=2)}")
        # endregion

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
        logger.debug(f"ASSERTION {self.response_not_decoded.status_code} vs {expected_status_code}")
        assert self.response_not_decoded.status_code == expected_status_code

    def deserialize_response(self, target_data_class: dataclass):
        self.response_decoded = target_data_class(**self.response_not_decoded.json())
