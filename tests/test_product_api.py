from pickle import FALSE

import pytest

from constants.test import ExpectedCodes, ExpectedMessages, ProductRelated
from models.common import Category, UserType, GeneralResponse


class TestProductAPI:

    def test_get_all_products(self, product_service):
        response = product_service.get_all_products()
        assert len(response.products) > 0
        for product in response.products:
            assert isinstance(product.id, int)
            assert isinstance(product.category, Category)
            assert isinstance(product.category.usertype, UserType)

    @pytest.mark.parametrize("run_service_with_overridden_method",
                             ProductRelated.WRONG_METHODS_FOR_GET_ALL_PRODUCTS,
                             indirect=True)
    def test_get_all_products_with_wrong_method(self, run_service_with_overridden_method):
        product_service = run_service_with_overridden_method
        response = product_service.override_deserialization_to(GeneralResponse).get_all_products()
        product_service.reset_deserialization()
        assert response.responseCode == ExpectedCodes.UNSUPPORTED_METHOD
        assert response.message == ExpectedMessages.UNSUPPORTED_METHOD

    @pytest.mark.parametrize("product_searching", ProductRelated.TSHIRT_STRINGS_IN_DIFFERENT_CASES, indirect=True)
    def test_search_product(self, product_searching):
        response, input_param = product_searching
        assert len(response.products) > 0
        for product in response.products:
            assert input_param.lower() in product.category.category.lower()


    def test_search_product_without_search_parameter(self, product_service):
        response = product_service.override_payload_with_none().override_deserialization_to(
            GeneralResponse).search_product(search_string="tshirt")
        product_service.reset_none_payload().reset_deserialization()
        assert response.responseCode == ExpectedCodes.BAD_REQUEST
        assert response.message == ExpectedMessages.MISSING_SEARCH_PARAMETER
