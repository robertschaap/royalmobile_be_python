class Cart:
    carts = [
        {
            'id': "new-cart",
            'items': [],
            'totals': {
                'monthly_price': "",
                'onetime_price': "",
            }
        }
    ]

    def get_cart_by_id(self):
        return self.carts[0]
