import uuid

class Cart:
    carts = []

    def __init__(self):
        self.carts.append({
            'id': "new-cart",
            'items': [],
            'totals': {
                'monthly_price': "",
                'onetime_price': "",
            }
        })

    def get_cart_by_id(self, cart_id):
        return next((x for x in self.carts if x["id"] == cart_id), None)

    def create_cart(self):
        self.carts.append({
            'id': uuid.uuid4(),
            'items': [],
            'totals': {
                'monthly_price': "",
                'onetime_price': "",
            }
        })

    def add_cart_item(self, cart_id, cart_item):
        index = next((i for i, x in enumerate(self.carts) if x["id"] == cart_id), None)

        if index != None:
            cart = self.carts.pop(index)
            cart["items"].append(cart_item)

            self.carts.append(cart)

            return cart

        return None
