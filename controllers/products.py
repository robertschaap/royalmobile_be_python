from flask import Blueprint
from models.products import ProductsModel
from utils.api import ApiResponse

products_controller = Blueprint('products_controller', __name__)
products_model = ProductsModel()

@products_controller.route('/api/products')
def get_products():
    try:
        products = products_model.get_products()
        return ApiResponse.success(products)
    except:
        return ApiResponse.error("Products could not be found")
