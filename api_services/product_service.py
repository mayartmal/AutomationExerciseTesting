from api_services.base_service import BaseService
from constants.urls.endpoints import Endpoints
from factory.product_factory import ProductFactory
from models.common import GeneralResponse, ProductsResponse


class ProductService(BaseService):

    def __init__(self):
        super().__init__()
        self.factory = ProductFactory

    def get_all_products(self):
        return self.build_request(endpoint=Endpoints.PRODUCT_GET_LIST,
                                  payload=None,
                                  expected_code=self.http_status.OK,
                                  deserialize_to=ProductsResponse,
                                  deserialize=True).get().response_decoded

    def search_product(self, search_string: str):
        return self.build_request(endpoint=Endpoints.PRODUCT_SEARCH,
                                  payload=self.factory.search_product_payload(search_string=search_string),
                                  expected_code=self.http_status.OK,
                                  deserialize_to=ProductsResponse,
                                  deserialize=True).post().response_decoded
