from dataclasses import dataclass
from http import HTTPStatus
from typing import Any, Optional

from api_services.http_wrapper import HTTPWrapper
from constants.urls.endpoints import Endpoints
from models.common import RequestParameters


class BaseService(HTTPWrapper):
    """
    A base class for API services that extends HTTPWrapper with predefined settings
    """

    def __init__(self):
        super().__init__(base_url=Endpoints.BASE_URL)
        # self.expected_status_code = None
        # self.method = None

    def build_request(self,
                      endpoint: str,
                      payload: Any,
                      expected_code: HTTPStatus,
                      decode_to: dataclass,
                      deserialize: bool = True):
        self.request_parameters = RequestParameters(endpoint=endpoint,
                                                    payload=payload,
                                                    expected_code=expected_code,
                                                    deserialize_to=decode_to,
                                                    deserialize=deserialize)
        return self

    def not_found(self):
        self.expected_status_code = self.http_status.NOT_FOUND
        return self


    def bad_request(self):
        #
        pass

    def default(self):
        self.expected_status_code = None
        return self

    def override_method_to(self, method: str):
        self.method = method
        return self

    def reset_method(self):
        self.method = None
        return self

    def no_deserialize(self):
        self.deserialize = False
        return self
    def reset_no_deserialize(self):
        self.deserialize = True
        return False

    def override_deserialization_to(self, class_name: dataclass):
        self.deserialize_to = class_name
        return self

    def reset_deserialization_to(self):
        self.deserialize_to = None
        return self



