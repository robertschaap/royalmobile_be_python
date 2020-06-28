from utils.stubs import get_products_stub

class ProductModel:
    def get_product(self, product_id):
        products_stub = get_products_stub()
        product = [x for x in products_stub if x["modelId"] == product_id][0]

        return product
