from utils.stubs import get_products_stub

class Products:
    def get_products(self):
        return get_products_stub() or []

    def get_product_by_model_id(self, model_id):
        products = self.get_products()

        return next((x for x in products if x.get("modelId") == model_id), None)

    def get_product_by_variant_id(self, variant_id):
        split = variant_id.split("-")
        model_id = "-".join(split[:2])

        products = self.get_products()
        product_by_model = next((x for x in products if x.get("modelId") == model_id), None)

        if product_by_model == None:
            return None

        product_variants = product_by_model["variants"]
        selected_variant = next((x for x in product_variants if x.get("variantId") == variant_id), None)

        if selected_variant == None:
            return None

        product_by_model["variants"] = [selected_variant]

        return product_by_model
