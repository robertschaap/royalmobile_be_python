from utils.stubs import get_products_stub

class ProductModel:
    def get_product(self, product_id):
        products_stub = get_products_stub() or []
        product = [x for x in products_stub if x["modelId"] == product_id]

        if len(product) != 0:
            return product[0]

        raise ValueError("Product could not be found")
