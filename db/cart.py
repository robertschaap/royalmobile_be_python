from uuid import uuid4

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

    def create_cart(self):
        cart = {
            'id': str(uuid4()),
            'items': [],
            'totals': {
                'monthly_price': "",
                'onetime_price': "",
            }
        }

        self.carts.append(cart)
        return cart

    def get_cart_by_id(self, cart_id):
        return next((x for x in self.carts if x["id"] == cart_id), None)

    def get_cart_index(self, cart_id):
        return next((i for i, x in enumerate(self.carts) if x["id"] == cart_id), None)


    def add_cart_item(self, cart_id, cart_item):
        index = self.get_cart_index(cart_id)

        if index != None:
            cart = self.carts.pop(index)
            cart_item["id"] = str(uuid4())
            cart_item["totals"] = {
                'monthly_price': "",
                'onetime_price': "",
            }

            cart["items"].append(cart_item)

            self.carts.append(cart)

            return cart

        return None

    def delete_cart_item(self, cart_id, item_id):
        index = self.get_cart_index(cart_id)

        if index != None:
            cart = self.carts.pop(index)
            item_index = next((i for i, x in enumerate(cart["items"]) if x["id"] == item_id), None)

            if item_index != None:
                cart["items"].pop(item_index)
                self.carts.append(cart)

                return cart

        return None
