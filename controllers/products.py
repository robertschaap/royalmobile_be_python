from flask import Blueprint
from models.products import ProductsModel
from utils.api import api_response, api_res_type

products_controller = Blueprint('products_controller', __name__)
products_model = ProductsModel()

@products_controller.route('/api/products')
def get_products():
    try:
        return api_response(
            api_res_type["success"],
            products_model.get_products(),
        )
    except:
        return api_response(
            api_res_type["error"],
            None,
            "error message"
        )
