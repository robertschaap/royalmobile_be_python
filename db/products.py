from utils.stubs import get_products_stub

class Products:
    def get_products(self):
        return get_products_stub() or []

    def get_product_by_model_id(self, model_id):
        products = get_products_stub() or []
        product = [x for x in products if x['modelId'] == model_id]

        if len(product) != 0:
            return product[0]

        return None
