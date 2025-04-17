

from api_services.base_service import BaseService
from constants.urls.endpoints import Endpoints
from models.common import GeneralResponse, BrandsResponse


class BrandService(BaseService):

    def __init__(self):
        super().__init__()

    def get_brands(self):
        return self.build_request(endpoint=Endpoints.BRAND_GET_LIST,
                                  payload=None,
                                  expected_code=self.http_status.OK,
                                  decode_to=BrandsResponse).get().response_decoded

