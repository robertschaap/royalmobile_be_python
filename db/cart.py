test_cart = {
    'id': "new-cart",
    'items': [],
    'totals': {
        'monthly_price': "",
        'onetime_price': "",
    }
}

class Cart:
    carts = []

    def __init__(self):
        self.carts.append(test_cart)

    def get_cart_by_id(self, id):
        return next((x for x in self.carts if x["id"] == id), None)
