from db import Connection
from uuid import uuid4

class CartModel:
    def get_cart_by_id(self, cart_id):
        cart = Connection.carts.get_cart_by_id(cart_id)

        if cart != None:
            return cart

        raise ValueError("Cart could not be found")

    def create_cart(self):
        return Connection.carts.create_cart()

    def add_cart_item(self, cart_id, variant_id, subscription_id):
        used_cart_id = cart_id

        if cart_id == "new":
            new_cart = self.create_cart()
            used_cart_id = new_cart.get("id")

        # Split off capacity and colour
        split = variant_id.split("-")
        model_id = "-".join(split[:2])

        # TODO: don't return the whole product but only the relevant variant
        product = Connection.products.get_product_by_model_id(model_id)
        subscription = Connection.subscriptions.get_subscription_by_id(subscription_id)

        if product == None or subscription == None:
            raise ValueError("Could not add cart item")

        updated_cart = Connection.carts.add_cart_item(used_cart_id, {
            'product': product,
            'subscription': subscription,
            'totals': None,
        })

        if updated_cart == None:
            raise ValueError("Cart could not be found")

        return updated_cart

    def delete_cart_item(self, cart_id, item_id):
        updated_cart = Connection.carts.delete_cart_item(cart_id, item_id)

    def post_order(self, cart_id):
        # TODO; implement properly once FE is ready for it
        return True
