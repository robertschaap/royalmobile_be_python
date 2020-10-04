from flask import Blueprint
from utils.api import ApiResponse
from models.cart import CartModel

cart_controller = Blueprint('cart_controller', __name__)
cart_model = CartModel()

@cart_controller.route('/api/cart/<id>')
def get_cart(id):
    try:
        cart = cart_model.get_card_by_id(id)
        return ApiResponse.success(cart)
    except:
        return ApiResponse.error('Could not get cart')

@cart_controller.route('/api/cart/<id>/item', methods=["PATCH"])
def patch_cart_item():
    # try to call a create cart route if no cart ID
    # then try to add a product
    try:
        cart = {
            'id': "cart-id",
            'items': [],
            'totals': {
                'monthly_price': "",
                'onetime_price': "",
            }

        }

        return ApiResponse.success(cart)
    except:
        return ApiResponse.error('Cart item could not be added')

@cart_controller.route('/api/cart/<id>/item/<item_id>', methods=["DELETE"])
def delete_cart_item():
    try:
        cart = {
            'id': "cart-id",
            'items': [],
            'totals': {
                'monthly_price': "",
                'onetime_price': "",
            }

        }

        return ApiResponse.success(cart)
    except:
        return ApiResponse.error('Cart item could not be deleted')

@cart_controller.route('/api/cart/order', methods=["POST"])
def post_cart_order():
    return ApiResponse.error('Cart order could not be placed')
