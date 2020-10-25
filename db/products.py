from utils.stubs import get_products_stub

class Products:
    def get_products(self):
        return get_products_stub() or []

    def get_product_by_model_id(self, model_id):
        products = self.get_products()

        return next((x for x in products if x['modelId'] == model_id), None)

    def get_product_by_variant_id(self, variant_id):
        split = variant_id.split("-")
        model_id = "-".join(split[:2])

        products = self.get_products()

        # TODO: don't return the whole product but only the relevant variant
        return next((x for x in products if x['modelId'] == model_id), None)
