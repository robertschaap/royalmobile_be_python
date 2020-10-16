from utils.stubs import get_products_stub

class Products:
    def get_products(self):
        return get_products_stub() or []

    def get_product_by_model_id(self, model_id):
        products = self.get_products()

        return next((x for x in products if x['modelId'] == model_id), None)
