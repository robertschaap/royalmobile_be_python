from uuid import uuid4

class Cart:
    carts = []

    def __init__(self):
        self.carts.append({
            'id': "new-cart",
            'items': [],
            'totals': {
                'monthly_price': "0",
                'onetime_price': "0",
            }
        })

    def create_cart(self):
        cart = {
            'id': str(uuid4()),
            'items': [],
            'totals': {
                'monthly_price': "0",
                'onetime_price': "0",
            }
        }

        self.carts.append(cart)
        return cart

    def get_cart_by_id(self, cart_id):
        return next((x for x in self.carts if x.get("id") == cart_id), None)

    def get_cart_index(self, cart_id):
        return next((i for i, x in enumerate(self.carts) if x.get("id") == cart_id), None)


    def add_cart_item(self, cart_id, cart_item):
        index = self.get_cart_index(cart_id)

        if index == None:
            return None

        cart = self.carts.pop(index)
        cart_item["id"] = str(uuid4())
        cart_item["totals"] = {
            'monthly_price': cart_item["subscription"]["regular_price"],
            'onetime_price': cart_item["product"]["variants"][0]["discounted_price"],
        }

        cart["items"].append(cart_item)
        cart["totals"] = self.update_cart_totals(cart.get("items"))

        self.carts.append(cart)

        return cart

    def delete_cart_item(self, cart_id, item_id):
        print(cart_id, item_id, flush=True)
        index = self.get_cart_index(cart_id)

        if index == None:
            return None

        cart = self.carts.pop(index)
        item_index = next((i for i, x in enumerate(cart["items"]) if x.get("id") == item_id), None)

        if item_index == None:
            return None

        cart["items"].pop(item_index)
        cart["totals"] = self.update_cart_totals(cart.get("items"))

        self.carts.append(cart)

        return cart

    # TODO: find a better place for this, the DB does not need to know about the calc part
    def update_cart_totals(self, cart_items):
        monthly_price = 0
        onetime_price = 0

        for item in cart_items:
            monthly_price += int(item.get("totals").get("monthly_price"))
            onetime_price += int(item.get("totals").get("onetime_price"))

        return {
            'monthly_price': str(monthly_price),
            'onetime_price': str(onetime_price),
        }
