from flask import Blueprint
from models.products import ProductsModel
from utils.api import ApiResponse

products_controller = Blueprint('products_controller', __name__)
products_model = ProductsModel()

@products_controller.route('/api/products')
def get_products():
    """
    :return: ApiResponse of Product list or empty list
    """
    products = products_model.get_products()
    return ApiResponse.success(products)
