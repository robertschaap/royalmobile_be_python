from flask import Blueprint, request
from utils.api import ApiResponse
from models.cart import CartModel

# TODO: figure out if we can add some sort of error handler
cart_controller = Blueprint('cart_controller', __name__)
cart_model = CartModel()

@cart_controller.route('/api/cart/<id>')
def get_cart(id):
    """
    :param str id: UUIDv4 formatted as string
    :return: ApiResponse of Cart or error
    """
    try:
        return ApiResponse.success(cart_model.get_cart_by_id(id))
    except:
        return ApiResponse.error('Could not get cart')

@cart_controller.route('/api/cart/<id>/item', methods=["PATCH"])
def add_cart_item(id):
    """
    :param str id: either UUIDv4 formatted as string or `new`
    :param str variantId: from request body
    :param str subscriptionId: from request body
    :return: ApiRespons of Cart with the added item or error
    """
    data = request.form or request.get_json(force=True)
    variant_id = data.get('variantId')
    subscription_id = data.get('subscriptionId')

    try:
        return ApiResponse.success(cart_model.add_cart_item(id, variant_id, subscription_id))
    except:
        return ApiResponse.error('Could not add cart item')

@cart_controller.route('/api/cart/<cart_id>/item/<item_id>', methods=["DELETE"])
def delete_cart_item(cart_id, item_id):
    """
    :param str cart_id: UUIDv4 formatted as string
    :param str item_id: UUIDv4 formatted as string
    :return: ApiResponse of Cart without the deleted item or error
    """
    try:
        cart = cart_model.delete_cart_item(cart_id, item_id)
        return ApiResponse.success(cart_model.delete_cart_item(cart_id, item_id))
    except:
        return ApiResponse.error('Could not delete cart item')

@cart_controller.route('/api/cart/order', methods=["POST"])
def post_order():
    """
    :param str cart_id: from request body
    """
    cart_id = request.values.get('cartId')
    result = cart_model.post_order(cart_id)

    if result == True:
        # TODO: check this, its similar to the Java version but why return the id though?
        return ApiResponse.success(cart_id)

    return ApiResponse.error('Could not post order')
