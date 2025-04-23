from http.client import responses
from typing import cast

import pytest

from api_services.brand_service import BrandService
from constants.test import ExpectedCodes, ExpectedMessages
from models.common import GeneralResponse
from tests.conftest import brand_service


class TestBrandAPI:

    def test_get_all_brands(self, brand_service):
        # Given: the brand service is initialized and ready to use

        # When: we request all available brands
        response = brand_service.get_all_brands()

        # Then: we should receive a non-empty list of valid brand objects
        assert len(response.brands) > 0
        for brand in response.brands:
            assert isinstance(brand.id, int)
            assert brand.brand
            assert isinstance(brand.brand, str)


    @pytest.mark.parametrize("run_service_with_overridden_method", [
        {"service_class": BrandService, "method": "POST"},
        {"service_class": BrandService, "method": "PUT"},
        {"service_class": BrandService, "method": "DELETE"}
        ], indirect=True)
    def test_get_all_brand_with_wrong_methods(self, run_service_with_overridden_method):
        brand_service = run_service_with_overridden_method
        response = brand_service.override_deserialization_to(GeneralResponse).get_all_brands()
        brand_service.reset_deserialization()
        assert response.responseCode == ExpectedCodes.UNSUPPORTED_METHOD
        assert response.message == ExpectedMessages.UNSUPPORTED_METHOD



        # response = brand_service.override_deserialization_to(
        #     GeneralResponse).get_all_brands()
        # brand_service.reset_deserialization()
        # assert response.responseCode == ExpectedCodes.UNSUPPORTED_METHOD
        # assert response.message == ExpectedMessages.UNSUPPORTED_METHOD

