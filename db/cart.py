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

    def get_cart_by_id(self, id):
        return next((x for x in self.carts if x["id"] == id), None)

    def create_cart(self):
        self.carts.append({
            'id': uuid.uuid4(),
            'items': [],
            'totals': {
                'monthly_price': "",
                'onetime_price': "",
            }
        })
