from utils.stubs import get_products_stub
from db.connection import Connection

class ProductModel:
    def get_product(self, id):
        product = Connection.products.get_product_by_model_id(id)

        if product != None:
            return product

        raise ValueError("Product could not be found")
