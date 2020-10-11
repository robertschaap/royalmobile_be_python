from db import Connection

class CartModel:
    def get_cart_by_id(self, id):
        return Connection.carts.get_cart_by_id()

    def post_order(self, cart_id):
        # TODO; implement properly once FE is ready for it
        return True
