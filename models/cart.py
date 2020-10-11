from db.connection import Connection

class CartModel:
    def get_cart_by_id(self, id):
        return Connection.carts.get_cart_by_id()
