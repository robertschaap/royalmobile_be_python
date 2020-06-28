from flask import Blueprint
from models.product import ProductModel
from utils.api import api_response, api_res_type

product_controller = Blueprint('product_controller', __name__)
product_model = ProductModel()

@product_controller.route('/api/product/<id>')
def get_product(id):
    try:
        return api_response(
            api_res_type["success"],
            product_model.get_product(id),
        )
    except:
        return api_response(
            api_res_type["error"],
            None,
            "Product could not be found"
        )
