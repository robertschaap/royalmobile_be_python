from utils.stubs import get_products_stub
from db.connection import Connection

class ProductsModel:
    def get_products(self):
        return Connection.products.get_products()
