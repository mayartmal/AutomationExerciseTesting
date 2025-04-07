from constants.urls.endpoints import Endpoints
from api_services.http_wrapper import HTTPWrapper
from typing import Any
from http import HTTPStatus
from models.common import RequestParameters


class BaseService(HTTPWrapper):
    """
    A base class for API services that extends HTTPClient with predefined settings
    """
    def __init__(self):
        super().__init__(base_url=Endpoints.BASE_URL)

    def build_request(self,
                      endpoint: str,
                      payload: Any,
                      expected_code: HTTPStatus):
        self.request_parameters = RequestParameters(endpoint=endpoint,
                                                    payload=payload,
                                                    expected_code=expected_code)

        # print(self.request_parameters)
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

