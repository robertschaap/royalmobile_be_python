from flask import Blueprint, request
from utils.api import ApiResponse
from models.cart import CartModel

# TODO: figure out if we can add some sort of error handler
cart_controller = Blueprint('cart_controller', __name__)
cart_model = CartModel()

@cart_controller.route('/api/cart/<id>')
def get_cart(id):
    try:
        return ApiResponse.success(cart_model.get_cart_by_id(id))
    except:
        return ApiResponse.error('Could not get cart')

@cart_controller.route('/api/cart/<id>/item', methods=["PATCH"])
def add_cart_item(id):
    data = request.form or request.get_json(force=True)
    variant_id = data.get('variantId')
    subscription_id = data.get('subscriptionId')

    try:
        return ApiResponse.success(cart_model.add_cart_item(id, variant_id, subscription_id))
    except:
        return ApiResponse.error('Could not add cart item')

@cart_controller.route('/api/cart/<id>/item/<item_id>', methods=["DELETE"])
def delete_cart_item(id, item_id):
    try:
        cart = cart_model.delete_cart_item(id, item_id)
        return ApiResponse.success(cart_model.delete_cart_item(id, item_id))
    except:
        return ApiResponse.error('Could not delete cart item')

@cart_controller.route('/api/cart/order', methods=["POST"])
def post_order():
    cart_id = request.values.get('cartId')
    result = cart_model.post_order(cart_id)

    if result == True:
        # TODO: check this, its similar to the Java version but why return the id though?
        return ApiResponse.success(cart_id)

    return ApiResponse.error('Could not post order')
