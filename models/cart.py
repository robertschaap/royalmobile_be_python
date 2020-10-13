from db import Connection

class CartModel:
    def get_cart_by_id(self, cart_id):
        cart = Connection.carts.get_cart_by_id(cart_id)

        if cart != None:
            return cart

        raise ValueError("Cart could not be found")

    def create_cart(self):
        return Connection.carts.get_cart_by_id("new-cart")

    def post_order(self, cart_id):
        # TODO; implement properly once FE is ready for it
        return True
