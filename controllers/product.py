from flask import Blueprint
from models.product import ProductModel
from utils.api import ApiResponse

product_controller = Blueprint('product_controller', __name__)
product_model = ProductModel()

@product_controller.route('/api/product/<id>')
def get_product(id):
    try:
        product = product_model.get_product(id)
        return ApiResponse.success(product)
    except:
        return ApiResponse.error("Product could not be found")
