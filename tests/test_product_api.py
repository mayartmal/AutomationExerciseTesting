from constants.test import ExpectedCodes, ExpectedMessages
from models.common import Category, UserType, GeneralResponse


class TestProductAPI:

    def test_get_all_products(self, product_service):
        # Given

        # When
        response = product_service.get_all_products()

        # Then
        assert len(response.products) > 0
        for product in response.products:
            assert isinstance(product.id, int)
            assert isinstance(product.category, Category)
            assert isinstance(product.category.usertype, UserType)

    def test_get_all_products_with_wrong_method(self, product_service):
        # Given

        # When
        response = product_service.override_method_to("POST").override_deserialization_to(GeneralResponse).get_all_products()
        product_service.reset_deserialization()

        # Then
        assert response.responseCode == ExpectedCodes.UNSUPPORTED_METHOD
        assert response.message == ExpectedMessages.UNSUPPORTED_METHOD

    def test_search_product(self, product_service):
        # Given
        # The product service is available

        # When
        response = product_service.search_product(search_string="tshirt")

        # Then
        assert len(response.products) > 0
        for product in response.products:
            assert "tshirt" in product.category.category.lower()

    def test_search_product_without_search_parameter(self, product_service):

        response = product_service.override_payload_with_none().override_deserialization_to(GeneralResponse).search_product(search_string="tshirt")
        product_service.reset_none_payload().reset_deserialization()

        assert response.responseCode == ExpectedCodes.BAD_REQUEST
        assert response.message == ExpectedMessages.MISSING_SEARCH_PARAMETER