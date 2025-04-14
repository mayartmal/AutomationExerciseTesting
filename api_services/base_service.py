from dataclasses import dataclass
from http import HTTPStatus
from typing import Any

from api_services.http_wrapper import HTTPWrapper
from constants.urls.endpoints import Endpoints
from models.common import RequestParameters


class BaseService(HTTPWrapper):
    """
    A base class for API services that extends HTTPWrapper with predefined settings
    """

    def __init__(self):
        super().__init__(base_url=Endpoints.BASE_URL)
        self.expected_code = None

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
        self.expected_code = self.http_status.NOT_FOUND
        return self

        # yield self
        # self.expected_code = None

    def bad_request(self):
        #
        pass

    def default(self):
        self.expected_code = None
        return self


