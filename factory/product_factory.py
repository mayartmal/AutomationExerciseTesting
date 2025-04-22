from models.common import SearchProduct


class ProductFactory:

    @staticmethod
    def search_product_payload(search_string: str):
        return SearchProduct(
            search_product=search_string
        )