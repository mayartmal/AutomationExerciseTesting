import pytest

from constants.test import ExpectedCodes, ExpectedMessages, BrandRelated
from models.common import GeneralResponse
from tests.conftest import brand_service


class TestBrandAPI:

    def test_get_all_brands(self, brand_service):
        response = brand_service.get_all_brands()
        assert len(response.brands) > 0
        for brand in response.brands:
            assert isinstance(brand.id, int)
            assert brand.brand
            assert isinstance(brand.brand, str)

    @pytest.mark.parametrize("run_service_with_overridden_method",
                             BrandRelated.WRONG_METHODS_FOR_GET_ALL_BRANDS,
                             indirect=True)
    def test_get_all_brand_with_wrong_methods(self, run_service_with_overridden_method):
        brand_service = run_service_with_overridden_method
        response = brand_service.override_deserialization_to(GeneralResponse).get_all_brands()
        brand_service.reset_deserialization()
        assert response.responseCode == ExpectedCodes.UNSUPPORTED_METHOD
        assert response.message == ExpectedMessages.UNSUPPORTED_METHOD
