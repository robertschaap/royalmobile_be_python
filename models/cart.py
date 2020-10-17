from db import Connection

class CartModel:
    def get_cart_by_id(self, cart_id):
        cart = Connection.carts.get_cart_by_id(cart_id)

        if cart != None:
            return cart

        raise ValueError("Cart could not be found")

    def create_cart(self):
        return Connection.carts.create_cart()

    def add_cart_item(self, cart_id, variant_id, subscription_id):
        if cart_id == "new":
            self.create_cart()

        product = Connection.products.get_product_by_model_id("apple-iphonex1")
        subscription = Connection.subscriptions.get_subscription_by_id("royalmobile-20gb-1year")

        if product == None or subscription == None:
            raise ValueError("Could not add cart item")

        updated_cart = Connection.carts.add_cart_item(cart_id, {
            'id': 'a_uuid',
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
