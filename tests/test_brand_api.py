from constants.test import ExpectedCodes, ExpectedMessages
from models.common import GeneralResponse


class TestBrandAPI:

    def test_get_all_brands(self, brand_service):
        # Given: the brand service is initialized and ready to use

        # When: we request all available brands
        response = brand_service.get_brands()

        # Then: we should receive a non-empty list of valid brand objects
        assert len(response.brands) > 0
        for brand in response.brands:
            assert isinstance(brand.id, int)
            assert brand.brand
            assert isinstance(brand.brand, str)


    def test_get_all_brand_with_wrong_method(self, brand_service):
        response = brand_service.override_method_to("POST").override_deserialization_to(GeneralResponse).get_brands()
        brand_service.reset_deserialization_to()
        assert response.responseCode == ExpectedCodes.UNSUPPORTED_METHOD
        assert response.message == ExpectedMessages.UNSUPPORTED_METHOD

