from flask import Blueprint
from models.product import ProductModel
from utils.api import ApiResponse

product_controller = Blueprint('product_controller', __name__)
product_model = ProductModel()

@product_controller.route('/api/product/<model_id>')
def get_product(model_id):
    """
    :param str model_id: model ID `manufacturer-device`
    :return: `ApiResponse` of `Product` or error
    """
    try:
        product = product_model.get_product(model_id)
        return ApiResponse.success(product)
    except:
        return ApiResponse.error("Could not get product")
