class CartModel:
    def get_cart_by_id(self, id):
        cart = {
            'id': "cart-id",
            'items': [],
            'totals': {
                'monthly_price': "",
                'onetime_price': "",
            }
        }

        return cart
